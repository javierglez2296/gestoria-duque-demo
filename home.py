import dash
from dash import html

from components.home.hero import build_hero
from components.home.sections import (
    build_trust_section,
    build_stats_section,
    build_services_section,
    build_about_section,
    build_pillars_section,
    build_featured_section,
    build_process_section,
    build_testimonials_section,
    build_location_section,
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
        "Gestoría en Ávila para empresas, autónomos y particulares. "
        "Asesoría fiscal, laboral, contable y administrativa con atención cercana y profesional."
    ),
)


layout = html.Div(
    [
        build_hero(),
        build_trust_section(),
        build_stats_section(),
        build_services_section(),
        build_about_section(),
        build_pillars_section(),
        build_featured_section(),
        build_process_section(),
        build_testimonials_section(),
        build_location_section(),
        build_seo_section(),
        build_faq_section(),
        build_cta_section(),
        build_footer_section(),
        build_floating_whatsapp(),
    ],
    className="page-shell",
)
