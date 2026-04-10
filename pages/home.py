import dash
from dash import html

dash.register_page(
    __name__,
    path="/",
    title="Inicio",
    name="Inicio",
)

layout = html.Div(
    [
        html.H1("HOME OK"),
        html.P("La página está cargando bien."),
    ],
    style={"padding": "40px"},
)
