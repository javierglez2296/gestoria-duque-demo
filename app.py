from dash import Dash, html, page_container, Input, Output, State
import dash_bootstrap_components as dbc


TELEFONO = "920 000 000"
EMAIL = "info@gestoriaduque.com"
WHATSAPP_URL = "https://wa.me/34620000000"


def build_topbar():
    return html.Div(
        dbc.Container(
            html.Div(
                [
                    html.Div(
                        [
                            html.Span("Asesoría en Ávila", className="topbar-mini-text"),
                        ],
                        className="d-none d-md-flex align-items-center",
                    ),
                    html.Div(
                        [
                            html.A(
                                TELEFONO,
                                href=f"tel:{TELEFONO.replace(' ', '')}",
                                className="topbar-link",
                            ),
                            html.Span(className="topbar-separator d-none d-md-inline"),
                            html.A(
                                EMAIL,
                                href=f"mailto:{EMAIL}",
                                className="topbar-link d-none d-sm-inline",
                            ),
                        ],
                        className="d-flex align-items-center gap-3",
                    ),
                ],
                className="topbar-content",
            ),
            fluid=False,
        ),
        className="topbar topbar-clean",
    )


def build_navbar():
    return dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    html.Div(
                        [
                            html.Div("GESTORÍA DUQUE", className="brand-title"),
                            html.Div(
                                "Fiscal · Laboral · Contable",
                                className="brand-subtitle d-none d-md-block",
                            ),
                        ],
                        className="brand-lockup",
                    ),
                    href="/",
                    className="brand-link text-decoration-none",
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
                                "Solicitar información",
                                href="/#contacto",
                                className="navbar-cta ms-lg-3",
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
        className="navbar-premium navbar-premium-clean",
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
                                        html.A(
                                            "Inicio",
                                            href="/",
                                            className="site-footer-link d-block mb-2",
                                        ),
                                        html.A(
                                            "Servicios",
                                            href="/#servicios",
                                            className="site-footer-link d-block mb-2",
                                        ),
                                        html.A(
                                            "Contacto",
                                            href="/#contacto",
                                            className="site-footer-link d-block",
                                        ),
                                    ]
                                ),
                            ],
                            md=4,
                            className="mb-4",
                        ),
                        dbc.Col(
                            [
                                html.Div("Contacto", className="site-footer-title"),
                                html.P(TELEFONO, className="site-footer-text"),
                                html.P(EMAIL, className="site-footer-text"),
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
        build_topbar(),
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
