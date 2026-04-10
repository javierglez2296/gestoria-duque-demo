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
        "Asesoría fiscal, laboral, contable y trámites con una imagen moderna y profesional."
    ),
)

TELEFONO = "920 000 000"
EMAIL = "info@gestoriaduque.com"
WHATSAPP_URL = "https://wa.me/34620000000"

HERO_IMAGES = [
    "/assets/hero-2.jpg",
    "/assets/hero-1.jpg",
    "/assets/hero-3.jpg",
]


def build_hero():
    return html.Section(
        [
            dcc.Interval(
                id="home-hero-interval",
                interval=4500,
                n_intervals=0,
            ),
            dcc.Store(id="home-hero-index", data=0),
            html.Div(
                id="home-hero-bg",
                className="home-hero-bg",
                style={
                    "background": f"center center / cover no-repeat url('{HERO_IMAGES[0]}')",
                },
            ),
            html.Div(className="home-hero-overlay"),
            dbc.Container(
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Span("ASESORÍA INTEGRAL"),
                                            html.Span("ÁVILA"),
                                        ],
                                        className="home-hero-eyebrow home-hero-line",
                                    ),
                                    html.H1(
                                        "Gestión fiscal, laboral y contable con claridad y confianza.",
                                        className="home-hero-title home-hero-line",
                                    ),
                                    html.P(
                                        (
                                            "Acompañamos a autónomos, empresas y particulares "
                                            "con una atención cercana, procesos claros y una imagen "
                                            "profesional a la altura de su negocio."
                                        ),
                                        className="home-hero-subtitle home-hero-line",
                                    ),
                                    html.Div(
                                        [
                                            dbc.Button(
                                                "Solicitar información",
                                                href="#contacto",
                                                className="home-hero-btn home-hero-btn-primary home-hero-btn-1 home-hero-line",
                                            ),
                                            dbc.Button(
                                                "Ver servicios",
                                                href="#servicios",
                                                className="home-hero-btn home-hero-btn-secondary home-hero-btn-2 home-hero-line",
                                            ),
                                        ],
                                        className="home-hero-actions",
                                    ),
                                ],
                                className="home-hero-content",
                            ),
                            lg=6,
                            md=8,
                            xs=12,
                        ),
                    ],
                    className="min-vh-100 align-items-center",
                ),
                fluid=False,
                className="home-hero-container",
            ),
        ],
        className="home-hero-section",
    )


def build_services_preview():
    items = [
        {
            "title": "Asesoría fiscal",
            "text": "Impuestos, declaraciones, planificación y seguimiento fiscal para autónomos y empresas.",
        },
        {
            "title": "Asesoría laboral",
            "text": "Nóminas, contratos, altas, bajas y gestión laboral con soporte cercano y ágil.",
        },
        {
            "title": "Asesoría contable",
            "text": "Control contable, cierre, revisión y soporte para una gestión financiera más ordenada.",
        },
    ]

    return html.Section(
        dbc.Container(
            [
                html.Div("SERVICIOS", className="section-tag"),
                html.H2(
                    "Soluciones claras para cada área clave de tu actividad.",
                    className="section-title",
                ),
                html.P(
                    "Un enfoque profesional, cercano y bien estructurado para ayudarte a tomar mejores decisiones.",
                    className="section-subtitle",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.Div(item["title"], className="service-card-title"),
                                        html.P(item["text"], className="service-card-text"),
                                    ]
                                ),
                                className="service-card h-100",
                            ),
                            md=4,
                            className="mb-4",
                        )
                        for item in items
                    ],
                    className="mt-4",
                ),
            ],
            className="py-5",
        ),
        id="servicios",
        className="services-section",
    )


def build_contact_cta():
    return html.Section(
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            [
                                html.Div("CONTACTO", className="section-tag section-tag-light"),
                                html.H2(
                                    "Hablemos sobre cómo podemos ayudarte.",
                                    className="contact-title",
                                ),
                                html.P(
                                    "Te orientamos sin compromiso para encontrar la solución que mejor encaje contigo o con tu empresa.",
                                    className="contact-subtitle",
                                ),
                            ]
                        ),
                        lg=7,
                        md=12,
                    ),
                    dbc.Col(
                        html.Div(
                            [
                                html.A(
                                    f"Tel. {TELEFONO}",
                                    href=f"tel:{TELEFONO.replace(' ', '')}",
                                    className="contact-link",
                                ),
                                html.A(
                                    EMAIL,
                                    href=f"mailto:{EMAIL}",
                                    className="contact-link",
                                ),
                                html.A(
                                    "Escribir por WhatsApp",
                                    href=WHATSAPP_URL,
                                    target="_blank",
                                    className="contact-link contact-link-cta",
                                ),
                            ],
                            className="contact-box",
                        ),
                        lg=5,
                        md=12,
                    ),
                ],
                className="align-items-center g-4",
            ),
            className="py-5",
        ),
        id="contacto",
        className="contact-section",
    )


layout = html.Div(
    [
        build_hero(),
        build_services_preview(),
        build_contact_cta(),
    ],
    className="page-shell",
)


@callback(
    Output("home-hero-index", "data"),
    Input("home-hero-interval", "n_intervals"),
)
def rotate_hero(n):
    return n % len(HERO_IMAGES)


@callback(
    Output("home-hero-bg", "style"),
    Input("home-hero-index", "data"),
)
def update_hero_bg(index):
    return {
        "background": f"center center / cover no-repeat url('{HERO_IMAGES[index]}')"
    }
