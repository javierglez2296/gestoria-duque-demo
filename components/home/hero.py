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
                                        "GESTORÍA EN ÁVILA",
                                        className="hero-line hero-eyebrow",
                                    ),
                                    html.H1(
                                        "Asesoría fiscal, laboral y contable con una imagen moderna y profesional.",
                                        className="hero-line hero-title",
                                    ),
                                    html.P(
                                        "Trabajamos con autónomos, empresas y particulares para ayudarte a gestionar con claridad tus obligaciones y trámites.",
                                        className="hero-line hero-subtitle",
                                    ),
                                    html.Div(
                                        dbc.Button(
                                            "Solicitar información",
                                            href="#contacto",
                                            className="hero-cta-btn",
                                        ),
                                        className="hero-line",
                                    ),
                                ],
                                className="hero-copy-animate",
                            ),
                            lg=7,
                            md=9,
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
