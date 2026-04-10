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
                                    className="topbar-link me-3",
                                ),
                                html.A(
                                    EMAIL,
                                    href=f"mailto:{EMAIL}",
                                    className="topbar-link",
                                ),
                            ],
                            className="topbar-right d-flex justify-content-md-end flex-wrap",
                        ),
                        md=5,
                        className="d-flex align-items-center justify-content-start justify-content-md-end",
                    ),
                ],
                className="py-2 align-items-center",
            )
        ),
        className="topbar-premium",
    )


def build_navbar():
    return dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    html.Div(
                        [
                            html.Span("GESTORÍA", className="navbar-logo-main"),
                            html.Span("DUQUE", className="navbar-logo-sub"),
                        ],
                        className="navbar-logo",
                    ),
                    href="/",
                    className="text-decoration-none",
                ),
                dbc.NavbarToggler(id="navbar-toggler", n_clicks=0, className="border-0"),
                dbc.Collapse(
                    dbc.Nav(
                        [
                            dbc.NavLink("Inicio", href="/", className="nav-link-premium"),
                            dbc.NavLink("Servicios", href="/#servicios", className="nav-link-premium"),
                            dbc.NavLink("Contacto", href="/#contacto", className="nav-link-premium"),
                            dbc.Button(
                                "WhatsApp",
                                href=WHATSAPP_URL,
                                target="_blank",
                                className="navbar-btn navbar-btn-secondary",
                            ),
                            dbc.Button(
                                "Llamar ahora",
                                href=f"tel:{TELEFONO.replace(' ', '')}",
                                className="navbar-btn navbar-btn-primary",
                            ),
                        ],
                        className="ms-auto align-items-lg-center navbar-menu-premium",
                        navbar=True,
                    ),
                    id="navbar-collapse",
                    navbar=True,
                ),
            ],
            fluid=True,
            className="navbar-inner",
        ),
        sticky="top",
        className="navbar-premium-app",
    )


def build_footer():
    return html.Footer(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div("Gestoría Duque", className="footer-logo"),
                                html.P(
                                    "Asesoría fiscal, laboral y contable en Ávila con una imagen más clara, actual y profesional.",
                                    className="footer-text",
                                ),
                            ],
                            md=4,
                            className="mb-4",
                        ),
                        dbc.Col(
                            [
                                html.Div("Navegación", className="footer-title"),
                                html.A("Inicio", href="/", className="footer-link"),
                                html.A("Servicios", href="/#servicios", className="footer-link"),
                                html.A("Contacto", href="/#contacto", className="footer-link"),
                            ],
                            md=4,
                            className="mb-4",
                        ),
                        dbc.Col(
                            [
                                html.Div("Contacto", className="footer-title"),
                                html.Div(TELEFONO, className="footer-text"),
                                html.Div(EMAIL, className="footer-text"),
                                html.Div("Ávila", className="footer-text"),
                            ],
                            md=4,
                            className="mb-4",
                        ),
                    ]
                ),
                html.Hr(className="footer-divider"),
                html.Div(
                    "© 2026 Gestoría Duque · Todos los derechos reservados",
                    className="footer-bottom",
                ),
            ]
        ),
        className="footer-premium",
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
