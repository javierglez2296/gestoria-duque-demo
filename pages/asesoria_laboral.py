import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path="/asesoria-laboral",
    title="Asesoría laboral | Gestoría Duque",
    name="Asesoría laboral",
)

layout = html.Div(
    dbc.Container(
        [
            html.Section(
                [
                    html.Div("Servicios", className="section-tag"),
                    html.H1("Asesoría laboral", className="service-page-title"),
                    html.P(
                        "Ofrecemos apoyo laboral para empresas y autónomos con una gestión ágil, ordenada y cercana en el día a día.",
                        className="service-page-subtitle",
                    ),
                ],
                className="service-page-hero",
            ),
            html.Section(
                [
                    html.H2("Servicios laborales", className="service-page-section-title"),
                    html.Ul(
                        [
                            html.Li("Nóminas y seguros sociales."),
                            html.Li("Altas, bajas y variaciones."),
                            html.Li("Contratos y documentación laboral."),
                            html.Li("Asistencia en la gestión laboral diaria."),
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
