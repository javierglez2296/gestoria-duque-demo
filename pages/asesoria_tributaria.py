import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path="/asesoria-tributaria",
    title="Asesoría tributaria | Gestoría Duque",
    name="Asesoría tributaria",
)

layout = html.Div(
    dbc.Container(
        [
            html.Section(
                [
                    html.Div("Servicios", className="section-tag"),
                    html.H1("Asesoría tributaria", className="service-page-title"),
                    html.P(
                        "Le ayudamos a cumplir sus obligaciones fiscales con claridad, planificación y seguimiento continuo.",
                        className="service-page-subtitle",
                    ),
                ],
                className="service-page-hero",
            ),
            html.Section(
                [
                    html.H2("Servicios tributarios", className="service-page-section-title"),
                    html.Ul(
                        [
                            html.Li("Impuestos periódicos."),
                            html.Li("Planificación y control fiscal."),
                            html.Li("Presentación de declaraciones."),
                            html.Li("Seguimiento de obligaciones tributarias."),
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
