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
                            "background": "rgba(255,255,255,0.90)",
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
                                    "fontSize": "clamp(2.55rem, 4.5vw, 4.85rem)",
                                    "lineHeight": "0.98",
                                    "letterSpacing": "-0.055em",
                                    "fontWeight": "700",
                                    "color": "#ffffff",
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
                                    "color": "rgba(255,255,255,0.82)",
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
                        className="me-4 mb-2 reveal reveal-5",
                        style={
                            "display": "inline-block",
                            "color": "rgba(255,255,255,0.72)",
                            "fontWeight": "500",
                            "fontSize": "0.95rem",
                        },
                    ),
                    html.Div(
                        "Atención cercana en Ávila",
                        className="mb-2 reveal reveal-6",
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
                            "boxShadow": "0 16px 34px rgba(0,0,0,0.16)",
                        },
                    ),
                    html.A(
                        "Llamar ahora",
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


def build_contact_card():
    return dbc.Card(
        dbc.CardBody(
            [
                html.Div(
                    "Contacto directo",
                    className="mb-3",
                    style={
                        "fontSize": "0.76rem",
                        "letterSpacing": "0.16em",
                        "textTransform": "uppercase",
                        "fontWeight": "700",
                        "color": "#4b5563",
                    },
                ),
                html.H2(
                    "Soluciones profesionales con trayectoria y trato cercano",
                    className="mb-4",
                    style={
                        "fontSize": "1.55rem",
                        "lineHeight": "1.18",
                        "letterSpacing": "-0.03em",
                        "fontWeight": "700",
                        "color": "#111827",
                        "maxWidth": "520px",
                    },
                ),
                html.P(
                    "Asesoramiento fiscal, laboral y contable para empresas, autónomos y particulares, con una atención clara, profesional y personalizada.",
                    className="mb-4",
                    style={
                        "color": "#6b7280",
                        "lineHeight": "1.85",
                        "fontSize": "0.98rem",
                    },
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    "Desde 1950",
                                    style={
                                        "fontWeight": "700",
                                        "fontSize": "1.05rem",
                                        "color": "#111827",
                                        "marginBottom": "0.2rem",
                                    },
                                ),
                                html.Div(
                                    "Trayectoria consolidada",
                                    style={
                                        "fontSize": "0.92rem",
                                        "color": "#6b7280",
                                    },
                                ),
                            ],
                            style={
                                "padding": "1rem 1.1rem",
                                "border": "1px solid rgba(17, 24, 39, 0.08)",
                                "borderRadius": "18px",
                                "background": "#f8fafc",
                            },
                        ),
                        html.Div(
                            [
                                html.Div(
                                    "Ávila",
                                    style={
                                        "fontWeight": "700",
                                        "fontSize": "1.05rem",
                                        "color": "#111827",
                                        "marginBottom": "0.2rem",
                                    },
                                ),
                                html.Div(
                                    "Cercanía y atención local",
                                    style={
                                        "fontSize": "0.92rem",
                                        "color": "#6b7280",
                                    },
                                ),
                            ],
                            style={
                                "padding": "1rem 1.1rem",
                                "border": "1px solid rgba(17, 24, 39, 0.08)",
                                "borderRadius": "18px",
                                "background": "#f8fafc",
                            },
                        ),
                    ],
                    style={
                        "display": "grid",
                        "gridTemplateColumns": "1fr 1fr",
                        "gap": "0.9rem",
                        "marginBottom": "1.45rem",
                    },
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    "Teléfono",
                                    className="mb-1",
                                    style={
                                        "fontWeight": "600",
                                        "color": "#111827",
                                    },
                                ),
                                html.Div(
                                    TELEFONO_1,
                                    style={
                                        "color": "#6b7280",
                                        "fontSize": "0.98rem",
                                    },
                                ),
                            ],
                            className="mb-3",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    "Móvil",
                                    className="mb-1",
                                    style={
                                        "fontWeight": "600",
                                        "color": "#111827",
                                    },
                                ),
                                html.Div(
                                    TELEFONO_2,
                                    style={
                                        "color": "#6b7280",
                                        "fontSize": "0.98rem",
                                    },
                                ),
                            ],
                            className="mb-3",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    "Email",
                                    className="mb-1",
                                    style={
                                        "fontWeight": "600",
                                        "color": "#111827",
                                    },
                                ),
                                html.Div(
                                    EMAIL,
                                    style={
                                        "color": "#6b7280",
                                        "fontSize": "0.98rem",
                                        "wordBreak": "break-word",
                                    },
                                ),
                            ],
                            className="mb-3",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    "Dirección",
                                    className="mb-1",
                                    style={
                                        "fontWeight": "600",
                                        "color": "#111827",
                                    },
                                ),
                                html.Div(
                                    DIRECCION,
                                    style={
                                        "color": "#6b7280",
                                        "fontSize": "0.98rem",
                                        "lineHeight": "1.75",
                                    },
                                ),
                            ],
                            className="mb-4",
                        ),
                    ],
                    style={
                        "paddingTop": "1rem",
                        "borderTop": "1px solid rgba(17, 24, 39, 0.08)",
                    },
                ),
                dbc.Button(
                    "Solicitar información",
                    href=f"mailto:{EMAIL}",
                    color="dark",
                    className="w-100 fw-semibold mb-2",
                    style={
                        "padding": "0.95rem 1.2rem",
                        "minHeight": "54px",
                        "borderRadius": "999px",
                        "background": "#111827",
                        "border": "none",
                        "fontSize": "0.98rem",
                    },
                ),
                dbc.Button(
                    "Contactar por WhatsApp",
                    href=WHATSAPP_URL,
                    target="_blank",
                    color="light",
                    className="w-100 fw-semibold border-0",
                    style={
                        "padding": "0.95rem 1.2rem",
                        "minHeight": "54px",
                        "borderRadius": "999px",
                        "background": "#eef2f7",
                        "color": "#111827",
                        "fontSize": "0.98rem",
                    },
                ),
            ]
        ),
        className="border-0 h-100",
        style={
            "borderRadius": "28px",
            "background": "rgba(255,255,255,0.94)",
            "boxShadow": "0 30px 80px rgba(15, 23, 42, 0.18)",
            "backdropFilter": "blur(10px)",
            "WebkitBackdropFilter": "blur(10px)",
            "padding": "0.25rem",
        },
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
                        "linear-gradient(90deg, rgba(8, 12, 20, 0.84) 0%, "
                        "rgba(8, 12, 20, 0.70) 34%, rgba(8, 12, 20, 0.38) 100%)"
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
                                style={"paddingRight": "1.2rem"},
                            ),
                            lg=7,
                            className="mb-5 mb-lg-0",
                        ),
                        dbc.Col(
                            build_contact_card(),
                            lg=5,
                            className="reveal reveal-4",
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
