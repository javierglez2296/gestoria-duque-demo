from dash import html
import dash_bootstrap_components as dbc


def build_hero():
    return html.Section(
        [
            html.Div(className="hero-image-layer"),
            html.Div(className="hero-overlay"),
            dbc.Container(
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Span("Asesoría integral"),
                                            html.Span("Ávila"),
                                        ],
                                        className="hero-line hero-eyebrow",
                                    ),
                                    html.H1(
                                        "Gestión fiscal, laboral y contable con claridad y confianza.",
                                        className="hero-line hero-title",
                                    ),
                                    html.P(
                                        "Ayudamos a autónomos, empresas y particulares con una atención cercana, procesos claros y una imagen moderna y profesional.",
                                        className="hero-line hero-subtitle",
                                    ),
                                    html.Div(
                                        [
                                            dbc.Button(
                                                "Solicitar información",
                                                href="#contacto",
                                                className="hero-cta-btn",
                                            ),
                                            dbc.Button(
                                                "Ver servicios",
                                                href="#servicios",
                                                className="hero-secondary-btn",
                                            ),
                                        ],
                                        className="hero-line hero-actions",
                                    ),
                                ],
                                className="hero-copy-animate",
                            ),
                            lg=7,
                            xl=6,
                            md=9,
                            xs=12,
                        ),
                    ],
                    className="align-items-center hero-row",
                ),
                fluid="lg",
                className="hero-content-wrap",
            ),
        ],
        className="hero-premium-section",
    )
