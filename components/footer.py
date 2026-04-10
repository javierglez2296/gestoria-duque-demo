from dash import html
import dash_bootstrap_components as dbc


def build_footer():
    return html.Footer(
        dbc.Container(
            [
                dbc.Row(
                    [
                        # MARCA
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.Div("Gestoría Duque", className="footer-logo"),
                                        html.P(
                                            "Asesoría fiscal, laboral y contable en Ávila. "
                                            "Una forma más clara, moderna y profesional de gestionar.",
                                            className="footer-text",
                                        ),
                                    ]
                                )
                            ],
                            md=4,
                            className="mb-4",
                        ),

                        # NAVEGACIÓN
                        dbc.Col(
                            [
                                html.Div("Navegación", className="footer-title"),
                                html.A("Inicio", href="/", className="footer-link"),
                                html.A("Servicios", href="/#servicios", className="footer-link"),
                                html.A("Contacto", href="/#contacto", className="footer-link"),
                            ],
                            md=4,
                            className="mb-4",
                        ),

                        # CONTACTO
                        dbc.Col(
                            [
                                html.Div("Contacto", className="footer-title"),
                                html.Div("920 000 000", className="footer-text"),
                                html.Div("info@gestoriaduque.com", className="footer-text"),
                                html.Div("Ávila", className="footer-text"),
                            ],
                            md=4,
                            className="mb-4",
                        ),
                    ]
                ),

                html.Hr(className="footer-divider"),

                html.Div(
                    "© 2026 Gestoría Duque · Todos los derechos reservados",
                    className="footer-bottom",
                ),
            ]
        ),
        className="footer-premium",
    )
