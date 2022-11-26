import dash
from dash import html, dcc, Input, Output, State, html
import dash_bootstrap_components as dbc
from dash import page_registry, page_container

from dash_extensions.enrich import (
    DashProxy,
    MultiplexerTransform,
    html,
    dcc,
)

external_stylesheets = [dbc.themes.JOURNAL]

app = DashProxy(
    __name__,
    transforms=[MultiplexerTransform()],
    use_pages=True,
    prevent_initial_callbacks=True,
    suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets,
)

server = app.server

GENLAC_LOGO = "/assets/genlac.png"

dropdown = dbc.Row([
    dbc.Col(
        dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("Educación", header=True),
            dbc.DropdownMenuItem("Tasa de escolarización pre-primaria (5 años)", href="/"),
            dbc.DropdownMenuItem("Tasa de escolarización pre-primaria (3 a 5 años)", href="/tasa-escolarizacion-pre-primaria-35"),
            dbc.DropdownMenuItem("Tasa neta de escolarización primaria", href="/tasa-neta-escolarizacion-primaria"),
            dbc.DropdownMenuItem("Tasa neta de escolarización secundaria", href="/tasa-neta-escolarizacion-secundaria"),
            dbc.DropdownMenuItem("Tasa neta de escolarización terciaria", href="/tasa-neta-escolarizacion-terciaria"),
            dbc.DropdownMenuItem("Tasa de finalización del nivel primario", href="/tasa-finalizacion-primario"),
            dbc.DropdownMenuItem("Tasa de finalización del nivel secundario", href="/tasa-finalizacion-secundario"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Desarrollo", header=True),
            dbc.DropdownMenuItem("Matrimonio precoz", href="/matrimonio-precoz"),
            dbc.DropdownMenuItem("Porcentaje de jóvenes de 15 a 24 fuera de la escuela y del mercado laboral", href="/jovenes-fuera-escuela-trabajo"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Actividades y uso del tiempo", header=True),
            dbc.DropdownMenuItem("Participación en actividades de cuidado", href="/participacion-actividades-cuidado"),
            dbc.DropdownMenuItem("Horas semanales dedicadas a actividades de cuidado", href="/horas-actividades-cuidado"),
            dbc.DropdownMenuItem("Participación en actividades de cuidado de niños", href="/participacion-actividades-cuidado-ninos"),
            dbc.DropdownMenuItem("Horas semanales dedicadas a actividades de cuidado de niños", href="/horas-actividades-cuidado-ninos"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Puntajes en pruebas", header=True),
            dbc.DropdownMenuItem("Puntaje promedio en pruebas estandarizadas para alumnos de tercer grado", href="/puntajes-tercero"),
            dbc.DropdownMenuItem("Puntaje promedio en pruebas estandarizadas para alumnos de sexto grado", href="/puntajes-sexto"),
            dbc.DropdownMenuItem("Puntaje promedio en pruebas estandarizadas para alumnos de 15 años", href="/puntajes-15"),
            dbc.DropdownMenuItem("Ratio de puntajes en pruebas estandarizadas para alumnos de tercer grado", href="/ratio-tercero"),
            dbc.DropdownMenuItem("Ratio de puntajes en pruebas estandarizadas para alumnos de sexto grado", href="/ratio-sexto"),
            dbc.DropdownMenuItem("Ratio de puntajes en pruebas estandarizadas para alumnos de 15 años", href="/ratio-15"),
            dbc.DropdownMenuItem("Porcentaje de mujeres en el 10% más bajo de puntajes en tercer grado", href="/mujeres-10-bajo-tercero"),
            dbc.DropdownMenuItem("Porcentaje de mujeres en el 10% más bajo de puntajes en sexto grado", href="/mujeres-10-bajo-sexto"),
            dbc.DropdownMenuItem("Porcentaje de mujeres en el 10% más bajo de puntajes de alumnos de 15 años", href="/mujeres-bajo-10-15"),
            dbc.DropdownMenuItem("Porcentaje de mujeres en el 10% más alto de puntajes en tercer grado", href="/mujeres-10-alto-tercero"),
            dbc.DropdownMenuItem("Porcentaje de mujeres en el 10% más alto de puntajes en sexto grado", href="/mujeres-10-alto-sexto"),
            dbc.DropdownMenuItem("Porcentaje de mujeres en el 10% más alto de puntajes de alumnos de 15 años", href="/mujeres-10-alto-15"),
            dbc.DropdownMenuItem("Porcentaje de mujeres entre los alumnos de 15 años analfabetos funcionales", href="/mujeres-analfabeta-funcional"),
        ],
        size="lg",
        nav=True,
        in_navbar=True,
        label="Indicadores",
        className="ms-0",
        toggle_style={"color": "#460074"},
        align_end=False,
        style={'width':'100%'}

        )
    )
],
className="g-0 ms-auto flex-nowrap mt-5 mt-md-0",
align="center",
)


navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                        dbc.Collapse(
                            dropdown, 
                            className="ml-auto",
                            id="navbar-collapse",
                            is_open=False,
                            navbar=True,
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
        ],
    fluid=True),
    #outline=True, 
    color="light",
    dark=True,
)
# Definimos el layout:
app.layout = html.Div(
    [
        dcc.Store(id="store", data='Argentina'),
        dbc.Container([
    dbc.Row(
        [
            navbar # Navbar
        ]
    ),
    html.Br(),        
    dbc.Row(
        [
            dash.page_container # Contenido de cada pagina
        ]
    )
], fluid=True)
    ]
)


if __name__ == "__main__":
    app.run_server()