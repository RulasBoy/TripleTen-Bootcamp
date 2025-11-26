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

# Crear datos de ejemplo simulando datos de videojuegos
np.random.seed(42)
years = list(range(2000, 2021))
platforms = ['PS4', 'Xbox', 'PC', 'Switch']

# Crear un DataFrame de ejemplo
data_dict = {
    'Año': [],
    'Plataforma': [],
    'Juegos_Lanzados': []
}

for year in years:
    for platform in platforms:
        data_dict['Año'].append(year)
        data_dict['Plataforma'].append(platform)
        # Generar números aleatorios de juegos lanzados
        data_dict['Juegos_Lanzados'].append(np.random.randint(50, 200))

df = pd.DataFrame(data_dict)

# Calcular totales por año
df_totales = df.groupby('Año')['Juegos_Lanzados'].sum().reset_index()

# Definir el layout (diseño) del dashboard
app.layout = html.Div(children=[
    
    # Encabezado principal
    html.H1(
        children='Dashboard de Análisis de Videojuegos',
        style={
            'textAlign': 'center',
            'color': '#2c3e50',
            'marginBottom': 10
        }
    ),
    
    # Descripción
    html.Div(
        children='Análisis de lanzamientos de videojuegos por año y plataforma',
        style={
            'textAlign': 'center',
            'color': '#7f8c8d',
            'marginBottom': 30,
            'fontSize': 16
        }
    ),
    
    # Sección de métricas clave
    html.Div([
        html.Div([
            html.H3('Total de Juegos', style={'color': '#3498db'}),
            html.H2(f"{df['Juegos_Lanzados'].sum():,}", style={'color': '#2c3e50'})
        ], style={
            'width': '23%',
            'display': 'inline-block',
            'textAlign': 'center',
            'backgroundColor': '#ecf0f1',
            'padding': 20,
            'margin': '0 1%',
            'borderRadius': 10
        }),
        
        html.Div([
            html.H3('Plataformas', style={'color': '#e74c3c'}),
            html.H2(f"{len(platforms)}", style={'color': '#2c3e50'})
        ], style={
            'width': '23%',
            'display': 'inline-block',
            'textAlign': 'center',
            'backgroundColor': '#ecf0f1',
            'padding': 20,
            'margin': '0 1%',
            'borderRadius': 10
        }),
        
        html.Div([
            html.H3('Años Analizados', style={'color': '#2ecc71'}),
            html.H2(f"{len(years)}", style={'color': '#2c3e50'})
        ], style={
            'width': '23%',
            'display': 'inline-block',
            'textAlign': 'center',
            'backgroundColor': '#ecf0f1',
            'padding': 20,
            'margin': '0 1%',
            'borderRadius': 10
        }),
        
        html.Div([
            html.H3('Promedio/Año', style={'color': '#f39c12'}),
            html.H2(f"{int(df_totales['Juegos_Lanzados'].mean())}", style={'color': '#2c3e50'})
        ], style={
            'width': '23%',
            'display': 'inline-block',
            'textAlign': 'center',
            'backgroundColor': '#ecf0f1',
            'padding': 20,
            'margin': '0 1%',
            'borderRadius': 10
        }),
    ], style={'marginBottom': 30}),
    
    # Gráfico de áreas apiladas
    html.Div([
        dcc.Graph(
            id='grafico-areas-apiladas',
            figure={
                'data': [
                    go.Scatter(
                        x=df[df['Plataforma'] == platform]['Año'],
                        y=df[df['Plataforma'] == platform]['Juegos_Lanzados'],
                        mode='lines',
                        name=platform,
                        stackgroup='one',
                        fillcolor=['rgba(52, 152, 219, 0.7)',
                                   'rgba(231, 76, 60, 0.7)',
                                   'rgba(46, 204, 113, 0.7)',
                                   'rgba(243, 156, 18, 0.7)'][i]
                    ) for i, platform in enumerate(platforms)
                ],
                'layout': go.Layout(
                    title='Juegos Lanzados por Año y Plataforma',
                    xaxis={'title': 'Año'},
                    yaxis={'title': 'Número de Juegos'},
                    hovermode='x unified',
                    height=500
                )
            }
        )
    ], style={'marginBottom': 30}),
    
    # Gráfico de líneas (Total por año)
    html.Div([
        dcc.Graph(
            id='grafico-total-anual',
            figure={
                'data': [
                    go.Scatter(
                        x=df_totales['Año'],
                        y=df_totales['Juegos_Lanzados'],
                        mode='lines+markers',
                        name='Total',
                        line=dict(color='#9b59b6', width=3),
                        marker=dict(size=8)
                    )
                ],
                'layout': go.Layout(
                    title='Total de Juegos Lanzados por Año',
                    xaxis={'title': 'Año'},
                    yaxis={'title': 'Total de Juegos'},
                    hovermode='closest',
                    height=400
                )
            }
        )
    ]),
    
])

# Lógica del dashboard, no cambies las líneas a continuación
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=3000)

