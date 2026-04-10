import dash
from dash import html
from components.home.hero import build_hero

dash.register_page(
    __name__,
    path="/",
    title="Inicio",
    name="Inicio",
)

layout = html.Div(
    [
        build_hero(),
    ],
    className="page-shell",
)
