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
                                        [
                                            html.Span("Gestión fiscal, laboral y contable "),
                                            html.Br(),
                                            html.Span("con claridad y confianza."),
                                        ],
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
                                                className="hero-cta-btn me-2",
                                            ),
                                            dbc.Button(
                                                "Ver servicios",
                                                href="#servicios",
                                                className="hero-secondary-btn",
                                            ),
                                        ],
                                        className="hero-line hero-actions d-flex flex-wrap gap-2",
                                    ),
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.Div("Fiscal", className="hero-metric-label"),
                                                    html.Div("Autónomos y empresas", className="hero-metric-value"),
                                                ],
                                                className="hero-metric-card",
                                            ),
                                            html.Div(
                                                [
                                                    html.Div("Laboral", className="hero-metric-label"),
                                                    html.Div("Nóminas, altas y contratos", className="hero-metric-value"),
                                                ],
                                                className="hero-metric-card",
                                            ),
                                            html.Div(
                                                [
                                                    html.Div("Contable", className="hero-metric-label"),
                                                    html.Div("Orden y seguimiento", className="hero-metric-value"),
                                                ],
                                                className="hero-metric-card",
                                            ),
                                        ],
                                        className="hero-line hero-metrics",
                                    ),
                                ],
                                className="hero-copy-animate",
                            ),
                            lg=8,
                            md=10,
                            xs=12,
                        ),
                    ],
                    className="align-items-center min-vh-100",
                ),
                fluid="lg",
                className="hero-content-wrap",
            ),
        ],
        className="hero-premium-section",
    )
