import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path="/asesoria-juridica",
    title="Asesoría jurídica | Gestoría Duque",
    name="Asesoría jurídica",
)

layout = html.Div(
    dbc.Container(
        [
            html.Section(
                [
                    html.Div("Servicios", className="section-tag"),
                    html.H1("Asesoría jurídica", className="service-page-title"),
                    html.P(
                        "Prestamos apoyo jurídico con una visión práctica, clara y orientada a proteger sus intereses.",
                        className="service-page-subtitle",
                    ),
                ],
                className="service-page-hero",
            ),
            html.Section(
                [
                    html.H2("Apoyo jurídico", className="service-page-section-title"),
                    html.Ul(
                        [
                            html.Li("Orientación legal en trámites y procedimientos."),
                            html.Li("Revisión documental."),
                            html.Li("Apoyo en incidencias y consultas."),
                            html.Li("Acompañamiento profesional en cada caso."),
                        ],
                        className="service-page-list",
                    ),
                ],
                className="service-page-content",
            ),
        ],
        fluid="lg",
    ),
    className="service-page-shell",
)
