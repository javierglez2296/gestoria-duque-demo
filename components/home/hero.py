from dash import html, dcc
import dash_bootstrap_components as dbc

from components.home.data import (
    TELEFONO_1,
    EMAIL,
    HERO_SLIDES,
)


def hero_indicator(index, active=False):
    return html.Button(
        id={"type": "hero-indicator", "index": index},
        n_clicks=0,
        style={
            "width": "28px" if active else "10px",
            "height": "10px",
            "borderRadius": "999px",
            "border": "none",
            "padding": "0",
            "marginRight": "10px",
            "background": "#ffffff" if active else "rgba(255,255,255,0.34)",
            "transition": "all 0.28s ease",
            "cursor": "pointer",
        },
    )


def build_hero_content(slide_index):
    slide = HERO_SLIDES[slide_index]

    return html.Div(
        key=f"hero-content-{slide_index}",
        className="hero-content-animate",
        children=[
            html.Div(
                [
                    html.Span(
                        "",
                        style={
                            "display": "inline-block",
                            "width": "42px",
                            "height": "1px",
                            "background": "rgba(255,255,255,0.72)",
                            "marginRight": "12px",
                            "verticalAlign": "middle",
                        },
                    ),
                    html.Span(slide["eyebrow"]),
                ],
                id="hero-eyebrow",
                className="mb-4 reveal reveal-1",
                style={
                    "display": "inline-flex",
                    "alignItems": "center",
                    "fontWeight": "700",
                    "fontSize": "0.76rem",
                    "letterSpacing": "0.16em",
                    "color": "rgba(255,255,255,0.88)",
                    "textTransform": "uppercase",
                },
            ),
            html.Div(
                [
                    html.Div(
                        style={
                            "width": "6px",
                            "height": "138px",
                            "background": "rgba(255,255,255,0.65)",
                            "marginRight": "24px",
                            "flexShrink": "0",
                            "alignSelf": "flex-start",
                        }
                    ),
                    html.Div(
                        [
                            html.H1(
                                slide["title"],
                                id="hero-title",
                                className="mb-4 reveal reveal-2",
                                style={
                                    "fontSize": "clamp(2.2rem, 4vw, 3.8rem)",
                                    "lineHeight": "0.98",
                                    "letterSpacing": "-0.055em",
                                    "fontWeight": "700",
                                    "color": "rgba(255,255,255,0.94)",
                                    "maxWidth": "780px",
                                    "marginBottom": "1.35rem",
                                },
                            ),
                            html.P(
                                slide["text"],
                                id="hero-text",
                                className="mb-4 reveal reveal-3",
                                style={
                                    "fontSize": "1.02rem",
                                    "lineHeight": "1.9",
                                    "color": "rgba(255,255,255,0.72)",
                                    "maxWidth": "640px",
                                    "marginBottom": "0",
                                },
                            ),
                        ],
                        style={"minWidth": "0"},
                    ),
                ],
                style={
                    "display": "flex",
                    "alignItems": "flex-start",
                    "marginBottom": "2rem",
                },
            ),
            html.Div(
                [
                    html.Div(
                        "Más de 70 años de experiencia",
                        className="me-4 mb-2 reveal reveal-4",
                        style={
                            "display": "inline-block",
                            "color": "rgba(255,255,255,0.88)",
                            "fontWeight": "600",
                            "fontSize": "0.95rem",
                        },
                    ),
                    html.Div(
                        "Asesoramiento fiscal, laboral y contable",
                        className="mb-2 reveal reveal-5",
                        style={
                            "display": "inline-block",
                            "color": "rgba(255,255,255,0.72)",
                            "fontWeight": "500",
                            "fontSize": "0.95rem",
                        },
                    ),
                ],
                className="mb-4",
                style={"maxWidth": "880px"},
            ),
            html.Div(
                [
                    dbc.Button(
                        "Solicitar información",
                        href=f"mailto:{EMAIL}",
                        color="light",
                        className="fw-semibold me-3 mb-2 reveal reveal-5",
                        style={
                            "padding": "0.95rem 1.45rem",
                            "minHeight": "54px",
                            "fontSize": "0.98rem",
                            "color": "#111827",
                            "background": "#ffffff",
                            "border": "none",
                            "borderRadius": "999px",
                            "boxShadow": "0 10px 22px rgba(0,0,0,0.14)",
                        },
                    ),
                    html.A(
                        f"Llamar: {TELEFONO_1}",
                        href=f"tel:{TELEFONO_1.replace(' ', '')}",
                        className="reveal reveal-6",
                        style={
                            "display": "inline-flex",
                            "alignItems": "center",
                            "minHeight": "54px",
                            "color": "rgba(255,255,255,0.92)",
                            "fontWeight": "600",
                            "fontSize": "0.98rem",
                            "textDecoration": "none",
                            "padding": "0.95rem 0",
                        },
                    ),
                ],
                className="mb-4",
            ),
            html.Div(
                id="hero-indicators",
                children=[
                    hero_indicator(i, active=(i == slide_index))
                    for i in range(len(HERO_SLIDES))
                ],
                className="reveal reveal-6",
                style={
                    "display": "flex",
                    "alignItems": "center",
                    "marginTop": "0.95rem",
                },
            ),
        ],
    )


def build_hero():
    slide = HERO_SLIDES[0]

    return html.Section(
        [
            dcc.Store(id="hero-slide-index", data=0),
            dcc.Interval(id="hero-autoplay", interval=5000, n_intervals=0),
            html.Div(
                id="hero-background",
                style={
                    "position": "absolute",
                    "inset": "0",
                    "backgroundImage": f"url('{slide['image']}')",
                    "backgroundSize": "cover",
                    "backgroundPosition": "center",
                    "transition": "background-image 0.7s ease-in-out",
                    "transform": "scale(1.02)",
                },
            ),
            html.Div(
                style={
                    "position": "absolute",
                    "inset": "0",
                    "background": (
                        "linear-gradient(90deg, rgba(8, 12, 20, 0.92) 0%, "
                        "rgba(8, 12, 20, 0.78) 42%, rgba(8, 12, 20, 0.42) 100%)"
                    ),
                }
            ),
            html.Div(
                style={
                    "position": "absolute",
                    "inset": "0",
                    "background": (
                        "linear-gradient(180deg, rgba(255,255,255,0.02) 0%, "
                        "rgba(255,255,255,0.00) 55%, rgba(0,0,0,0.12) 100%)"
                    ),
                    "zIndex": "1",
                }
            ),
            dbc.Container(
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                id="hero-content",
                                children=build_hero_content(0),
                                style={"maxWidth": "980px"},
                            ),
                            lg=9,
                            xl=8,
                            className="mb-5 mb-lg-0",
                        ),
                    ],
                    className="align-items-center",
                    style={
                        "minHeight": "88vh",
                        "position": "relative",
                        "zIndex": "2",
                        "paddingTop": "3rem",
                        "paddingBottom": "3rem",
                    },
                ),
                style={"position": "relative", "zIndex": "2"},
            ),
            html.Div(
                [
                    html.Button(
                        "←",
                        id="hero-prev",
                        n_clicks=0,
                        style={
                            "width": "52px",
                            "height": "52px",
                            "borderRadius": "999px",
                            "border": "1px solid rgba(255,255,255,0.14)",
                            "background": "rgba(255,255,255,0.08)",
                            "color": "white",
                            "fontSize": "1.2rem",
                            "backdropFilter": "blur(8px)",
                            "WebkitBackdropFilter": "blur(8px)",
                            "marginRight": "0.75rem",
                            "cursor": "pointer",
                        },
                    ),
                    html.Button(
                        "→",
                        id="hero-next",
                        n_clicks=0,
                        style={
                            "width": "52px",
                            "height": "52px",
                            "borderRadius": "999px",
                            "border": "1px solid rgba(255,255,255,0.14)",
                            "background": "rgba(255,255,255,0.08)",
                            "color": "white",
                            "fontSize": "1.2rem",
                            "backdropFilter": "blur(8px)",
                            "WebkitBackdropFilter": "blur(8px)",
                            "cursor": "pointer",
                        },
                    ),
                ],
                className="d-none d-lg-flex",
                style={
                    "position": "absolute",
                    "right": "40px",
                    "bottom": "38px",
                    "zIndex": "3",
                },
            ),
        ],
        className="section-fade",
        style={
            "position": "relative",
            "minHeight": "88vh",
            "overflow": "hidden",
        },
    )
