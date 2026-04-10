import dash
from dash import html, dcc, Input, Output, State, callback

from components.home.data import HERO_SLIDES
from components.home.hero import build_hero, build_hero_content
from components.home.sections import (
    build_stats_section,
    build_services_section,
    build_pillars_section,
    build_featured_section,
    build_process_section,
    build_testimonials_section,
    build_seo_section,
    build_faq_section,
    build_cta_section,
    build_footer_section,
    build_floating_whatsapp,
)

dash.register_page(
    __name__,
    path="/",
    title="Gestoría en Ávila | Asesoría fiscal, laboral y contable",
    name="Inicio",
    description=(
        "Gestoría en Ávila para autónomos, empresas y particulares. "
        "Asesoría fiscal, laboral, contable y trámites con una imagen moderna, clara y profesional."
    ),
)

layout = html.Div(
    [
        dcc.Interval(id="page-load-trigger", interval=180, n_intervals=0, max_intervals=1),
        build_hero(),
        build_stats_section(),
        build_services_section(),
        build_pillars_section(),
        build_featured_section(),
        build_process_section(),
        build_testimonials_section(),
        build_seo_section(),
        build_faq_section(),
        build_cta_section(),
        build_footer_section(),
        build_floating_whatsapp(),
    ],
    id="page-root",
    className="page-shell",
    style={
        "background": "#ffffff",
        "overflow": "hidden",
    },
)


@callback(
    Output("page-root", "className"),
    Input("page-load-trigger", "n_intervals"),
)
def activate_page_animation(_):
    return "page-shell page-loaded"


@callback(
    Output("hero-slide-index", "data"),
    Input("hero-autoplay", "n_intervals"),
    Input("hero-prev", "n_clicks"),
    Input("hero-next", "n_clicks"),
    Input({"type": "hero-indicator", "index": dash.ALL}, "n_clicks"),
    State("hero-slide-index", "data"),
    prevent_initial_call=True,
)
def update_hero_slide(_, prev_clicks, next_clicks, indicator_clicks, current_index):
    triggered = dash.ctx.triggered_id

    if triggered == "hero-prev":
        return (current_index - 1) % len(HERO_SLIDES)

    if triggered == "hero-next":
        return (current_index + 1) % len(HERO_SLIDES)

    if isinstance(triggered, dict) and triggered.get("type") == "hero-indicator":
        return triggered["index"]

    return (current_index + 1) % len(HERO_SLIDES)


@callback(
    Output("hero-background", "style"),
    Output("hero-content", "children"),
    Input("hero-slide-index", "data"),
)
def render_hero_slide(index):
    slide = HERO_SLIDES[index]

    background_style = {
        "position": "absolute",
        "inset": "0",
        "backgroundImage": f"url('{slide['image']}')",
        "backgroundSize": "cover",
        "backgroundPosition": "center",
        "transition": "background-image 0.7s ease-in-out",
        "transform": "scale(1.02)",
    }

    return background_style, build_hero_content(index)
