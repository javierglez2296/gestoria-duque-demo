import dash
from dash import html, dcc, Input, Output, State, callback
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

HERO_SLIDES = [
    {
        "eyebrow": "GESTORÍA EN ÁVILA · FISCAL · LABORAL · CONTABLE",
        "title": "Gestoría en Ávila para autónomos, empresas y particulares",
        "text": "Asesoría fiscal, laboral, contable y trámites con atención clara, cercana y profesional.",
        "image": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1800&q=80",
    },
    {
        "eyebrow": "MÁS DE 70 AÑOS DE EXPERIENCIA",
        "title": "Experiencia, orden y confianza para tu gestión",
        "text": "Una propuesta moderna para un despacho con trayectoria, cercanía y capacidad real de ayudar.",
        "image": "https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=1800&q=80",
    },
    {
        "eyebrow": "DESPACHO LOCAL · ATENCIÓN DIRECTA",
        "title": "Tu tranquilidad, nuestra prioridad",
        "text": "Haz que la web transmita mejor lo que ya aporta la gestoría: claridad, servicio y confianza.",
        "image": "https://images.unsplash.com/photo-1520607162513-77705c0f0d4a?auto=format&fit=crop&w=1800&q=80",
    },
]

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
        className="text-uppercase fw-bold mb-3 reveal-up",
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
            "background": "rgba(255,255,255,0.16)",
            "border": "1px solid rgba(255,255,255,0.18)",
            "color": "white",
            "fontWeight": "600",
            "fontSize": "0.93rem",
            "backdropFilter": "blur(10px)",
            "WebkitBackdropFilter": "blur(10px)",
            "boxShadow": "0 10px 24px rgba(0, 0, 0, 0.08)",
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
            style={
                "padding": "1.2rem 0.25rem",
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


def hero_indicator(index, active=False):
    return html.Button(
        id={"type": "hero-indicator", "index": index},
        n_clicks=0,
        style={
            "width": "26px" if active else "10px",
            "height": "10px",
            "borderRadius": "999px",
            "border": "none",
            "padding": "0",
            "marginRight": "10px",
            "background": "#ffffff" if active else "rgba(255,255,255,0.30)",
            "transition": "all 0.28s ease",
            "cursor": "pointer",
        },
    )


def build_hero():
    slide = HERO_SLIDES[0]

    return html.Section(
        [
            dcc.Store(id="hero-slide-index", data=0),
            dcc.Interval(id="hero-autoplay", interval=5000, n_intervals=0),

            html.Div(
                id="hero-background",
                style={
                    "position": "absolute",
                    "inset": "0",
                    "backgroundImage": f"url('{slide['image']}')",
                    "backgroundSize": "cover",
                    "backgroundPosition": "center",
                    "transition": "background-image 0.7s ease-in-out",
                    "transform": "scale(1.02)",
                },
            ),

            html.Div(
                style={
                    "position": "absolute",
                    "inset": "0",
                    "background": (
                        "linear-gradient(90deg, rgba(7, 12, 22, 0.88) 0%, "
                        "rgba(7, 12, 22, 0.72) 38%, rgba(7, 12, 22, 0.42) 100%)"
                    ),
                }
            ),

            html.Div(
                style={
                    "position": "absolute",
                    "top": "-120px",
                    "right": "-100px",
                    "width": "320px",
                    "height": "320px",
                    "borderRadius": "999px",
                    "background": "rgba(255,255,255,0.06)",
                    "filter": "blur(40px)",
                    "zIndex": "1",
                }
            ),

            dbc.Container(
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                id="hero-content",
                                children=[],
                            ),
                            lg=7,
                            className="mb-5 mb-lg-0",
                        ),
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.Div(
                                            "Contacto",
                                            className="mb-3",
                                            style={
                                                "fontSize": "0.75rem",
                                                "letterSpacing": "0.14em",
                                                "textTransform": "uppercase",
                                                "fontWeight": "700",
                                                "color": "#98a2b3",
                                            },
                                        ),
                                        html.H2(
                                            "Una gestoría de confianza, con experiencia y trato cercano",
                                            className="fw-bold mb-4",
                                            style={
                                                "fontSize": "1.7rem",
                                                "lineHeight": "1.08",
                                                "letterSpacing": "-0.045em",
                                                "color": "#101828",
                                            },
                                        ),
                                        html.Div(
                                            [
                                                html.Div(
                                                    "Servicios principales",
                                                    className="fw-semibold mb-2",
                                                    style={"color": "#101828"},
                                                ),
                                                html.Div(
                                                    "Asesoría fiscal · laboral · contable · trámites",
                                                    className="mb-4",
                                                    style={
                                                        "color": "#667085",
                                                        "lineHeight": "1.8",
                                                    },
                                                ),
                                            ]
                                        ),
                                        html.Hr(style={"opacity": "0.08"}),
                                        html.Div("📞 Teléfono", className="fw-semibold mb-1", style={"color": "#101828"}),
                                        html.Div(TELEFONO_1, className="mb-3", style={"color": "#667085"}),
                                        html.Div("📱 Móvil", className="fw-semibold mb-1", style={"color": "#101828"}),
                                        html.Div(TELEFONO_2, className="mb-3", style={"color": "#667085"}),
                                        html.Div("✉️ Email", className="fw-semibold mb-1", style={"color": "#101828"}),
                                        html.Div(EMAIL, className="mb-3", style={"color": "#667085"}),
                                        html.Div("📍 Dirección", className="fw-semibold mb-1", style={"color": "#101828"}),
                                        html.Div(
                                            DIRECCION,
                                            className="mb-4",
                                            style={
                                                "color": "#667085",
                                                "lineHeight": "1.75",
                                            },
                                        ),
                                        dbc.Button(
                                            "Contactar por WhatsApp",
                                            href=WHATSAPP_URL,
                                            target="_blank",
                                            color="dark",
                                            className="w-100 rounded-pill fw-semibold mb-2",
                                            style={
                                                "padding": "1rem 1.2rem",
                                                "minHeight": "54px",
                                                "background": "#111827",
                                                "border": "none",
                                            },
                                        ),
                                        dbc.Button(
                                            "Enviar email",
                                            href=f"mailto:{EMAIL}",
                                            color="light",
                                            className="w-100 rounded-pill fw-semibold border",
                                            style={
                                                "padding": "1rem 1.2rem",
                                                "minHeight": "54px",
                                                "background": "#ffffff",
                                            },
                                        ),
                                    ]
                                ),
                                className="border-0 h-100",
                                style={
                                    "borderRadius": "30px",
                                    "background": "rgba(255,255,255,0.94)",
                                    "boxShadow": "0 32px 90px rgba(16, 24, 40, 0.18)",
                                    "backdropFilter": "blur(12px)",
                                    "WebkitBackdropFilter": "blur(12px)",
                                    "padding": "0.2rem",
                                },
                            ),
                            lg=5,
                            className="reveal reveal-4",
                        ),
                    ],
                    className="align-items-center",
                    style={"minHeight": "88vh", "position": "relative", "zIndex": "2"},
                ),
                style={"position": "relative", "zIndex": "2"},
            ),

            html.Div(
                [
                    html.Button(
                        "←",
                        id="hero-prev",
                        n_clicks=0,
                        style={
                            "width": "54px",
                            "height": "54px",
                            "borderRadius": "999px",
                            "border": "1px solid rgba(255,255,255,0.15)",
                            "background": "rgba(255,255,255,0.08)",
                            "color": "white",
                            "fontSize": "1.3rem",
                            "backdropFilter": "blur(8px)",
                            "WebkitBackdropFilter": "blur(8px)",
                            "marginRight": "0.75rem",
                            "cursor": "pointer",
                        },
                    ),
                    html.Button(
                        "→",
                        id="hero-next",
                        n_clicks=0,
                        style={
                            "width": "54px",
                            "height": "54px",
                            "borderRadius": "999px",
                            "border": "1px solid rgba(255,255,255,0.15)",
                            "background": "rgba(255,255,255,0.08)",
                            "color": "white",
                            "fontSize": "1.3rem",
                            "backdropFilter": "blur(8px)",
                            "WebkitBackdropFilter": "blur(8px)",
                            "cursor": "pointer",
                        },
                    ),
                ],
                className="d-none d-lg-flex",
                style={
                    "position": "absolute",
                    "right": "40px",
                    "bottom": "38px",
                    "zIndex": "3",
                },
            ),
        ],
        className="section-fade",
        style={
            "position": "relative",
            "minHeight": "88vh",
            "overflow": "hidden",
        },
    )
def build_hero_content(slide_index):
    slide = HERO_SLIDES[slide_index]

    return html.Div(
        key=f"hero-content-{slide_index}",
        className="hero-content-animate",
        children=[
            html.Div(
                id="hero-eyebrow",
                children=slide["eyebrow"],
                className="mb-4 reveal reveal-1",
                style={
                    "display": "inline-flex",
                    "alignItems": "center",
                    "padding": "0.62rem 0.95rem",
                    "borderRadius": "999px",
                    "background": "rgba(255,255,255,0.08)",
                    "border": "1px solid rgba(255,255,255,0.14)",
                    "backdropFilter": "blur(8px)",
                    "WebkitBackdropFilter": "blur(8px)",
                    "fontWeight": "700",
                    "fontSize": "0.75rem",
                    "letterSpacing": "0.12em",
                    "color": "rgba(255,255,255,0.92)",
                    "textTransform": "uppercase",
                },
            ),
            html.H1(
                id="hero-title",
                children=slide["title"],
                className="fw-bold mb-4 reveal reveal-2",
                style={
                    "fontSize": "clamp(3rem, 5.1vw, 5.7rem)",
                    "lineHeight": "0.92",
                    "letterSpacing": "-0.075em",
                    "color": "#ffffff",
                    "maxWidth": "820px",
                },
            ),
            html.P(
                id="hero-text",
                children=slide["text"],
                className="mb-4 reveal reveal-3",
                style={
                    "fontSize": "1.05rem",
                    "lineHeight": "1.95",
                    "color": "rgba(255,255,255,0.82)",
                    "maxWidth": "650px",
                },
            ),
            html.Div(
                [
                    html.Div(
                        "Desde 1950",
                        className="me-4 mb-2 reveal reveal-4",
                        style={
                            "display": "inline-block",
                            "color": "#ffffff",
                            "fontWeight": "700",
                            "fontSize": "0.98rem",
                        },
                    ),
                    html.Div(
                        "Fiscal · Laboral · Contable",
                        className="me-4 mb-2 reveal reveal-5",
                        style={
                            "display": "inline-block",
                            "color": "rgba(255,255,255,0.76)",
                            "fontWeight": "600",
                            "fontSize": "0.96rem",
                        },
                    ),
                    html.Div(
                        "Atención local en Ávila",
                        className="mb-2 reveal reveal-6",
                        style={
                            "display": "inline-block",
                            "color": "rgba(255,255,255,0.76)",
                            "fontWeight": "600",
                            "fontSize": "0.96rem",
                        },
                    ),
                ],
                className="mb-4",
            ),
            html.Div(
                [
                    dbc.Button(
                        "Solicitar información",
                        href=f"mailto:{EMAIL}",
                        color="light",
                        className="rounded-pill fw-bold me-2 mb-2 reveal reveal-5",
                        style={
                            "padding": "1rem 1.5rem",
                            "minHeight": "58px",
                            "fontSize": "1rem",
                            "color": "#101828",
                            "background": "#ffffff",
                            "border": "none",
                            "boxShadow": "0 18px 42px rgba(0,0,0,0.18)",
                        },
                    ),
                    dbc.Button(
                        "Llamar ahora",
                        href=f"tel:{TELEFONO_1.replace(' ', '')}",
                        color="link",
                        className="fw-semibold text-decoration-none mb-2 reveal reveal-6",
                        style={
                            "padding": "1rem 1rem",
                            "minHeight": "58px",
                            "fontSize": "1rem",
                            "color": "white",
                        },
                    ),
                ],
                className="mb-4",
            ),
            html.Div(
                id="hero-indicators",
                children=[
                    hero_indicator(i, active=(i == slide_index))
                    for i in range(len(HERO_SLIDES))
                ],
                className="reveal reveal-6",
                style={
                    "display": "flex",
                    "alignItems": "center",
                    "marginTop": "0.75rem",
                },
            ),
        ],
    )
hero_section = build_hero()

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
    className="section-fade",
    style={"paddingTop": "3rem", "paddingBottom": "4rem"},
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

pillars_section = html.Section(
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

process_section = html.Section(
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

testimonials_section = html.Section(
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

seo_section = html.Section(
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

faq_section = html.Section(
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

footer_section = html.Footer(
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
        dcc.Interval(id="page-load-trigger", interval=180, n_intervals=0, max_intervals=1),
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
    id="page-root",
    className="page-shell",
    style={
        "background": "#ffffff",
        "overflow": "hidden",
    },
)


@callback(
    Output("page-root", "className"),
    Input("page-load-trigger", "n_intervals"),
)
def activate_page_animation(_):
    return "page-shell page-loaded"


@callback(
    Output("hero-slide-index", "data"),
    Input("hero-autoplay", "n_intervals"),
    Input("hero-prev", "n_clicks"),
    Input("hero-next", "n_clicks"),
    Input({"type": "hero-indicator", "index": dash.ALL}, "n_clicks"),
    State("hero-slide-index", "data"),
    prevent_initial_call=True,
)
def update_hero_slide(_, prev_clicks, next_clicks, indicator_clicks, current_index):
    triggered = dash.ctx.triggered_id

    if triggered == "hero-prev":
        return (current_index - 1) % len(HERO_SLIDES)

    if triggered == "hero-next":
        return (current_index + 1) % len(HERO_SLIDES)

    if isinstance(triggered, dict) and triggered.get("type") == "hero-indicator":
        return triggered["index"]

    return (current_index + 1) % len(HERO_SLIDES)


@callback(
    Output("hero-background", "style"),
    Output("hero-content", "children"),
    Input("hero-slide-index", "data"),
)
def render_hero_slide(index):
    slide = HERO_SLIDES[index]

    background_style = {
        "position": "absolute",
        "inset": "0",
        "backgroundImage": f"url('{slide['image']}')",
        "backgroundSize": "cover",
        "backgroundPosition": "center",
        "transition": "background-image 0.7s ease-in-out",
        "transform": "scale(1.02)",
    }

    return background_style, build_hero_content(index)
