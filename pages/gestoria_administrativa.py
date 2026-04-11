import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path="/gestoria-administrativa",
    title="Gestoría administrativa | Gestoría Duque",
    name="Gestoría administrativa",
)

layout = html.Div(
    dbc.Container(
        [
            html.Section(
                [
                    html.Div("Servicios", className="section-tag"),
                    html.H1("Gestoría administrativa", className="service-page-title"),
                    html.P(
                        "Gestionamos trámites administrativos para particulares, autónomos y empresas con una atención clara, cercana y profesional.",
                        className="service-page-subtitle",
                    ),
                ],
                className="service-page-hero",
            ),
            html.Section(
                [
                    html.H2("Qué podemos ayudarle a gestionar", className="service-page-section-title"),
                    html.Ul(
                        [
                            html.Li("Tramitación de expedientes y documentación administrativa."),
                            html.Li("Gestiones con organismos públicos."),
                            html.Li("Apoyo en trámites para particulares y profesionales."),
                            html.Li("Seguimiento ordenado de cada procedimiento."),
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
