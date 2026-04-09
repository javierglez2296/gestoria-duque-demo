from dash import Dash, html, page_container
import dash_bootstrap_components as dbc


def build_navbar():
    return html.Div(
        [
            dbc.Container(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Div(
                                    [
                                        html.Span("📍", className="me-2"),
                                        html.Span("Ávila · Atención cercana y profesional"),
                                    ],
                                    className="small",
                                    style={"color": "#475467"},
                                ),
                                md=6,
                                className="d-none d-md-flex align-items-center",
                            ),
                            dbc.Col(
                                html.Div(
                                    [
                                        html.A(
                                            "📞 920 000 000",
                                            href="tel:920000000",
                                            style={
                                                "textDecoration": "none",
                                                "color": "#475467",
                                                "fontWeight": "600",
                                                "marginRight": "1rem",
                                            },
                                        ),
                                        html.A(
                                            "✉️ info@gestoriaduque.com",
                                            href="mailto:info@gestoriaduque.com",
                                            style={
                                                "textDecoration": "none",
                                                "color": "#475467",
                                                "fontWeight": "600",
                                            },
                                        ),
                                    ],
                                    className="small d-flex justify-content-md-end flex-wrap",
                                ),
                                md=6,
                                className="d-flex align-items-center justify-content-start justify-content-md-end",
                            ),
                        ],
                        className="py-2",
                    )
                ],
                fluid=True,
                style={"borderBottom": "1px solid rgba(15, 23, 42, 0.06)"},
            ),
            dbc.Navbar(
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
                                            "letterSpacing": "-0.03em",
                                        },
                                    ),
                                    html.Span(
                                        " Duque",
                                        style={
                                            "color": "#0d6efd",
                                            "fontWeight": "800",
                                            "letterSpacing": "-0.03em",
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
                                dbc.NavLink("Inicio", href="/", className="fw-semibold px-3"),
                                dbc.NavLink("Servicios", href="#servicios", className="fw-semibold px-3"),
                                dbc.NavLink("Contacto", href="#contacto", className="fw-semibold px-3"),
                            ],
                            className="ms-auto d-none d-lg-flex",
                            navbar=True,
                        ),
                        html.Div(
                            [
                                dbc.Button(
                                    "Llamar ahora",
                                    href="tel:920000000",
                                    color="primary",
                                    className="rounded-pill px-4 fw-semibold d-none d-md-inline-flex",
                                    style={
                                        "boxShadow": "0 10px 22px rgba(13, 110, 253, 0.18)",
                                    },
                                )
                            ],
                            className="ms-3",
                        ),
                    ],
                    fluid=True,
                ),
                color="white",
                dark=False,
                sticky="top",
                className="shadow-sm",
                style={
                    "background": "rgba(255,255,255,0.92)",
                    "backdropFilter": "blur(10px)",
                    "WebkitBackdropFilter": "blur(10px)",
                },
            ),
        ]
    )


app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
    title="Gestoría Demo",
    update_title=None,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
        {
            "name": "description",
            "content": "Gestoría en Ávila para autónomos, empresas y particulares. Demo de renovación web con enfoque profesional, local y comercial.",
        },
    ],
)

server = app.server

app.layout = html.Div(
    [
        build_navbar(),
        html.Main(
            page_container,
            className="site-main",
            style={"background": "#ffffff"},
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
