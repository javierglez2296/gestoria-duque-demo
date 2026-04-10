import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

from components.home.data import (
    TELEFONO_1,
    TELEFONO_2,
    EMAIL,
    DIRECCION,
    WHATSAPP_URL,
    HERO_SLIDES,
)


def hero_indicator(index, active=False):
    return html.Button(
        id={"type": "hero-indicator", "index": index},
        n_clicks=0,
        style={
            "width": "26px" if active else "10px",
            "height": "10px",
            "borderRadius": "999px",
            "border": "none",
            "padding": "0",
            "marginRight": "10px",
            "background": "#ffffff" if active else "rgba(255,255,255,0.30)",
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
                slide["eyebrow"],
                className="mb-4 reveal reveal-1",
                style={
                    "display": "inline-flex",
                    "alignItems": "center",
                    "padding": "0.62rem 0.95rem",
                    "borderRadius": "999px",
                    "background": "rgba(255,255,255,0.08)",
                    "border": "1px solid rgba(255,255,255,0.14)",
                    "backdropFilter": "blur(8px)",
                    "WebkitBackdropFilter": "blur(8px)",
                    "fontWeight": "700",
                    "fontSize": "0.75rem",
                    "letterSpacing": "0.12em",
                    "color": "rgba(255,255,255,0.92)",
                    "textTransform": "uppercase",
                },
            ),
            html.H1(
                slide["title"],
                className="fw-bold mb-4 reveal reveal-2",
                style={
                    "fontSize": "clamp(3rem, 5.1vw, 5.7rem)",
                    "lineHeight": "0.92",
                    "letterSpacing": "-0.075em",
                    "color": "#ffffff",
                    "maxWidth": "820px",
                },
            ),
            html.P(
                slide["text"],
                className="mb-4 reveal reveal-3",
                style={
                    "fontSize": "1.05rem",
                    "lineHeight": "1.95",
                    "color": "rgba(255,255,255,0.82)",
                    "maxWidth": "650px",
                },
            ),
            html.Div(
                [
                    html.Div(
                        "Desde 1950",
                        className="me-4 mb-2 reveal reveal-4",
                        style={
                            "display": "inline-block",
                            "color": "#ffffff",
                            "fontWeight": "700",
                            "fontSize": "0.98rem",
                        },
                    ),
                    html.Div(
                        "Fiscal · Laboral · Contable",
                        className="me-4 mb-2 reveal reveal-5",
                        style={
                            "display": "inline-block",
                            "color": "rgba(255,255,255,0.76)",
                            "fontWeight": "600",
                            "fontSize": "0.96rem",
                        },
                    ),
                    html.Div(
                        "Atención local en Ávila",
                        className="mb-2 reveal reveal-6",
                        style={
                            "display": "inline-block",
                            "color": "rgba(255,255,255,0.76)",
                            "fontWeight": "600",
                            "fontSize": "0.96rem",
                        },
                    ),
                ],
                className="mb-4",
            ),
            html.Div(
                [
                    dbc.Button(
                        "Solicitar información",
                        href=f"mailto:{EMAIL}",
                        color="light",
                        className="rounded-pill fw-bold me-2 mb-2 reveal reveal-5",
                        style={
                            "padding": "1rem 1.5rem",
                            "minHeight": "58px",
                            "fontSize": "1rem",
                            "color": "#101828",
                            "background": "#ffffff",
                            "border": "none",
                            "boxShadow": "0 18px 42px rgba(0,0,0,0.18)",
                        },
                    ),
                    dbc.Button(
                        "Llamar ahora",
                        href=f"tel:{TELEFONO_1.replace(' ', '')}",
                        color="link",
                        className="fw-semibold text-decoration-none mb-2 reveal reveal-6",
                        style={
                            "padding": "1rem 1rem",
                            "minHeight": "58px",
                            "fontSize": "1rem",
                            "color": "white",
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
                    "marginTop": "0.75rem",
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
                        "linear-gradient(90deg, rgba(7, 12, 22, 0.88) 0%, "
                        "rgba(7, 12, 22, 0.72) 38%, rgba(7, 12, 22, 0.42) 100%)"
                    ),
                }
            ),
            html.Div(
                style={
                    "position": "absolute",
                    "top": "-120px",
                    "right": "-100px",
                    "width": "320px",
                    "height": "320px",
                    "borderRadius": "999px",
                    "background": "rgba(255,255,255,0.06)",
                    "filter": "blur(40px)",
                    "zIndex": "1",
                }
            ),
            dbc.Container(
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(id="hero-content", children=build_hero_content(0)),
                            lg=7,
                            className="mb-5 mb-lg-0",
                        ),
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.Div(
                                            "Contacto",
                                            className="mb-3",
                                            style={
                                                "fontSize": "0.75rem",
                                                "letterSpacing": "0.14em",
                                                "textTransform": "uppercase",
                                                "fontWeight": "700",
                                                "color": "#98a2b3",
                                            },
                                        ),
                                        html.H2(
                                            "Una gestoría de confianza, con experiencia y trato cercano",
                                            className="fw-bold mb-4",
                                            style={
                                                "fontSize": "1.7rem",
                                                "lineHeight": "1.08",
                                                "letterSpacing": "-0.045em",
                                                "color": "#101828",
                                            },
                                        ),
                                        html.Div(
                                            [
                                                html.Div(
                                                    "Servicios principales",
                                                    className="fw-semibold mb-2",
                                                    style={"color": "#101828"},
                                                ),
                                                html.Div(
                                                    "Asesoría fiscal · laboral · contable · trámites",
                                                    className="mb-4",
                                                    style={
                                                        "color": "#667085",
                                                        "lineHeight": "1.8",
                                                    },
                                                ),
                                            ]
                                        ),
                                        html.Hr(style={"opacity": "0.08"}),
                                        html.Div("📞 Teléfono", className="fw-semibold mb-1", style={"color": "#101828"}),
                                        html.Div(TELEFONO_1, className="mb-3", style={"color": "#667085"}),
                                        html.Div("📱 Móvil", className="fw-semibold mb-1", style={"color": "#101828"}),
                                        html.Div(TELEFONO_2, className="mb-3", style={"color": "#667085"}),
                                        html.Div("✉️ Email", className="fw-semibold mb-1", style={"color": "#101828"}),
                                        html.Div(EMAIL, className="mb-3", style={"color": "#667085"}),
                                        html.Div("📍 Dirección", className="fw-semibold mb-1", style={"color": "#101828"}),
                                        html.Div(
                                            DIRECCION,
                                            className="mb-4",
                                            style={
                                                "color": "#667085",
                                                "lineHeight": "1.75",
                                            },
                                        ),
                                        dbc.Button(
                                            "Contactar por WhatsApp",
                                            href=WHATSAPP_URL,
                                            target="_blank",
                                            color="dark",
                                            className="w-100 rounded-pill fw-semibold mb-2",
                                            style={
                                                "padding": "1rem 1.2rem",
                                                "minHeight": "54px",
                                                "background": "#111827",
                                                "border": "none",
                                            },
                                        ),
                                        dbc.Button(
                                            "Enviar email",
                                            href=f"mailto:{EMAIL}",
                                            color="light",
                                            className="w-100 rounded-pill fw-semibold border",
                                            style={
                                                "padding": "1rem 1.2rem",
                                                "minHeight": "54px",
                                                "background": "#ffffff",
                                            },
                                        ),
                                    ]
                                ),
                                className="border-0 h-100",
                                style={
                                    "borderRadius": "30px",
                                    "background": "rgba(255,255,255,0.94)",
                                    "boxShadow": "0 32px 90px rgba(16, 24, 40, 0.18)",
                                    "backdropFilter": "blur(12px)",
                                    "WebkitBackdropFilter": "blur(12px)",
                                    "padding": "0.2rem",
                                },
                            ),
                            lg=5,
                            className="reveal reveal-4",
                        ),
                    ],
                    className="align-items-center",
                    style={"minHeight": "88vh", "position": "relative", "zIndex": "2"},
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
                            "width": "54px",
                            "height": "54px",
                            "borderRadius": "999px",
                            "border": "1px solid rgba(255,255,255,0.15)",
                            "background": "rgba(255,255,255,0.08)",
                            "color": "white",
                            "fontSize": "1.3rem",
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
                            "width": "54px",
                            "height": "54px",
                            "borderRadius": "999px",
                            "border": "1px solid rgba(255,255,255,0.15)",
                            "background": "rgba(255,255,255,0.08)",
                            "color": "white",
                            "fontSize": "1.3rem",
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
