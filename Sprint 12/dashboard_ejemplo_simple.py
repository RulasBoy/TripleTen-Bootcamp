#!/usr/bin/python
# -*- codificación: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# Definir estilos externos para el dashboard
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Crear la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Definir el layout (diseño) del dashboard
app.layout = html.Div(children=[
    
    # Encabezado principal
    html.H1(children='Dashboard de Función Lineal'),
    
    # Descripción
    html.Div(children='''
        Este es un dashboard simple que muestra una función lineal: y = x
    '''),
    
    # Gráfico de función lineal
    dcc.Graph(
        id='grafico-lineal',
        figure={
            'data': [
                go.Scatter(
                    x=pd.Series(range(-100, 100, 1)), 
                    y=pd.Series(range(-100, 100, 1)), 
                    mode='lines',
                    name='y = x',
                    line=dict(color='blue', width=2)
                )
            ],
            'layout': go.Layout(
                title='Función Lineal',
                xaxis={'title': 'x'},
                yaxis={'title': 'y'},
                hovermode='closest'
            )
        }
    ),
    
])

# Lógica del dashboard, no cambies las líneas a continuación
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=3000)

