from dash import html
import dash_bootstrap_components as dbc

from components.home.data import (
    TELEFONO_1,
    EMAIL,
    DIRECCION,
    WHATSAPP_URL,
    SERVICIOS,
    PILARES,
    SERVICIO_DESTACADO,
    PROCESO,
    TESTIMONIOS,
    FAQS,
)
from components.home.ui import (
    section_tag,
    stat_card,
    service_card,
    pillar_card,
    list_check,
    process_card,
    testimonial_card,
)


def build_stats_section():
    return html.Section(
        dbc.Container(
            dbc.Row(
                [
                    stat_card("Desde 1950", "Trayectoria y experiencia"),
                    stat_card("Ávila", "Presencia local y cercanía"),
                    stat_card("Integral", "Fiscal, laboral, contable y trámites"),
                ],
                className="g-3",
            )
        ),
        className="section-fade",
        style={"paddingTop": "3rem", "paddingBottom": "4rem"},
    )


def build_services_section():
    return html.Section(
        dbc.Container(
            [
                section_tag("Servicios"),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H2(
                                    "Diseñada para que el visitante entienda rápido qué hacéis y por qué merece la pena contactar",
                                    className="fw-bold mb-3 reveal-up",
                                    style={
                                        "fontSize": "clamp(2.1rem, 3.7vw, 3.25rem)",
                                        "lineHeight": "1.02",
                                        "letterSpacing": "-0.055em",
                                        "color": "#101828",
                                        "maxWidth": "820px",
                                    },
                                ),
                                html.P(
                                    "Aquí la web ya no parece una lista tradicional de servicios. Tiene más ritmo, más aire y una percepción mucho más premium.",
                                    className="mb-5 reveal-up",
                                    style={
                                        "color": "#667085",
                                        "lineHeight": "1.92",
                                        "maxWidth": "820px",
                                        "fontSize": "1.02rem",
                                    },
                                ),
                            ]
                        )
                    ]
                ),
                dbc.Row([service_card(s["icono"], s["titulo"], s["texto"]) for s in SERVICIOS]),
            ]
        ),
        id="servicios",
        className="section-fade",
        style={
            "paddingTop": "3rem",
            "paddingBottom": "4.8rem",
            "scrollMarginTop": "120px",
        },
    )


def build_pillars_section():
    return html.Section(
        dbc.Container(
            [
                section_tag("Pilares"),
                dbc.Row(
                    [
                        dbc.Col(
                            html.H2(
                                "Una gestoría local puede parecer muchísimo más potente con una presentación adecuada",
                                className="fw-bold mb-4 reveal-up",
                                style={
                                    "fontSize": "clamp(2rem, 3.4vw, 3rem)",
                                    "lineHeight": "1.04",
                                    "letterSpacing": "-0.05em",
                                    "color": "#101828",
                                    "maxWidth": "760px",
                                },
                            ),
                            lg=7,
                        ),
                        dbc.Col(
                            html.P(
                                "No se trata solo de diseño. Se trata de percepción, confianza y capacidad de convertir una visita en una llamada.",
                                className="mb-4 mb-lg-0 reveal-up",
                                style={
                                    "color": "#667085",
                                    "lineHeight": "1.9",
                                    "maxWidth": "520px",
                                },
                            ),
                            lg=5,
                            className="d-flex align-items-end",
                        ),
                    ],
                    className="mb-2",
                ),
                dbc.Row([pillar_card(p["numero"], p["titulo"], p["texto"]) for p in PILARES]),
            ]
        ),
        className="section-fade",
        style={
            "paddingTop": "4.6rem",
            "paddingBottom": "4.6rem",
            "background": "#f8fafc",
        },
    )


def build_featured_section():
    return html.Section(
        dbc.Container(
            dbc.Card(
                dbc.CardBody(
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    section_tag("Enfoque"),
                                    html.H2(
                                        "Más de 70 años ayudando a clientes en Ávila",
                                        className="fw-bold mb-3 reveal-up",
                                        style={
                                            "fontSize": "clamp(2rem, 3vw, 2.7rem)",
                                            "lineHeight": "1.05",
                                            "letterSpacing": "-0.04em",
                                            "color": "#101828",
                                        },
                                    ),
                                    html.P(
                                        "La experiencia del despacho es una ventaja enorme. Esta sección la convierte en algo visible, memorable y comercialmente útil.",
                                        className="mb-4 mb-lg-0 reveal-up",
                                        style={
                                            "color": "#667085",
                                            "lineHeight": "1.9",
                                            "maxWidth": "720px",
                                        },
                                    ),
                                ],
                                lg=7,
                                className="mb-4 mb-lg-0",
                            ),
                            dbc.Col(
                                [list_check(text) for text in SERVICIO_DESTACADO],
                                lg=5,
                                className="d-flex flex-column justify-content-center reveal-up",
                            ),
                        ]
                    )
                ),
                className="border-0",
                style={
                    "borderRadius": "30px",
                    "background": "linear-gradient(135deg, #ffffff 0%, #f8fbff 100%)",
                    "boxShadow": "0 24px 62px rgba(16, 24, 40, 0.08)",
                },
            )
        ),
        className="section-fade",
        style={"paddingBottom": "4.8rem"},
    )


def build_process_section():
    return html.Section(
        dbc.Container(
            [
                section_tag("Proceso"),
                dbc.Row(
                    [
                        dbc.Col(
                            html.H2(
                                "Una experiencia simple y elegante ayuda a reducir fricción y a generar más contacto",
                                className="fw-bold mb-4 reveal-up",
                                style={
                                    "fontSize": "clamp(2rem, 3.35vw, 3rem)",
                                    "lineHeight": "1.04",
                                    "letterSpacing": "-0.05em",
                                    "color": "#101828",
                                    "maxWidth": "780px",
                                },
                            ),
                            lg=7,
                        ),
                        dbc.Col(
                            html.P(
                                "Cuando el proceso se entiende rápido, el visitante siente menos distancia y más confianza para dar el paso.",
                                className="mb-4 mb-lg-0 reveal-up",
                                style={
                                    "color": "#667085",
                                    "lineHeight": "1.9",
                                    "maxWidth": "520px",
                                },
                            ),
                            lg=5,
                            className="d-flex align-items-end",
                        ),
                    ],
                    className="mb-3",
                ),
                dbc.Row([process_card(p["numero"], p["titulo"], p["texto"]) for p in PROCESO]),
            ]
        ),
        className="section-fade",
        style={"paddingTop": "4.6rem", "paddingBottom": "4.6rem"},
    )


def build_testimonials_section():
    return html.Section(
        dbc.Container(
            [
                section_tag("Opiniones"),
                html.H2(
                    "La confianza aumenta mucho cuando la imagen se apoya en testimonios reales",
                    className="fw-bold mb-3 reveal-up",
                    style={
                        "fontSize": "clamp(2rem, 3.2vw, 3rem)",
                        "lineHeight": "1.04",
                        "letterSpacing": "-0.05em",
                        "color": "#101828",
                        "maxWidth": "780px",
                    },
                ),
                html.P(
                    "En la versión final sustituiría estos ejemplos por reseñas reales de Google o testimonios auténticos del despacho.",
                    className="mb-5 reveal-up",
                    style={
                        "color": "#667085",
                        "lineHeight": "1.9",
                        "maxWidth": "780px",
                    },
                ),
                dbc.Row([testimonial_card(t["nombre"], t["texto"]) for t in TESTIMONIOS]),
            ]
        ),
        className="section-fade",
        style={
            "paddingTop": "4.6rem",
            "paddingBottom": "4.6rem",
            "background": "#f8fafc",
        },
    )


def build_seo_section():
    return html.Section(
        dbc.Container(
            [
                section_tag("SEO local"),
                html.H2(
                    "Gestoría en Ávila con enfoque fiscal, laboral, contable y administrativo",
                    className="fw-bold mb-3 reveal-up",
                    style={
                        "fontSize": "clamp(1.95rem, 3vw, 2.65rem)",
                        "lineHeight": "1.06",
                        "letterSpacing": "-0.04em",
                        "color": "#101828",
                        "maxWidth": "860px",
                    },
                ),
                html.P(
                    "Esta home está pensada para apoyar búsquedas como gestoría en Ávila, asesoría fiscal en Ávila, asesoría laboral en Ávila, gestoría para autónomos en Ávila o asesoría contable en Ávila. Además, mejora mucho la percepción del despacho al explicar mejor qué hace, a quién ayuda y cómo contactar.",
                    className="mb-0 reveal-up",
                    style={
                        "color": "#667085",
                        "lineHeight": "1.95",
                        "maxWidth": "1040px",
                    },
                ),
            ]
        ),
        className="section-fade",
        style={"paddingTop": "4.6rem", "paddingBottom": "4.6rem"},
    )


def build_faq_section():
    return html.Section(
        dbc.Container(
            [
                section_tag("Preguntas frecuentes"),
                html.H2(
                    "Dudas habituales antes de contactar con una gestoría",
                    className="fw-bold mb-4 reveal-up",
                    style={
                        "fontSize": "clamp(1.9rem, 3vw, 2.5rem)",
                        "lineHeight": "1.06",
                        "letterSpacing": "-0.04em",
                        "color": "#101828",
                    },
                ),
                dbc.Accordion(
                    [
                        dbc.AccordionItem(
                            html.P(
                                texto,
                                className="mb-0",
                                style={"color": "#667085", "lineHeight": "1.8"},
                            ),
                            title=pregunta,
                        )
                        for pregunta, texto in FAQS
                    ],
                    start_collapsed=True,
                    always_open=False,
                ),
            ]
        ),
        className="section-fade",
        style={
            "paddingTop": "4.6rem",
            "paddingBottom": "4.6rem",
            "background": "#f8fafc",
        },
    )


def build_cta_section():
    return html.Section(
        dbc.Container(
            dbc.Card(
                dbc.CardBody(
                    [
                        section_tag("Contacto"),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.H2(
                                            "Una mejor imagen digital suele traducirse en más llamadas y más contactos",
                                            className="fw-bold mb-3 reveal-up",
                                            style={
                                                "fontSize": "clamp(2rem, 3.45vw, 3rem)",
                                                "lineHeight": "1.03",
                                                "letterSpacing": "-0.05em",
                                                "color": "#101828",
                                                "maxWidth": "780px",
                                            },
                                        ),
                                        html.P(
                                            "Esta demo está pensada para que el visitante entienda rápido el valor del despacho y vea fácil el siguiente paso.",
                                            className="mb-0 reveal-up",
                                            style={
                                                "color": "#667085",
                                                "lineHeight": "1.9",
                                                "maxWidth": "700px",
                                            },
                                        ),
                                    ],
                                    lg=8,
                                    className="mb-4 mb-lg-0",
                                ),
                                dbc.Col(
                                    [
                                        dbc.Button(
                                            "Llamar ahora",
                                            href=f"tel:{TELEFONO_1.replace(' ', '')}",
                                            color="primary",
                                            className="w-100 rounded-pill fw-bold mb-2",
                                            style={
                                                "padding": "1rem 1.4rem",
                                                "minHeight": "56px",
                                                "boxShadow": "0 12px 30px rgba(13, 110, 253, 0.22)",
                                            },
                                        ),
                                        dbc.Button(
                                            "WhatsApp",
                                            href=WHATSAPP_URL,
                                            target="_blank",
                                            color="success",
                                            className="w-100 rounded-pill fw-bold mb-2",
                                            style={"padding": "1rem 1.4rem", "minHeight": "56px"},
                                        ),
                                        dbc.Button(
                                            "Enviar email",
                                            href=f"mailto:{EMAIL}",
                                            color="light",
                                            className="w-100 rounded-pill fw-semibold border",
                                            style={"padding": "1rem 1.4rem", "minHeight": "56px"},
                                        ),
                                    ],
                                    lg=4,
                                    className="reveal-up",
                                ),
                            ]
                        ),
                    ]
                ),
                className="border-0",
                style={
                    "borderRadius": "30px",
                    "background": "linear-gradient(180deg, #ffffff 0%, #fbfcfe 100%)",
                    "boxShadow": "0 26px 76px rgba(16, 24, 40, 0.10)",
                },
            )
        ),
        id="contacto",
        className="section-fade",
        style={
            "paddingTop": "2rem",
            "paddingBottom": "5rem",
            "scrollMarginTop": "120px",
        },
    )


def build_footer_section():
    return html.Footer(
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Div(
                                "Gestoría Duque · Demo",
                                className="fw-bold mb-2 reveal-up",
                                style={
                                    "color": "#101828",
                                    "fontSize": "1.05rem",
                                    "letterSpacing": "-0.02em",
                                },
                            ),
                            html.Div(
                                "Propuesta visual de renovación web con enfoque premium, local y comercial.",
                                className="reveal-up",
                                style={"color": "#667085", "lineHeight": "1.8"},
                            ),
                        ],
                        md=6,
                        className="mb-4 mb-md-0",
                    ),
                    dbc.Col(
                        [
                            html.Div(f"📍 {DIRECCION}", className="mb-2 reveal-up", style={"color": "#667085"}),
                            html.Div(f"📞 {TELEFONO_1}", className="mb-2 reveal-up", style={"color": "#667085"}),
                            html.Div(f"✉️ {EMAIL}", className="reveal-up", style={"color": "#667085"}),
                        ],
                        md=6,
                        className="text-md-end",
                    ),
                ]
            )
        ),
        className="section-fade",
        style={
            "paddingTop": "2rem",
            "paddingBottom": "2.5rem",
            "borderTop": "1px solid rgba(15, 23, 42, 0.08)",
            "background": "#ffffff",
        },
    )


def build_floating_whatsapp():
    return html.A(
        "WhatsApp",
        href=WHATSAPP_URL,
        target="_blank",
        style={
            "position": "fixed",
            "right": "22px",
            "bottom": "22px",
            "zIndex": "999",
            "background": "linear-gradient(135deg, #25D366 0%, #1fb85a 100%)",
            "color": "white",
            "textDecoration": "none",
            "padding": "0.95rem 1.2rem",
            "borderRadius": "999px",
            "fontWeight": "700",
            "letterSpacing": "0.01em",
            "boxShadow": "0 16px 34px rgba(0, 0, 0, 0.18)",
        },
    )
