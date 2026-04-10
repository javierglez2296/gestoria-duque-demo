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
        ("Atención cercana", "Trato directo y profesional"),
        ("Servicio integral", "Fiscal, laboral y contable"),
        ("Ávila", "Despacho local de confianza"),
    ]

    return html.Section(
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            [
                                html.Div(
                                    titulo,
                                    className="fw-bold mb-1",
                                    style={
                                        "color": "#101828",
                                        "fontSize": "1.02rem",
                                        "letterSpacing": "-0.02em",
                                    },
                                ),
                                html.Div(
                                    texto,
                                    style={
                                        "color": "#667085",
                                        "fontSize": "0.94rem",
                                        "lineHeight": "1.6",
                                    },
                                ),
                            ],
                            className="h-100",
                            style={
                                "padding": "1.1rem 1rem",
                                "borderRadius": "18px",
                                "background": "rgba(255,255,255,0.86)",
                                "border": "1px solid rgba(16,24,40,0.06)",
                                "boxShadow": "0 10px 30px rgba(16,24,40,0.04)",
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
            "paddingTop": "2.2rem",
            "paddingBottom": "3rem",
            "background": "linear-gradient(180deg, #ffffff 0%, #fbfcfe 100%)",
        },
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
                                    "Servicios de asesoría fiscal, laboral, contable y administrativa en Ávila",
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
                                    "Ofrecemos un servicio profesional y cercano para autónomos, empresas y particulares que buscan apoyo estable en su gestión diaria.",
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


def build_about_section():
    return html.Section(
        dbc.Container(
            dbc.Card(
                dbc.CardBody(
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    section_tag("Despacho"),
                                    html.H2(
                                        "Más de 70 años acompañando a empresas, autónomos y particulares en Ávila",
                                        className="fw-bold mb-3 reveal-up",
                                        style={
                                            "fontSize": "clamp(2rem, 3.2vw, 2.95rem)",
                                            "lineHeight": "1.04",
                                            "letterSpacing": "-0.05em",
                                            "color": "#101828",
                                            "maxWidth": "780px",
                                        },
                                    ),
                                    html.P(
                                        "Nuestra gestoría combina experiencia, cercanía y atención profesional para ofrecer un servicio claro, estable y adaptado a las necesidades reales de cada cliente.",
                                        className="mb-3 reveal-up",
                                        style={
                                            "color": "#667085",
                                            "lineHeight": "1.9",
                                            "maxWidth": "760px",
                                        },
                                    ),
                                    html.P(
                                        "Trabajamos en el ámbito fiscal, laboral, contable y administrativo, ayudando tanto en la gestión diaria como en trámites concretos que requieren orden, confianza y agilidad.",
                                        className="mb-0 reveal-up",
                                        style={
                                            "color": "#667085",
                                            "lineHeight": "1.9",
                                            "maxWidth": "760px",
                                        },
                                    ),
                                ],
                                lg=7,
                                className="mb-4 mb-lg-0",
                            ),
                            dbc.Col(
                                [
                                    html.Div(
                                        [
                                            html.Div(
                                                "Nuestra forma de trabajar",
                                                className="fw-semibold mb-3 reveal-up",
                                                style={
                                                    "color": "#101828",
                                                    "fontSize": "1rem",
                                                },
                                            ),
                                            html.Div(
                                                [
                                                    html.Div(
                                                        "• Atención directa y cercana",
                                                        className="mb-2 reveal-up",
                                                        style={"color": "#344054", "fontWeight": "600"},
                                                    ),
                                                    html.Div(
                                                        "• Explicaciones claras y sencillas",
                                                        className="mb-2 reveal-up",
                                                        style={"color": "#344054", "fontWeight": "600"},
                                                    ),
                                                    html.Div(
                                                        "• Experiencia en la gestión del día a día",
                                                        className="mb-2 reveal-up",
                                                        style={"color": "#344054", "fontWeight": "600"},
                                                    ),
                                                    html.Div(
                                                        "• Acompañamiento estable para clientes y negocios",
                                                        className="reveal-up",
                                                        style={"color": "#344054", "fontWeight": "600"},
                                                    ),
                                                ]
                                            ),
                                        ],
                                        style={
                                            "padding": "1.5rem",
                                            "borderRadius": "22px",
                                            "background": "linear-gradient(180deg, #ffffff 0%, #f8fbff 100%)",
                                            "boxShadow": "0 18px 46px rgba(16, 24, 40, 0.06)",
                                            "height": "100%",
                                        },
                                    )
                                ],
                                lg=5,
                            ),
                        ]
                    )
                ),
                className="border-0",
                style={
                    "borderRadius": "30px",
                    "background": "linear-gradient(135deg, #ffffff 0%, #fbfcfe 100%)",
                    "boxShadow": "0 24px 62px rgba(16, 24, 40, 0.08)",
                },
            )
        ),
        className="section-fade",
        style={
            "paddingTop": "4.4rem",
            "paddingBottom": "4.8rem",
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
                                "Un despacho de confianza se apoya en experiencia, cercanía y una gestión bien explicada",
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
                                "La confianza del cliente se construye con una atención profesional, una comunicación clara y una forma de trabajar estable en el tiempo.",
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
                                    section_tag("Especialidades"),
                                    html.H2(
                                        "Experiencia, cercanía y servicio profesional para el día a día de tus gestiones",
                                        className="fw-bold mb-3 reveal-up",
                                        style={
                                            "fontSize": "clamp(2rem, 3vw, 2.7rem)",
                                            "lineHeight": "1.05",
                                            "letterSpacing": "-0.04em",
                                            "color": "#101828",
                                        },
                                    ),
                                    html.P(
                                        "La trayectoria del despacho permite ofrecer una atención sólida, clara y orientada a resolver con agilidad las necesidades de cada cliente.",
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
                                "Una atención clara y bien organizada ayuda a resolver cada gestión con más tranquilidad",
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
                                "Cuando el cliente entiende el proceso y se siente acompañado, la relación resulta más sencilla, más cercana y más eficaz.",
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
                    "La confianza se refuerza cuando la atención profesional se traduce en buenas experiencias",
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
                    "Estas opiniones representan el tipo de trato cercano, claro y profesional que una gestoría consolidada busca ofrecer a sus clientes.",
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


def build_location_section():
    return html.Section(
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
                                        "fontSize": "clamp(2rem, 3.2vw, 2.9rem)",
                                        "lineHeight": "1.04",
                                        "letterSpacing": "-0.05em",
                                        "color": "#101828",
                                        "maxWidth": "760px",
                                    },
                                ),
                                html.P(
                                    "Atendemos desde nuestra oficina en Ávila, ofreciendo un servicio próximo, claro y profesional para clientes particulares, autónomos y empresas.",
                                    className="mb-4 reveal-up",
                                    style={
                                        "color": "#667085",
                                        "lineHeight": "1.9",
                                        "maxWidth": "720px",
                                    },
                                ),
                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            html.Div(
                                                "Datos de contacto",
                                                className="fw-semibold mb-3 reveal-up",
                                                style={"color": "#101828"},
                                            ),
                                            html.Div(
                                                f"📍 {DIRECCION}",
                                                className="mb-2 reveal-up",
                                                style={"color": "#667085", "lineHeight": "1.8"},
                                            ),
                                            html.Div(
                                                f"📞 {TELEFONO_1}",
                                                className="mb-2 reveal-up",
                                                style={"color": "#667085"},
                                            ),
                                            html.Div(
                                                f"✉️ {EMAIL}",
                                                className="mb-4 reveal-up",
                                                style={"color": "#667085"},
                                            ),
                                            dbc.Button(
                                                "Contactar por WhatsApp",
                                                href=WHATSAPP_URL,
                                                target="_blank",
                                                color="success",
                                                className="rounded-pill fw-semibold me-2 mb-2",
                                                style={
                                                    "padding": "0.95rem 1.2rem",
                                                    "minHeight": "52px",
                                                },
                                            ),
                                            dbc.Button(
                                                "Enviar email",
                                                href=f"mailto:{EMAIL}",
                                                color="light",
                                                className="rounded-pill fw-semibold border mb-2",
                                                style={
                                                    "padding": "0.95rem 1.2rem",
                                                    "minHeight": "52px",
                                                },
                                            ),
                                        ]
                                    ),
                                    className="border-0 reveal-up",
                                    style={
                                        "borderRadius": "24px",
                                        "background": "#ffffff",
                                        "boxShadow": "0 18px 46px rgba(16, 24, 40, 0.06)",
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
                                                style={"color": "#101828"},
                                            ),
                                            html.Div(
                                                "Aquí puedes integrar un mapa de Google Maps, una imagen de la oficina o una captura de ubicación para reforzar la confianza del visitante.",
                                                className="mb-4 reveal-up",
                                                style={
                                                    "color": "#667085",
                                                    "lineHeight": "1.85",
                                                    "maxWidth": "620px",
                                                },
                                            ),
                                            html.Div(
                                                style={
                                                    "height": "340px",
                                                    "borderRadius": "22px",
                                                    "background": (
                                                        "linear-gradient(135deg, #edf4ff 0%, #f8fbff 100%)"
                                                    ),
                                                    "border": "1px solid rgba(13,110,253,0.08)",
                                                    "display": "flex",
                                                    "alignItems": "center",
                                                    "justifyContent": "center",
                                                    "color": "#667085",
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
                                    "borderRadius": "28px",
                                    "background": "linear-gradient(180deg, #ffffff 0%, #fbfcfe 100%)",
                                    "boxShadow": "0 20px 54px rgba(16, 24, 40, 0.06)",
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
            "paddingTop": "4.6rem",
            "paddingBottom": "4.8rem",
            "background": "#f8fafc",
        },
    )


def build_seo_section():
    return html.Section(
        dbc.Container(
            [
                section_tag("Gestoría en Ávila"),
                html.H2(
                    "Asesoría fiscal, laboral, contable y administrativa para empresas, autónomos y particulares",
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
                    "Ofrecemos apoyo profesional en gestiones fiscales, laborales, contables y administrativas desde Ávila, con una atención cercana y orientada a resolver de forma clara las necesidades de cada cliente.",
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
                                            "Contacta con nuestra gestoría en Ávila",
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
                                            "Estamos aquí para ayudarte con tus necesidades fiscales, laborales, contables y administrativas de forma clara, cercana y profesional.",
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
                                "Gestoría Duque",
                                className="fw-bold mb-2 reveal-up",
                                style={
                                    "color": "#101828",
                                    "fontSize": "1.05rem",
                                    "letterSpacing": "-0.02em",
                                },
                            ),
                            html.Div(
                                "Asesoría fiscal, laboral, contable y administrativa en Ávila con atención cercana y profesional.",
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
