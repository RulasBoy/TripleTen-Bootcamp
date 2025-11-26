#!/usr/bin/python
# -*- codificación: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# Definir estilos externos para el dashboard
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Crear la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Crear datos de ejemplo
x_values = np.linspace(-10, 10, 100)

# Definir el layout (diseño) del dashboard
app.layout = html.Div(children=[
    
    # Encabezado principal
    html.H1(
        children='Dashboard de Funciones Matemáticas',
        style={'textAlign': 'center', 'color': '#2c3e50'}
    ),
    
    # Descripción
    html.Div(
        children='Un ejemplo de dashboard con múltiples visualizaciones',
        style={'textAlign': 'center', 'marginBottom': 30}
    ),
    
    # Primera fila de gráficos
    html.Div([
        # Gráfico 1: Funciones lineales
        html.Div([
            dcc.Graph(
                id='grafico-lineal',
                figure={
                    'data': [
                        go.Scatter(
                            x=x_values,
                            y=x_values,
                            mode='lines',
                            name='y = x',
                            line=dict(color='blue', width=2)
                        ),
                        go.Scatter(
                            x=x_values,
                            y=2*x_values,
                            mode='lines',
                            name='y = 2x',
                            line=dict(color='red', width=2)
                        ),
                        go.Scatter(
                            x=x_values,
                            y=-x_values,
                            mode='lines',
                            name='y = -x',
                            line=dict(color='green', width=2)
                        ),
                    ],
                    'layout': go.Layout(
                        title='Funciones Lineales',
                        xaxis={'title': 'x'},
                        yaxis={'title': 'y'},
                        hovermode='closest'
                    )
                }
            )
        ], style={'width': '48%', 'display': 'inline-block'}),
        
        # Gráfico 2: Función cuadrática
        html.Div([
            dcc.Graph(
                id='grafico-cuadratico',
                figure={
                    'data': [
                        go.Scatter(
                            x=x_values,
                            y=x_values**2,
                            mode='lines',
                            name='y = x²',
                            line=dict(color='purple', width=2)
                        ),
                    ],
                    'layout': go.Layout(
                        title='Función Cuadrática',
                        xaxis={'title': 'x'},
                        yaxis={'title': 'y'},
                        hovermode='closest'
                    )
                }
            )
        ], style={'width': '48%', 'display': 'inline-block', 'float': 'right'}),
    ]),
    
    # Segunda fila: Gráfico de barras
    html.Div([
        dcc.Graph(
            id='grafico-barras',
            figure={
                'data': [
                    go.Bar(
                        x=['Categoría A', 'Categoría B', 'Categoría C', 'Categoría D'],
                        y=[20, 35, 30, 25],
                        marker=dict(color=['#3498db', '#e74c3c', '#2ecc71', '#f39c12'])
                    )
                ],
                'layout': go.Layout(
                    title='Ejemplo de Gráfico de Barras',
                    xaxis={'title': 'Categorías'},
                    yaxis={'title': 'Valores'},
                )
            }
        )
    ], style={'marginTop': 30}),
    
])

# Lógica del dashboard, no cambies las líneas a continuación
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=3000)

