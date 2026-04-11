import dash
from dash import html, dcc, Input, Output, callback
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

HERO_IMAGES = [
    "/assets/hero-1.jpg",
    "/assets/hero-2.jpg",
    "/assets/hero-3.jpg",
]


def build_hero():
    return html.Section(
        [
            dcc.Interval(
                id="hero-interval",
                interval=4000,
                n_intervals=0,
            ),
            html.Div(
                id="hero-bg",
                className="hero-image-layer",
                style={"backgroundImage": f"url('{HERO_IMAGES[0]}')"},
            ),
            html.Div(className="hero-overlay"),
            dbc.Container(
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                [
                                    html.Div(
                                        "Gestoría en Ávila",
                                        className="hero-eyebrow hero-line",
                                    ),
                                    html.H1(
                                        "Asesoría fiscal, laboral y contable con una atención clara y profesional.",
                                        className="hero-title hero-line",
                                    ),
                                    html.P(
                                        (
                                            "Ayudamos a autónomos, empresas y particulares con una gestión "
                                            "cercana, ordenada y orientada a resolver trámites y obligaciones "
                                            "sin complicaciones."
                                        ),
                                        className="hero-subtitle hero-line",
                                    ),
                                    html.Div(
                                        [
                                            dcc.Link(
                                                dbc.Button(
                                                    "Solicitar información",
                                                    className="hero-cta-btn",
                                                ),
                                                href="/presupuesto",
                                            ),
                                            html.A(
                                                "Ver servicios",
                                                href="#servicios",
                                                className="btn hero-secondary-btn",
                                            ),
                                        ],
                                        className="hero-actions hero-line",
                                    ),
                                ],
                                className="hero-copy-animate",
                            ),
                            lg=7,
                            xl=6,
                            md=9,
                            xs=12,
                        ),
                    ],
                    className="hero-row",
                ),
                fluid="lg",
                className="hero-content-wrap",
            ),
        ],
        className="hero-premium-section",
    )


def build_trust_strip():
    items = [
        {
            "title": "Atención cercana",
            "text": "Trato directo y seguimiento claro de cada caso.",
        },
        {
            "title": "Gestión integral",
            "text": "Fiscal, laboral, contable y trámites en un solo despacho.",
        },
        {
            "title": "Respuesta profesional",
            "text": "Una forma clara y ordenada de resolver sus necesidades.",
        },
    ]

    return html.Section(
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            [
                                html.Div(item["title"], className="trust-strip-value"),
                                html.P(item["text"], className="trust-strip-label"),
                            ],
                            className="trust-strip-card",
                        ),
                        md=4,
                        className="mb-3 mb-md-0",
                    )
                    for item in items
                ],
                className="g-3",
            ),
            fluid="lg",
        ),
        className="trust-strip-section",
    )


def build_services():
    services = [
        {
            "title": "Asesoría fiscal",
            "text": (
                "Planificación y presentación de impuestos, seguimiento de "
                "obligaciones tributarias y apoyo continuo para autónomos y empresas."
            ),
        },
        {
            "title": "Asesoría laboral",
            "text": (
                "Gestión laboral, nóminas, seguros sociales, altas, bajas y "
                "apoyo en el día a día de la empresa."
            ),
        },
        {
            "title": "Asesoría contable",
            "text": (
                "Contabilidad clara, organizada y orientada a que la información "
                "económica sea útil para tomar decisiones."
            ),
        },
    ]

    return html.Section(
        dbc.Container(
            [
                html.Div(id="servicios", className="section-anchor"),
                html.Div(
                    [
                        html.Div("Servicios", className="section-tag"),
                        html.H2(
                            "Una gestoría pensada para acompañarle con claridad en cada paso.",
                            className="section-title",
                        ),
                        html.P(
                            (
                                "Trabajamos con autónomos, empresas y particulares para ofrecer "
                                "una atención profesional, cercana y bien estructurada."
                            ),
                            className="section-subtitle",
                        ),
                    ],
                    className="section-header",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.H3(
                                            item["title"],
                                            className="service-card-title",
                                        ),
                                        html.P(
                                            item["text"],
                                            className="service-card-text",
                                        ),
                                    ]
                                ),
                                className="service-card h-100",
                            ),
                            lg=4,
                            md=6,
                            xs=12,
                        )
                        for item in services
                    ],
                    className="services-grid g-4",
                ),
            ],
            fluid="lg",
        ),
        className="services-section",
    )


def build_contact():
    return html.Section(
        dbc.Container(
            [
                html.Div(id="contacto", className="section-anchor"),
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                [
                                    html.Div(
                                        "Contacto",
                                        className="section-tag section-tag-light",
                                    ),
                                    html.H2(
                                        "Hablemos sobre lo que necesita.",
                                        className="contact-title",
                                    ),
                                    html.P(
                                        (
                                            "Si desea información, presupuesto o resolver una duda, "
                                            "puede escribirnos y le responderemos lo antes posible."
                                        ),
                                        className="contact-subtitle",
                                    ),
                                ]
                            ),
                            lg=7,
                            className="mb-4 mb-lg-0",
                        ),
                        dbc.Col(
                            html.Div(
                                [
                                    dcc.Link(
                                        "Solicitar presupuesto",
                                        href="/presupuesto",
                                        className="contact-link contact-link-cta",
                                    ),
                                    html.A(
                                        "Escribir por email",
                                        href="mailto:info@gestoriaduque.com",
                                        className="contact-link",
                                    ),
                                    html.A(
                                        "Abrir WhatsApp",
                                        href="https://wa.me/34620000000",
                                        target="_blank",
                                        rel="noopener noreferrer",
                                        className="contact-link",
                                    ),
                                ],
                                className="contact-box",
                            ),
                            lg=5,
                        ),
                    ],
                    className="align-items-center",
                ),
            ],
            fluid="lg",
        ),
        className="contact-section",
    )


layout = html.Div(
    [
        build_hero(),
        build_trust_strip(),
        build_services(),
        build_contact(),
    ],
    className="page-shell",
)


@callback(
    Output("hero-bg", "style"),
    Input("hero-interval", "n_intervals"),
)
def update_hero_bg(n_intervals):
    image = HERO_IMAGES[n_intervals % len(HERO_IMAGES)]
    return {"backgroundImage": f"url('{image}')"}
