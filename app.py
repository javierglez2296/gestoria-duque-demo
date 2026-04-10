from dash import Dash, html, page_container, Input, Output, State
import dash_bootstrap_components as dbc


EMAIL = "info@gestoriaduque.com"
WHATSAPP_URL = "https://wa.me/34620000000"


def build_navbar():
    return dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    html.Div(
                        html.Img(
                            src="assets/logo-duque.png",
                            alt="Gestoría Duque",
                            className="navbar-logo-img",
                        ),
                        className="navbar-logo",
                    ),
                    href="/",
                    className="text-decoration-none d-flex align-items-center",
                ),
                dbc.NavbarToggler(
                    id="navbar-toggler",
                    n_clicks=0,
                    className="navbar-toggler-premium",
                ),
                dbc.Collapse(
                    dbc.Nav(
                        [
                            dbc.NavLink(
                                "Inicio",
                                href="/",
                                className="nav-link-premium",
                            ),
                            dbc.NavLink(
                                "Servicios",
                                href="/#servicios",
                                className="nav-link-premium",
                            ),
                            dbc.NavLink(
                                "Contacto",
                                href="/#contacto",
                                className="nav-link-premium",
                            ),
                            dbc.Button(
                                "WhatsApp",
                                href=WHATSAPP_URL,
                                target="_blank",
                                rel="noopener noreferrer",
                                className="navbar-whatsapp ms-lg-2",
                            ),
                            dbc.Button(
                                "Solicitar información",
                                href="/presupuesto",
                                className="navbar-cta ms-lg-2",
                            ),
                        ],
                        className="ms-auto align-items-lg-center navbar-nav-premium",
                        navbar=True,
                    ),
                    id="navbar-collapse",
                    navbar=True,
                ),
            ],
            fluid=False,
            className="navbar-container-premium",
        ),
        sticky="top",
        className="navbar-premium",
        dark=False,
    )


def build_footer():
    return html.Footer(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div("Gestoría Duque", className="site-footer-title"),
                                html.P(
                                    "Asesoría fiscal, laboral y contable en Ávila con una imagen clara, actual y profesional.",
                                    className="site-footer-text",
                                ),
                            ],
                            md=4,
                            className="mb-4",
                        ),
                        dbc.Col(
                            [
                                html.Div("Navegación", className="site-footer-title"),
                                html.Div(
                                    [
                                        html.A("Inicio", href="/", className="site-footer-link d-block mb-2"),
                                        html.A("Servicios", href="/#servicios", className="site-footer-link d-block mb-2"),
                                        html.A("Contacto", href="/#contacto", className="site-footer-link d-block mb-2"),
                                        html.A("Solicitar presupuesto", href="/presupuesto", className="site-footer-link d-block"),
                                    ]
                                ),
                            ],
                            md=4,
                            className="mb-4",
                        ),
                        dbc.Col(
                            [
                                html.Div("Contacto", className="site-footer-title"),
                                html.P(EMAIL, className="site-footer-text"),
                                html.P("WhatsApp disponible", className="site-footer-text"),
                                html.P("Ávila", className="site-footer-text"),
                            ],
                            md=4,
                            className="mb-4",
                        ),
                    ]
                ),
            ],
        ),
        className="site-footer",
    )


app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
    title="Gestoría Duque | Demo premium",
    update_title=None,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
        {
            "name": "description",
            "content": "Gestoría en Ávila para autónomos, empresas y particulares. Demo premium con enfoque visual moderno, local y comercial.",
        },
        {"name": "theme-color", "content": "#ffffff"},
    ],
)

server = app.server

app.layout = html.Div(
    [
        build_navbar(),
        html.Main(
            page_container,
            className="site-main",
        ),
        build_footer(),
    ],
    className="site-shell",
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


if __name__ == "__main__":
    app.run(debug=True)
