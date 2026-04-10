from dash import html
import dash_bootstrap_components as dbc


# =========================================================
# SECTION TAG (EYEBROW)
# =========================================================
def section_tag(text):
    return html.Div(
        text,
        className="fw-semibold mb-3",
        style={
            "fontSize": "0.72rem",
            "letterSpacing": "0.18em",
            "textTransform": "uppercase",
            "color": "#9ca3af",
        },
    )


# =========================================================
# SECTION TITLE
# =========================================================
def section_title(text):
    return html.H2(
        text,
        className="fw-semibold mb-3",
        style={
            "fontSize": "clamp(1.8rem, 2.6vw, 2.4rem)",
            "letterSpacing": "-0.03em",
            "color": "#111827",
        },
    )


# =========================================================
# SECTION SUBTITLE
# =========================================================
def section_subtitle(text):
    return html.P(
        text,
        className="mb-0",
        style={
            "color": "#6b7280",
            "fontSize": "1.05rem",
            "lineHeight": "1.7",
            "maxWidth": "680px",
        },
    )


# =========================================================
# STAT CARD (ULTRA CLEAN)
# =========================================================
def stat_card(value, label):
    return dbc.Col(
        dbc.Card(
            dbc.CardBody(
                [
                    html.Div(
                        value,
                        className="fw-semibold",
                        style={
                            "fontSize": "clamp(2rem, 3vw, 2.6rem)",
                            "letterSpacing": "-0.04em",
                            "color": "#111827",
                            "lineHeight": "1",
                        },
                    ),
                    html.Div(
                        label,
                        className="mt-2",
                        style={
                            "color": "#6b7280",
                            "fontSize": "0.95rem",
                        },
                    ),
                ]
            ),
            className="h-100 border-0 stat-card-premium",
        ),
        md=4,
        className="mb-4",
    )


# =========================================================
# FEATURE CARD (SERVICIOS)
# =========================================================
def feature_card(title, text, icon=None):
    return dbc.Col(
        dbc.Card(
            dbc.CardBody(
                [
                    html.Div(
                        icon if icon else "•",
                        style={
                            "fontSize": "1.2rem",
                            "color": "#111827",
                            "marginBottom": "12px",
                        },
                    ),
                    html.H5(
                        title,
                        className="fw-semibold",
                        style={
                            "fontSize": "1.1rem",
                            "color": "#111827",
                            "letterSpacing": "-0.01em",
                        },
                    ),
                    html.P(
                        text,
                        style={
                            "color": "#6b7280",
                            "fontSize": "0.95rem",
                            "lineHeight": "1.7",
                        },
                    ),
                ]
            ),
            className="border-0 h-100 feature-card-premium",
        ),
        md=4,
        className="mb-4",
    )


# =========================================================
# CTA BUTTON (TOLEDO STYLE)
# =========================================================
def cta_button(text, href="#"):
    return dbc.Button(
        text,
        href=href,
        className="px-4 py-2 fw-semibold",
        style={
            "backgroundColor": "#111827",
            "border": "none",
            "borderRadius": "8px",
            "fontSize": "0.95rem",
        },
    )


# =========================================================
# SECTION WRAPPER
# =========================================================
def section_block(children, light=False):
    return html.Section(
        dbc.Container(children, fluid="lg"),
        style={
            "paddingTop": "90px",
            "paddingBottom": "90px",
            "backgroundColor": "#f9fafb" if light else "#ffffff",
        },
    )
