from dash import Dash, html, page_container
import dash_bootstrap_components as dbc

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
    title="Gestoría Demo",
    update_title=None,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
        {
            "name": "description",
            "content": "Gestoría en Ávila para autónomos, empresas y particulares. Demo de renovación web con enfoque profesional, local y comercial.",
        },
    ],
)

server = app.server

app.layout = html.Div(
    page_container,
    className="site-shell",
)

if __name__ == "__main__":
    app.run(debug=True)
