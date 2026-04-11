import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path="/externalizacion-de-servicios",
    title="Externalización de servicios | Gestoría Duque",
    name="Externalización de servicios",
)

layout = html.Div(
    dbc.Container(
        [
            html.Section(
                [
                    html.Div("Servicios", className="section-tag"),
                    html.H1("Externalización de servicios", className="service-page-title"),
                    html.P(
                        "Ayudamos a empresas a delegar procesos administrativos y de gestión para ganar tiempo, orden y eficiencia.",
                        className="service-page-subtitle",
                    ),
                ],
                className="service-page-hero",
            ),
            html.Section(
                [
                    html.H2("Cómo le ayudamos", className="service-page-section-title"),
                    html.Ul(
                        [
                            html.Li("Apoyo externo en procesos administrativos."),
                            html.Li("Gestión documental y operativa."),
                            html.Li("Refuerzo profesional para picos de trabajo."),
                            html.Li("Más foco para su actividad principal."),
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
