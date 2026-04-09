from dash import Dash, html, page_container
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
                                html.Span("Ávila", className="me-3"),
                                html.Span("Más de 70 años de experiencia", className="me-3"),
                                html.Span("Atención cercana y profesional"),
                            ],
                            className="small d-none d-md-flex flex-wrap",
                            style={
                                "color": "#667085",
                                "fontWeight": "600",
                                "gap": "0.25rem",
                            },
                        ),
                        md=7,
                        className="d-flex align-items-center",
                    ),
                    dbc.Col(
                        html.Div(
                            [
                                html.A(
                                    f"📞 {TELEFONO}",
                                    href=f"tel:{TELEFONO.replace(' ', '')}",
                                    style={
                                        "textDecoration": "none",
                                        "color": "#344054",
                                        "fontWeight": "600",
                                        "marginRight": "1rem",
                                    },
                                ),
                                html.A(
                                    f"✉️ {EMAIL}",
                                    href=f"mailto:{EMAIL}",
                                    style={
                                        "textDecoration": "none",
                                        "color": "#344054",
                                        "fontWeight": "600",
                                    },
                                ),
                            ],
                            className="small d-flex justify-content-md-end flex-wrap",
                        ),
                        md=5,
                        className="d-flex align-items-center justify-content-start justify-content-md-end",
                    ),
                ],
                className="py-2",
            )
        ),
        style={
            "borderBottom": "1px solid rgba(15, 23, 42, 0.06)",
            "background": "rgba(255,255,255,0.82)",
            "backdropFilter": "blur(10px)",
            "WebkitBackdropFilter": "blur(10px)",
        },
    )


def build_navbar():
    return dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    dbc.NavbarBrand(
                        [
                            html.Span(
                                "Gestoría",
                                style={
                                    "color": "#101828",
                                    "fontWeight": "800",
                                    "letterSpacing": "-0.04em",
                                    "fontSize": "1.25rem",
                                },
                            ),
                            html.Span(
                                " Duque",
                                style={
                                    "color": "#0d6efd",
                                    "fontWeight": "800",
                                    "letterSpacing": "-0.04em",
                                    "fontSize": "1.25rem",
                                },
                            ),
                        ],
                        className="mb-0",
                    ),
                    href="/",
                    style={"textDecoration": "none"},
                ),
                dbc.Nav(
                    [
                        dbc.NavLink(
                            "Inicio",
                            href="/",
                            className="fw-semibold px-3",
                            style={"color": "#344054"},
                        ),
                        dbc.NavLink(
                            "Servicios",
                            href="#servicios",
                            className="fw-semibold px-3",
                            style={"color": "#344054"},
                        ),
                        dbc.NavLink(
                            "Contacto",
                            href="#contacto",
                            className="fw-semibold px-3",
                            style={"color": "#344054"},
                        ),
                    ],
                    className="ms-auto d-none d-lg-flex",
                    navbar=True,
                ),
                html.Div(
                    [
                        dbc.Button(
                            "WhatsApp",
                            href=WHATSAPP_URL,
                            target="_blank",
                            color="light",
                            className="rounded-pill fw-semibold border me-2 d-none d-md-inline-flex",
                            style={
                                "padding": "0.72rem 1.15rem",
                                "minHeight": "44px",
                                "background": "rgba(255,255,255,0.78)",
                            },
                        ),
                        dbc.Button(
                            "Llamar ahora",
                            href=f"tel:{TELEFONO.replace(' ', '')}",
                            color="primary",
                            className="rounded-pill fw-semibold",
                            style={
                                "padding": "0.72rem 1.2rem",
                                "minHeight": "44px",
                                "boxShadow": "0 10px 22px rgba(13, 110, 253, 0.18)",
                            },
                        ),
                    ],
                    className="ms-3 d-flex align-items-center",
                ),
            ],
            fluid=True,
            style={"maxWidth": "1280px"},
        ),
        color="white",
        dark=False,
        sticky="top",
        className="shadow-sm",
        style={
            "background": "rgba(255,255,255,0.88)",
            "backdropFilter": "blur(14px)",
            "WebkitBackdropFilter": "blur(14px)",
            "borderBottom": "1px solid rgba(15, 23, 42, 0.06)",
        },
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
            style={
                "background": "#ffffff",
            },
        ),
    ],
    className="site-shell",
    style={
        "backgroundColor": "#ffffff",
        "minHeight": "100vh",
    },
)

if __name__ == "__main__":
    app.run(debug=True)
