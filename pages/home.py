import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path="/",
    title="Gestoría en Ávila | Asesoría fiscal, laboral y contable",
    name="Inicio",
    description=(
        "Gestoría en Ávila para autónomos, empresas y particulares. "
        "Asesoría fiscal, laboral, contable y trámites con una imagen moderna, clara y profesional."
    ),
)

TELEFONO_1 = "920 000 000"
TELEFONO_2 = "620 000 000"
EMAIL = "info@gestoriaduque.com"
DIRECCION = "Paseo de San Roque 00, 05003 Ávila"
WHATSAPP_URL = "https://wa.me/34620000000"

SERVICIOS = [
    {
        "icono": "📊",
        "titulo": "Asesoría fiscal y contable",
        "texto": "Impuestos, declaraciones, IVA, IRPF, contabilidad y seguimiento económico con un enfoque claro y ordenado.",
    },
    {
        "icono": "👥",
        "titulo": "Asesoría laboral",
        "texto": "Contratos, nóminas, seguros sociales, altas, bajas e incidencias laborales para el día a día del negocio.",
    },
    {
        "icono": "🏢",
        "titulo": "Empresas y sociedades",
        "texto": "Apoyo para pymes y sociedades que buscan estructura, control administrativo y acompañamiento estable.",
    },
    {
        "icono": "🧾",
        "titulo": "Trámites administrativos",
        "texto": "Documentación, certificados, autorizaciones y gestiones con organismos públicos de forma ágil.",
    },
    {
        "icono": "🚗",
        "titulo": "Tráfico y vehículos",
        "texto": "Transferencias, cambios de titularidad y documentación relacionada con vehículos de forma sencilla.",
    },
    {
        "icono": "🙋",
        "titulo": "Atención a particulares",
        "texto": "Ayuda clara y cercana para resolver trámites concretos o recibir orientación puntual.",
    },
]

PILARES = [
    {
        "numero": "01",
        "titulo": "Claridad",
        "texto": "Explicar bien qué hacéis y cómo ayudáis genera confianza mucho antes del primer contacto.",
    },
    {
        "numero": "02",
        "titulo": "Cercanía",
        "texto": "Una gestoría local debe transmitir atención humana, accesible y fácil de entender.",
    },
    {
        "numero": "03",
        "titulo": "Solidez",
        "texto": "Una imagen bien trabajada hace que el despacho parezca más serio, más actual y más fiable.",
    },
]

SERVICIO_DESTACADO = [
    "Fiscalidad y contabilidad para autónomos",
    "Gestión laboral y nóminas",
    "Asesoría para sociedades y pymes",
    "Trámites administrativos y documentación",
]

PROCESO = [
    {
        "numero": "01",
        "titulo": "Escuchamos tu caso",
        "texto": "Entendemos qué necesitas y qué situación quieres resolver.",
    },
    {
        "numero": "02",
        "titulo": "Te orientamos con claridad",
        "texto": "Te explicamos el camino más conveniente de forma sencilla.",
    },
    {
        "numero": "03",
        "titulo": "Lo gestionamos contigo",
        "texto": "Nos ocupamos del proceso para darte más tiempo, orden y tranquilidad.",
    },
]

TESTIMONIOS = [
    {
        "nombre": "Autónomo de Ávila",
        "texto": "Transmiten mucha confianza y explican todo de forma clara. Se nota experiencia.",
    },
    {
        "nombre": "Empresa local",
        "texto": "Atención cercana y muy profesional. Responden rápido y ordenan todo muy bien.",
    },
    {
        "nombre": "Cliente particular",
        "texto": "Me ayudaron con varios trámites sin complicaciones y con un trato excelente.",
    },
]

FAQS = [
    (
        "¿Trabajáis con autónomos y empresas?",
        "Sí. La gestoría está orientada a autónomos, pymes, sociedades y también particulares.",
    ),
    (
        "¿Lleváis fiscal, laboral y contabilidad?",
        "Sí. La idea es ofrecer un servicio integral para que el cliente tenga un punto de apoyo claro y estable.",
    ),
    (
        "¿La atención es solo presencial?",
        "La base está en Ávila, pero muchas gestiones también pueden apoyarse por teléfono o email.",
    ),
]


def section_tag(text):
    return html.Div(
        text,
        className="text-uppercase fw-bold mb-3",
        style={
            "fontSize": "0.76rem",
            "letterSpacing": "0.18em",
            "color": "#667085",
        },
    )


def glass_chip(text):
    return html.Span(
        text,
        className="d-inline-flex align-items-center me-2 mb-2",
        style={
            "padding": "0.75rem 1rem",
            "borderRadius": "999px",
            "background": "rgba(255,255,255,0.72)",
            "border": "1px solid rgba(15, 23, 42, 0.08)",
            "color": "#344054",
            "fontWeight": "600",
            "fontSize": "0.93rem",
            "backdropFilter": "blur(10px)",
            "WebkitBackdropFilter": "blur(10px)",
            "boxShadow": "0 10px 24px rgba(16, 24, 40, 0.04)",
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
                "background": "rgba(255,255,255,0.88)",
                "boxShadow": "0 18px 44px rgba(16, 24, 40, 0.06)",
            },
        ),
        md=4,
        className="mb-3",
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
                "background": "rgba(255,255,255,0.9)",
                "boxShadow": "0 18px 46px rgba(16, 24, 40, 0.06)",
            },
        ),
        lg=4,
        md=6,
        className="mb-4",
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
        className="mb-4",
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
            style={
                "padding": "1.2rem 0.25rem",
            },
        ),
        md=4,
        className="mb-4",
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
        className="mb-4",
    )


hero_section = html.Section(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Div(
                                "GESTORÍA EN ÁVILA · FISCAL · LABORAL · CONTABLE · TRÁMITES",
                                className="mb-4",
                                style={
                                    "display": "inline-flex",
                                    "alignItems": "center",
                                    "padding": "0.72rem 1rem",
                                    "borderRadius": "999px",
                                    "background": "rgba(255,255,255,0.8)",
                                    "border": "1px solid rgba(15, 23, 42, 0.08)",
                                    "fontWeight": "700",
                                    "fontSize": "0.78rem",
                                    "letterSpacing": "0.08em",
                                    "color": "#0d6efd",
                                    "boxShadow": "0 8px 22px rgba(16, 24, 40, 0.04)",
                                },
                            ),
                            html.H1(
                                "Una gestoría con imagen actual, sólida y preparada para transmitir confianza en segundos",
                                className="fw-bold mb-4",
                                style={
                                    "fontSize": "clamp(2.9rem, 5.3vw, 5.5rem)",
                                    "lineHeight": "0.96",
                                    "letterSpacing": "-0.07em",
                                    "color": "#101828",
                                    "maxWidth": "900px",
                                },
                            ),
                            html.P(
                                "Esta versión de home está diseñada para que el despacho se perciba mucho más moderno, más profesional y más fiable. "
                                "Menos aspecto de gestoría clásica. Más sensación de firma sólida y actual.",
                                className="mb-4",
                                style={
                                    "fontSize": "1.08rem",
                                    "lineHeight": "1.95",
                                    "color": "#475467",
                                    "maxWidth": "740px",
                                },
                            ),
                            html.Div(
                                [
                                    glass_chip("Más de 70 años de experiencia"),
                                    glass_chip("Despacho local en Ávila"),
                                    glass_chip("Asesoría integral"),
                                    glass_chip("Atención clara y cercana"),
                                ],
                                className="mb-4",
                            ),
                            html.Div(
                                [
                                    dbc.Button(
                                        "Llamar ahora",
                                        href=f"tel:{TELEFONO_1.replace(' ', '')}",
                                        color="primary",
                                        className="rounded-pill fw-bold me-2 mb-2",
                                        style={
                                            "padding": "1rem 1.6rem",
                                            "minHeight": "58px",
                                            "fontSize": "1rem",
                                            "boxShadow": "0 14px 34px rgba(13, 110, 253, 0.22)",
                                        },
                                    ),
                                    dbc.Button(
                                        "WhatsApp",
                                        href=WHATSAPP_URL,
                                        target="_blank",
                                        color="light",
                                        className="rounded-pill fw-semibold border me-2 mb-2",
                                        style={
                                            "padding": "1rem 1.6rem",
                                            "minHeight": "58px",
                                            "fontSize": "1rem",
                                            "background": "rgba(255,255,255,0.82)",
                                        },
                                    ),
                                    dbc.Button(
                                        "Enviar email",
                                        href=f"mailto:{EMAIL}",
                                        color="link",
                                        className="fw-semibold text-decoration-none mb-2",
                                        style={
                                            "padding": "1rem 1rem",
                                            "minHeight": "58px",
                                            "fontSize": "1rem",
                                            "color": "#101828",
                                        },
                                    ),
                                ]
                            ),
                        ],
                        lg=7,
                        className="mb-5 mb-lg-0",
                    ),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.Div(
                                        "Despacho local · confianza directa",
                                        className="mb-3 fw-bold",
                                        style={
                                            "fontSize": "0.78rem",
                                            "letterSpacing": "0.14em",
                                            "textTransform": "uppercase",
                                            "color": "#0d6efd",
                                        },
                                    ),
                                    html.H2(
                                        "Un bloque de contacto más elegante genera mejor sensación de marca",
                                        className="fw-bold mb-4",
                                        style={
                                            "fontSize": "1.78rem",
                                            "lineHeight": "1.08",
                                            "letterSpacing": "-0.04em",
                                            "color": "#101828",
                                        },
                                    ),
                                    html.Div("📞 Teléfono", className="fw-semibold mb-1", style={"color": "#101828"}),
                                    html.Div(TELEFONO_1, className="mb-3", style={"color": "#667085"}),
                                    html.Div("📱 Móvil", className="fw-semibold mb-1", style={"color": "#101828"}),
                                    html.Div(TELEFONO_2, className="mb-3", style={"color": "#667085"}),
                                    html.Div("✉️ Email", className="fw-semibold mb-1", style={"color": "#101828"}),
                                    html.Div(EMAIL, className="mb-3", style={"color": "#667085"}),
                                    html.Div("📍 Dirección", className="fw-semibold mb-1", style={"color": "#101828"}),
                                    html.Div(DIRECCION, className="mb-4", style={"color": "#667085", "lineHeight": "1.7"}),
                                    dbc.Button(
                                        "Solicitar información",
                                        href=f"mailto:{EMAIL}",
                                        color="primary",
                                        className="w-100 rounded-pill fw-bold mb-2",
                                        style={"padding": "1rem 1.2rem", "minHeight": "54px"},
                                    ),
                                    dbc.Button(
                                        "Contactar por WhatsApp",
                                        href=WHATSAPP_URL,
                                        target="_blank",
                                        color="success",
                                        className="w-100 rounded-pill fw-semibold",
                                        style={"padding": "1rem 1.2rem", "minHeight": "54px"},
                                    ),
                                ]
                            ),
                            className="border-0",
                            style={
                                "borderRadius": "30px",
                                "background": "rgba(255,255,255,0.84)",
                                "boxShadow": "0 28px 80px rgba(16, 24, 40, 0.10)",
                                "backdropFilter": "blur(12px)",
                                "WebkitBackdropFilter": "blur(12px)",
                            },
                        ),
                        lg=5,
                    ),
                ],
                className="align-items-center",
            )
        ]
    ),
    style={
        "paddingTop": "5.6rem",
        "paddingBottom": "4.7rem",
        "background": (
            "radial-gradient(circle at 0% 0%, rgba(13,110,253,0.15), transparent 28%),"
            "radial-gradient(circle at 100% 0%, rgba(25,135,84,0.08), transparent 24%),"
            "linear-gradient(180deg, #ffffff 0%, #f7faff 54%, #ffffff 100%)"
        ),
    },
)

stats_section = html.Section(
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
    style={"paddingBottom": "4rem"},
)

services_section = html.Section(
    dbc.Container(
        [
            section_tag("Servicios"),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H2(
                                "Diseñada para que el visitante entienda rápido qué hacéis y por qué merece la pena contactar",
                                className="fw-bold mb-3",
                                style={
                                    "fontSize": "clamp(2.1rem, 3.7vw, 3.25rem)",
                                    "lineHeight": "1.02",
                                    "letterSpacing": "-0.055em",
                                    "color": "#101828",
                                    "maxWidth": "820px",
                                },
                            ),
                            html.P(
                                "Aquí la web ya no parece una lista tradicional de servicios. Tiene más ritmo, más aire y una percepción más premium.",
                                className="mb-5",
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
    style={
        "paddingTop": "3rem",
        "paddingBottom": "4.8rem",
        "scrollMarginTop": "120px",
    },
)

pillars_section = html.Section(
    dbc.Container(
        [
            section_tag("Pilares"),
            dbc.Row(
                [
                    dbc.Col(
                        html.H2(
                            "Una gestoría local puede parecer muchísimo más potente con una presentación adecuada",
                            className="fw-bold mb-4",
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
                            className="mb-4 mb-lg-0",
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
    style={
        "paddingTop": "4.6rem",
        "paddingBottom": "4.6rem",
        "background": "#f8fafc",
    },
)

featured_section = html.Section(
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
                                    className="fw-bold mb-3",
                                    style={
                                        "fontSize": "clamp(2rem, 3vw, 2.7rem)",
                                        "lineHeight": "1.05",
                                        "letterSpacing": "-0.04em",
                                        "color": "#101828",
                                    },
                                ),
                                html.P(
                                    "La experiencia del despacho es una ventaja enorme. Esta sección la convierte en algo visible, memorable y comercialmente útil.",
                                    className="mb-4 mb-lg-0",
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
                            [
                                list_check(text) for text in SERVICIO_DESTACADO
                            ],
                            lg=5,
                            className="d-flex flex-column justify-content-center",
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
    style={"paddingBottom": "4.8rem"},
)

process_section = html.Section(
    dbc.Container(
        [
            section_tag("Proceso"),
            dbc.Row(
                [
                    dbc.Col(
                        html.H2(
                            "Una experiencia simple y elegante ayuda a reducir fricción y a generar más contacto",
                            className="fw-bold mb-4",
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
                            className="mb-4 mb-lg-0",
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
    style={"paddingTop": "4.6rem", "paddingBottom": "4.6rem"},
)

testimonials_section = html.Section(
    dbc.Container(
        [
            section_tag("Opiniones"),
            html.H2(
                "La confianza aumenta mucho cuando la imagen se apoya en testimonios reales",
                className="fw-bold mb-3",
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
                className="mb-5",
                style={
                    "color": "#667085",
                    "lineHeight": "1.9",
                    "maxWidth": "780px",
                },
            ),
            dbc.Row([testimonial_card(t["nombre"], t["texto"]) for t in TESTIMONIOS]),
        ]
    ),
    style={
        "paddingTop": "4.6rem",
        "paddingBottom": "4.6rem",
        "background": "#f8fafc",
    },
)

seo_section = html.Section(
    dbc.Container(
        [
            section_tag("SEO local"),
            html.H2(
                "Gestoría en Ávila con enfoque fiscal, laboral, contable y administrativo",
                className="fw-bold mb-3",
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
                className="mb-0",
                style={
                    "color": "#667085",
                    "lineHeight": "1.95",
                    "maxWidth": "1040px",
                },
            ),
        ]
    ),
    style={"paddingTop": "4.6rem", "paddingBottom": "4.6rem"},
)

faq_section = html.Section(
    dbc.Container(
        [
            section_tag("Preguntas frecuentes"),
            html.H2(
                "Dudas habituales antes de contactar con una gestoría",
                className="fw-bold mb-4",
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
    style={
        "paddingTop": "4.6rem",
        "paddingBottom": "4.6rem",
        "background": "#f8fafc",
    },
)

cta_section = html.Section(
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
                                        className="fw-bold mb-3",
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
                                        className="mb-0",
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
    style={
        "paddingTop": "2rem",
        "paddingBottom": "5rem",
        "scrollMarginTop": "120px",
    },
)

footer_section = html.Footer(
    dbc.Container(
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            "Gestoría Duque · Demo",
                            className="fw-bold mb-2",
                            style={
                                "color": "#101828",
                                "fontSize": "1.05rem",
                                "letterSpacing": "-0.02em",
                            },
                        ),
                        html.Div(
                            "Propuesta visual de renovación web con enfoque premium, local y comercial.",
                            style={"color": "#667085", "lineHeight": "1.8"},
                        ),
                    ],
                    md=6,
                    className="mb-4 mb-md-0",
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
    style={
        "paddingTop": "2rem",
        "paddingBottom": "2.5rem",
        "borderTop": "1px solid rgba(15, 23, 42, 0.08)",
        "background": "#ffffff",
    },
)

floating_whatsapp = html.A(
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

layout = html.Div(
    [
        hero_section,
        stats_section,
        services_section,
        pillars_section,
        featured_section,
        process_section,
        testimonials_section,
        seo_section,
        faq_section,
        cta_section,
        footer_section,
        floating_whatsapp,
    ],
    style={
        "background": "#ffffff",
        "overflow": "hidden",
    },
)
