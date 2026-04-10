from dash import html
import dash_bootstrap_components as dbc
from components.home.data import HERO_SLIDES


def build_hero():
    slide = HERO_SLIDES[0]

    return html.Div(
        style={
            "minHeight": "85vh",
            "display": "flex",
            "alignItems": "center",
            "backgroundImage": f"""
                linear-gradient(90deg, rgba(8,12,20,0.85) 0%, rgba(8,12,20,0.65) 50%, rgba(8,12,20,0.3) 100%),
                url('{slide['image']}')
            """,
            "backgroundSize": "cover",
            "backgroundPosition": "center",
            "color": "white",
        },
        children=[
            dbc.Container(
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div(
                                    slide["eyebrow"],
                                    style={
                                        "textTransform": "uppercase",
                                        "fontSize": "0.75rem",
                                        "letterSpacing": "0.15em",
                                        "marginBottom": "1rem",
                                        "opacity": "0.8",
                                    },
                                ),
                                html.H1(
                                    slide["title"],
                                    style={
                                        "fontSize": "clamp(2.5rem, 4vw, 4rem)",
                                        "lineHeight": "1.05",
                                        "fontWeight": "700",
                                        "marginBottom": "1rem",
                                    },
                                ),
                                html.P(
                                    slide["text"],
                                    style={
                                        "fontSize": "1.1rem",
                                        "lineHeight": "1.8",
                                        "maxWidth": "600px",
                                        "opacity": "0.85",
                                        "marginBottom": "2rem",
                                    },
                                ),
                                dbc.Button(
                                    "Solicitar información",
                                    href="#contacto",
                                    color="light",
                                    className="fw-semibold",
                                    style={
                                        "padding": "0.9rem 1.5rem",
                                        "borderRadius": "999px",
                                    },
                                ),
                            ],
                            lg=7,
                        )
                    ],
                    style={"minHeight": "85vh", "alignItems": "center"},
                )
            )
        ],
    )
