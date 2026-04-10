import os
import smtplib
from email.message import EmailMessage

import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path="/presupuesto",
    title="Solicitar presupuesto | Gestoría Duque",
    name="Solicitar presupuesto",
    description="Solicita presupuesto para servicios de gestoría en Ávila.",
)

DESTINATARIO = "info@gestoriaduque.com"


def form_group(label, field, required=False):
    return html.Div(
        [
            html.Label(
                [
                    label,
                    html.Span(" *", className="budget-required") if required else None,
                ],
                className="budget-label",
            ),
            field,
        ],
        className="budget-group",
    )


layout = html.Div(
    dbc.Container(
        [
            html.Div(
                [
                    html.Div("Solicitud de presupuesto", className="budget-eyebrow"),
                    html.H1(
                        "Cuéntenos qué necesita y le responderemos lo antes posible.",
                        className="budget-title",
                    ),
                    html.P(
                        "Complete el formulario y enviaremos su solicitud a nuestro equipo.",
                        className="budget-subtitle",
                    ),
                ],
                className="budget-header",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    form_group(
                                        "Nombre de la empresa",
                                        dbc.Input(
                                            id="empresa",
                                            type="text",
                                            placeholder="Nombre de la empresa",
                                            className="budget-input",
                                        ),
                                        required=True,
                                    ),
                                    form_group(
                                        "Persona de contacto",
                                        dbc.Input(
                                            id="contacto",
                                            type="text",
                                            placeholder="Persona de contacto",
                                            className="budget-input",
                                        ),
                                        required=True,
                                    ),
                                    form_group(
                                        "Dirección",
                                        dbc.Input(
                                            id="direccion",
                                            type="text",
                                            placeholder="Dirección",
                                            className="budget-input",
                                        ),
                                    ),
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                form_group(
                                                    "Ciudad",
                                                    dbc.Input(
                                                        id="ciudad",
                                                        type="text",
                                                        placeholder="Ciudad",
                                                        className="budget-input",
                                                    ),
                                                ),
                                                md=6,
                                            ),
                                            dbc.Col(
                                                form_group(
                                                    "Código postal",
                                                    dbc.Input(
                                                        id="codigo_postal",
                                                        type="text",
                                                        placeholder="Código postal",
                                                        className="budget-input",
                                                    ),
                                                ),
                                                md=6,
                                            ),
                                        ]
                                    ),
                                    form_group(
                                        "Email",
                                        dbc.Input(
                                            id="email",
                                            type="email",
                                            placeholder="Email",
                                            className="budget-input",
                                        ),
                                        required=True,
                                    ),
                                    form_group(
                                        "Teléfono",
                                        dbc.Input(
                                            id="telefono",
                                            type="text",
                                            placeholder="Teléfono",
                                            className="budget-input",
                                        ),
                                        required=True,
                                    ),
                                    form_group(
                                        "Actividad de la empresa",
                                        dbc.Input(
                                            id="actividad",
                                            type="text",
                                            placeholder="Actividad de la empresa",
                                            className="budget-input",
                                        ),
                                    ),
                                    form_group(
                                        "Cómo nos ha conocido",
                                        dbc.Input(
                                            id="conocido",
                                            type="text",
                                            placeholder="Cómo nos ha conocido",
                                            className="budget-input",
                                        ),
                                    ),
                                    form_group(
                                        "Seleccione la materia sobre la que desea el presupuesto",
                                        dbc.Select(
                                            id="materia",
                                            options=[
                                                {"label": "Asesoría Laboral", "value": "Asesoría Laboral"},
                                                {"label": "Asesoría Fiscal", "value": "Asesoría Fiscal"},
                                                {"label": "Asesoría Contable", "value": "Asesoría Contable"},
                                                {"label": "Autónomos", "value": "Autónomos"},
                                                {"label": "Empresas", "value": "Empresas"},
                                                {"label": "Trámites", "value": "Trámites"},
                                                {"label": "Otros", "value": "Otros"},
                                            ],
                                            value="Asesoría Laboral",
                                            className="budget-input",
                                        ),
                                        required=True,
                                    ),
                                    form_group(
                                        "Describa lo que desea que le enviemos en el presupuesto",
                                        dbc.Textarea(
                                            id="descripcion",
                                            placeholder="Explique brevemente qué necesita",
                                            className="budget-textarea",
                                            rows=6,
                                        ),
                                        required=True,
                                    ),
                                    html.Div(
                                        [
                                            dbc.Checkbox(
                                                id="terminos",
                                                className="budget-checkbox-input",
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
                                                htmlFor="terminos",
                                                className="budget-checkbox-label",
                                            ),
                                        ],
                                        className="budget-checkbox-wrap",
                                    ),
                                    html.Div(
                                        id="budget-message",
                                        className="budget-message",
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
                                ]
                            ),
                            className="budget-card",
                        ),
                        lg=9,
                    ),
                ],
                justify="center",
            ),
        ],
        fluid="lg",
        className="budget-page",
    )
)


def _clean(value):
    return (value or "").strip()


def _is_valid_email(value):
    value = _clean(value)
    return "@" in value and "." in value.split("@")[-1]


def enviar_email(
    empresa,
    contacto,
    direccion,
    ciudad,
    codigo_postal,
    email,
    telefono,
    actividad,
    conocido,
    materia,
    descripcion,
):
    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")
    smtp_use_tls = os.getenv("SMTP_USE_TLS", "true").lower() == "true"
    remitente = os.getenv("SMTP_FROM", smtp_user or DESTINATARIO)

    if not smtp_host or not smtp_user or not smtp_password:
        raise RuntimeError(
            "Faltan variables SMTP_HOST, SMTP_USER o SMTP_PASSWORD en el entorno."
        )

    asunto = f"Nuevo formulario de presupuesto - {empresa}"

    cuerpo = f"""
Nueva solicitud de presupuesto recibida

Nombre de la empresa: {empresa}
Persona de contacto: {contacto}
Dirección: {direccion}
Ciudad: {ciudad}
Código postal: {codigo_postal}
Email: {email}
Teléfono: {telefono}
Actividad de la empresa: {actividad}
Cómo nos ha conocido: {conocido}
Materia: {materia}

Descripción:
{descripcion}
""".strip()

    msg = EmailMessage()
    msg["Subject"] = asunto
    msg["From"] = remitente
    msg["To"] = DESTINATARIO
    msg["Reply-To"] = email
    msg.set_content(cuerpo)

    with smtplib.SMTP(smtp_host, smtp_port, timeout=20) as server:
        if smtp_use_tls:
            server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)


@callback(
    Output("budget-message", "children"),
    Output("budget-message", "className"),
    Input("budget-submit", "n_clicks"),
    State("empresa", "value"),
    State("contacto", "value"),
    State("direccion", "value"),
    State("ciudad", "value"),
    State("codigo_postal", "value"),
    State("email", "value"),
    State("telefono", "value"),
    State("actividad", "value"),
    State("conocido", "value"),
    State("materia", "value"),
    State("descripcion", "value"),
    State("terminos", "value"),
    prevent_initial_call=True,
)
def submit_budget_form(
    n_clicks,
    empresa,
    contacto,
    direccion,
    ciudad,
    codigo_postal,
    email,
    telefono,
    actividad,
    conocido,
    materia,
    descripcion,
    terminos,
):
    empresa = _clean(empresa)
    contacto = _clean(contacto)
    direccion = _clean(direccion)
    ciudad = _clean(ciudad)
    codigo_postal = _clean(codigo_postal)
    email = _clean(email)
    telefono = _clean(telefono)
    actividad = _clean(actividad)
    conocido = _clean(conocido)
    materia = _clean(materia)
    descripcion = _clean(descripcion)

    errores = []

    if not empresa:
        errores.append("Debe indicar el nombre de la empresa.")
    if not contacto:
        errores.append("Debe indicar la persona de contacto.")
    if not email:
        errores.append("Debe indicar un email.")
    elif not _is_valid_email(email):
        errores.append("El email no tiene un formato válido.")
    if not telefono:
        errores.append("Debe indicar un teléfono.")
    if not materia:
        errores.append("Debe seleccionar una materia.")
    if not descripcion:
        errores.append("Debe describir su solicitud.")
    if not terminos:
        errores.append("Debe aceptar la política de privacidad y las condiciones.")

    if errores:
        return (
            html.Ul([html.Li(e) for e in errores], className="mb-0"),
            "budget-message budget-message-error",
        )

    try:
        enviar_email(
            empresa=empresa,
            contacto=contacto,
            direccion=direccion,
            ciudad=ciudad,
            codigo_postal=codigo_postal,
            email=email,
            telefono=telefono,
            actividad=actividad,
            conocido=conocido,
            materia=materia,
            descripcion=descripcion,
        )
    except Exception as e:
        return (
            f"No se pudo enviar la solicitud. Revise la configuración del correo. Detalle: {e}",
            "budget-message budget-message-error",
        )

    return (
        "Solicitud enviada correctamente. Nos pondremos en contacto con usted lo antes posible.",
        "budget-message budget-message-success",
    )
