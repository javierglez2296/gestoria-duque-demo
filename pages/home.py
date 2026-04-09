import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path="/",
    title="Gestoría en Ávila para autónomos, empresas y particulares | Demo",
    name="Inicio",
    description=(
        "Gestoría en Ávila especializada en asesoría fiscal, laboral, contable y trámites "
        "para autónomos, empresas y particulares."
    ),
)

TELEFONO_1 = "920 000 000"
TELEFONO_2 = "620 000 000"
EMAIL = "info@gestoriaduque.com"
DIRECCION = "Paseo de San Roque 00, 05003 Ávila"

SERVICIOS = [
    {
        "icono": "📊",
        "titulo": "Asesoría fiscal y contable",
        "texto": "Impuestos, contabilidad, cierres, declaraciones, IVA, IRPF y seguimiento fiscal para autónomos y empresas.",
    },
    {
        "icono": "👥",
        "titulo": "Asesoría laboral",
        "texto": "Contratos, nóminas, seguros sociales, altas y bajas, gestión laboral y apoyo en el día a día de tu negocio.",
    },
    {
        "icono": "🏢",
        "titulo": "Gestión para empresas",
        "texto": "Apoyo administrativo y asesoramiento para sociedades, pymes y negocios que buscan orden, control y tranquilidad.",
    },
    {
        "icono": "🧾",
        "titulo": "Trámites administrativos",
        "texto": "Gestiones con organismos públicos, certificados, documentación, autorizaciones y trámites habituales.",
    },
    {
        "icono": "🚗",
        "titulo": "Transferencias y vehículos",
        "texto": "Cambios de titularidad, gestiones de tráfico y documentación relacionada con vehículos.",
    },
    {
        "icono": "🙋",
        "titulo": "Atención a particulares",
        "texto": "Ayuda clara y cercana para personas que necesitan resolver trámites o recibir asesoramiento puntual.",
    },
]

VENTAJAS = [
    "Más de 70 años de experiencia",
    "Atención cercana y profesional",
    "Gestión para autónomos, empresas y particulares",
    "Despacho local en Ávila",
]

FAQS = [
    (
        "¿Atendéis a autónomos y empresas?",
        "Sí. La gestoría está orientada tanto a autónomos como a pymes, sociedades y también particulares que necesitan ayuda con trámites concretos.",
    ),
    (
        "¿Podéis llevar fiscal, laboral y contabilidad?",
        "Sí. La idea es ofrecer un servicio integral para que el cliente tenga un único punto de apoyo en su gestión diaria.",
    ),
    (
        "¿Trabajáis solo en Ávila?",
        "La base local está en Ávila, lo que aporta cercanía y confianza, pero muchas gestiones pueden apoyarse también de forma ágil por teléfono o email.",
    ),
]


# =========================================================
# HELPERS
# =========================================================
def section_eyebrow(text):
    return html.Div(
        text,
        className="text-uppercase fw-bold small mb-2",
        style={
            "letterSpacing": "0.08em",
            "color": "#667085",
        },
    )


def metric_card(value, label):
    return dbc.Card(
        dbc.CardBody(
            [
                html.Div(
                    value,
                    className="fw-bold mb-1",
                    style={
                        "fontSize": "1.7rem",
                        "lineHeight": "1.1",
                        "color": "#101828",
                    },
                ),
                html.Div(
                    label,
                    style={
                        "fontSize": "0.92rem",
                        "color": "#667085",
                    },
                ),
            ]
        ),
        className="border-0 rounded-4 h-100",
        style={
            "background": "#ffffff",
            "boxShadow": "0 12px 28px rgba(16, 24, 40, 0.06)",
        },
    )


def service_card(icono, titulo, texto):
    return dbc.Col(
        dbc.Card(
            dbc.CardBody(
                [
                    html.Div(icono, className="mb-3", style={"fontSize": "2rem"}),
                    html.H3(
                        titulo,
                        className="h5 fw-bold mb-2",
                        style={"color": "#101828"},
                    ),
                    html.P(
                        texto,
                        className="mb-0",
                        style={"color": "#667085", "lineHeight": "1.7"},
                    ),
                ]
            ),
            className="border-0 rounded-4 h-100",
            style={
                "background": "#ffffff",
                "boxShadow": "0 14px 34px rgba(16, 24, 40, 0.06)",
            },
        ),
        lg=4,
        md=6,
        className="mb-4",
    )


def advantage_chip(text):
    return html.Span(
        text,
        className="d-inline-flex align-items-center rounded-pill px-3 py-2 me-2 mb-2",
        style={
            "background": "#ffffff",
            "border": "1px solid rgba(15, 23, 42, 0.08)",
            "fontWeight": "600",
            "color": "#344054",
            "boxShadow": "0 4px 10px rgba(16, 24, 40, 0.04)",
        },
    )


def simple_step(number, title, text):
    return dbc.Col(
        dbc.Card(
            dbc.CardBody(
                [
                    html.Div(
                        str(number),
                        className="d-inline-flex align-items-center justify-content-center rounded-circle mb-3",
                        style={
                            "width": "42px",
                            "height": "42px",
                            "background": "#0d6efd",
                            "color": "white",
                            "fontWeight": "700",
                        },
                    ),
                    html.H3(title, className="h5 fw-bold mb-2"),
                    html.P(
                        text,
                        className="mb-0",
                        style={"color": "#667085", "lineHeight": "1.7"},
                    ),
                ]
            ),
            className="border-0 rounded-4 h-100",
            style={
                "background": "#ffffff",
                "boxShadow": "0 12px 30px rgba(16, 24, 40, 0.06)",
            },
        ),
        md=4,
        className="mb-4",
    )


# =========================================================
# SECTIONS
# =========================================================
hero_section = html.Div(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Div(
                                "GESTORÍA EN ÁVILA · ASESORÍA FISCAL · LABORAL · CONTABLE",
                                className="mb-3",
                                style={
                                    "display": "inline-block",
                                    "padding": "0.5rem 0.9rem",
                                    "borderRadius": "999px",
                                    "background": "#eef4ff",
                                    "color": "#0d6efd",
                                    "fontWeight": "700",
                                    "fontSize": "0.82rem",
                                    "letterSpacing": "0.03em",
                                },
                            ),
                            html.H1(
                                "Gestoría en Ávila para autónomos, empresas y particulares",
                                className="fw-bold mb-3",
                                style={
                                    "fontSize": "clamp(2.15rem, 4.5vw, 4rem)",
                                    "lineHeight": "1.05",
                                    "letterSpacing": "-0.04em",
                                    "color": "#101828",
                                    "maxWidth": "850px",
                                },
                            ),
                            html.P(
                                "Te ayudamos con fiscalidad, laboral, contabilidad y trámites administrativos "
                                "para que ganes tranquilidad, ahorres tiempo y tomes decisiones con más seguridad.",
                                className="mb-4",
                                style={
                                    "fontSize": "1.08rem",
                                    "color": "#475467",
                                    "lineHeight": "1.8",
                                    "maxWidth": "780px",
                                },
                            ),
                            html.Div(
                                [advantage_chip(v) for v in VENTAJAS],
                                className="mb-4",
                            ),
                            html.Div(
                                [
                                    dbc.Button(
                                        f"Llamar: {TELEFONO_1}",
                                        href=f"tel:{TELEFONO_1.replace(' ', '')}",
                                        color="primary",
                                        className="rounded-pill px-4 py-2 fw-semibold me-2 mb-2",
                                    ),
                                    dbc.Button(
                                        "Pedir información",
                                        href=f"mailto:{EMAIL}",
                                        color="light",
                                        className="rounded-pill px-4 py-2 fw-semibold border mb-2",
                                    ),
                                ]
                            ),
                        ],
                        lg=7,
                        className="mb-4 mb-lg-0",
                    ),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.Div(
                                        "Contacto rápido",
                                        className="fw-bold mb-3",
                                        style={"color": "#0d6efd"},
                                    ),
                                    html.H2(
                                        "Habla con nosotros",
                                        className="h4 fw-bold mb-3",
                                        style={"color": "#101828"},
                                    ),
                                    html.Div(
                                        [
                                            html.Div("📞 Teléfono", className="fw-semibold mb-1"),
                                            html.Div(TELEFONO_1, className="mb-3", style={"color": "#667085"}),
                                            html.Div("📱 Móvil", className="fw-semibold mb-1"),
                                            html.Div(TELEFONO_2, className="mb-3", style={"color": "#667085"}),
                                            html.Div("✉️ Email", className="fw-semibold mb-1"),
                                            html.Div(EMAIL, className="mb-3", style={"color": "#667085"}),
                                            html.Div("📍 Dirección", className="fw-semibold mb-1"),
                                            html.Div(DIRECCION, className="mb-4", style={"color": "#667085"}),
                                        ]
                                    ),
                                    dbc.Button(
                                        "Escríbenos ahora",
                                        href=f"mailto:{EMAIL}",
                                        color="primary",
                                        className="w-100 rounded-pill fw-semibold py-2",
                                    ),
                                ]
                            ),
                            className="border-0 rounded-4 h-100",
                            style={
                                "background": "#ffffff",
                                "boxShadow": "0 18px 48px rgba(16, 24, 40, 0.08)",
                            },
                        ),
                        lg=5,
                    ),
                ],
                className="align-items-center",
            )
        ]
    ),
    className="py-5",
    style={
        "background": (
            "radial-gradient(circle at top left, rgba(13,110,253,0.10), transparent 35%),"
            "radial-gradient(circle at top right, rgba(25,135,84,0.06), transparent 30%),"
            "linear-gradient(180deg, #ffffff 0%, #f8fafc 100%)"
        )
    },
)

metrics_section = html.Div(
    dbc.Container(
        dbc.Row(
            [
                dbc.Col(metric_card("Desde 1950", "Trayectoria y confianza"), md=4, className="mb-3"),
                dbc.Col(metric_card("Ávila", "Atención local y cercana"), md=4, className="mb-3"),
                dbc.Col(metric_card("Integral", "Fiscal, laboral, contable y trámites"), md=4, className="mb-3"),
            ],
            className="g-3",
        )
    ),
    className="pb-4",
)

services_section = html.Div(
    dbc.Container(
        [
            section_eyebrow("Servicios"),
            html.H2(
                "Una gestoría pensada para resolver el día a día de clientes y negocios",
                className="fw-bold mb-3",
                style={
                    "fontSize": "clamp(1.8rem, 3vw, 2.6rem)",
                    "color": "#101828",
                },
            ),
            html.P(
                "Servicios de asesoría y gestión con un enfoque práctico, cercano y profesional. "
                "La idea es que el cliente sepa qué le estás resolviendo y por qué puede confiar en ti.",
                className="mb-4",
                style={"color": "#667085", "lineHeight": "1.8", "maxWidth": "860px"},
            ),
            dbc.Row([service_card(s["icono"], s["titulo"], s["texto"]) for s in SERVICIOS]),
        ]
    ),
    className="py-5",
)

trust_section = html.Div(
    dbc.Container(
        dbc.Card(
            dbc.CardBody(
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                section_eyebrow("Confianza"),
                                html.H2(
                                    "Más de 70 años ayudando a clientes en Ávila",
                                    className="fw-bold mb-3",
                                    style={"color": "#101828"},
                                ),
                                html.P(
                                    "Una gestoría transmite mucho más cuando combina experiencia, cercanía y claridad. "
                                    "Este bloque está pensado para reforzar precisamente eso: trayectoria, presencia local "
                                    "y capacidad para acompañar a autónomos, empresas y particulares.",
                                    className="mb-0",
                                    style={"color": "#667085", "lineHeight": "1.8"},
                                ),
                            ],
                            lg=8,
                            className="mb-4 mb-lg-0",
                        ),
                        dbc.Col(
                            html.Div(
                                [
                                    html.Div("✔ Experiencia consolidada", className="mb-2 fw-semibold"),
                                    html.Div("✔ Atención cercana", className="mb-2 fw-semibold"),
                                    html.Div("✔ Despacho local", className="mb-2 fw-semibold"),
                                    html.Div("✔ Servicio profesional", className="fw-semibold"),
                                ],
                                style={"color": "#344054"},
                            ),
                            lg=4,
                            className="d-flex align-items-center",
                        ),
                    ]
                )
            ),
            className="border-0 rounded-4",
            style={
                "background": "linear-gradient(135deg, #ffffff 0%, #f8fbff 100%)",
                "boxShadow": "0 16px 40px rgba(16, 24, 40, 0.06)",
            },
        )
    ),
    className="pb-5",
)

how_it_works_section = html.Div(
    dbc.Container(
        [
            section_eyebrow("Cómo trabajáis"),
            html.H2(
                "Una web más clara también ayuda a captar mejor",
                className="fw-bold mb-3",
                style={"color": "#101828"},
            ),
            html.P(
                "Este bloque funciona muy bien para explicar el proceso de forma sencilla y bajar fricción al cliente.",
                className="mb-4",
                style={"color": "#667085", "lineHeight": "1.8"},
            ),
            dbc.Row(
                [
                    simple_step(1, "Cuéntanos tu caso", "Llámanos o escríbenos para explicarnos qué necesitas."),
                    simple_step(2, "Analizamos tu situación", "Valoramos el trámite o servicio y te orientamos con claridad."),
                    simple_step(3, "Te ayudamos a resolverlo", "Nos ocupamos de la gestión para que ganes tiempo y tranquilidad."),
                ]
            ),
        ]
    ),
    className="py-5",
    style={"background": "#f8fafc"},
)

seo_text_section = html.Div(
    dbc.Container(
        [
            section_eyebrow("SEO local"),
            html.H2(
                "Gestoría y asesoría en Ávila con enfoque fiscal, laboral y contable",
                className="fw-bold mb-3",
                style={"color": "#101828"},
            ),
            html.P(
                "Si una gestoría quiere captar clientes desde Google, necesita una home que explique con claridad qué hace, "
                "dónde está y para quién trabaja. Esta versión demo está pensada para posicionar mejor búsquedas como "
                "gestoría en Ávila, asesoría fiscal en Ávila, asesoría laboral en Ávila o gestoría para autónomos en Ávila.",
                className="mb-3",
                style={"color": "#667085", "lineHeight": "1.8"},
            ),
            html.P(
                "También refuerza la propuesta de valor del despacho: experiencia, cercanía, servicios claros y contacto visible. "
                "Eso no solo ayuda al SEO, también mejora mucho la conversión cuando alguien entra por primera vez en la web.",
                className="mb-0",
                style={"color": "#667085", "lineHeight": "1.8"},
            ),
        ]
    ),
    className="py-5",
)

faq_section = html.Div(
    dbc.Container(
        [
            section_eyebrow("Preguntas frecuentes"),
            html.H2(
                "Dudas habituales antes de contactar con una gestoría",
                className="fw-bold mb-4",
                style={"color": "#101828"},
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        [html.P(texto, className="mb-0", style={"color": "#667085"})],
                        title=pregunta,
                    )
                    for pregunta, texto in FAQS
                ],
                start_collapsed=True,
                always_open=False,
            ),
        ]
    ),
    className="py-5",
)

cta_section = html.Div(
    dbc.Container(
        dbc.Card(
            dbc.CardBody(
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                section_eyebrow("Contacto"),
                                html.H2(
                                    "Una web mejor debería llevar más llamadas y más contactos",
                                    className="fw-bold mb-2",
                                    style={"color": "#101828"},
                                ),
                                html.P(
                                    "Esta demo está orientada a que el visitante entienda rápido qué hacéis y cómo contactar. "
                                    "Ese es el objetivo real de una gestoría local en internet.",
                                    className="mb-0",
                                    style={"color": "#667085", "lineHeight": "1.8"},
                                ),
                            ],
                            lg=8,
                            className="mb-3 mb-lg-0",
                        ),
                        dbc.Col(
                            html.Div(
                                [
                                    dbc.Button(
                                        f"Llamar ahora",
                                        href=f"tel:{TELEFONO_1.replace(' ', '')}",
                                        color="primary",
                                        className="rounded-pill px-4 py-2 fw-semibold w-100 mb-2",
                                    ),
                                    dbc.Button(
                                        "Enviar email",
                                        href=f"mailto:{EMAIL}",
                                        color="light",
                                        className="rounded-pill px-4 py-2 fw-semibold border w-100",
                                    ),
                                ]
                            ),
                            lg=4,
                            className="d-flex align-items-center",
                        ),
                    ]
                )
            ),
            className="border-0 rounded-4",
            style={
                "background": "#ffffff",
                "boxShadow": "0 16px 40px rgba(16, 24, 40, 0.08)",
            },
        )
    ),
    className="pb-5",
)

footer_section = html.Div(
    dbc.Container(
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            "Gestoría Demo",
                            className="fw-bold mb-2",
                            style={"color": "#101828"},
                        ),
                        html.Div(
                            "Versión de muestra para enseñar una propuesta de renovación web.",
                            style={"color": "#667085"},
                        ),
                    ],
                    md=6,
                    className="mb-3 mb-md-0",
                ),
                dbc.Col(
                    [
                        html.Div(f"📍 {DIRECCION}", className="mb-2", style={"color": "#667085"}),
                        html.Div(f"📞 {TELEFONO_1}", className="mb-2", style={"color": "#667085"}),
                        html.Div(f"✉️ {EMAIL}", style={"color": "#667085"}),
                    ],
                    md=6,
                    className="text-md-end",
                ),
            ]
        )
    ),
    className="py-4",
    style={"borderTop": "1px solid rgba(15, 23, 42, 0.08)", "background": "#ffffff"},
)

layout = html.Div(
    [
        hero_section,
        metrics_section,
        services_section,
        trust_section,
        how_it_works_section,
        seo_text_section,
        faq_section,
        cta_section,
        footer_section,
    ]
)
