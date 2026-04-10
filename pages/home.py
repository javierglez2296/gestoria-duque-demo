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
WHATSAPP_URL = "https://wa.me/3462000000"


def section_eyebrow(text):
    return html.Div(text, className="section-eyebrow")


def stat_item(number, label):
    return dbc.Col(
        html.Div(
            [
                html.Div(number, className="stat-number"),
                html.Div(label, className="stat-label"),
            ],
            className="stat-card",
        ),
        xs=12,
        sm=6,
        lg=3,
    )


def service_card(title, description):
    return dbc.Col(
        html.Div(
            [
                html.Div(className="service-card-line"),
                html.H3(title, className="service-card-title"),
                html.P(description, className="service-card-text"),
                html.A("Más información", href="#contacto", className="service-card-link"),
            ],
            className="service-card",
        ),
        xs=12,
        md=6,
        className="mb-4",
    )


def benefit_item(title, text):
    return dbc.Col(
        html.Div(
            [
                html.H3(title, className="benefit-title"),
                html.P(text, className="benefit-text"),
            ],
            className="benefit-card",
        ),
        xs=12,
        md=6,
        lg=3,
        className="mb-4",
    )


def build_hero():
    return html.Section(
        [
            html.Div(className="hero-overlay"),
            dbc.Container(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.Span("Asesoría integral"),
                                                html.Span("Ávila"),
                                            ],
                                            className="hero-eyebrow",
                                        ),
                                        html.H1(
                                            "Gestión fiscal, laboral y contable con claridad y confianza.",
                                            className="hero-title",
                                        ),
                                        html.P(
                                            (
                                                "Acompañamos a autónomos, empresas y particulares con una "
                                                "atención cercana, procesos claros y una imagen profesional "
                                                "a la altura de su negocio."
                                            ),
                                            className="hero-subtitle",
                                        ),
                                        html.Div(
                                            [
                                                dbc.Button(
                                                    "Solicitar información",
                                                    href="#contacto",
                                                    className="hero-btn hero-btn-primary",
                                                ),
                                                dbc.Button(
                                                    "Ver servicios",
                                                    href="#servicios",
                                                    className="hero-btn hero-btn-secondary",
                                                ),
                                            ],
                                            className="hero-actions",
                                        ),
                                    ],
                                    className="hero-content",
                                ),
                                lg=7,
                                xl=6,
                            )
                        ],
                        justify="start",
                    )
                ],
                fluid=False,
                className="hero-container",
            ),
        ],
        className="home-hero",
    )


def build_stats():
    return html.Section(
        dbc.Container(
            [
                dbc.Row(
                    [
                        stat_item("+15", "años acompañando a clientes"),
                        stat_item("+300", "gestiones y trámites al año"),
                        stat_item("24h", "respuesta más ágil y cercana"),
                        stat_item("360º", "visión fiscal, laboral y contable"),
                    ],
                    className="g-4",
                )
            ]
        ),
        className="stats-section",
    )


def build_about():
    return html.Section(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                section_eyebrow("Despacho profesional"),
                                html.H2(
                                    "Una gestoría moderna con la solidez y la seriedad que transmite un gran despacho.",
                                    className="section-title",
                                ),
                            ],
                            lg=5,
                            className="mb-4 mb-lg-0",
                        ),
                        dbc.Col(
                            [
                                html.P(
                                    (
                                        "Nuestro objetivo es que cada cliente entienda qué se está haciendo, "
                                        "por qué se está haciendo y cómo impacta en su negocio o en su situación personal."
                                    ),
                                    className="section-text",
                                ),
                                html.P(
                                    (
                                        "Combinamos trato cercano, rigor técnico y una forma de trabajar más clara, "
                                        "ágil y ordenada. Sin complicaciones innecesarias y con una imagen más actual."
                                    ),
                                    className="section-text",
                                ),
                            ],
                            lg=7,
                        ),
                    ],
                    align="center",
                )
            ]
        ),
        className="about-section",
    )


def build_services():
    return html.Section(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                section_eyebrow("Servicios"),
                                html.H2(
                                    "Soluciones para autónomos, empresas y particulares.",
                                    className="section-title text-center text-lg-start",
                                ),
                                html.P(
                                    (
                                        "Organizamos cada área de trabajo de forma clara para que el cliente "
                                        "sepa exactamente en qué podemos ayudarle."
                                    ),
                                    className="section-text text-center text-lg-start services-intro",
                                ),
                            ],
                            lg=8,
                            className="mx-auto mb-5",
                        )
                    ],
                    justify="center",
                ),
                dbc.Row(
                    [
                        service_card(
                            "Asesoría fiscal",
                            "Impuestos, planificación, presentación de modelos y seguimiento tributario con una visión ordenada y preventiva.",
                        ),
                        service_card(
                            "Asesoría laboral",
                            "Nóminas, contratos, altas, bajas, seguros sociales y apoyo continuo en la gestión del día a día laboral.",
                        ),
                        service_card(
                            "Asesoría contable",
                            "Contabilidad clara, control documental y apoyo en la interpretación de los números de su negocio.",
                        ),
                        service_card(
                            "Gestoría administrativa",
                            "Trámites, certificados, documentación, gestiones oficiales y acompañamiento administrativo ágil.",
                        ),
                    ],
                    className="g-4",
                    id="servicios",
                ),
            ]
        ),
        className="services-section",
    )


def build_benefits():
    return html.Section(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                section_eyebrow("Por qué elegirnos"),
                                html.H2(
                                    "Profesionalidad, cercanía y una forma de trabajar más clara.",
                                    className="section-title text-center",
                                ),
                            ],
                            lg=8,
                            className="mx-auto mb-5 text-center",
                        )
                    ]
                ),
                dbc.Row(
                    [
                        benefit_item(
                            "Atención cercana",
                            "Una relación más humana, directa y fácil de entender desde el primer contacto.",
                        ),
                        benefit_item(
                            "Rigor y orden",
                            "Procesos estructurados, documentación clara y seguimiento serio de cada asunto.",
                        ),
                        benefit_item(
                            "Visión integral",
                            "Fiscal, laboral, contable y administrativa conectadas para evitar errores y duplicidades.",
                        ),
                        benefit_item(
                            "Imagen actual",
                            "Un despacho que transmite confianza, modernidad y profesionalidad.",
                        ),
                    ],
                    className="g-4",
                ),
            ]
        ),
        className="benefits-section",
    )


def build_process():
    return html.Section(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                section_eyebrow("Cómo trabajamos"),
                                html.H2(
                                    "Un proceso simple, claro y bien acompañado.",
                                    className="section-title text-center",
                                ),
                            ],
                            lg=8,
                            className="mx-auto mb-5 text-center",
                        )
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                [
                                    html.Div("01", className="process-number"),
                                    html.H3("Escuchamos su caso", className="process-title"),
                                    html.P(
                                        "Analizamos su situación y entendemos qué necesita realmente.",
                                        className="process-text",
                                    ),
                                ],
                                className="process-card",
                            ),
                            xs=12,
                            md=4,
                            className="mb-4",
                        ),
                        dbc.Col(
                            html.Div(
                                [
                                    html.Div("02", className="process-number"),
                                    html.H3("Ordenamos la gestión", className="process-title"),
                                    html.P(
                                        "Definimos el enfoque, la documentación y los pasos a seguir.",
                                        className="process-text",
                                    ),
                                ],
                                className="process-card",
                            ),
                            xs=12,
                            md=4,
                            className="mb-4",
                        ),
                        dbc.Col(
                            html.Div(
                                [
                                    html.Div("03", className="process-number"),
                                    html.H3("Le acompañamos", className="process-title"),
                                    html.P(
                                        "Mantenemos una relación ágil, cercana y profesional en el tiempo.",
                                        className="process-text",
                                    ),
                                ],
                                className="process-card",
                            ),
                            xs=12,
                            md=4,
                            className="mb-4",
                        ),
                    ],
                    className="g-4",
                ),
            ]
        ),
        className="process-section",
    )


def build_contact():
    return html.Section(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                section_eyebrow("Contacto"),
                                html.H2(
                                    "Estamos en Ávila para ayudarle con una atención clara y profesional.",
                                    className="section-title",
                                ),
                                html.P(
                                    (
                                        "Si necesita apoyo fiscal, laboral, contable o administrativo, "
                                        "puede escribirnos o llamarnos y estudiaremos su caso sin compromiso."
                                    ),
                                    className="section-text",
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.Span("Teléfono", className="contact-label"),
                                                html.A(
                                                    TELEFONO_1,
                                                    href=f"tel:{TELEFONO_1.replace(' ', '')}",
                                                    className="contact-value",
                                                ),
                                            ],
                                            className="contact-item",
                                        ),
                                        html.Div(
                                            [
                                                html.Span("Móvil", className="contact-label"),
                                                html.A(
                                                    TELEFONO_2,
                                                    href=f"tel:{TELEFONO_2.replace(' ', '')}",
                                                    className="contact-value",
                                                ),
                                            ],
                                            className="contact-item",
                                        ),
                                        html.Div(
                                            [
                                                html.Span("Email", className="contact-label"),
                                                html.A(
                                                    EMAIL,
                                                    href=f"mailto:{EMAIL}",
                                                    className="contact-value",
                                                ),
                                            ],
                                            className="contact-item",
                                        ),
                                        html.Div(
                                            [
                                                html.Span("Dirección", className="contact-label"),
                                                html.Div(DIRECCION, className="contact-value"),
                                            ],
                                            className="contact-item",
                                        ),
                                    ],
                                    className="contact-list",
                                ),
                                html.Div(
                                    [
                                        dbc.Button(
                                            "Escribir por WhatsApp",
                                            href=WHATSAPP_URL,
                                            target="_blank",
                                            className="hero-btn hero-btn-primary me-3 mb-3",
                                        ),
                                        dbc.Button(
                                            "Solicitar información",
                                            href=f"mailto:{EMAIL}",
                                            className="hero-btn hero-btn-secondary mb-3",
                                        ),
                                    ],
                                    className="mt-4",
                                ),
                            ],
                            lg=6,
                            className="mb-4 mb-lg-0",
                        ),
                        dbc.Col(
                            html.Div(
                                [
                                    html.Div("Oficina", className="office-badge"),
                                    html.H3("Despacho profesional en Ávila", className="office-title"),
                                    html.P(
                                        (
                                            "Atendemos a clientes que buscan una gestoría seria, clara y actual, "
                                            "con trato cercano y una presentación profesional cuidada."
                                        ),
                                        className="office-text",
                                    ),
                                    html.Div(className="office-image"),
                                ],
                                className="office-card",
                            ),
                            lg=6,
                        ),
                    ],
                    id="contacto",
                    align="center",
                )
            ]
        ),
        className="contact-section",
    )


layout = html.Div(
    [
        build_hero(),
        build_stats(),
        build_about(),
        build_services(),
        build_benefits(),
        build_process(),
        build_contact(),
    ],
    className="premium-home",
)
