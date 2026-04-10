from dash import html
import dash_bootstrap_components as dbc


def build_navbar():
    return html.Div(
        dbc.Container(
            [
                html.Div(
                    [
                        dbc.NavbarBrand(
                            [
                                html.Span("Gestoría", className="brand-main"),
                                html.Span("Duque", className="brand-accent ms-1"),
                            ],
                            href="/",
                            className="navbar-brand-premium",
                        ),
                        html.Div(
                            [
                                dbc.Nav(
                                    [
                                        dbc.NavLink("Inicio", href="/", className="nav-link-premium"),
                                        dbc.NavLink("Servicios", href="#servicios", className="nav-link-premium"),
                                        dbc.NavLink("Contacto", href="#contacto", className="nav-link-premium"),
                                    ],
                                    className="navbar-links-premium d-none d-lg-flex",
                                ),
                                html.Div(
                                    [
                                        dbc.Button(
                                            "WhatsApp",
                                            href="https://wa.me/34620000000",
                                            target="_blank",
                                            className="navbar-btn navbar-btn-ghost",
                                        ),
                                        dbc.Button(
                                            "Llamar ahora",
                                            href="tel:+34920000000",
                                            className="navbar-btn navbar-btn-primary",
                                        ),
                                    ],
                                    className="navbar-actions-premium d-none d-lg-flex",
                                ),
                                dbc.Button(
                                    html.Span("Menú"),
                                    id="navbar-mobile-toggle",
                                    className="navbar-mobile-toggle d-lg-none",
                                ),
                            ],
                            className="navbar-right-premium",
                        ),
                    ],
                    className="navbar-shell-premium",
                ),
                dbc.Collapse(
                    html.Div(
                        [
                            dbc.NavLink("Inicio", href="/", className="nav-link-mobile"),
                            dbc.NavLink("Servicios", href="#servicios", className="nav-link-mobile"),
                            dbc.NavLink("Contacto", href="#contacto", className="nav-link-mobile"),
                            html.Div(
                                [
                                    dbc.Button(
                                        "WhatsApp",
                                        href="https://wa.me/34620000000",
                                        target="_blank",
                                        className="navbar-btn navbar-btn-ghost w-100",
                                    ),
                                    dbc.Button(
                                        "Llamar ahora",
                                        href="tel:+34920000000",
                                        className="navbar-btn navbar-btn-primary w-100",
                                    ),
                                ],
                                className="navbar-mobile-actions",
                            ),
                        ],
                        className="navbar-mobile-panel",
                    ),
                    id="navbar-mobile-collapse",
                    is_open=False,
                ),
            ],
            fluid="lg",
        ),
        className="site-navbar-wrap",
    )
