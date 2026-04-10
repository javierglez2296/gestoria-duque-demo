from dash import html
import dash_bootstrap_components as dbc
from components.home.data import HERO_SLIDES


def build_hero():
    slide = HERO_SLIDES[0]

    return html.Div(
        style={
            "minHeight": "90vh",
            "display": "flex",
            "alignItems": "center",
            "position": "relative",
            "overflow": "hidden",
            "backgroundImage": f"url('{slide['image']}')",
            "backgroundSize": "cover",
            "backgroundPosition": "center",
        },
        children=[
            html.Div(
                style={
                    "position": "absolute",
                    "inset": "0",
                    "background": "linear-gradient(90deg, rgba(10,14,22,0.92) 0%, rgba(10,14,22,0.75) 45%, rgba(10,14,22,0.35) 100%)",
                }
            ),
            dbc.Container(
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div(
                                    slide["eyebrow"],
                                    className="hero-fade hero-delay-1",
                                    style={
                                        "textTransform": "uppercase",
                                        "fontSize": "0.75rem",
                                        "letterSpacing": "0.18em",
                                        "marginBottom": "1.2rem",
                                        "color": "rgba(255,255,255,0.8)",
                                        "fontWeight": "700",
                                    },
                                ),
                                html.H1(
                                    slide["title"],
                                    className="hero-fade hero-delay-2",
                                    style={
                                        "fontSize": "clamp(2.6rem, 4.5vw, 4.2rem)",
                                        "lineHeight": "1.02",
                                        "fontWeight": "700",
                                        "letterSpacing": "-0.04em",
                                        "color": "white",
                                        "marginBottom": "1.4rem",
                                        "maxWidth": "780px",
                                    },
                                ),
                                html.P(
                                    slide["text"],
                                    className="hero-fade hero-delay-3",
                                    style={
                                        "fontSize": "1.05rem",
                                        "lineHeight": "1.9",
                                        "maxWidth": "620px",
                                        "color": "rgba(255,255,255,0.75)",
                                        "marginBottom": "2.2rem",
                                    },
                                ),
                                html.Div(
                                    [
                                        dbc.Button(
                                            "Solicitar información",
                                            href="#contacto",
                                            color="light",
                                            className="fw-semibold me-3",
                                            style={
                                                "padding": "0.95rem 1.5rem",
                                                "borderRadius": "999px",
                                                "boxShadow": "0 10px 25px rgba(0,0,0,0.2)",
                                            },
                                        ),
                                        html.A(
                                            "Llamar ahora",
                                            href="tel:920000000",
                                            style={
                                                "color": "white",
                                                "fontWeight": "600",
                                                "textDecoration": "none",
                                                "opacity": "0.9",
                                            },
                                        ),
                                    ],
                                    className="hero-fade hero-delay-4",
                                ),
                            ],
                            lg=8,
                        )
                    ],
                    style={
                        "minHeight": "90vh",
                        "alignItems": "center",
                        "position": "relative",
                        "zIndex": "2",
                    },
                )
            ),
        ],
    )
