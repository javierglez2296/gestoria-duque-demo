from dash import html
import dash_bootstrap_components as dbc


def build_navbar():
    return dbc.Navbar(
        dbc.Container(
            [
                # LOGO
                html.A(
                    html.Div(
                        [
                            html.Span("GESTORÍA", className="navbar-logo-main"),
                            html.Span("DUQUE", className="navbar-logo-sub"),
                        ],
                        className="navbar-logo",
                    ),
                    href="/",
                    className="text-decoration-none",
                ),

                # BOTÓN MOBILE
                dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),

                # MENÚ
                dbc.Collapse(
                    dbc.Nav(
                        [
                            dbc.NavLink("Inicio", href="/", className="nav-link-premium"),
                            dbc.NavLink("Servicios", href="/#servicios", className="nav-link-premium"),
                            dbc.NavLink("Contacto", href="/#contacto", className="nav-link-premium"),

                            dbc.Button(
                                "Solicitar información",
                                href="/#contacto",
                                className="navbar-cta",
                            ),
                        ],
                        className="ms-auto align-items-center",
                        navbar=True,
                    ),
                    id="navbar-collapse",
                    navbar=True,
                ),
            ],
            fluid=False,
        ),
        className="navbar-premium",
        sticky="top",
    )
