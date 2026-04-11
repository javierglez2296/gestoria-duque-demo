from dash import Dash, html, page_container, Input, Output, State
import dash_bootstrap_components as dbc

TELEFONO = "920 000 000"
EMAIL = "info@gestoriaduque.com"
WHATSAPP_URL = "https://wa.me/34620000000"


def build_topbar():
    return html.Div(
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            [
                                html.Span("Ávila"),
                                html.Span("Más de 70 años de experiencia"),
                                html.Span("Atención cercana y profesional"),
                            ],
                            className="topbar-left d-none d-md-flex",
                        ),
                        md=7,
                        className="d-flex align-items-center",
                    ),
                    dbc.Col(
                        html.Div(
                            [
                                html.A(
                                    TELEFONO,
                                    href=f"tel:{TELEFONO.replace(' ', '')}",
                                    className="topbar-link",
                                ),
                                html.A(
                                    EMAIL,
                                    href=f"mailto:{EMAIL}",
                                    className="topbar-link",
                                ),
                            ],
                            className="topbar-right",
                        ),
                        md=5,
                        className="d-flex align-items-center justify-content-md-end",
                    ),
                ],
                className="g-2 align-items-center",
            ),
            fluid="lg",
        ),
        className="topbar-premium",
    )


def build_navbar():
    return dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    html.Img(
                        src="/assets/logo-duque.png",
                        alt="Gestoría Duque",
                        className="navbar-logo-img",
                    ),
                    href="/",
                    className="navbar-logo",
                ),
                dbc.NavbarToggler(id="navbar-toggler", className="navbar-toggler-premium"),
                dbc.Collapse(
                    dbc.Nav(
                        [
                            dbc.NavItem(
                                dbc.NavLink("Inicio", href="/", className="nav-link-premium")
                            ),
                            html.Div(
                                [
                                    html.Button(
                                        "Servicios",
                                        id="services-dropdown-toggle",
                                        className="nav-link-premium nav-dropdown-trigger",
                                        n_clicks=0,
                                        type="button",
                                    ),
                                    html.Div(
                                        [
                                            html.A(
                                                "Gestoría administrativa",
                                                href="#servicios",
                                                className="services-dropdown-link",
                                            ),
                                            html.A(
                                                "Asesoría laboral",
                                                href="#servicios",
                                                className="services-dropdown-link",
                                            ),
                                            html.A(
                                                "Asesoría tributaria",
                                                href="#servicios",
                                                className="services-dropdown-link",
                                            ),
                                            html.A(
                                                "Asesoría jurídica",
                                                href="#servicios",
                                                className="services-dropdown-link",
                                            ),
                                            html.A(
                                                "Externalización de servicios",
                                                href="#servicios",
                                                className="services-dropdown-link",
                                            ),
                                        ],
                                        id="services-dropdown-menu",
                                        className="services-dropdown-menu",
                                    ),
                                ],
                                className="services-dropdown-wrap",
                            ),
                            dbc.NavItem(
                                dbc.NavLink(
                                    "Presupuesto",
                                    href="/presupuesto",
                                    className="nav-link-premium",
                                )
                            ),
                            dbc.NavItem(
                                dbc.NavLink(
                                    "Contacto",
                                    href="#contacto",
                                    className="nav-link-premium",
                                )
                            ),
                            html.A(
                                "WhatsApp",
                                href=WHATSAPP_URL,
                                target="_blank",
                                rel="noopener noreferrer",
                                className="navbar-whatsapp",
                            ),
                            html.A(
                                "Solicitar información",
                                href="/presupuesto",
                                className="navbar-cta",
                            ),
                        ],
                        className="ms-auto navbar-nav-premium align-items-lg-center",
                        navbar=True,
                    ),
                    id="navbar-collapse",
                    is_open=False,
                    navbar=True,
                ),
            ],
            fluid="lg",
            className="navbar-container-premium",
        ),
        className="navbar-premium",
        sticky="top",
    )


app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
)

server = app.server

app.layout = html.Div(
    [
        build_topbar(),
        build_navbar(),
        html.Main(page_container, className="site-main"),
    ]
)


@app.callback(
    Output("navbar-collapse", "is_open"),
    Input("navbar-toggler", "n_clicks"),
    State("navbar-collapse", "is_open"),
)
def toggle_navbar(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("services-dropdown-menu", "className"),
    Input("services-dropdown-toggle", "n_clicks"),
    prevent_initial_call=False,
)
def toggle_services_dropdown(n_clicks):
    if n_clicks and n_clicks % 2 == 1:
        return "services-dropdown-menu services-dropdown-menu-open"
    return "services-dropdown-menu"


if __name__ == "__main__":
    app.run(debug=True)
