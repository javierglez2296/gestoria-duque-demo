from dash import html
import dash_bootstrap_components as dbc

from components.home.data import (
    DIRECCION,
    TELEFONO_1,
    EMAIL,
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


def build_trust_section():
    items = [
        ("Desde 1950", "Trayectoria consolidada"),
        ("Atención cercana", "Relación directa y profesional"),
        ("Servicio integral", "Fiscal, laboral y contable"),
        ("Ávila", "Despacho local de confianza"),
    ]

    return html.Div(
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            [
                                html.Div(
                                    titulo,
                                    className="fw-semibold mb-1",
                                    style={
                                        "color": "#111827",
                                        "fontSize": "1rem",
                                        "letterSpacing": "-0.02em",
                                    },
                                ),
                                html.Div(
                                    texto,
                                    style={
                                        "color": "#6b7280",
                                        "fontSize": "0.93rem",
                                        "lineHeight": "1.7",
                                    },
                                ),
                            ],
                            className="h-100",
                            style={
                                "padding": "1.15rem 1rem",
                                "borderRadius": "16px",
                                "background": "#ffffff",
                                "border": "1px solid rgba(17, 24, 39, 0.06)",
                            },
                        ),
                        lg=3,
                        md=6,
                        className="mb-3 reveal-up",
                    )
                    for titulo, texto in items
                ],
                className="g-3",
            )
        ),
        className="section-fade",
        style={
            "paddingTop": "2rem",
            "paddingBottom": "2.8rem",
            "background": "#ffffff",
        },
    )


def build_stats_section():
    return html.Div(
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
        style={"paddingTop": "2.5rem", "paddingBottom": "4rem"},
    )


def build_services_section():
    return html.Div(
        dbc.Container(
            [
                section_tag("Servicios"),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H2(
                                    "Servicios de asesoría fiscal, laboral, contable y administrativa en Ávila",
                                    className="fw-bold mb-3 reveal-up",
                                    style={
                                        "fontSize": "clamp(2rem, 3.2vw, 2.95rem)",
                                        "lineHeight": "1.06",
                                        "letterSpacing": "-0.045em",
                                        "color": "#111827",
                                        "maxWidth": "860px",
                                    },
                                ),
                                html.P(
                                    "Prestamos un servicio profesional y cercano para empresas, autónomos y particulares que necesitan apoyo estable y una gestión bien coordinada.",
                                    className="mb-5 reveal-up",
                                    style={
                                        "color": "#6b7280",
                                        "lineHeight": "1.9",
                                        "maxWidth": "820px",
                                        "fontSize": "1rem",
                                    },
                                ),
                            ]
                        )
                    ]
                ),
                dbc.Row(
                    [service_card(s["icono"], s["titulo"], s["texto"]) for s in SERVICIOS],
                    className="g-4",
                ),
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


def build_about_section():
    return html.Div(
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(
                        [
                            section_tag("Despacho"),
                            html.H2(
                                "Más de 70 años acompañando a empresas, autónomos y particulares en Ávila",
                                className="fw-bold mb-3 reveal-up",
                                style={
                                    "fontSize": "clamp(2rem, 3vw, 2.75rem)",
                                    "lineHeight": "1.08",
                                    "letterSpacing": "-0.04em",
                                    "color": "#111827",
                                    "maxWidth": "760px",
                                },
                            ),
                            html.P(
                                "Nuestra gestoría combina experiencia, cercanía y atención profesional para ofrecer un servicio claro, estable y adaptado a las necesidades reales de cada cliente.",
                                className="mb-3 reveal-up",
                                style={
                                    "color": "#6b7280",
                                    "lineHeight": "1.9",
                                    "maxWidth": "760px",
                                },
                            ),
                            html.P(
                                "Trabajamos en el ámbito fiscal, laboral, contable y administrativo, ayudando tanto en la gestión diaria como en trámites concretos que requieren orden, confianza y agilidad.",
                                className="mb-0 reveal-up",
                                style={
                                    "color": "#6b7280",
                                    "lineHeight": "1.9",
                                    "maxWidth": "760px",
                                },
                            ),
                        ],
                        lg=7,
                        className="mb-4 mb-lg-0",
                    ),
                    dbc.Col(
                        html.Div(
                            [
                                html.Div(
                                    "Forma de trabajo",
                                    className="fw-semibold mb-3 reveal-up",
                                    style={
                                        "color": "#111827",
                                        "fontSize": "0.98rem",
                                        "letterSpacing": "0.02em",
                                        "textTransform": "uppercase",
                                    },
                                ),
                                html.Div(
                                    "• Atención directa y cercana",
                                    className="mb-2 reveal-up",
                                    style={"color": "#374151", "fontWeight": "600"},
                                ),
                                html.Div(
                                    "• Explicaciones claras y sencillas",
                                    className="mb-2 reveal-up",
                                    style={"color": "#374151", "fontWeight": "600"},
                                ),
                                html.Div(
                                    "• Experiencia en la gestión del día a día",
                                    className="mb-2 reveal-up",
                                    style={"color": "#374151", "fontWeight": "600"},
                                ),
                                html.Div(
                                    "• Acompañamiento estable para clientes y negocios",
                                    className="reveal-up",
                                    style={"color": "#374151", "fontWeight": "600"},
                                ),
                            ],
                            style={
                                "padding": "1.75rem",
                                "borderRadius": "20px",
                                "background": "#f8fafc",
                                "border": "1px solid rgba(17, 24, 39, 0.06)",
                                "height": "100%",
                            },
                        ),
                        lg=5,
                    ),
                ],
                className="align-items-stretch",
            )
        ),
        className="section-fade",
        style={
            "paddingTop": "4.2rem",
            "paddingBottom": "4.6rem",
            "background": "#ffffff",
        },
    )


def build_pillars_section():
    return html.Div(
        dbc.Container(
            [
                section_tag("Pilares"),
                dbc.Row(
                    [
                        dbc.Col(
                            html.H2(
                                "La confianza se construye con experiencia, cercanía y una gestión bien explicada",
                                className="fw-bold mb-4 reveal-up",
                                style={
                                    "fontSize": "clamp(2rem, 3.1vw, 2.8rem)",
                                    "lineHeight": "1.08",
                                    "letterSpacing": "-0.04em",
                                    "color": "#111827",
                                    "maxWidth": "760px",
                                },
                            ),
                            lg=7,
                        ),
                        dbc.Col(
                            html.P(
                                "La relación con el cliente se refuerza mediante una atención profesional, una comunicación clara y una forma de trabajar estable en el tiempo.",
                                className="mb-4 mb-lg-0 reveal-up",
                                style={
                                    "color": "#6b7280",
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
                dbc.Row(
                    [pillar_card(p["numero"], p["titulo"], p["texto"]) for p in PILARES],
                    className="g-4",
                ),
            ]
        ),
        className="section-fade",
        style={
            "paddingTop": "4.4rem",
            "paddingBottom": "4.4rem",
            "background": "#f8fafc",
        },
    )


def build_featured_section():
    return html.Div(
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(
                        [
                            section_tag("Especialidades"),
                            html.H2(
                                "Áreas en las que el despacho ofrece un acompañamiento estable y profesional",
                                className="fw-bold mb-3 reveal-up",
                                style={
                                    "fontSize": "clamp(1.95rem, 3vw, 2.65rem)",
                                    "lineHeight": "1.08",
                                    "letterSpacing": "-0.04em",
                                    "color": "#111827",
                                    "maxWidth": "700px",
                                },
                            ),
                            html.P(
                                "La trayectoria del despacho permite ofrecer una atención sólida, ordenada y orientada a resolver con claridad las necesidades habituales de gestión.",
                                className="mb-4 mb-lg-0 reveal-up",
                                style={
                                    "color": "#6b7280",
                                    "lineHeight": "1.9",
                                    "maxWidth": "720px",
                                },
                            ),
                        ],
                        lg=7,
                        className="mb-4 mb-lg-0",
                    ),
                    dbc.Col(
                        html.Div(
                            [list_check(text) for text in SERVICIO_DESTACADO],
                            className="reveal-up",
                            style={
                                "padding": "1.5rem",
                                "borderRadius": "20px",
                                "background": "#ffffff",
                                "border": "1px solid rgba(17, 24, 39, 0.06)",
                                "height": "100%",
                            },
                        ),
                        lg=5,
                    ),
                ],
                className="align-items-stretch",
            )
        ),
        className="section-fade",
        style={"paddingBottom": "4.8rem"},
    )


def build_process_section():
    return html.Div(
        dbc.Container(
            [
                section_tag("Proceso"),
                dbc.Row(
                    [
                        dbc.Col(
                            html.H2(
                                "Una gestión clara y bien organizada aporta tranquilidad y confianza",
                                className="fw-bold mb-4 reveal-up",
                                style={
                                    "fontSize": "clamp(2rem, 3.05vw, 2.8rem)",
                                    "lineHeight": "1.08",
                                    "letterSpacing": "-0.04em",
                                    "color": "#111827",
                                    "maxWidth": "760px",
                                },
                            ),
                            lg=7,
                        ),
                        dbc.Col(
                            html.P(
                                "Cuando cada paso se explica con claridad y el cliente se siente acompañado, la relación resulta más sencilla, más cercana y más eficaz.",
                                className="mb-4 mb-lg-0 reveal-up",
                                style={
                                    "color": "#6b7280",
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
                dbc.Row(
                    [process_card(p["numero"], p["titulo"], p["texto"]) for p in PROCESO],
                    className="g-4",
                ),
            ]
        ),
        className="section-fade",
        style={"paddingTop": "4.4rem", "paddingBottom": "4.4rem"},
    )


def build_testimonials_section():
    return html.Div(
        dbc.Container(
            [
                section_tag("Opiniones"),
                html.H2(
                    "La experiencia del cliente refuerza la confianza en el despacho",
                    className="fw-bold mb-3 reveal-up",
                    style={
                        "fontSize": "clamp(2rem, 3vw, 2.8rem)",
                        "lineHeight": "1.08",
                        "letterSpacing": "-0.04em",
                        "color": "#111827",
                        "maxWidth": "760px",
                    },
                ),
                html.P(
                    "Estas opiniones reflejan el tipo de atención cercana, clara y profesional que una gestoría consolidada busca ofrecer en cada gestión.",
                    className="mb-5 reveal-up",
                    style={
                        "color": "#6b7280",
                        "lineHeight": "1.9",
                        "maxWidth": "760px",
                    },
                ),
                dbc.Row(
                    [testimonial_card(t["nombre"], t["texto"]) for t in TESTIMONIOS],
                    className="g-4",
                ),
            ]
        ),
        className="section-fade",
        style={
            "paddingTop": "4.4rem",
            "paddingBottom": "4.4rem",
            "background": "#f8fafc",
        },
    )


def build_location_section():
    return html.Div(
        dbc.Container(
            [
                section_tag("Ubicación"),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H2(
                                    "Gestoría en Ávila con atención cercana y presencial",
                                    className="fw-bold mb-3 reveal-up",
                                    style={
                                        "fontSize": "clamp(2rem, 3vw, 2.75rem)",
                                        "lineHeight": "1.08",
                                        "letterSpacing": "-0.04em",
                                        "color": "#111827",
                                        "maxWidth": "740px",
                                    },
                                ),
                                html.P(
                                    "Atendemos desde nuestra oficina en Ávila, ofreciendo un servicio próximo, claro y profesional para particulares, autónomos y empresas.",
                                    className="mb-4 reveal-up",
                                    style={
                                        "color": "#6b7280",
                                        "lineHeight": "1.9",
                                        "maxWidth": "700px",
                                    },
                                ),
                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            html.Div(
                                                "Datos de contacto",
                                                className="fw-semibold mb-3 reveal-up",
                                                style={"color": "#111827"},
                                            ),
                                            html.Div(
                                                f"📍 {DIRECCION}",
                                                className="mb-2 reveal-up",
                                                style={"color": "#6b7280", "lineHeight": "1.8"},
                                            ),
                                            html.Div(
                                                f"📞 {TELEFONO_1}",
                                                className="mb-2 reveal-up",
                                                style={"color": "#6b7280"},
                                            ),
                                            html.Div(
                                                f"✉️ {EMAIL}",
                                                className="mb-4 reveal-up",
                                                style={"color": "#6b7280"},
                                            ),
                                            dbc.Button(
                                                "Contactar por WhatsApp",
                                                href=WHATSAPP_URL,
                                                target="_blank",
                                                color="light",
                                                className="fw-semibold me-2 mb-2 border-0",
                                                style={
                                                    "padding": "0.9rem 1.2rem",
                                                    "minHeight": "50px",
                                                    "borderRadius": "999px",
                                                    "background": "#eef2f7",
                                                    "color": "#111827",
                                                },
                                            ),
                                            dbc.Button(
                                                "Enviar email",
                                                href=f"mailto:{EMAIL}",
                                                color="dark",
                                                className="fw-semibold mb-2 border-0",
                                                style={
                                                    "padding": "0.9rem 1.2rem",
                                                    "minHeight": "50px",
                                                    "borderRadius": "999px",
                                                    "background": "#111827",
                                                },
                                            ),
                                        ]
                                    ),
                                    className="border-0 reveal-up",
                                    style={
                                        "borderRadius": "20px",
                                        "background": "#ffffff",
                                        "border": "1px solid rgba(17, 24, 39, 0.06)",
                                    },
                                ),
                            ],
                            lg=5,
                            className="mb-4 mb-lg-0",
                        ),
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody(
                                    html.Div(
                                        [
                                            html.Div(
                                                "Mapa / oficina",
                                                className="fw-semibold mb-3 reveal-up",
                                                style={"color": "#111827"},
                                            ),
                                            html.Div(
                                                "Aquí puedes integrar Google Maps, una imagen real de la oficina o una referencia visual de la ubicación para reforzar la confianza del visitante.",
                                                className="mb-4 reveal-up",
                                                style={
                                                    "color": "#6b7280",
                                                    "lineHeight": "1.85",
                                                    "maxWidth": "620px",
                                                },
                                            ),
                                            html.Div(
                                                style={
                                                    "height": "340px",
                                                    "borderRadius": "18px",
                                                    "background": "#f8fafc",
                                                    "border": "1px solid rgba(17, 24, 39, 0.06)",
                                                    "display": "flex",
                                                    "alignItems": "center",
                                                    "justifyContent": "center",
                                                    "color": "#6b7280",
                                                    "fontWeight": "600",
                                                    "fontSize": "1rem",
                                                },
                                                className="reveal-up",
                                                children="Espacio para mapa o imagen de ubicación",
                                            ),
                                        ]
                                    )
                                ),
                                className="border-0 h-100",
                                style={
                                    "borderRadius": "22px",
                                    "background": "#ffffff",
                                    "border": "1px solid rgba(17, 24, 39, 0.06)",
                                },
                            ),
                            lg=7,
                        ),
                    ],
                    className="align-items-stretch",
                ),
            ]
        ),
        className="section-fade",
        style={
            "paddingTop": "4.4rem",
            "paddingBottom": "4.8rem",
            "background": "#f8fafc",
        },
    )


def build_seo_section():
    return html.Div(
        dbc.Container(
            [
                section_tag("Gestoría en Ávila"),
                html.H2(
                    "Asesoría fiscal, laboral, contable y administrativa para empresas, autónomos y particulares",
                    className="fw-bold mb-3 reveal-up",
                    style={
                        "fontSize": "clamp(1.9rem, 2.8vw, 2.5rem)",
                        "lineHeight": "1.08",
                        "letterSpacing": "-0.04em",
                        "color": "#111827",
                        "maxWidth": "860px",
                    },
                ),
                html.P(
                    "Prestamos apoyo profesional en gestiones fiscales, laborales, contables y administrativas desde Ávila, con una atención cercana y orientada a resolver con claridad las necesidades de cada cliente.",
                    className="mb-0 reveal-up",
                    style={
                        "color": "#6b7280",
                        "lineHeight": "1.95",
                        "maxWidth": "1040px",
                    },
                ),
            ]
        ),
        className="section-fade",
        style={"paddingTop": "4.4rem", "paddingBottom": "4.4rem"},
    )


def build_faq_section():
    return html.Div(
        dbc.Container(
            [
                section_tag("Preguntas frecuentes"),
                html.H2(
                    "Dudas habituales antes de contactar con una gestoría",
                    className="fw-bold mb-4 reveal-up",
                    style={
                        "fontSize": "clamp(1.9rem, 2.8vw, 2.45rem)",
                        "lineHeight": "1.08",
                        "letterSpacing": "-0.04em",
                        "color": "#111827",
                    },
                ),
                dbc.Accordion(
                    [
                        dbc.AccordionItem(
                            html.P(
                                texto,
                                className="mb-0",
                                style={"color": "#6b7280", "lineHeight": "1.8"},
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
            "paddingTop": "4.4rem",
            "paddingBottom": "4.4rem",
            "background": "#f8fafc",
        },
    )


def build_cta_section():
    return html.Div(
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(
                        [
                            section_tag("Contacto"),
                            html.H2(
                                "Contacte con nuestra gestoría en Ávila",
                                className="fw-bold mb-3 reveal-up",
                                style={
                                    "fontSize": "clamp(2rem, 3vw, 2.75rem)",
                                    "lineHeight": "1.08",
                                    "letterSpacing": "-0.04em",
                                    "color": "#111827",
                                    "maxWidth": "740px",
                                },
                            ),
                            html.P(
                                "Estamos a su disposición para ayudarle en cuestiones fiscales, laborales, contables y administrativas con una atención cercana, clara y profesional.",
                                className="mb-0 reveal-up",
                                style={
                                    "color": "#6b7280",
                                    "lineHeight": "1.9",
                                    "maxWidth": "720px",
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
                                color="dark",
                                className="w-100 fw-semibold mb-2 border-0",
                                style={
                                    "padding": "0.95rem 1.4rem",
                                    "minHeight": "54px",
                                    "borderRadius": "999px",
                                    "background": "#111827",
                                },
                            ),
                            dbc.Button(
                                "WhatsApp",
                                href=WHATSAPP_URL,
                                target="_blank",
                                color="light",
                                className="w-100 fw-semibold mb-2 border-0",
                                style={
                                    "padding": "0.95rem 1.4rem",
                                    "minHeight": "54px",
                                    "borderRadius": "999px",
                                    "background": "#eef2f7",
                                    "color": "#111827",
                                },
                            ),
                            dbc.Button(
                                "Enviar email",
                                href=f"mailto:{EMAIL}",
                                color="link",
                                className="w-100 fw-semibold text-decoration-none",
                                style={
                                    "padding": "0.95rem 1.4rem",
                                    "minHeight": "54px",
                                    "color": "#4b5563",
                                },
                            ),
                        ],
                        lg=4,
                        className="reveal-up",
                    ),
                ],
                className="align-items-center",
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
                                "Gestoría Duque",
                                className="fw-semibold mb-2 reveal-up",
                                style={
                                    "color": "#111827",
                                    "fontSize": "1.02rem",
                                    "letterSpacing": "-0.02em",
                                },
                            ),
                            html.Div(
                                "Asesoría fiscal, laboral, contable y administrativa en Ávila con atención cercana y profesional.",
                                className="reveal-up",
                                style={"color": "#6b7280", "lineHeight": "1.8"},
                            ),
                        ],
                        md=6,
                        className="mb-4 mb-md-0",
                    ),
                    dbc.Col(
                        [
                            html.Div(f"📍 {DIRECCION}", className="mb-2 reveal-up", style={"color": "#6b7280"}),
                            html.Div(f"📞 {TELEFONO_1}", className="mb-2 reveal-up", style={"color": "#6b7280"}),
                            html.Div(f"✉️ {EMAIL}", className="reveal-up", style={"color": "#6b7280"}),
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
            "background": "#111827",
            "color": "white",
            "textDecoration": "none",
            "padding": "0.92rem 1.18rem",
            "borderRadius": "999px",
            "fontWeight": "700",
            "letterSpacing": "0.01em",
            "boxShadow": "0 14px 30px rgba(15, 23, 42, 0.18)",
        },
    )
