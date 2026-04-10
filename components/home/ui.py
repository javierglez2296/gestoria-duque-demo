from dash import html
import dash_bootstrap_components as dbc


def section_tag(text):
    return html.Div(
        text,
        className="text-uppercase fw-bold mb-3 reveal-up",
        style={
            "fontSize": "0.76rem",
            "letterSpacing": "0.18em",
            "color": "#667085",
        },
    )


def stat_card(value, label):
    return dbc.Col(
        dbc.Card(
            dbc.CardBody(
                [
                    html.Div(
                        value,
                        className="fw-bold mb-1",
                        style={
                            "fontSize": "clamp(1.9rem, 3vw, 2.6rem)",
                            "lineHeight": "1",
                            "letterSpacing": "-0.05em",
                            "color": "#101828",
                        },
                    ),
                    html.Div(
                        label,
                        style={
                            "color": "#667085",
                            "fontSize": "0.96rem",
                            "lineHeight": "1.5",
                        },
                    ),
                ]
            ),
            className="border-0 h-100",
            style={
                "borderRadius": "24px",
                "background": "rgba(255,255,255,0.92)",
                "boxShadow": "0 18px 44px rgba(16, 24, 40, 0.06)",
            },
        ),
        md=4,
        className="mb-3 reveal-up",
    )


def service_card(icono, titulo, texto):
    return dbc.Col(
        dbc.Card(
            dbc.CardBody(
                [
                    html.Div(
                        icono,
                        className="mb-4",
                        style={
                            "width": "58px",
                            "height": "58px",
                            "display": "flex",
                            "alignItems": "center",
                            "justifyContent": "center",
                            "fontSize": "1.65rem",
                            "borderRadius": "18px",
                            "background": "linear-gradient(135deg, #eef4ff 0%, #f8fbff 100%)",
                            "boxShadow": "inset 0 1px 0 rgba(255,255,255,0.8)",
                        },
                    ),
                    html.H3(
                        titulo,
                        className="fw-bold mb-2",
                        style={
                            "fontSize": "1.14rem",
                            "letterSpacing": "-0.02em",
                            "color": "#101828",
                        },
                    ),
                    html.P(
                        texto,
                        className="mb-0",
                        style={
                            "color": "#667085",
                            "lineHeight": "1.85",
                            "fontSize": "0.97rem",
                        },
                    ),
                ]
            ),
            className="border-0 h-100",
            style={
                "borderRadius": "26px",
                "background": "rgba(255,255,255,0.96)",
                "boxShadow": "0 18px 46px rgba(16, 24, 40, 0.06)",
            },
        ),
        lg=4,
        md=6,
        className="mb-4 reveal-up",
    )


def pillar_card(numero, titulo, texto):
    return dbc.Col(
        dbc.Card(
            dbc.CardBody(
                [
                    html.Div(
                        numero,
                        className="fw-bold mb-3",
                        style={
                            "fontSize": "0.82rem",
                            "letterSpacing": "0.18em",
                            "color": "#0d6efd",
                        },
                    ),
                    html.H3(
                        titulo,
                        className="fw-bold mb-2",
                        style={
                            "fontSize": "1.2rem",
                            "letterSpacing": "-0.03em",
                            "color": "#101828",
                        },
                    ),
                    html.P(
                        texto,
                        className="mb-0",
                        style={
                            "color": "#667085",
                            "lineHeight": "1.85",
                        },
                    ),
                ]
            ),
            className="border-0 h-100",
            style={
                "borderRadius": "26px",
                "background": "#ffffff",
                "boxShadow": "0 16px 40px rgba(16, 24, 40, 0.06)",
            },
        ),
        md=4,
        className="mb-4 reveal-up",
    )


def list_check(text):
    return html.Div(
        [
            html.Span("●", className="me-2", style={"color": "#0d6efd"}),
            html.Span(text),
        ],
        className="mb-3",
        style={
            "color": "#344054",
            "fontWeight": "600",
            "lineHeight": "1.6",
        },
    )


def process_card(numero, titulo, texto):
    return dbc.Col(
        html.Div(
            [
                html.Div(
                    numero,
                    className="fw-bold mb-3",
                    style={
                        "fontSize": "0.82rem",
                        "letterSpacing": "0.18em",
                        "color": "#0d6efd",
                    },
                ),
                html.H3(
                    titulo,
                    className="fw-bold mb-2",
                    style={
                        "fontSize": "1.22rem",
                        "letterSpacing": "-0.03em",
                        "color": "#101828",
                    },
                ),
                html.P(
                    texto,
                    className="mb-0",
                    style={
                        "color": "#667085",
                        "lineHeight": "1.85",
                        "maxWidth": "320px",
                    },
                ),
            ],
            style={"padding": "1.2rem 0.25rem"},
        ),
        md=4,
        className="mb-4 reveal-up",
    )


def testimonial_card(nombre, texto):
    return dbc.Col(
        dbc.Card(
            dbc.CardBody(
                [
                    html.Div(
                        "★★★★★",
                        className="mb-3",
                        style={
                            "color": "#f59e0b",
                            "fontSize": "0.96rem",
                            "letterSpacing": "0.08em",
                        },
                    ),
                    html.P(
                        f"“{texto}”",
                        className="mb-4",
                        style={
                            "color": "#344054",
                            "lineHeight": "1.95",
                            "fontSize": "0.98rem",
                        },
                    ),
                    html.Div(
                        nombre,
                        className="fw-semibold",
                        style={"color": "#101828"},
                    ),
                ]
            ),
            className="border-0 h-100",
            style={
                "borderRadius": "26px",
                "background": "linear-gradient(180deg, #ffffff 0%, #fbfcfe 100%)",
                "boxShadow": "0 18px 44px rgba(16, 24, 40, 0.06)",
            },
        ),
        md=4,
        className="mb-4 reveal-up",
    )
