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
WHATSAPP_URL = "https://wa.me/34620000000"

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

PROBLEMAS = [
    {
        "numero": 1,
        "titulo": "No sabes qué impuestos o trámites te tocan",
        "texto": "Te orientamos de forma clara para que sepas qué hacer y cuándo hacerlo.",
    },
    {
        "numero": 2,
        "titulo": "Pierdes tiempo con papeleo y gestiones",
        "texto": "Nos ocupamos de la parte administrativa para que ganes tiempo y tranquilidad.",
    },
    {
        "numero": 3,
        "titulo": "Tienes dudas y no sabes a quién llamar",
        "texto": "Tienes un despacho cercano al que consultar cuando lo necesites.",
    },
]

RESULTADOS = [
    {
        "numero": 1,
        "titulo": "Más tranquilidad",
        "texto": "Sientes que tu gestión está en orden y bien acompañada.",
    },
    {
        "numero": 2,
        "titulo": "Más tiempo",
        "texto": "Te centras en tu trabajo o negocio mientras la gestoría te apoya.",
    },
    {
        "numero": 3,
        "titulo": "Más seguridad",
        "texto": "Reducir errores y actuar con criterio también evita muchos problemas futuros.",
    },
]

PASOS = [
    {
        "numero": 1,
        "titulo": "Cuéntanos tu caso",
        "texto": "Llámanos, escríbenos o ven al despacho para explicarnos qué necesitas.",
    },
    {
        "numero": 2,
        "titulo": "Te orientamos",
        "texto": "Analizamos tu situación y te explicamos la mejor forma de resolverla.",
    },
    {
        "numero": 3,
        "titulo": "Lo gestionamos contigo",
        "texto": "Nos encargamos del proceso para que todo sea más fácil, claro y ágil.",
    },
]

REVIEWS = [
    {
        "nombre": "Cliente autónomo",
        "texto": "Atención muy cercana y profesional. Me ayudan con todo y me da mucha tranquilidad.",
    },
    {
        "nombre": "Empresa local",
        "texto": "Muy buena experiencia. Responden rápido y se nota que conocen bien el trabajo.",
    },
    {
        "nombre": "Cliente particular",
        "texto": "Me resolvieron varios trámites de forma clara y sin complicaciones.",
    },
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
                        "fontSize": "1.8rem",
                        "lineHeight": "1.1",
                        "color": "#101828",
                    },
                ),
                html.Div(
                    label,
                    style={
                        "fontSize": "0.95rem",
                        "color": "#667085",
                    },
                ),
            ]
        ),
        className="border-0 rounded-4 h-100",
        style={
            "background": "#ffffff",
            "boxShadow": "0 14px 36px rgba(16, 24, 40, 0.07)",
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
                        style={"color": "#667085", "lineHeight": "1.75"},
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


def info_step(number, title, text, color="#0d6efd"):
    return dbc.Col(
        dbc.Card(
            dbc.CardBody(
                [
                    html.Div(
                        str(number),
                        className="d-inline-flex align-items-center justify-content-center rounded-circle mb-3",
                        style={
                            "width": "46px",
                            "height": "46px",
                            "background": color,
                            "color": "white",
                            "fontWeight": "700",
                            "fontSize": "1rem",
                        },
                    ),
                    html.H3(title, className="h5 fw-bold mb-2", style={"color": "#101828"}),
                    html.P(
                        text,
                        className="mb-0",
                        style={"color": "#667085", "lineHeight": "1.75"},
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


def review_card(nombre, texto):
    return dbc.Col(
        dbc.Card(
            dbc.CardBody(
                [
                    html.Div("★★★★★", className="mb-3", style={"color": "#f59e0b", "fontSize": "1.05rem"}),
                    html.P(
                        f"“{texto}”",
                        className="mb-3",
                        style={"color": "#344054", "lineHeight": "1.8"},
                    ),
                    html.Div(nombre, className="fw-semibold", style={"color": "#101828"}),
                ]
            ),
            className="border-0 rounded-4 h-100",
            style={
                "background": "#ffffff",
                "boxShadow": "0 14px 34px rgba(16, 24, 40, 0.06)",
            },
        ),
        md=4,
        className="mb-4",
    )


hero_section = html.Div(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Div(
                                "GESTORÍA EN ÁVILA · FISCAL · LABORAL · CONTABLE · TRÁMITES",
                                className="mb-3",
                                style={
                                    "display": "inline-block",
                                    "padding": "0.55rem 0.95rem",
                                    "borderRadius": "999px",
                                    "background": "#eef4ff",
                                    "color": "#0d6efd",
                                    "fontWeight": "700",
                                    "fontSize": "0.82rem",
                                    "letterSpacing": "0.03em",
                                },
                            ),
                            html.H1(
                                "Una gestoría en Ávila que transmite confianza desde el primer segundo",
                                className="fw-bold mb-3",
                                style={
                                    "fontSize": "clamp(2.3rem, 4.8vw, 4.3rem)",
                                    "lineHeight": "1.03",
                                    "letterSpacing": "-0.05em",
                                    "color": "#101828",
                                    "maxWidth": "860px",
                                },
                            ),
                            html.P(
                                "Ayuda profesional para autónomos, empresas y particulares en fiscalidad, laboral, contabilidad y trámites. "
                                "Una web más clara, más premium y más orientada a generar llamadas y contactos.",
                                className="mb-4",
                                style={
                                    "fontSize": "1.08rem",
                                    "color": "#475467",
                                    "lineHeight": "1.85",
                                    "maxWidth": "760px",
                                },
                            ),
                            html.Div(
                                [
                                    html.Span("✔ Más de 70 años ayudando a clientes", className="me-3 mb-2 d-inline-block"),
                                    html.Span("✔ Respuesta cercana", className="me-3 mb-2 d-inline-block"),
                                    html.Span("✔ Gestión clara y profesional", className="mb-2 d-inline-block"),
                                ],
                                style={
                                    "fontSize": "0.96rem",
                                    "color": "#667085",
                                    "marginBottom": "1.1rem",
                                },
                            ),
                            html.Div(
                                [advantage_chip(v) for v in VENTAJAS],
                                className="mb-4",
                            ),
                            html.Div(
                                [
                                    dbc.Button(
                                        "Llamar ahora",
                                        href=f"tel:{TELEFONO_1.replace(' ', '')}",
                                        color="primary",
                                        className="rounded-pill px-4 py-3 fw-bold me-2 mb-2",
                                        style={
                                            "fontSize": "1rem",
                                            "boxShadow": "0 10px 24px rgba(13, 110, 253, 0.25)",
                                        },
                                    ),
                                    dbc.Button(
                                        "WhatsApp",
                                        href=WHATSAPP_URL,
                                        target="_blank",
                                        color="success",
                                        className="rounded-pill px-4 py-3 fw-bold me-2 mb-2",
                                        style={"fontSize": "1rem"},
                                    ),
                                    dbc.Button(
                                        "Enviar email",
                                        href=f"mailto:{EMAIL}",
                                        color="light",
                                        className="rounded-pill px-4 py-3 fw-semibold border mb-2",
                                        style={"fontSize": "1rem"},
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
                                    html.Div("📞 Teléfono", className="fw-semibold mb-1"),
                                    html.Div(TELEFONO_1, className="mb-3", style={"color": "#667085"}),
                                    html.Div("📱 Móvil", className="fw-semibold mb-1"),
                                    html.Div(TELEFONO_2, className="mb-3", style={"color": "#667085"}),
                                    html.Div("✉️ Email", className="fw-semibold mb-1"),
                                    html.Div(EMAIL, className="mb-3", style={"color": "#667085"}),
                                    html.Div("📍 Dirección", className="fw-semibold mb-1"),
                                    html.Div(DIRECCION, className="mb-4", style={"color": "#667085"}),
                                    dbc.Button(
                                        "Escríbenos ahora",
                                        href=f"mailto:{EMAIL}",
                                        color="primary",
                                        className="w-100 rounded-pill fw-semibold py-3 mb-2",
                                    ),
                                    dbc.Button(
                                        "Abrir WhatsApp",
                                        href=WHATSAPP_URL,
                                        target="_blank",
                                        color="success",
                                        className="w-100 rounded-pill fw-semibold py-3",
                                    ),
                                ]
                            ),
                            className="border-0 rounded-4 h-100",
                            style={
                                "background": "#ffffff",
                                "boxShadow": "0 20px 54px rgba(16, 24, 40, 0.10)",
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
            "radial-gradient(circle at top left, rgba(13,110,253,0.12), transparent 35%),"
            "radial-gradient(circle at top right, rgba(25,135,84,0.07), transparent 30%),"
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

problems_section = html.Div(
    dbc.Container(
        [
            section_eyebrow("Problemas comunes"),
            html.H2(
                "Muchos clientes llegan con dudas, papeleo y sensación de ir tarde",
                className="fw-bold mb-3",
                style={
                    "fontSize": "clamp(1.8rem, 3vw, 2.6rem)",
                    "color": "#101828",
                },
            ),
            html.P(
                "Una buena web de gestoría no solo enumera servicios. También deja claro qué problemas ayuda a resolver y por qué merece la pena contactar.",
                className="mb-4",
                style={"color": "#667085", "lineHeight": "1.8", "maxWidth": "880px"},
            ),
            dbc.Row(
                [info_step(item["numero"], item["titulo"], item["texto"], color="#dc3545") for item in PROBLEMAS]
            ),
        ]
    ),
    className="py-5",
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
                "Servicios de asesoría y gestión con un enfoque práctico, cercano y profesional. La idea es que el visitante entienda rápido qué hacéis y a quién ayudáis.",
                className="mb-4",
                style={"color": "#667085", "lineHeight": "1.8", "maxWidth": "860px"},
            ),
            dbc.Row([service_card(s["icono"], s["titulo"], s["texto"]) for s in SERVICIOS]),
        ]
    ),
    className="py-5",
)

results_section = html.Div(
    dbc.Container(
        [
            section_eyebrow("Lo que consigue el cliente"),
            html.H2(
                "Cuando una gestoría funciona bien, se nota en la tranquilidad del cliente",
                className="fw-bold mb-3",
                style={"color": "#101828"},
            ),
            html.P(
                "Este bloque ayuda mucho a vender porque pone el foco en el beneficio final: menos estrés, más claridad y mejor apoyo en el día a día.",
                className="mb-4",
                style={"color": "#667085", "lineHeight": "1.8", "maxWidth": "860px"},
            ),
            dbc.Row(
                [info_step(item["numero"], item["titulo"], item["texto"], color="#198754") for item in RESULTADOS]
            ),
        ]
    ),
    className="py-5",
    style={"background": "#f8fafc"},
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
                                    "Una gestoría transmite mucho más cuando combina experiencia, cercanía y claridad. Este bloque refuerza trayectoria, presencia local y capacidad para acompañar a autónomos, empresas y particulares.",
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

reviews_section = html.Div(
    dbc.Container(
        [
            section_eyebrow("Opiniones"),
            html.H2(
                "Una gestoría local convierte mucho mejor cuando transmite confianza real",
                className="fw-bold mb-3",
                style={"color": "#101828"},
            ),
            html.P(
                "Aquí deberías poner reseñas reales de Google o testimonios de clientes. Aunque sea una demo, este bloque hace muchísimo para convertir.",
                className="mb-4",
                style={"color": "#667085", "lineHeight": "1.8", "maxWidth": "860px"},
            ),
            dbc.Row([review_card(r["nombre"], r["texto"]) for r in REVIEWS]),
        ]
    ),
    className="py-5",
)

how_it_works_section = html.Div(
    dbc.Container(
        [
            section_eyebrow("Cómo trabajáis"),
            html.H2(
                "Un proceso sencillo también ayuda a generar más contactos",
                className="fw-bold mb-3",
                style={"color": "#101828"},
            ),
            html.P(
                "Explicar el proceso reduce fricción y hace que la persona vea más fácil dar el paso de llamar o escribir.",
                className="mb-4",
                style={"color": "#667085", "lineHeight": "1.8"},
            ),
            dbc.Row(
                [info_step(item["numero"], item["titulo"], item["texto"], color="#0d6efd") for item in PASOS]
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
                "Si una gestoría quiere captar clientes desde Google, necesita una home que explique con claridad qué hace, dónde está y para quién trabaja. Esta versión demo está pensada para posicionar mejor búsquedas como gestoría en Ávila, asesoría fiscal en Ávila, asesoría laboral en Ávila o gestoría para autónomos en Ávila.",
                className="mb-3",
                style={"color": "#667085", "lineHeight": "1.8"},
            ),
            html.P(
                "También refuerza la propuesta de valor del despacho: experiencia, cercanía, servicios claros y contacto visible. Eso no solo ayuda al SEO, también mejora bastante la conversión cuando alguien entra por primera vez en la web.",
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
                [
                    html.Div(
                        "CONTACTO",
                        className="text-uppercase fw-bold small text-center mb-2",
                        style={"letterSpacing": "0.08em", "color": "#667085"},
                    ),
                    html.H2(
                        "Una web mejor debería llevar más llamadas y más contactos",
                        className="fw-bold mb-3 text-center",
                        style={"color": "#101828"},
                    ),
                    html.P(
                        "Esta demo está pensada para que el visitante entienda rápido qué hacéis, por qué confiar y cómo contactar en segundos.",
                        className="text-center mb-4",
                        style={"color": "#667085", "lineHeight": "1.8", "maxWidth": "820px", "margin": "0 auto"},
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Button(
                                    "Llamar ahora",
                                    href=f"tel:{TELEFONO_1.replace(' ', '')}",
                                    color="primary",
                                    className="w-100 rounded-pill fw-bold py-3",
                                    style={"boxShadow": "0 10px 24px rgba(13, 110, 253, 0.22)"},
                                ),
                                md=4,
                                className="mb-2",
                            ),
                            dbc.Col(
                                dbc.Button(
                                    "WhatsApp",
                                    href=WHATSAPP_URL,
                                    target="_blank",
                                    color="success",
                                    className="w-100 rounded-pill fw-bold py-3",
                                ),
                                md=4,
                                className="mb-2",
                            ),
                            dbc.Col(
                                dbc.Button(
                                    "Enviar email",
                                    href=f"mailto:{EMAIL}",
                                    color="light",
                                    className="w-100 rounded-pill fw-bold py-3 border",
                                ),
                                md=4,
                                className="mb-2",
                            ),
                        ]
                    ),
                ]
            ),
            className="border-0 rounded-4",
            style={
                "background": "#ffffff",
                "boxShadow": "0 22px 60px rgba(16, 24, 40, 0.10)",
            },
        )
    ),
    className="py-5",
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

whatsapp_floating_button = html.A(
    "WhatsApp",
    href=WHATSAPP_URL,
    target="_blank",
    style={
        "position": "fixed",
        "right": "20px",
        "bottom": "20px",
        "zIndex": "999",
        "background": "#25D366",
        "color": "white",
        "textDecoration": "none",
        "padding": "0.9rem 1.15rem",
        "borderRadius": "999px",
        "fontWeight": "700",
        "boxShadow": "0 12px 28px rgba(0, 0, 0, 0.18)",
    },
)

layout = html.Div(
    [
        hero_section,
        metrics_section,
        problems_section,
        services_section,
        results_section,
        trust_section,
        reviews_section,
        how_it_works_section,
        seo_text_section,
        faq_section,
        cta_section,
        footer_section,
        whatsapp_floating_button,
    ]
)
