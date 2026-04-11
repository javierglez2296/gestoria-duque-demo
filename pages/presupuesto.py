import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path="/presupuesto",
    title="Solicitud de presupuesto | Gestoría Duque",
    name="Presupuesto",
    description=(
        "Solicite presupuesto para servicios de gestoría, asesoría fiscal, "
        "laboral, tributaria, jurídica o externalización de servicios."
    ),
)


def build_input(label, input_id, placeholder, required=False, type_="text"):
    return html.Div(
        [
            html.Label(
                [
                    label,
                    html.Span(" *", className="budget-required") if required else None,
                ],
                htmlFor=input_id,
                className="budget-label",
            ),
            dbc.Input(
                id=input_id,
                type=type_,
                placeholder=placeholder,
                className="budget-input",
            ),
        ],
        className="budget-group",
    )


def build_budget_sidebar():
    items = [
        {
            "title": "Respuesta clara",
            "text": (
                "Revisamos su solicitud y le respondemos con una propuesta "
                "adaptada a lo que realmente necesita."
            ),
        },
        {
            "title": "Atención personalizada",
            "text": (
                "Cada caso se estudia de forma individual para ofrecerle una "
                "orientación profesional y útil."
            ),
        },
        {
            "title": "Proceso ágil",
            "text": (
                "Le contactaremos lo antes posible para ampliar información "
                "o enviarle el presupuesto correspondiente."
            ),
        },
    ]

    return html.Div(
        [
            html.Div("Solicitud de presupuesto", className="budget-eyebrow"),
            html.H1(
                "Cuéntenos qué necesita y le responderemos lo antes posible.",
                className="budget-title",
            ),
            html.P(
                "Complete el formulario y prepararemos una respuesta clara, "
                "profesional y adaptada a su caso.",
                className="budget-subtitle",
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(item["title"], className="budget-feature-title"),
                            html.P(item["text"], className="budget-feature-text"),
                        ],
                        className="budget-feature-card",
                    )
                    for item in items
                ],
                className="budget-feature-list",
            ),
        ],
        className="budget-sidebar",
    )


def build_budget_form():
    return dbc.Card(
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            build_input(
                                "Nombre de la empresa",
                                "empresa",
                                "Nombre de la empresa",
                                required=True,
                            ),
                            md=6,
                        ),
                        dbc.Col(
                            build_input(
                                "Persona de contacto",
                                "contacto",
                                "Persona de contacto",
                                required=True,
                            ),
                            md=6,
                        ),
                    ],
                    className="g-4",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            build_input(
                                "Dirección",
                                "direccion",
                                "Dirección",
                            ),
                            md=12,
                        ),
                    ],
                    className="g-4",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            build_input(
                                "Ciudad",
                                "ciudad",
                                "Ciudad",
                            ),
                            md=6,
                        ),
                        dbc.Col(
                            build_input(
                                "Código postal",
                                "codigo_postal",
                                "Código postal",
                            ),
                            md=6,
                        ),
                    ],
                    className="g-4",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            build_input(
                                "Email",
                                "email",
                                "Email",
                                required=True,
                                type_="email",
                            ),
                            md=6,
                        ),
                        dbc.Col(
                            build_input(
                                "Teléfono",
                                "telefono",
                                "Teléfono",
                                required=True,
                            ),
                            md=6,
                        ),
                    ],
                    className="g-4",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            build_input(
                                "Actividad de la empresa",
                                "actividad",
                                "Actividad de la empresa",
                            ),
                            md=6,
                        ),
                        dbc.Col(
                            build_input(
                                "Cómo nos ha conocido",
                                "origen",
                                "Cómo nos ha conocido",
                            ),
                            md=6,
                        ),
                    ],
                    className="g-4",
                ),
                html.Div(
                    [
                        html.Label(
                            [
                                "Seleccione la materia sobre la que desea el presupuesto",
                                html.Span(" *", className="budget-required"),
                            ],
                            htmlFor="materia",
                            className="budget-label",
                        ),
                        dcc.Dropdown(
                            id="materia",
                            options=[
                                {
                                    "label": "Gestoría administrativa",
                                    "value": "Gestoría administrativa",
                                },
                                {
                                    "label": "Asesoría laboral",
                                    "value": "Asesoría laboral",
                                },
                                {
                                    "label": "Asesoría tributaria",
                                    "value": "Asesoría tributaria",
                                },
                                {
                                    "label": "Asesoría jurídica",
                                    "value": "Asesoría jurídica",
                                },
                                {
                                    "label": "Externalización de servicios",
                                    "value": "Externalización de servicios",
                                },
                            ],
                            value="Asesoría laboral",
                            clearable=False,
                            className="budget-dropdown",
                        ),
                    ],
                    className="budget-group",
                ),
                html.Div(
                    [
                        html.Label(
                            [
                                "Describa lo que desea que le enviemos en el presupuesto",
                                html.Span(" *", className="budget-required"),
                            ],
                            htmlFor="mensaje",
                            className="budget-label",
                        ),
                        dbc.Textarea(
                            id="mensaje",
                            placeholder="Explique brevemente qué necesita",
                            className="budget-textarea",
                        ),
                    ],
                    className="budget-group",
                ),
                html.Div(
                    [
                        dbc.Checkbox(
                            id="privacidad",
                            className="budget-checkbox",
                        ),
                        html.Label(
                            [
                                "He leído y acepto la ",
                                html.A(
                                    "Política de privacidad",
                                    href="/politica-privacidad",
                                    className="budget-inline-link",
                                ),
                                " y las condiciones de uso.",
                            ],
                            htmlFor="privacidad",
                            className="budget-checkbox-label",
                        ),
                    ],
                    className="budget-checkbox-wrap",
                ),
                html.Div(
                    dbc.Button(
                        "Enviar solicitud",
                        id="budget-submit",
                        className="budget-submit-btn",
                        n_clicks=0,
                    ),
                    className="budget-submit-wrap",
                ),
                html.Div(id="budget-response"),
            ]
        ),
        className="budget-card",
    )


layout = html.Div(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        build_budget_sidebar(),
                        lg=5,
                        className="mb-4 mb-lg-0",
                    ),
                    dbc.Col(
                        build_budget_form(),
                        lg=7,
                    ),
                ],
                className="budget-layout-row",
            ),
        ],
        fluid="lg",
        className="budget-page",
    )
)


@callback(
    Output("budget-response", "children"),
    Input("budget-submit", "n_clicks"),
    State("empresa", "value"),
    State("contacto", "value"),
    State("email", "value"),
    State("telefono", "value"),
    State("materia", "value"),
    State("mensaje", "value"),
    State("privacidad", "value"),
    prevent_initial_call=True,
)
def submit_budget(
    n_clicks,
    empresa,
    contacto,
    email,
    telefono,
    materia,
    mensaje,
    privacidad,
):
    required_values = [empresa, contacto, email, telefono, materia, mensaje]

    if not all(required_values):
        return html.Div(
            "Revise los campos obligatorios antes de enviar la solicitud.",
            className="budget-message budget-message-error",
        )

    if not privacidad:
        return html.Div(
            "Debe aceptar la política de privacidad para poder enviar la solicitud.",
            className="budget-message budget-message-error",
        )

    return html.Div(
        "Solicitud enviada correctamente. Nos pondremos en contacto con usted lo antes posible.",
        className="budget-message budget-message-success",
    )
