from dash import Dash, html, page_container, Input, Output, State, dcc
import dash_bootstrap_components as dbc

WHATSAPP_URL = "https://wa.me/34620000000"


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
                dbc.NavbarToggler(
                    id="navbar-toggler",
                    className="navbar-toggler-premium",
                ),
                dbc.Collapse(
                    dbc.Nav(
                        [
                            dbc.NavItem(
                                dcc.Link(
                                    "Inicio",
                                    href="/",
                                    className="nav-link-premium",
                                )
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
                                            dcc.Link(
                                                "Gestoría administrativa",
                                                href="/gestoria-administrativa",
                                                className="services-dropdown-link",
                                            ),
                                            dcc.Link(
                                                "Asesoría laboral",
                                                href="/asesoria-laboral",
                                                className="services-dropdown-link",
                                            ),
                                            dcc.Link(
                                                "Asesoría tributaria",
                                                href="/asesoria-tributaria",
                                                className="services-dropdown-link",
                                            ),
                                            dcc.Link(
                                                "Asesoría jurídica",
                                                href="/asesoria-juridica",
                                                className="services-dropdown-link",
                                            ),
                                            dcc.Link(
                                                "Externalización de servicios",
                                                href="/externalizacion-de-servicios",
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
                                dcc.Link(
                                    "Presupuesto",
                                    href="/presupuesto",
                                    className="nav-link-premium",
                                )
                            ),
                            dbc.NavItem(
                                html.A(
                                    "Contacto",
                                    href="#contacto",
                                    className="nav-link-premium",
                                )
                            ),
                        ],
                        className="navbar-nav-premium ms-auto",
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
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
        {
            "name": "description",
            "content": (
                "Gestoría en Ávila para autónomos, empresas y particulares. "
                "Asesoría fiscal, laboral, contable y trámites con una imagen moderna, clara y profesional."
            ),
        },
    ],
    title="Gestoría Duque",
    update_title=None,
)

server = app.server

app.layout = html.Div(
    [
        dcc.Location(id="main-url"),
        build_navbar(),
        html.Main(page_container, className="site-main"),
    ]
)


@app.callback(
    Output("navbar-collapse", "is_open"),
    Input("navbar-toggler", "n_clicks"),
    State("navbar-collapse", "is_open"),
)
def toggle_navbar(n_clicks, is_open):
    if n_clicks:
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
