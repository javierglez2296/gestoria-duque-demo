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
        "Asesoría fiscal, laboral, contable y trámites con atención clara, cercana y profesional."
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
        "texto": "Impuestos, contabilidad, cierres, IVA, IRPF y declaraciones con un enfoque claro, ordenado y profesional.",
    },
    {
        "icono": "👥",
        "titulo": "Asesoría laboral",
        "texto": "Contratos, nóminas, seguros sociales, altas, bajas e incidencias del día a día laboral de tu negocio.",
    },
    {
        "icono": "🏢",
        "titulo": "Empresas y sociedades",
        "texto": "Apoyo para pymes y sociedades que buscan control, orden administrativo y acompañamiento constante.",
    },
    {
        "icono": "🧾",
        "titulo": "Trámites administrativos",
        "texto": "Certificados, autorizaciones, documentación y gestiones habituales con organismos públicos.",
    },
    {
        "icono": "🚗",
        "titulo": "Tráfico y vehículos",
        "texto": "Transferencias, cambios de titularidad y documentación relacionada con vehículos de forma ágil.",
    },
    {
        "icono": "🙋",
        "titulo": "Atención a particulares",
        "texto": "Acompañamiento cercano para resolver trámites concretos o recibir orientación puntual con claridad.",
    },
]

BENEFICIOS = [
    {
        "titulo": "Claridad",
        "texto": "Una web premium ayuda a que el cliente entienda rápido qué hacéis y por qué puede confiar.",
    },
    {
        "titulo": "Confianza",
        "texto": "Una mejor presentación transmite orden, experiencia y sensación de despacho sólido.",
    },
    {
        "titulo": "Conversión",
        "texto": "Cuanto más fácil es entenderos y contactar, más probable es que os llamen o escriban.",
    },
]

PROCESO = [
    {
        "numero": "01",
        "titulo": "Entendemos tu caso",
        "texto": "Escuchamos qué necesitas y en qué contexto te podemos ayudar.",
    },
    {
        "numero": "02",
        "titulo": "Te orientamos",
        "texto": "Te explicamos con claridad qué pasos conviene seguir y cómo resolverlo.",
    },
    {
        "numero": "03",
        "titulo": "Lo gestionamos contigo",
        "texto": "Nos ocupamos del proceso para darte más orden, tiempo y tranquilidad.",
    },
]

TESTIMONIOS = [
    {
        "nombre": "Autónomo de Ávila",
        "texto": "Muy buena atención. Transmiten confianza y te explican todo con claridad.",
    },
    {
        "nombre": "Empresa local",
        "texto": "Profesionales, cercanos y rápidos. Se nota experiencia en la forma de trabajar.",
    },
    {
        "nombre": "Cliente particular",
        "texto": "Me ayudaron con varios trámites de forma sencilla y con un trato excelente.",
    },
]

FAQS = [
    (
        "¿Trabajáis con autónomos y empresas?",
        "Sí. La gestoría está orientada a autónomos, pymes, sociedades y también particulares.",
    ),
    (
        "¿Lleváis fiscal, laboral y contabilidad?",
        "Sí. El objetivo es ofrecer un servicio integral para que el cliente tenga un apoyo estable y claro.",
    ),
    (
        "¿Solo atendéis en Ávila?",
        "La base del despacho está en Ávila, lo que refuerza la cercanía local, aunque muchas gestiones también se pueden apoyar por teléfono o email.",
    ),
]


def section_kicker(text):
    return html.Div(
        text,
        className="text-uppercase fw-bold mb-3",
        style={
            "fontSize": "0.76rem",
            "letterSpacing": "0.16em",
            "color": "#667085",
        },
    )


def pill(text):
    return html.Span(
        text,
        className="d-inline-flex align-items-center me-2 mb-2",
        style={
            "padding": "0.72rem 1rem",
            "borderRadius": "999px",
            "background": "rgba(255,255,255,0.82)",
            "border": "1px solid rgba(15, 23, 42, 0.08)",
            "color": "#344054",
            "fontWeight": "600",
            "fontSize": "0.94rem",
            "boxShadow": "0 8px 18px rgba(16, 24, 40, 0.04)",
            "backdropFilter": "blur(10px)",
            "WebkitBackdropFilter": "blur(10px)",
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
                            "fontSize": "clamp(1.8rem, 3vw, 2.5rem)",
                            "lineHeight": "1",
                            "letterSpacing": "-0.05em",
                            "color": "#101828",
                        },
                    ),
                    html.Div(
                        label,
                        style={
                            "color": "#667085",
                            "fontSize": "0.95rem",
                        },
                    ),
                ]
            ),
            className="border-0 h-100",
            style={
                "borderRadius": "22px",
                "background": "#ffffff",
                "boxShadow": "0 14px 34px rgba(16, 24, 40, 0.06)",
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
                            "width": "56px",
                            "height": "56px",
                            "display": "flex",
                            "alignItems": "center",
                            "justifyContent": "center",
                            "fontSize": "1.7rem",
                            "borderRadius": "18px",
                            "background": "linear-gradient(135deg, #eef4ff 0%, #f8fbff 100%)",
                        },
                    ),
                    html.H3(
                        titulo,
                        className="fw-bold mb-2",
                        style={
                            "fontSize": "1.15rem",
                            "color": "#101828",
                            "letterSpacing": "-0.02em",
                        },
                    ),
                    html.P(
                        texto,
                        className="mb-0",
                        style={
                            "color": "#667085",
                            "lineHeight": "1.8",
                            "fontSize": "0.97rem",
                        },
                    ),
                ]
            ),
            className="border-0 h-100",
            style={
                "borderRadius": "24px",
                "background": "rgba(255,255,255,0.92)",
                "boxShadow": "0 18px 42px rgba(16, 24, 40, 0.06)",
            },
        ),
        lg=4,
        md=6,
        className="mb-4",
    )


def benefit_card(titulo, texto):
    return dbc.Col(
        dbc.Card(
            dbc.CardBody(
                [
                    html.Div(
                        "•",
                        className="mb-3",
                        style={
                            "fontSize": "2rem",
                            "lineHeight": "1",
                            "fontWeight": "700",
                            "color": "#0d6efd",
                        },
                    ),
                    html.H3(
                        titulo,
                        className="fw-bold mb-2",
                        style={
                            "fontSize": "1.12rem",
                            "color": "#101828",
                            "letterSpacing": "-0.02em",
                        },
                    ),
                    html.P(
                        texto,
                        className="mb-0",
                        style={"color": "#667085", "lineHeight": "1.8"},
                    ),
                ]
            ),
            className="border-0 h-100",
            style={
                "borderRadius": "24px",
                "background": "#ffffff",
                "boxShadow": "0 16px 38px rgba(16, 24, 40, 0.06)",
            },
        ),
        md=4,
        className="mb-4",
    )


def process_item(numero, titulo, texto):
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
                        "fontSize": "1.2rem",
                        "color": "#101828",
                        "letterSpacing": "-0.03em",
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
                            "fontSize": "0.98rem",
                            "letterSpacing": "0.08em",
                        },
                    ),
                    html.P(
                        f"“{texto}”",
                        className="mb-4",
                        style={
                            "color": "#344054",
                            "lineHeight": "1.9",
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
                "borderRadius": "24px",
                "background": "linear-gradient(180deg, #ffffff 0%, #fbfcfe 100%)",
                "boxShadow": "0 16px 42px rgba(16, 24, 40, 0.06)",
            },
        ),
        md=4,
        className="mb-4",
    )


top_strip = html.Div(
    dbc.Container(
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        "Ávila · Más de 70 años de experiencia · Atención cercana y profesional",
                        className="small",
                        style={"color": "#667085", "fontWeight": "600"},
                    ),
                    md=8,
                    className="d-none d-md-flex align-items-center",
                ),
                dbc.Col(
                    html.Div(
                        [
                            html.A(
                                "📞 920 000 000",
                                href=f"tel:{TELEFONO_1.replace(' ', '')}",
                                style={
                                    "textDecoration": "none",
                                    "color": "#344054",
                                    "fontWeight": "600",
                                    "marginRight": "1rem",
                                },
                            ),
                            html.A(
                                "✉️ info@gestoriaduque.com",
                                href=f"mailto:{EMAIL}",
                                style={
                                    "textDecoration": "none",
                                    "color": "#344054",
                                    "fontWeight": "600",
                                },
                            ),
                        ],
                        className="small d-flex justify-content-md-end flex-wrap",
                    ),
                    md=4,
                    className="d-flex align-items-center justify-content-start justify-content-md-end",
                ),
            ],
            className="py-2",
        )
    ),
    style={
        "borderBottom": "1px solid rgba(15, 23, 42, 0.06)",
        "background": "rgba(255,255,255,0.86)",
        "backdropFilter": "blur(10px)",
        "WebkitBackdropFilter": "blur(10px)",
    },
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
                                    "background": "rgba(255,255,255,0.78)",
                                    "border": "1px solid rgba(15, 23, 42, 0.08)",
                                    "fontWeight": "700",
                                    "fontSize": "0.78rem",
                                    "letterSpacing": "0.08em",
                                    "color": "#0d6efd",
                                    "boxShadow": "0 8px 22px rgba(16, 24, 40, 0.04)",
                                },
                            ),
                            html.H1(
                                "Una imagen más premium para una gestoría que quiera destacar de verdad",
                                className="fw-bold mb-4",
                                style={
                                    "fontSize": "clamp(2.8rem, 5vw, 5.2rem)",
                                    "lineHeight": "0.97",
                                    "letterSpacing": "-0.065em",
                                    "color": "#101828",
                                    "maxWidth": "860px",
                                },
                            ),
                            html.P(
                                "Esta home está planteada para que el despacho se perciba como más sólido, más actual y mucho más fiable. "
                                "No solo para verse mejor, sino para convertir mejor.",
                                className="mb-4",
                                style={
                                    "fontSize": "1.08rem",
                                    "lineHeight": "1.9",
                                    "color": "#475467",
                                    "maxWidth": "720px",
                                },
                            ),
                            html.Div(
                                [
                                    pill("Más de 70 años de experiencia"),
                                    pill("Despacho local en Ávila"),
                                    pill("Asesoría fiscal, laboral y contable"),
                                    pill("Trato claro y cercano"),
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
                                            "padding": "1rem 1.55rem",
                                            "minHeight": "58px",
                                            "fontSize": "1rem",
                                            "boxShadow": "0 14px 32px rgba(13, 110, 253, 0.22)",
                                        },
                                    ),
                                    dbc.Button(
                                        "Abrir WhatsApp",
                                        href=WHATSAPP_URL,
                                        target="_blank",
                                        color="light",
                                        className="rounded-pill fw-semibold border me-2 mb-2",
                                        style={
                                            "padding": "1rem 1.55rem",
                                            "minHeight": "58px",
                                            "fontSize": "1rem",
                                            "background": "rgba(255,255,255,0.86)",
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
                                        "Contacto directo",
                                        className="mb-2 fw-bold",
                                        style={
                                            "fontSize": "0.78rem",
                                            "letterSpacing": "0.14em",
                                            "textTransform": "uppercase",
                                            "color": "#0d6efd",
                                        },
                                    ),
                                    html.H2(
                                        "Una presencia digital más fuerte genera más confianza",
                                        className="fw-bold mb-4",
                                        style={
                                            "fontSize": "1.8rem",
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
                                        style={"padding": "0.98rem 1.2rem", "minHeight": "54px"},
                                    ),
                                    dbc.Button(
                                        "Contactar por WhatsApp",
                                        href=WHATSAPP_URL,
                                        target="_blank",
                                        color="success",
                                        className="w-100 rounded-pill fw-semibold",
                                        style={"padding": "0.98rem 1.2rem", "minHeight": "54px"},
                                    ),
                                ]
                            ),
                            className="border-0",
                            style={
                                "borderRadius": "30px",
                                "background": "rgba(255,255,255,0.84)",
                                "boxShadow": "0 26px 70px rgba(16, 24, 40, 0.10)",
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
        "paddingTop": "5.4rem",
        "paddingBottom": "4.5rem",
        "background": (
            "radial-gradient(circle at 0% 0%, rgba(13,110,253,0.14), transparent 28%),"
            "radial-gradient(circle at 100% 0%, rgba(25,135,84,0.08), transparent 24%),"
            "linear-gradient(180deg, #ffffff 0%, #f7faff 56%, #ffffff 100%)"
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
            section_kicker("Servicios"),
            html.H2(
                "Una propuesta visual más actual puede cambiar por completo la percepción del despacho",
                className="fw-bold mb-3",
                style={
                    "fontSize": "clamp(2rem, 3.5vw, 3.1rem)",
                    "lineHeight": "1.03",
                    "letterSpacing": "-0.05em",
                    "color": "#101828",
                    "maxWidth": "780px",
                },
            ),
            html.P(
                "La web no debería parecer una lista genérica de servicios. Debería hacer que el visitante entienda rápido qué resolvéis, a quién ayudáis y por qué merece la pena contactar.",
                className="mb-5",
                style={
                    "color": "#667085",
                    "lineHeight": "1.9",
                    "maxWidth": "860px",
                    "fontSize": "1.01rem",
                },
            ),
            dbc.Row([service_card(s["icono"], s["titulo"], s["texto"]) for s in SERVICIOS]),
        ]
    ),
    id="servicios",
    style={"paddingTop": "3rem", "paddingBottom": "4.5rem"},
)

benefits_section = html.Section(
    dbc.Container(
        [
            section_kicker("Valor"),
            dbc.Row(
                [
                    dbc.Col(
                        html.H2(
                            "Más que una web bonita: una imagen que transmite orden, seriedad y confianza",
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
                            "Cuando una gestoría se presenta mejor, parece más sólida. Y cuando parece más sólida, convierte mejor.",
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
            dbc.Row([benefit_card(b["titulo"], b["texto"]) for b in BENEFICIOS]),
        ]
    ),
    style={
        "paddingTop": "4.5rem",
        "paddingBottom": "4.5rem",
        "background": "#f8fafc",
    },
)

positioning_section = html.Section(
    dbc.Container(
        dbc.Card(
            dbc.CardBody(
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                section_kicker("Confianza"),
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
                                    "La combinación de experiencia, despacho local y trato cercano tiene muchísimo valor. Esta sección está pensada para que se perciba de inmediato.",
                                    className="mb-0",
                                    style={
                                        "color": "#667085",
                                        "lineHeight": "1.9",
                                        "maxWidth": "720px",
                                    },
                                ),
                            ],
                            lg=8,
                            className="mb-4 mb-lg-0",
                        ),
                        dbc.Col(
                            html.Div(
                                [
                                    html.Div("✔ Atención cercana y profesional", className="mb-3 fw-semibold"),
                                    html.Div("✔ Trayectoria consolidada", className="mb-3 fw-semibold"),
                                    html.Div("✔ Servicios bien definidos", className="mb-3 fw-semibold"),
                                    html.Div("✔ Contacto visible y sencillo", className="fw-semibold"),
                                ],
                                style={"color": "#344054", "fontSize": "1rem"},
                            ),
                            lg=4,
                            className="d-flex align-items-center",
                        ),
                    ]
                )
            ),
            className="border-0",
            style={
                "borderRadius": "30px",
                "background": "linear-gradient(135deg, #ffffff 0%, #f8fbff 100%)",
                "boxShadow": "0 24px 60px rgba(16, 24, 40, 0.08)",
            },
        )
    ),
    style={"paddingBottom": "4.5rem"},
)

process_section = html.Section(
    dbc.Container(
        [
            section_kicker("Proceso"),
            dbc.Row(
                [
                    dbc.Col(
                        html.H2(
                            "Una experiencia sencilla y elegante también ayuda a vender mejor",
                            className="fw-bold mb-4",
                            style={
                                "fontSize": "clamp(2rem, 3.3vw, 2.9rem)",
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
                            "Explicar el proceso reduce fricción y da sensación de orden. Eso facilita mucho que el visitante dé el paso.",
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
            dbc.Row([process_item(p["numero"], p["titulo"], p["texto"]) for p in PROCESO]),
        ]
    ),
    style={"paddingTop": "4.5rem", "paddingBottom": "4.5rem"},
)

testimonials_section = html.Section(
    dbc.Container(
        [
            section_kicker("Opiniones"),
            html.H2(
                "La confianza aumenta muchísimo cuando se apoya en testimonios reales",
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
                "En la versión final conviene sustituir estos textos por reseñas reales de Google o testimonios auténticos del despacho.",
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
        "paddingTop": "4.5rem",
        "paddingBottom": "4.5rem",
        "background": "#f8fafc",
    },
)

seo_section = html.Section(
    dbc.Container(
        [
            section_kicker("SEO local"),
            html.H2(
                "Gestoría en Ávila con enfoque fiscal, laboral, contable y administrativo",
                className="fw-bold mb-3",
                style={
                    "fontSize": "clamp(1.95rem, 3vw, 2.6rem)",
                    "lineHeight": "1.06",
                    "letterSpacing": "-0.04em",
                    "color": "#101828",
                    "maxWidth": "860px",
                },
            ),
            html.P(
                "Esta home está pensada para reforzar búsquedas como gestoría en Ávila, asesoría fiscal en Ávila, asesoría laboral en Ávila, gestoría para autónomos en Ávila o asesoría contable en Ávila. Al mismo tiempo, mejora bastante la conversión al explicar mejor qué hace el despacho, a quién ayuda y cómo contactar.",
                className="mb-0",
                style={
                    "color": "#667085",
                    "lineHeight": "1.95",
                    "maxWidth": "1040px",
                },
            ),
        ]
    ),
    style={"paddingTop": "4.5rem", "paddingBottom": "4.5rem"},
)

faq_section = html.Section(
    dbc.Container(
        [
            section_kicker("Preguntas frecuentes"),
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
        "paddingTop": "4.5rem",
        "paddingBottom": "4.5rem",
        "background": "#f8fafc",
    },
)

cta_section = html.Section(
    dbc.Container(
        dbc.Card(
            dbc.CardBody(
                [
                    section_kicker("Contacto"),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.H2(
                                        "Una mejor imagen digital suele traer más llamadas y más contactos",
                                        className="fw-bold mb-3",
                                        style={
                                            "fontSize": "clamp(2rem, 3.4vw, 3rem)",
                                            "lineHeight": "1.03",
                                            "letterSpacing": "-0.05em",
                                            "color": "#101828",
                                            "maxWidth": "760px",
                                        },
                                    ),
                                    html.P(
                                        "Esta demo está construida para que el visitante entienda rápido qué hacéis, por qué confiar y cómo contactar sin fricción.",
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
                "boxShadow": "0 24px 70px rgba(16, 24, 40, 0.10)",
            },
        )
    ),
    id="contacto",
    style={"paddingTop": "2rem", "paddingBottom": "5rem"},
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
        top_strip,
        hero_section,
        stats_section,
        services_section,
        benefits_section,
        positioning_section,
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
