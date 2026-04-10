from dash import html
import dash_bootstrap_components as dbc


def section_tag(text):
    return html.Div(
        text,
        className="text-uppercase fw-bold mb-3 reveal-up",
        style={
            "fontSize": "0.75rem",
            "letterSpacing": "0.18em",
            "color": "#6b7280",
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
                            "fontSize": "clamp(1.8rem, 2.8vw, 2.4rem)",
                            "lineHeight": "1",
                            "letterSpacing": "-0.045em",
                            "color": "#111827",
                        },
                    ),
                    html.Div(
                        label,
                        style={
                            "color": "#6b7280",
                            "fontSize": "0.95rem",
                            "lineHeight": "1.55",
                        },
                    ),
                ]
            ),
            className="border-0 h-100",
            style={
                "borderRadius": "18px",
                "background": "#ffffff",
                "border": "1px solid rgba(17, 24, 39, 0.06)",
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
                            "width": "54px",
                            "height": "54px",
                            "display": "flex",
                            "alignItems": "center",
                            "justifyContent": "center",
                            "fontSize": "1.45rem",
                            "borderRadius": "14px",
                            "background": "#f8fafc",
                            "border": "1px solid rgba(17, 24, 39, 0.05)",
                        },
                    ),
                    html.H3(
                        titulo,
                        className="fw-semibold mb-2",
                        style={
                            "fontSize": "1.08rem",
                            "letterSpacing": "-0.02em",
                            "color": "#111827",
                            "lineHeight": "1.35",
                        },
                    ),
                    html.P(
                        texto,
                        className="mb-0",
                        style={
                            "color": "#6b7280",
                            "lineHeight": "1.82",
                            "fontSize": "0.96rem",
                        },
                    ),
                ]
            ),
            className="border-0 h-100",
            style={
                "borderRadius": "20px",
                "background": "#ffffff",
                "border": "1px solid rgba(17, 24, 39, 0.06)",
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
                            "fontSize": "0.8rem",
                            "letterSpacing": "0.18em",
                            "color": "#6b7280",
                        },
                    ),
                    html.H3(
                        titulo,
                        className="fw-semibold mb-2",
                        style={
                            "fontSize": "1.12rem",
                            "letterSpacing": "-0.02em",
                            "color": "#111827",
                            "lineHeight": "1.35",
                        },
                    ),
                    html.P(
                        texto,
                        className="mb-0",
                        style={
                            "color": "#6b7280",
                            "lineHeight": "1.82",
                            "fontSize": "0.96rem",
                        },
                    ),
                ]
            ),
            className="border-0 h-100",
            style={
                "borderRadius": "20px",
                "background": "#ffffff",
                "border": "1px solid rgba(17, 24, 39, 0.06)",
            },
        ),
        md=4,
        className="mb-4 reveal-up",
    )


def list_check(text):
    return html.Div(
        [
            html.Span(
                "—",
                className="me-2",
                style={
                    "color": "#111827",
                    "fontWeight": "700",
                },
            ),
            html.Span(text),
        ],
        className="mb-3",
        style={
            "color": "#374151",
            "fontWeight": "600",
            "lineHeight": "1.65",
            "fontSize": "0.97rem",
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
                        "fontSize": "0.8rem",
                        "letterSpacing": "0.18em",
                        "color": "#6b7280",
                    },
                ),
                html.H3(
                    titulo,
                    className="fw-semibold mb-2",
                    style={
                        "fontSize": "1.12rem",
                        "letterSpacing": "-0.02em",
                        "color": "#111827",
                        "lineHeight": "1.35",
                    },
                ),
                html.P(
                    texto,
                    className="mb-0",
                    style={
                        "color": "#6b7280",
                        "lineHeight": "1.82",
                        "maxWidth": "320px",
                        "fontSize": "0.96rem",
                    },
                ),
            ],
            style={
                "padding": "1.1rem 0.25rem",
            },
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
                            "color": "#a16207",
                            "fontSize": "0.92rem",
                            "letterSpacing": "0.08em",
                        },
                    ),
                    html.P(
                        f"“{texto}”",
                        className="mb-4",
                        style={
                            "color": "#374151",
                            "lineHeight": "1.9",
                            "fontSize": "0.97rem",
                        },
                    ),
                    html.Div(
                        nombre,
                        className="fw-semibold",
                        style={"color": "#111827"},
                    ),
                ]
            ),
            className="border-0 h-100",
            style={
                "borderRadius": "20px",
                "background": "#ffffff",
                "border": "1px solid rgba(17, 24, 39, 0.06)",
            },
        ),
        md=4,
        className="mb-4 reveal-up",
    )
