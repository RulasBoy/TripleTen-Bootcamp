#!/usr/bin/python
# -*- codificación: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# Definir estilos externos (opcional)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Crear la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# ============================================================
# TU CÓDIGO AQUÍ
# ============================================================

# 1. Cargar y preparar datos (si es necesario)
# Ejemplo:
# df = pd.read_csv('datos.csv')
# df_procesado = df.groupby('columna').sum()

# 2. Definir el layout del dashboard
app.layout = html.Div(children=[
    
    # Agrega aquí tus componentes:
    # - Encabezados (html.H1, html.H2, etc.)
    # - Párrafos (html.P)
    # - Gráficos (dcc.Graph)
    # - Controles (dcc.Dropdown, dcc.Slider, etc.)
    
    html.H1(children='Mi Dashboard'),
    
    html.Div(children='Descripción del dashboard'),
    
    # Ejemplo de gráfico
    dcc.Graph(
        id='mi-grafico',
        figure={
            'data': [
                # Tus datos aquí
                go.Scatter(
                    x=[1, 2, 3, 4, 5],
                    y=[1, 4, 9, 16, 25],
                    mode='lines+markers',
                    name='Datos de ejemplo'
                )
            ],
            'layout': go.Layout(
                title='Título del Gráfico',
                xaxis={'title': 'Eje X'},
                yaxis={'title': 'Eje Y'}
            )
        }
    ),
    
])

# ============================================================
# FIN DE TU CÓDIGO
# ============================================================

# Lógica del dashboard, no cambies las líneas a continuación
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=3000)

