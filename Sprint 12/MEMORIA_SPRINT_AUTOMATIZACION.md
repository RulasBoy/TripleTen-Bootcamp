# Sprint 12 - Automatización
## Memoria de Conceptos y Ejercicios

---

## 1. Introducción a la Automatización

### Objetivos del Sprint:
- Aprender a recopilar requisitos de clientes para dashboards
- Trazar gráficos comunes con la librería Dash
- Agregar elementos interactivos a dashboards
- Diseñar dashboards con HTML
- Definir la lógica de un dashboard

---

## 2. Data Pipelines (ETL)

### ¿Qué son?
Programas especiales que se ejecutan según horarios para recopilar, fusionar, transformar y almacenar datos automáticamente.

### Usos de los pipelines:
- Analizar datos en Internet y almacenarlos en bases de datos
- Recopilar información sobre visitas y compras para análisis de cohortes
- Detectar anomalías en comportamiento de usuarios
- Analizar pruebas A/B
- Enviar reportes automáticos

### ETL: Extract, Transform, Load

#### 1. Extracción (Extract)
Recopilar datos de fuentes variadas:
- Sitios web
- Bases de datos corporativas
- APIs externas

#### 2. Transformación (Transform)
- Estandarizar datos (texto a números, fechas)
- Categorizar información
- Convertir a formato conveniente
- Calcular métricas (ejemplo: LTV)

#### 3. Carga (Load)
- Guardar datos agregados en bases de datos
- Crear informes
- Generar envíos automáticos

### Flujo completo:
```
Fuente de datos → Recolección de datos → Procesamiento de datos → 
Transformación de datos → Guardar datos y generar informes → 
Tablas con datos filtrados y agregados → Informes y dashboards
```

---

## 3. Ejercicio ETL - Henry y el Coche Usado

### Pregunta:
Henry quiere comprar un coche usado y necesita configurar Super ETL para:
1. Descargar páginas HTML con anuncios
2. Extraer marcas de coches, precios y números de teléfono del formato HTML
3. Almacenar estos tres parámetros en la base de datos

### Respuesta Correcta:
**Conectarse a sitios catalogados (Extraer), obtener la información necesaria de los anuncios (Transformar), almacenar los datos en la base de datos (Cargar).**

### Explicación:
El orden correcto del proceso ETL es:
1. **Extract:** Conectarse a sitios y descargar HTML (fuente de datos)
2. **Transform:** Procesar y extraer información específica del HTML
3. **Load:** Almacenar datos limpios en la base de datos

---

## 4. Acceso Directo a Bases de Datos

### Ventajas del Acceso Directo:
1. **Velocidad:** No esperar por archivos de volcado
2. **Autonomía:** Automatización sin depender de colegas
3. **Exploración:** Acceso directo a información valiosa

---

## 5. SQLAlchemy - Conexión a Bases de Datos

### ¿Qué es SQLAlchemy?
Librería que permite:
- Leer datos de bases de datos a DataFrames de pandas
- Guardar DataFrames en bases de datos con un solo comando

### Parámetros de Conexión Necesarios:
- **SGBD:** Sistema Gestor de Base de Datos (PostgreSQL, MySQL, SQLite, etc.)
- **Ubicación:** Dirección IP del servidor y puerto
- **Credenciales:** Usuario y contraseña
- **Nombre:** Nombre de la base de datos específica

### String de Conexión:

```python
# Ejemplo PostgreSQL
connection_string = 'postgresql://usuario:contraseña@localhost:5432/nombre_bd'

# Ejemplo SQLite
connection_string = 'sqlite:///ruta/a/base_de_datos.db'
```

### Crear Conexión:

```python
from sqlalchemy import create_engine

db_config = {
    'user': 'my_user',
    'pwd': 'my_user_password',
    'host': 'localhost',
    'port': 5432,
    'db': 'games'
}

connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(
    db_config['user'],
    db_config['pwd'],
    db_config['host'],
    db_config['port'],
    db_config['db']
)

engine = create_engine(connection_string)
```

### Leer Datos de la BD:

```python
query = '''
    SELECT game_id, name, platform, year_of_release
    FROM data_raw
'''

data_raw = pd.io.sql.read_sql(query, con=engine, index_col='game_id')
```

### Guardar Datos en la BD:

```python
df.to_sql(name='nombre_tabla', con=engine, if_exists='append', index=False)
```

### Parámetros `if_exists`:
- **`'replace'`:** Elimina datos existentes y guarda nuevos
- **`'append'`:** Agrega nuevas filas al final de la tabla
- **`'fail'`:** Error si la tabla ya existe (por defecto)

---

## 6. Pipeline Completo con Parámetros

### Elementos Clave de un Pipeline:

1. **Parámetros de entrada** usando `getopt` o `argparse`
2. **Lectura de datos** con filtros SQL (WHERE, BETWEEN)
3. **Procesamiento y transformación** con pandas
4. **Eliminación de registros antiguos** con DELETE
5. **Almacenamiento de datos procesados**

### Ejemplo de Parámetros de Entrada:

```python
import sys
import getopt

unixOptions = "sdt:edt"
gnuOptions = ["start_dt=", "end_dt="]

fullCmdArguments = sys.argv
argumentList = fullCmdArguments[1:]  # Excluir nombre del script

try:
    arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
    print(str(err))
    sys.exit(2)

start_dt = ''
end_dt = ''
for currentArgument, currentValue in arguments:
    if currentArgument in ("-sdt", "--start_dt"):
        start_dt = currentValue
    elif currentArgument in ("-edt", "--end_dt"):
        end_dt = currentValue
```

### Consulta SQL con Filtros Dinámicos:

```python
query = '''
    SELECT *
    FROM data_raw
    WHERE year_of_release::TIMESTAMP BETWEEN '{}'::TIMESTAMP AND '{}'::TIMESTAMP
'''.format(start_dt, end_dt)
```

### Eliminar Registros Antiguos con DELETE:

```python
# Eliminar registros más antiguos entre start_dt y end_dt
query = '''
    DELETE FROM agg_games_year 
    WHERE year_of_release BETWEEN '{}'::TIMESTAMP AND '{}'::TIMESTAMP
'''.format(start_dt, end_dt)

engine.execute(query)
```

### Comando DELETE SQL (Sintaxis General):

```sql
DELETE FROM nombre_de_la_tabla 
WHERE condiciones_para_encontrar_registros_a_eliminar;
```

**Ejemplo:**
```sql
DELETE FROM data_raw WHERE rating = 'E';
```

---

## 7. Ejercicio Práctico: Pipeline Ministerio de Salud Chile

### Objetivo:
Cargar registros anuales de salud de archivos CSV individuales a una base de datos central del Ministerio de Salud.

### Desafíos del Ejercicio:
- **Caracteres especiales:** ñ, ó aparecen como � (requiere encoding='latin1')
- **Consistencia de estructura:** Verificar tipos de datos
- **Filas vacías:** Eliminar filas con mayoría de valores '*'
- **Evitar duplicados:** Validar si el año ya está cargado
- **Inconsistencias en nombres de columnas**

### Datasets:
- Egresos Hospitalarios 2020
- Egresos Hospitalarios 2019
- Egresos Hospitalarios 2018

### Funciones Principales del Pipeline:

#### 1. `parse_arguments()`
Analiza los argumentos de línea de comandos para obtener la ruta del archivo.

```python
def parse_arguments():
    unixOptions = "f:"
    gnuOptions = ["file="]
    
    fullCmdArguments = sys.argv
    argumentList = fullCmdArguments[1:]
    
    try:
        arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
    except getopt.error as err:
        print(str(err))
        sys.exit(2)
    
    file_path = ''
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-f", "--file"):
            file_path = currentValue
    
    return file_path
```

#### 2. `extract_year_from_path(file_path)`
Extrae el año del nombre del archivo.

```python
def extract_year_from_path(file_path):
    year = file_path.split('/')[-1].split('.')[0][-4:]
    return year
```

#### 3. `data_already_exists(engine, table_name, year)`
Valida si los datos del año ya están en la base de datos.

```python
def data_already_exists(engine, table_name, year):
    try:
        with engine.connect() as connection:
            query = text(f'SELECT * FROM {table_name} WHERE ANO_EGRESO={year}')
            result = connection.execute(query)
            exists = result.fetchone() is not None
    except OperationalError:
        exists = False
    return exists
```

#### 4. `load_data(file_path)`
Carga el archivo CSV en un DataFrame.

```python
def load_data(file_path):
    df = pd.read_csv(file_path, encoding='latin1', delimiter=';')
    return df
```

#### 5. `preprocess_data(df, threshold=0.5)`
Limpia y preprocesa los datos:
- Elimina filas con demasiados valores '*'
- Convierte tipos de datos
- Renombra columnas

```python
def preprocess_data(df, threshold=0.5):
    # Calcular número de columnas
    num_columns = df.shape[1]
    
    # Determinar número de '*' permitidos
    allowed_stars = int(num_columns * threshold)
    
    # Filtrar filas que exceden el umbral
    cleaned_df = df[df.apply(lambda x: (x == '*').sum() <= allowed_stars, axis=1)]
    
    # Convertir tipos de datos
    cleaned_df.loc[:,'COMUNA_RESIDENCIA'] = cleaned_df['COMUNA_RESIDENCIA'].astype(int)
    cleaned_df.loc[:,'REGION_RESIDENCIA'] = cleaned_df['REGION_RESIDENCIA'].astype(int)
    cleaned_df.loc[:,'ANO_EGRESO'] = cleaned_df['ANO_EGRESO'].astype(int)
    
    # Renombrar columnas
    new_column_names = [
        'PERTENENCIA_ESTABLECIMIENTO_SALUD', 'SEXO', 'GRUPO_EDAD', 'ETNIA',
        'GLOSA_PAIS_ORIGEN', 'COMUNA_RESIDENCIA', 'GLOSA_COMUNA_RESIDENCIA',
        'REGION_RESIDENCIA', 'GLOSA_REGION_RESIDENCIA', 'PREVISION',
        'GLOSA_PREVISION', 'ANO_EGRESO', 'DIAG1', 'DIAG2', 'DIAS_ESTADA',
        'CONDICION_EGRESO', 'INTERV_Q', 'PROCED'
    ]
    old_column_names = cleaned_df.columns
    column_mapping = dict(zip(old_column_names, new_column_names))
    cleaned_df.rename(columns=column_mapping, inplace=True)
    
    return cleaned_df
```

#### 6. `create_db_engine(db_name)`
Crea la conexión a la base de datos SQLite.

```python
def create_db_engine(db_name):
    connection_string = f'sqlite:///{db_name}'
    engine = create_engine(connection_string)
    print(f'[INFO]: Connection Checked: {connection_string}')
    return engine
```

#### 7. `save_to_database(df, engine, table_name)`
Guarda el DataFrame en la base de datos.

```python
def save_to_database(df, engine, table_name):
    df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
```

#### 8. `validate_data(engine, table_name)`
Valida los datos cargados.

```python
def validate_data(engine, table_name):
    with engine.connect() as connection:
        query = text(f'SELECT ANO_EGRESO, count(*) FROM {table_name} GROUP BY ANO_EGRESO')
        result = connection.execute(query)
        rows = result.fetchall()
        for row in rows[:100]:
            print(row)
```

### Ejecución del Pipeline:

```bash
python pipeline.py -f datasets/EGRESOS_2020/EGRE_DATOS_ABIERTOS_2020.csv
```

### Resultado Esperado:

Después de cargar los tres archivos:
```
(2018, 1620450)
(2019, 1623335)
(2020, 1292935)
```

Si intentas cargar un archivo ya existente:
```
Los datos ya existen en la base de datos. No se realizó ninguna acción.
(2018, 1620450)
(2019, 1623335)
(2020, 1292935)
```

---

## 8. Buenas Prácticas en Pipelines

### 1. Configuración Separada
Almacenar configuración de BD en diccionarios o archivos separados:
```python
db_config = {
    'user': 'my_user',
    'pwd': 'my_user_password',
    'host': 'localhost',
    'port': 5432,
    'db': 'games'
}
```

### 2. Filtrado en SQL
Filtrar datos en SQL antes de cargarlos a pandas (más eficiente):
```python
query = '''
    SELECT *
    FROM data_raw
    WHERE year_of_release BETWEEN '2018' AND '2020'
'''
```

### 3. Validación de Duplicados
Siempre validar si los datos ya existen antes de insertar.

### 4. Manejo de Encoding
Especificar encoding adecuado para caracteres especiales:
```python
df = pd.read_csv(file_path, encoding='latin1', delimiter=';')
```

### 5. Limpieza de Datos
Implementar umbral (threshold) para valores faltantes o inválidos.

### 6. Conversión de Tipos
Convertir tipos de datos explícitamente:
```python
df['columna'] = df['columna'].astype(int)
df['fecha'] = pd.to_datetime(df['fecha'])
```

### 7. Manejo de Errores
Usar try-except para manejar errores de base de datos:
```python
try:
    # operación de BD
except OperationalError as e:
    # manejar error
```

---

## 9. Resumen de Comandos Importantes

### SQLAlchemy:
```python
# Crear engine
engine = create_engine(connection_string)

# Leer datos
df = pd.io.sql.read_sql(query, con=engine, index_col='id')

# Guardar datos
df.to_sql(name='tabla', con=engine, if_exists='append', index=False)

# Ejecutar comando SQL directo
engine.execute(query)
```

### SQL Útiles para Pipelines:
```sql
-- Seleccionar con filtro de fechas
SELECT * FROM tabla
WHERE fecha BETWEEN '2020-01-01' AND '2020-12-31';

-- Eliminar registros
DELETE FROM tabla WHERE condicion;

-- Agrupar y contar
SELECT año, COUNT(*) FROM tabla GROUP BY año;
```

---

## Notas Finales

- Los pipelines ETL son fundamentales para la automatización
- SQLAlchemy simplifica la interacción con bases de datos desde Python
- Siempre validar duplicados y calidad de datos antes de cargar
- El orden ETL (Extract → Transform → Load) debe respetarse
- Usar parámetros de entrada hace los pipelines reutilizables y flexibles

---

---

## 10. Dashboards - Introducción

### ¿Qué es un Dashboard?

Un **dashboard (cuadro de mandos o tablero)** es un informe interactivo que refleja un conjunto de métricas de negocio esenciales para administrar una empresa que se actualiza automáticamente.

### Características Clave de un Dashboard:

1. **Actualizado automáticamente**
   - Los datos se actualizan periódicamente (cada día/hora/minuto)
   - Relación directa con automatización

2. **Interactivo**
   - Controles para filtrar información
   - Generalmente filtrado por tiempo

3. **Conjunto de métricas de negocio**
   - Información necesaria para resolver problemas comerciales

4. **Para gestión empresarial**
   - Usado para tomar decisiones de negocio

### Elementos Principales de un Dashboard:

1. **Encabezado:** Título e información general
2. **Cuadro de diálogo:** Selección de período de datos
3. **Gráficos:** Visualizaciones (ejemplo: gráficos de áreas apiladas)

**Ejemplo:** Dashboard de lanzamientos de juegos desglosados por año y plataforma con gráfico de áreas apiladas (cada plataforma con un color específico).

---

## 11. Librería Dash para Crear Dashboards

### ¿Qué es Dash?

**Dash** es un conjunto de librerías de Python para crear dashboards y mostrarlos en navegadores web.

### Componentes de Dash:

- **Dash y Plotly:** Se encargan de trazar los dashboards
- **Flask:** Microframework para mostrar dashboards en navegadores (aplicaciones web)

### Alternativas a Dash:

**Sistemas Comerciales (costosos):**
- Tableau
- QlikView
- Microsoft Power BI
- Amazon QuickSight

**Alternativa Gratuita:**
- Google Data Studio (funcionalidad limitada)

**Ventaja de Dash:** Gratuito, sin limitaciones, control total con código Python.

---

## 12. Estructura de un Dashboard con Dash

### Importaciones Necesarias:

```python
import dash
import dash_core_components as dcc  # Controles disponibles en Dash
import dash_html_components as html  # Elementos para mostrar en pantalla
import plotly.graph_objs as go  # Gráficos de plotly
import pandas as pd
```

### Definir el Diseño (Layout):

El **layout** es la parte gráfica que muestra todos los gráficos y controles del dashboard.

```python
# Definir estilos externos
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Crear aplicación Dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Definir layout
app.layout = html.Div(children=[
    # Contenido del dashboard aquí
])
```

### Ejemplo Completo: Dashboard de Función Lineal

```python
#!/usr/bin/python

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# Definir el diseño
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[  
    # Encabezado
    html.H1(children='Función lineal'),    
    
    # Gráfico
    dcc.Graph(
        figure={
            'data': [
                go.Scatter(
                    x=pd.Series(range(-100, 100, 1)), 
                    y=pd.Series(range(-100, 100, 1)), 
                    mode='lines',
                    name='linear_func'
                )
            ],
            'layout': go.Layout(
                xaxis={'title': 'x'},
                yaxis={'title': 'y'}
            )
        },      
        id='linear_func_id'
    ),         
])

# Lógica del dashboard
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=3000)
```

---

## 13. Componentes del Layout en Dash

### 1. Encabezado (html.H1)

```python
html.H1(children='Función lineal')
```

Genera el texto del encabezado del dashboard.

### 2. Gráfico (dcc.Graph)

```python
dcc.Graph(
    figure={...},
    id='linear_func_id'
)
```

**Parámetros de dcc.Graph:**
- **figure:** El gráfico en sí
- **id:** Identificador único para interacción con otros elementos

### 3. Parámetro figure

Contiene dos sub-parámetros:

**a) data:** Conjunto de elementos gráficos de plotly

```python
'data': [
    go.Scatter(
        x=pd.Series(range(-100, 100, 1)),  # Valores eje X
        y=pd.Series(range(-100, 100, 1)),  # Valores eje Y
        mode='lines',                       # Línea continua
        name='linear_func'                  # Nombre del gráfico
    )
]
```

**b) layout:** Características visuales del gráfico

```python
'layout': go.Layout(
    xaxis={'title': 'x'},
    yaxis={'title': 'y'}
)
```

### Tipos de mode en go.Scatter:

- `'lines'`: Línea continua
- `'markers'`: Puntos individuales
- `'lines+markers'`: Línea con marcadores

---

## 14. Conexión a SQLite en Dashboards

### ¿Por qué SQLite?

SQLite es un SGBD (Sistema de Gestión de Bases de Datos) minimalista ideal para dashboards:
- Contiene solo un archivo
- No requiere servidor
- No necesita usuario ni contraseña
- Perfecto para bases de datos pequeñas

### Conexión a SQLite:

```python
from sqlalchemy import create_engine

engine = create_engine('sqlite:///games.db', echo=False)
```

**Características:**
- String de conexión simple: solo ruta al archivo
- No requiere dirección IP, puerto, usuario o contraseña
- El archivo `.db` se crea automáticamente si no existe

### Diferencia con PostgreSQL:

```python
# PostgreSQL (requiere muchos parámetros)
engine = create_engine('postgresql://user:pwd@localhost:5432/dbname')

# SQLite (solo ruta al archivo)
engine = create_engine('sqlite:///games.db')
```

---

## 15. Lógica del Dashboard

### Ejecutar el Servidor:

```python
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=3000)
```

**Parámetros:**
- **host='0.0.0.0':** Permite acceso desde cualquier dirección IP
- **port=3000:** Puerto donde se ejecuta el dashboard

### Acceso al Dashboard:

Una vez ejecutado, el dashboard estará disponible en:
```
http://localhost:3000
```

---

## 16. Flujo de Trabajo: Dashboards y Pipelines

### Relación entre Dashboards y Automatización:

1. **Pipeline ETL:** Extrae, transforma y carga datos automáticamente
2. **Base de Datos:** Almacena datos actualizados
3. **Dashboard:** Lee datos de la BD y los visualiza
4. **Actualización:** Dashboard se refresca automáticamente

### Ejemplo de Flujo Completo:

```
Fuentes de datos → Pipeline ETL (programado) → 
Base de datos actualizada → Dashboard Dash → 
Visualización en navegador web
```

### Cuándo Necesitas un Dashboard:

- Informes que se solicitan regularmente
- Métricas que cambian con frecuencia
- Necesidad de filtrar datos interactivamente
- Toma de decisiones basada en datos actuales

**Ejemplo:** Si cada semana te piden calcular LTV para canales publicitarios, definitivamente necesitas un dashboard.

---

## Notas de Troubleshooting

### Si el Dashboard no Inicia:

1. Revisa la pestaña de terminal
2. Verifica que todos los paquetes estén instalados:
   ```bash
   pip install dash dash-core-components dash-html-components plotly pandas sqlalchemy
   ```
3. Confirma que el puerto no esté ocupado
4. Revisa errores de sintaxis en el código

---

## 17. Ejemplos Prácticos de Dashboards

### Archivos de Ejemplo Creados:

Se han creado **3 scripts de ejemplo** con diferentes niveles de complejidad:

#### 1. `dashboard_ejemplo_simple.py`
- Dashboard básico con función lineal
- Estructura mínima de Dash
- Ideal para aprendizaje inicial

#### 2. `dashboard_ejemplo_multiple.py`
- Múltiples gráficos en un solo dashboard
- Layout con columnas (inline-block)
- Funciones matemáticas variadas
- Gráficos de líneas y barras

#### 3. `dashboard_con_datos.py`
- Dashboard profesional completo
- Métricas clave (KPIs) visibles
- Gráfico de áreas apiladas
- Datos simulados de videojuegos
- Diseño con estilos CSS personalizados

### Cómo Ejecutar un Dashboard:

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Ejecutar el script
python dashboard_ejemplo_simple.py

# 3. Abrir navegador en:
http://localhost:3000
```

### Estructura de Carpetas del Proyecto:

```
Sprint 12/
├── MEMORIA_SPRINT_AUTOMATIZACION.md    # Documento con todos los conceptos
├── README_DASHBOARDS.md                # Guía de uso de dashboards
├── requirements.txt                    # Dependencias del proyecto
├── dashboard_ejemplo_simple.py         # Ejemplo básico
├── dashboard_ejemplo_multiple.py       # Ejemplo intermedio
├── dashboard_con_datos.py             # Ejemplo avanzado
├── datasets/                           # Carpeta de datos
└── notebook.ipynb                      # Jupyter notebook
```

---

## 18. Componentes HTML más Usados en Dash

### Elementos de Texto:
```python
html.H1()    # Encabezado nivel 1
html.H2()    # Encabezado nivel 2
html.H3()    # Encabezado nivel 3
html.P()     # Párrafo
html.Span()  # Texto inline
```

### Contenedores:
```python
html.Div()      # Contenedor genérico (como <div> en HTML)
html.Section()  # Sección
html.Header()   # Encabezado de página
html.Footer()   # Pie de página
```

### Layouts con Estilos:
```python
# Layout de dos columnas
html.Div([
    html.Div([...], style={'width': '48%', 'display': 'inline-block'}),
    html.Div([...], style={'width': '48%', 'float': 'right'}),
])
```

---

## 19. Tipos de Gráficos en Plotly

### Gráfico de Líneas:
```python
go.Scatter(
    x=datos_x,
    y=datos_y,
    mode='lines',              # 'lines', 'markers', 'lines+markers'
    name='Nombre',
    line=dict(color='blue', width=2)
)
```

### Gráfico de Barras:
```python
go.Bar(
    x=categorias,
    y=valores,
    name='Nombre',
    marker=dict(color='#3498db')
)
```

### Gráfico de Áreas Apiladas:
```python
go.Scatter(
    x=datos_x,
    y=datos_y,
    mode='lines',
    stackgroup='one',          # Apilar gráficos
    fillcolor='rgba(52, 152, 219, 0.7)'
)
```

### Gráfico de Dispersión:
```python
go.Scatter(
    x=datos_x,
    y=datos_y,
    mode='markers',
    marker=dict(size=10, color='blue')
)
```

### Gráfico de Pastel (Pie):
```python
go.Pie(
    labels=categorias,
    values=valores,
    hole=0.3                   # Para donut chart
)
```

---

## 20. Estilos CSS en Dash

### Propiedades Comunes:

```python
style={
    # Texto
    'textAlign': 'center',           # left, right, center, justify
    'color': '#2c3e50',              # Color del texto
    'fontSize': 16,                  # Tamaño de fuente (px)
    'fontWeight': 'bold',            # normal, bold
    
    # Fondo
    'backgroundColor': '#ecf0f1',    # Color de fondo
    
    # Espaciado
    'padding': 20,                   # Espaciado interno (px)
    'margin': '10px 20px',           # Espaciado externo
    'marginTop': 30,                 # Margen superior
    'marginBottom': 30,              # Margen inferior
    
    # Dimensiones
    'width': '48%',                  # Ancho
    'height': 400,                   # Alto (px)
    
    # Diseño
    'display': 'inline-block',       # inline, block, inline-block, flex
    'float': 'right',                # left, right
    'borderRadius': 10,              # Bordes redondeados
}
```

### Paleta de Colores Recomendada:

| Color | Código Hex | Uso |
|-------|------------|-----|
| Azul | `#3498db` | Información, datos positivos |
| Rojo | `#e74c3c` | Alertas, datos negativos |
| Verde | `#2ecc71` | Éxito, crecimiento |
| Naranja | `#f39c12` | Advertencias, neutro |
| Morado | `#9b59b6` | Creatividad, destacar |
| Gris Oscuro | `#2c3e50` | Texto principal |
| Gris Claro | `#ecf0f1` | Fondos, secciones |

---

## 21. Parámetros Importantes de Layout en Gráficos

### Configuración de Ejes:

```python
go.Layout(
    xaxis={
        'title': 'Eje X',
        'range': [0, 100],
        'showgrid': True,
        'gridcolor': '#ddd'
    },
    yaxis={
        'title': 'Eje Y',
        'range': [0, 1000],
        'showgrid': True
    }
)
```

### Configuración General:

```python
go.Layout(
    title='Título del Gráfico',
    hovermode='closest',           # 'x', 'y', 'closest', 'x unified'
    height=500,                    # Alto del gráfico
    showlegend=True,               # Mostrar leyenda
    legend=dict(
        orientation='h',           # 'v' (vertical) o 'h' (horizontal)
        x=0.5,
        y=1.1
    )
)
```

---

## 22. Tips y Buenas Prácticas

### 1. Organización del Código:
- Separa la lógica de datos del layout
- Usa variables para colores consistentes
- Comenta secciones importantes

### 2. Performance:
- Limita el número de puntos en gráficos (< 10,000)
- Usa `sample()` para datasets grandes
- Considera usar `dcc.Interval` para actualizaciones automáticas

### 3. Diseño:
- Usa una paleta de colores consistente
- Mantén espaciado uniforme (padding/margin)
- Agrupa elementos relacionados
- Usa títulos descriptivos

### 4. Accesibilidad:
- Colores con buen contraste
- Tamaños de fuente legibles (min 12px)
- Nombres descriptivos en gráficos

---

## 23. Recopilación de Requisitos para Dashboards

### Rol del Analista:

Al crear dashboards, debes convertirte temporalmente en:
- **Analista de negocios:** Entender el problema empresarial
- **Escritor técnico:** Documentar requisitos claramente

### ✅ Checklist: Detalles a Aclarar ANTES de Construir

| # | Aspecto | Pregunta Clave |
|---|---------|----------------|
| 1 | **Problema comercial** | ¿Qué problema debe resolver y quién lo usará? |
| 2 | **Frecuencia de uso** | ¿Con qué frecuencia se consultará? |
| 3 | **Estructura de datos** | ¿Qué KPIs, agrupaciones y cohortes necesitas? |
| 4 | **Tipo de datos** | ¿Valores absolutos, relativos o ambos? |
| 5 | **Fuentes de datos** | ¿De dónde provienen los datos? |
| 6 | **Base de datos** | ¿Dónde se almacenarán datos agregados? |
| 7 | **Frecuencia de actualización** | ¿Cada hora, día, semana? |
| 8 | **Gráficos** | ¿Qué visualizaciones y en qué orden? |
| 9 | **Controles** | ¿Qué filtros e interacciones necesitas? |

---

## 24. Proceso de Recopilación de Requisitos (8 Pasos)

### Paso 1: Identificar el Problema Empresarial 🎯

**Ejemplos de problemas:**
- "Queremos ver cómo las campañas publicitarias influyen en usuarios adquiridos"
- "Queremos ver qué productos se compran con más frecuencia"

**Preguntas críticas:**

#### ¿Es un dashboard la mejor solución?

| Situación | Solución Recomendada |
|-----------|---------------------|
| Cliente consultará **regularmente** | ✅ Dashboard |
| Cliente necesita ver **una sola vez** | ❌ Informe periódico |
| Toma de **decisiones continuas** | ✅ Dashboard |
| Análisis **puntual** | ❌ Reporte |

#### ¿Cuántos dashboards necesitas?

- **Un dashboard:** Un problema comercial específico, datos homogéneos
- **Varios dashboards:** Múltiples problemas comerciales, datos heterogéneos

---

### Paso 2: Determinar Datos Necesarios 📊

**Ejemplos:**

| Objetivo del Dashboard | Datos Requeridos |
|------------------------|------------------|
| LTV, retención y conversión | Datos de sesiones y compras de usuarios |
| Rentabilidad de inversiones | Datos de transacciones y estrategias |
| Efectividad de campañas | Datos de clics, conversiones y costos |
| Análisis de productos | Datos de ventas, inventario y categorías |

---

### Paso 3: Definir Métricas Agregadas 📈

**Estructura típica:**
```
Métrica Principal + Desgloses (Dimensiones)
```

**Ejemplo:**
- **Métricas:** LTV, tasa de conversión, tasa de retención
- **Desgloses:** 
  - Por país
  - Por tipo de dispositivo
  - Por canal publicitario

**Resultado:** Tabla con combinaciones de métricas × dimensiones

---

### Paso 4: Analizar Tipos de Gráficos 📉

**Reglas de diseño:**

1. **Importancia = Espacio**
   - Gráficos más importantes → Más espacio
   - Métricas secundarias → Menor tamaño

2. **Valores Absolutos vs Relativos**

| Tipo | Cuándo Usar | Ejemplo |
|------|-------------|---------|
| **Absolutos** | Ver cantidades reales | Ventas: $50,000 |
| **Relativos** | Ver proporciones/cambios | Ventas: 15% del total |
| **Ambos** | Comparar contexto | $50K (↑15%) |

**Tipos de gráficos comunes:**
- Líneas: Tendencias temporales
- Barras: Comparaciones entre categorías
- Áreas apiladas: Composición a lo largo del tiempo
- Pie/Donut: Distribución porcentual
- Dispersión: Relaciones entre variables

---

### Paso 5: Definir Controles y Filtros 🎛️

**Filtros esenciales:**

#### Filtro de Tiempo (casi siempre necesario):
```python
# Ejemplos de controles de tiempo
- Selector de rango de fechas
- Botones: Hoy | Esta semana | Este mes | Este año
- Deslizador temporal
```

#### Otros Filtros (basados en dimensiones):

| Si el dashboard muestra... | Necesitas filtro de... |
|----------------------------|------------------------|
| Ventas por región | Región/País |
| Usuarios por dispositivo | Tipo de dispositivo |
| Conversión por campaña | Canal/Campaña |
| Productos por categoría | Categoría |

**Regla general:** Si una métrica se desglosa por X, probablemente necesitas un filtro para X.

---

### Paso 6: Crear Borrador/Modelo del Dashboard 🎨

**Herramientas para bocetos:**
- Papel y lápiz
- Tabla simple
- Herramientas de diseño (Figma, Sketch)
- Presentación de diapositivas

**Ejemplo de borrador simple:**

```
+---------------------------------------+
|     TÍTULO DEL DASHBOARD              |
+---------------------------------------+
| Descripción breve del propósito       |
+---------------------------------------+
| [KPI 1] | [KPI 2] | [KPI 3] | [KPI 4] |
+---------------------------------------+
| Gráfico Principal                     |
| (Grande - Ocupa 60% del ancho)        |
|                                       |
+-------------------+-------------------+
| Gráfico           | Gráfico           |
| Secundario 1      | Secundario 2      |
| (30% ancho)       | (30% ancho)       |
+-------------------+-------------------+
| Filtros: [Fecha] [Región] [Categoría]|
+---------------------------------------+
```

**Elementos del borrador:**
- Posiciones relativas de gráficos
- Tamaños aproximados
- Tipos de visualizaciones
- Ubicación de filtros y controles

---

### Paso 7: Documentar Requisitos Técnicos 📝

**Características del documento:**

✅ **Debe ser:**
- Breve y conciso
- Claro y específico
- Acordado por todas las partes
- Fácil de entender

❌ **NO debe ser:**
- Excesivamente burocrático
- Largo y complejo
- Ambiguo o vago

**Formato del documento (flexible):**
- Documento formal (Word/Google Docs)
- Notas estructuradas
- Presentación (PowerPoint/Slides)
- Wiki/Confluence
- Ticket en sistema de gestión (JIRA, Trello)

**Contenido típico:**
1. Objetivo del dashboard
2. Usuarios principales
3. Fuentes de datos
4. Métricas y KPIs
5. Desgloses y filtros
6. Boceto visual
7. Frecuencia de actualización
8. Consideraciones especiales

---

### Paso 8: Coordinar con Equipo Técnico 👥

**Con administradores de bases de datos:**
- ¿Qué fuentes de datos puedo usar?
- ¿Necesito permisos especiales?
- ¿Hay limitaciones de acceso?

**Con ingenieros de datos:**
- ¿Qué base de datos almacenará los datos agregados?
- ¿En qué servidor se ejecutará el script del dashboard?
- ¿Cómo se programarán las actualizaciones?
- ¿Hay pipelines ETL existentes que pueda usar?

---

## 25. Elementos Básicos de Todo Dashboard

### 1. Encabezado 📌

**Propósito:** Decir al usuario qué ilustra el dashboard

**Ejemplos:**
```python
html.H1('Dashboard de Ventas Mensuales por Región')
html.H1('Análisis de Retención de Usuarios')
html.H1('Rendimiento de Campañas Publicitarias')
```

**Buenas prácticas:**
- Título descriptivo y específico
- Evitar títulos genéricos ("Dashboard", "Análisis")
- Incluir período si es relevante
- Usar tamaño de fuente prominente

---

### 2. Descripción del Dashboard 📄

**Propósito:** Explicar brevemente:
- Qué problema resuelve
- Cómo funciona (si hay algo inusual)
- Notas importantes para el usuario

**Ejemplo:**
```python
html.Div(
    children='''
    Este dashboard muestra las ventas mensuales desglosadas por región 
    y categoría de producto. Los datos se actualizan diariamente a las 
    6:00 AM. Use los filtros para explorar períodos específicos.
    ''',
    style={'padding': 20, 'backgroundColor': '#f0f0f0'}
)
```

**Qué incluir:**
- Propósito principal (1 frase)
- Frecuencia de actualización
- Instrucciones de uso básicas
- Notas importantes o limitaciones

---

### 3. Gráficos y Diagramas 📊

**Jerarquía visual:**

```
Métricas Clave (KPIs)
    ↓
Gráfico Principal
    ↓
Gráficos Secundarios
    ↓
Gráficos de Detalle
```

**Organización típica:**
- **Fila superior:** KPIs/Métricas resumen
- **Fila media:** Gráficos principales (grandes)
- **Fila inferior:** Gráficos de soporte (pequeños)

---

### 4. Controles 🎛️

**Tipos de controles en Dash:**

#### Controles de Entrada:
```python
# Selector de rango de fechas
dcc.DatePickerRange(id='date-range')

# Dropdown (menú desplegable)
dcc.Dropdown(
    id='region-dropdown',
    options=[{'label': 'Norte', 'value': 'N'},
             {'label': 'Sur', 'value': 'S'}]
)

# Slider (deslizador)
dcc.Slider(min=0, max=100, value=50)

# Radio buttons
dcc.RadioItems(
    options=[{'label': 'Diario', 'value': 'D'},
             {'label': 'Mensual', 'value': 'M'}]
)

# Checklist
dcc.Checklist(
    options=[{'label': 'Mostrar tendencia', 'value': 'trend'}]
)
```

**Ubicación de controles:**
- **Arriba del dashboard:** Filtros globales
- **Junto a gráficos:** Controles específicos
- **Barra lateral:** Muchos filtros/opciones

---

## 26. Dashboard vs Informe Periódico

### ¿Cuándo usar cada uno?

| Criterio | Dashboard | Informe Periódico |
|----------|-----------|-------------------|
| **Frecuencia de consulta** | Regular, continua | Ocasional, una vez |
| **Actualización** | Automática (tiempo real) | Manual o programada |
| **Interactividad** | Alta (filtros, clicks) | Baja (estático) |
| **Usuarios** | Múltiples, autoservicio | Específicos, audiencia fija |
| **Toma de decisiones** | Continua, operativa | Puntual, estratégica |
| **Costo de desarrollo** | Alto (inicial) | Bajo |
| **Costo de mantenimiento** | Bajo (automatizado) | Alto (manual) |

**Ejemplo de decisión:**

❓ **Pregunta del cliente:** "Quiero ver cómo están las ventas este mes"

✅ **Si pregunta cada semana/día:** → Dashboard  
❌ **Si pregunta solo una vez:** → Informe

---

## 27. Ejemplo Práctico: Requisitos de Dashboard

### Caso: Dashboard de E-commerce

**Problema comercial:**
"Necesitamos monitorear el rendimiento de ventas en tiempo real para tomar decisiones sobre inventario y promociones"

**Requisitos recopilados:**

#### 1. Usuarios:
- Gerente de ventas (usuario principal)
- Equipo de marketing (secundario)

#### 2. Frecuencia de uso:
- Diaria (cada mañana)
- En tiempo real durante eventos especiales

#### 3. KPIs principales:
- Ventas totales del día/mes
- Número de pedidos
- Ticket promedio
- Tasa de conversión

#### 4. Desgloses:
- Por categoría de producto
- Por región
- Por canal (web, móvil, tienda física)

#### 5. Gráficos:
- KPIs en tarjetas (parte superior)
- Ventas por hora (líneas)
- Top 10 productos (barras)
- Distribución por categoría (pie)
- Mapa de ventas por región

#### 6. Filtros:
- Rango de fechas
- Categoría de producto
- Región
- Canal de venta

#### 7. Fuentes de datos:
- Base de datos de transacciones (PostgreSQL)
- Sistema de inventario (API)

#### 8. Actualización:
- Cada 15 minutos

---

## 28. Creación de Gráficos Básicos en Dash

### Librerías Principales

```python
import dash_html_components as html  # Componentes HTML
import dash_core_components as dcc   # Gráficos y controles
import plotly.graph_objs as go       # Tipos de gráficos
```

| Librería | Alias | Propósito |
|----------|-------|-----------|
| `dash_html_components` | `html` | Etiquetas HTML (H1, Img, Label, etc.) |
| `dash_core_components` | `dcc` | Gráficos y controles interactivos |
| `plotly.graph_objs` | `go` | Tipos de gráficos de Plotly |

---

### Componentes HTML Básicos

#### Elementos de Texto:
```python
html.H1(children='Título Principal')     # Encabezado nivel 1
html.H2(children='Subtítulo')            # Encabezado nivel 2
html.Label('Etiqueta de texto')          # Etiqueta
html.P('Párrafo de texto')               # Párrafo
```

#### Otros Elementos:
```python
html.Img(src='url_de_imagen')            # Imagen
html.Br()                                 # Salto de línea
html.Div(children=[...])                  # Contenedor
```

**Documentación completa:** https://dash.plot.ly/dash-html-components

---

### Componente dcc.Graph - Estructura

```python
dcc.Graph(
    figure={
        'data': [...],      # Lista de gráficos
        'layout': go.Layout(...)  # Configuración visual
    },
    id='nombre_unico'       # ID para interactividad
)
```

#### Parámetros de dcc.Graph:

| Parámetro | Descripción | Requerido |
|-----------|-------------|-----------|
| `figure` | Diccionario con datos y layout | ✅ Sí |
| `id` | Identificador único del gráfico | ✅ Sí (para callbacks) |

#### Estructura de figure:

```python
figure = {
    'data': [
        go.Scatter(...),  # Gráfico 1
        go.Bar(...),      # Gráfico 2
        # Más gráficos...
    ],
    'layout': go.Layout(
        xaxis={'title': 'Eje X'},
        yaxis={'title': 'Eje Y'},
        title='Título del Gráfico'
    )
}
```

---

## 29. Tipos de Gráficos en Plotly

### 1. go.Scatter - Líneas, Áreas y Dispersión 📈

**Usos:**
- Gráficos de líneas
- Gráficos de áreas apiladas
- Diagramas de dispersión

#### Parámetros Principales:

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `x` | pd.Series | Valores del eje X |
| `y` | pd.Series | Valores del eje Y |
| `mode` | str | 'lines', 'markers', 'lines+markers' |
| `stackgroup` | str | 'one' para apilar áreas |
| `name` | str | Nombre para la leyenda |

#### Ejemplo 1: Gráfico de Líneas

```python
go.Scatter(
    x=pd.Series(range(-10, 10)),
    y=pd.Series(range(-10, 10)),
    mode='lines',
    name='Línea simple'
)
```

#### Ejemplo 2: Áreas Apiladas

```python
# Crear múltiples áreas apiladas
data = []
for continent in continents:
    current = df.query('Entity == @continent')
    data += [
        go.Scatter(
            x=current['Year'],
            y=current['Population'],
            mode='lines',
            stackgroup='one',  # CLAVE para apilar
            name=continent
        )
    ]
```

#### Ejemplo 3: Diagrama de Dispersión

```python
go.Scatter(
    x=current['Year'],
    y=current['Population'],
    mode='markers',  # Solo puntos
    name='Dispersión'
)
```

#### Modos Disponibles:

| Mode | Resultado |
|------|-----------|
| `'lines'` | Solo líneas continuas |
| `'markers'` | Solo puntos/marcadores |
| `'lines+markers'` | Líneas con puntos |

---

### 2. go.Bar - Gráficos de Barras 📊

**Usos:**
- Comparar categorías
- Mostrar distribuciones
- Barras apiladas o agrupadas

#### Parámetros Principales:

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `x` | pd.Series | Categorías (eje X) |
| `y` | pd.Series | Valores (eje Y) |
| `name` | str | Nombre para la leyenda |
| `barmode` | str | 'group' o 'stack' (en Layout) |

#### Ejemplo: Barras Agrupadas vs Apiladas

```python
# Preparar datos
data = [
    go.Bar(x=df['Entity'], y=df['Rural'], name='Rural'),
    go.Bar(x=df['Entity'], y=df['Urban'], name='Urban')
]

# Barras agrupadas (lado a lado)
dcc.Graph(
    figure={
        'data': data,
        'layout': go.Layout(
            barmode='group',  # Lado a lado
            xaxis={'title': 'Continente'},
            yaxis={'title': 'Población'}
        )
    }
)

# Barras apiladas (una sobre otra)
dcc.Graph(
    figure={
        'data': data,
        'layout': go.Layout(
            barmode='stack',  # Apiladas
            xaxis={'title': 'Continente'},
            yaxis={'title': 'Población'}
        )
    }
)
```

**⚠️ Importante:** `barmode` se especifica en `go.Layout`, NO en `go.Bar`

---

### 3. go.Pie - Gráficos Circulares 🥧

**Usos:**
- Mostrar proporciones
- Distribución porcentual
- Composición de un total

#### Parámetros Principales:

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `labels` | pd.Series | Nombres de categorías |
| `values` | pd.Series | Valores de categorías |
| `name` | str | Nombre del gráfico |
| `hole` | float | 0-1, crea donut chart |

#### Ejemplo Básico:

```python
go.Pie(
    labels=df['Entity'],      # Nombres (ej: continentes)
    values=df['Population'],  # Valores (ej: población)
    name='Distribución'
)
```

#### Ejemplo Donut Chart:

```python
go.Pie(
    labels=productos,
    values=ventas,
    hole=0.4,  # Agujero en el centro (40%)
    name='Ventas por Producto'
)
```

---

### 4. go.Box - Diagramas de Caja 📦

**Usos:**
- Mostrar distribución de datos
- Identificar outliers
- Comparar distribuciones entre grupos

#### Parámetros Principales:

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `y` | pd.Series | Valores de la variable |
| `name` | str | Nombre del grupo |
| `x` | pd.Series | Categorías (opcional) |

#### Ejemplo: Múltiples Boxplots

```python
boxplot_data = []
for country in ['Russia', 'Germany', 'Finland', 'Japan', 'France']:
    current = df.query('Entity == @country')
    boxplot_data += [
        go.Box(
            y=current['Urban'],
            name=country
        )
    ]

dcc.Graph(
    figure={
        'data': boxplot_data,
        'layout': go.Layout(
            xaxis={'title': 'País'},
            yaxis={'title': 'Nivel de Urbanización'}
        )
    }
)
```

---

### 5. go.Table - Tablas 📋

**Usos:**
- Mostrar datos tabulares
- Reportes detallados
- Datos exactos complementarios a gráficos

#### Parámetros Principales:

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `header` | dict | Encabezados de columnas |
| `cells` | dict | Celdas de la tabla |

#### Estructura de header:

```python
header = {
    'values': ['<b>Columna 1</b>', '<b>Columna 2</b>'],
    'fill_color': 'lightgrey',
    'align': 'center'
}
```

#### Estructura de cells:

```python
cells = {
    'values': df.T.values  # Transponer DataFrame
}
```

#### Ejemplo Completo:

```python
go.Table(
    header={
        'values': [
            '<b>País o Continente</b>',
            '<b>Año</b>',
            '<b>% Población Urbana</b>'
        ],
        'fill_color': 'lightgrey',
        'align': 'center'
    },
    cells={
        'values': urbanization_table.T.values
    }
)
```

#### Transposición de DataFrame:

**DataFrame original:**
```
Name     Apples  Bananas  Cheese
Anna     1       5        8
Helen    10      19       22
```

**DataFrame transpuesto (df.T):**
```
         Anna    Helen
Apples   1       10
Bananas  5       19
Cheese   8       22
```

**Uso:** `df.T.values` facilita pasar datos a las celdas de la tabla

---

## 30. Creación Dinámica de Gráficos

### Patrón Común: Bucle para Múltiples Series

```python
# Crear lista vacía
data = []

# Iterar sobre categorías
for category in df['Category'].unique():
    # Filtrar datos para categoría actual
    current = df.query('Category == @category')
    
    # Agregar gráfico a la lista
    data += [
        go.Scatter(
            x=current['X'],
            y=current['Y'],
            mode='lines',
            name=category
        )
    ]

# Usar en el dashboard
dcc.Graph(
    figure={
        'data': data,
        'layout': go.Layout(
            xaxis={'title': 'Eje X'},
            yaxis={'title': 'Eje Y'}
        )
    },
    id='mi_grafico'
)
```

### Ejemplo Práctico: Población por Continente

```python
# Preparar datos
population_by_year_lines = []

for continent in population_by_year['Entity'].unique():
    current = population_by_year.query('Entity == @continent')
    population_by_year_lines += [
        go.Scatter(
            x=current['Year'],
            y=current['Population'],
            mode='lines',
            name=continent
        )
    ]

# Mostrar en dashboard
app.layout = html.Div([
    html.H1('Población por Continente'),
    dcc.Graph(
        figure={
            'data': population_by_year_lines,
            'layout': go.Layout(
                xaxis={'title': 'Año'},
                yaxis={'title': 'Población'}
            )
        },
        id='population_chart'
    )
])
```

---

## 31. Parámetros Avanzados de go.Layout

### Configuración Completa:

```python
go.Layout(
    # Títulos
    title='Título del Gráfico',
    
    # Ejes
    xaxis={
        'title': 'Eje X',
        'showgrid': True,
        'gridcolor': '#ddd',
        'range': [0, 100]
    },
    yaxis={
        'title': 'Eje Y',
        'showgrid': True,
        'gridcolor': '#ddd'
    },
    
    # Leyenda
    showlegend=True,
    legend={
        'orientation': 'h',  # 'h' horizontal, 'v' vertical
        'x': 0.5,
        'y': 1.1
    },
    
    # Hover
    hovermode='closest',  # 'x', 'y', 'closest', False
    
    # Tamaño
    height=500,
    width=800,
    
    # Colores de fondo
    plot_bgcolor='#f8f9fa',
    paper_bgcolor='white',
    
    # Barras (solo para go.Bar)
    barmode='group'  # 'group' o 'stack'
)
```

---

## 32. Resumen de Tipos de Gráficos

| Tipo | Componente | Uso Principal | Parámetros Clave |
|------|------------|---------------|------------------|
| **Líneas** | `go.Scatter` | Tendencias temporales | `mode='lines'` |
| **Áreas apiladas** | `go.Scatter` | Composición temporal | `stackgroup='one'` |
| **Dispersión** | `go.Scatter` | Relaciones entre variables | `mode='markers'` |
| **Barras** | `go.Bar` | Comparar categorías | `barmode` en Layout |
| **Circular** | `go.Pie` | Proporciones | `labels`, `values` |
| **Caja** | `go.Box` | Distribuciones | `y` valores |
| **Tabla** | `go.Table` | Datos tabulares | `header`, `cells` |

---

## 33. Ejemplo Completo: Dashboard con Múltiples Gráficos

```python
#!/usr/bin/python
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# Cargar datos
df = pd.read_csv('datos.csv')

# Preparar gráficos
lineas = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='Línea')]
barras = [go.Bar(x=df['cat'], y=df['val'], name='Barras')]
pie = [go.Pie(labels=df['labels'], values=df['values'])]

# Crear app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Layout
app.layout = html.Div([
    html.H1('Dashboard Completo'),
    
    # Gráfico de líneas
    html.Label('Gráfico de Líneas:'),
    dcc.Graph(
        figure={'data': lineas, 'layout': go.Layout(...)},
        id='lineas'
    ),
    
    # Gráfico de barras
    html.Label('Gráfico de Barras:'),
    dcc.Graph(
        figure={'data': barras, 'layout': go.Layout(...)},
        id='barras'
    ),
    
    # Gráfico circular
    html.Label('Gráfico Circular:'),
    dcc.Graph(
        figure={'data': pie, 'layout': go.Layout()},
        id='pie'
    )
])

# Ejecutar
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=3000)
```

---

## 34. Recursos y Referencias

### Documentación Oficial:
- **Dash HTML Components:** https://dash.plot.ly/dash-html-components
- **Plotly Python:** https://plot.ly/python/
- **Galería de Dashboards:** https://dash-gallery.plotly.host/Portal/

### Tips de Uso:
1. Siempre usa `pd.Series` para x e y en gráficos
2. Crea gráficos dinámicamente en bucles cuando sea posible
3. Usa nombres descriptivos en el parámetro `name`
4. Transpón DataFrames con `.T` para tablas
5. Experimenta con parámetros avanzados para personalizar

---

## 109. Construir Dashboards en Tableau

### **¿Qué es un Dashboard?**

Un **dashboard** en Tableau es una colección de múltiples visualizaciones (hojas) en una sola página interactiva.

**Propósito:**
- Mostrar múltiples métricas relacionadas
- Permitir análisis comparativo
- Crear narrativa visual coherente
- Facilitar toma de decisiones

**Componentes:**
```
┌────────────────────────────────────┐
│  TÍTULO DEL DASHBOARD       [Filter]│ ← Header
├────────────────────────────────────┤
│  ┌──────────────────────────────┐  │
│  │   Gráfico Principal          │  │ ← Main viz
│  └──────────────────────────────┘  │
├────────────────────────────────────┤
│  ┌──────────┐    ┌──────────────┐  │
│  │ Gráfico 2│    │  Gráfico 3   │  │ ← Supporting
│  └──────────┘    └──────────────┘  │
└────────────────────────────────────┘
```

---

## 110. Planificación: Borradores de Dashboards

### **Paso 1: Diseñar Borrador (Wireframe)**

Antes de construir, **siempre crea un borrador en papel o herramienta de diseño**.

**Ejemplo de Borrador:**
```
┌────────────────────────────────────────────┐
│  Dashboard: Población Mundial    [Año: ▼] │ ← Parte Superior
├────────────────────────────────────────────┤
│                                            │
│     GRÁFICO DE ÁREAS APILADAS              │ ← Parte Central
│     (Crecimiento de población)             │
│                                            │
├────────────────────────────────────────────┤
│  ┌───────────────────┐ ┌─────────────────┐│
│  │ % Población       │ │ Urbano vs Rural ││ ← Parte Inferior
│  │ (por país)        │ │ (líneas)        ││
│  └───────────────────┘ └─────────────────┘│
└────────────────────────────────────────────┘

ESTRUCTURA:
├─ Header (Título + Filtro)
├─ Main (Gráfico principal - ancho completo)
└─ Details (2 gráficos lado a lado - 50/50)
```

### **Elementos del Ejemplo:**

| Sección | Contenido | Proporción |
|---------|-----------|------------|
| **Superior** | Título + Filtro de año | ~10% altura |
| **Central** | Gráfico de áreas apiladas (población total) | ~50% altura |
| **Inferior** | 2 gráficos lado a lado (% población + urbano/rural) | ~40% altura |

### **Preguntas de Diseño:**

```
Antes de construir, responde:

1. ¿Cuál es el mensaje principal?
   → "Evolución de la población mundial"

2. ¿Qué gráfico es MÁS importante?
   → Áreas apiladas (más grande)

3. ¿Qué gráficos son de apoyo?
   → % población y urbano/rural (más pequeños)

4. ¿Qué filtros son necesarios?
   → Año (para temporal)

5. ¿Cómo se organizan los elementos?
   → Vertical: Header → Main → Details
```

---

## 111. Preparar Gráficos para el Dashboard

### **Crear Gráfico: "% de Población"**

Antes de construir el dashboard, necesitamos crear un gráfico adicional que muestre la población como **porcentaje del total**.

**Paso 1: Duplicar Hoja Existente**

1. Clic derecho en hoja **"Stacked Area"** (o similar)
2. **"Duplicate"**
3. Renombrar a **"% Población"**

**Paso 2: Convertir a Porcentaje**

1. En la nueva hoja, ubica **"Population"** en el área de **Filas**
2. Clic derecho en **"SUM(Population)"**
3. **"Quick Table Calculation"** → **"Percent of Total"**

**Resultado Inicial (INCORRECTO):**
```
100% |▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓| 
 80% |▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    |
 60% |▓▓▓▓▓▓▓▓▓▓▓▓▓▓          |
 40% |▓▓▓▓▓▓▓▓                |
 20% |▓▓▓▓                    |
  0% |________________________|
     1950  1970  1990  2010

Problema: % calculado sobre TODA la tabla
         (no por año)
```

**Paso 3: Ajustar Cálculo**

1. Clic derecho en **"SUM(Population)"** (en Filas)
2. **"Compute Using"** → **"Table (down)"**

**Resultado Final (CORRECTO):**
```
100% |████████████████████████| China
 80% |████████████████████    | India
 60% |████████████            | USA
 40% |████████                | Indonesia
 20% |████                    | Brasil
  0% |________________________| Otros
     1950  1970  1990  2010

Ahora: % calculado por AÑO
       (cada columna suma 100%)
```

### **Por Qué "Table (down)"?**

```
COMPUTE USING:

Table (across):          Table (down): ⭐
  Calcula % por país      Calcula % por año
  (horizontal)            (vertical)
  
  China:                  1950:
  1950: 10%                China: 22%
  1970: 15%                India: 15%
  ...   ...                USA: 7%
                           Total: 100%
  
❌ NO queremos esto      ✅ SÍ queremos esto
```

---

## 112. Organizar y Nombrar Hojas

### **Preparar Hojas para Dashboard:**

Antes de construir dashboard, organiza tus hojas.

**Paso 1: Renombrar Hojas**

Nombres descriptivos y profesionales:

| Nombre Original | Nombre Final | Propósito |
|-----------------|--------------|-----------|
| Sheet 1 | **Población** | Gráfico de áreas apiladas |
| Sheet 2 | **% Población** | Porcentaje por país |
| Sheet 3 | **Urbano vs Rural** | Líneas urbano/rural |

**Cómo Renombrar:**
1. Doble clic en pestaña de hoja
2. Escribir nuevo nombre
3. Enter

**Paso 2: Ordenar Hojas**

Arrastra pestañas para ordenar lógicamente:
```
┌─────┬──────────────┬────────────────┬──────────┐
│ 🏠  │ Población    │ % Población    │ Urbano   │
└─────┴──────────────┴────────────────┴──────────┘
         ↑ Principal    ↑ Secundario    ↑ Terciario
```

### **Preparar Tooltips (Opcional pero Recomendado):**

**Mejorar información al pasar cursor:**

1. Clic en **"Tooltip"** en tarjeta de Marcas
2. Editar formato:

```
┌─────────────────────────────────────┐
│ Edit Tooltip                        │
├─────────────────────────────────────┤
│ <b><Sheet-value></b>                │
│                                     │
│ Year: <YEAR(Year)>                  │
│ Population: <SUM(Population)>       │
│ % of Total: <% of Total>            │
│                                     │
│ [✓] Include command buttons         │
│ [✓] Allow selection by category     │
└─────────────────────────────────────┘
```

**Resultado:**
```
Cuando usuario pasa cursor sobre gráfico:

┌──────────────────────────┐
│ China                    │
│ Year: 2020               │
│ Population: 1,439,323,776│
│ % of Total: 18.5%        │
└──────────────────────────┘
```

---

## 113. Crear Nuevo Dashboard

### **Paso 1: Iniciar Dashboard**

**Método 1:** Icono en la parte inferior
```
[Hojas]  [+]  [📊] ← Click aquí
              ↑
         Nuevo Dashboard
```

**Método 2:** Menú
- Dashboard → New Dashboard

**Método 3:** Atajo
- `Ctrl + M` (Windows)
- `Cmd + M` (Mac)

### **Resultado:**
```
┌────────────────────────────────────────┐
│ Dashboard 1                            │
├────────────────────────────────────────┤
│                                        │
│         [Arrastra hojas aquí]          │
│                                        │
│                                        │
└────────────────────────────────────────┘
```

---

## 114. Interface de Edición de Dashboard

### **Áreas Principales:**

```
┌─────────────────────────────────────────────────────┐
│ [Archivo] [Data] [Dashboard] [3]                   │
├──────┬──────────────────────────────────────────────┤
│  1   │                                              │
│ Size │                                              │
│ ──── │              2. ÁREA DE EDICIÓN              │
│      │           (Arrastra elementos aquí)          │
│ Auto │                                              │
│      │                                              │
│ ──── │                                              │
│  3   │                                              │
│Sheets│                                              │
│ ──── │                                              │
│□Pop. │                                              │
│□% P. │                                              │
│□Urb. │                                              │
│ ──── │                                              │
│  4   │                                              │
│Objs  │                                              │
│ ──── │                                              │
│[H]   │                                              │
│[V]   │                                              │
│[Text]│                                              │
│[Img] │                                              │
│[Nav] │                                              │
└──────┴──────────────────────────────────────────────┘

ÁREAS:
1. Control de Tamaño
2. Área de Edición (Canvas)
3. Lista de Hojas/Visualizaciones
4. Objetos Adicionales
```

### **Descripción de Áreas:**

| Área | Nombre | Función | Elementos |
|------|--------|---------|-----------|
| **1** | Size | Ajustar tamaño del dashboard | Desktop, Tablet, Phone, Custom |
| **2** | Canvas | Área de trabajo principal | Donde se construye el dashboard |
| **3** | Sheets | Lista de visualizaciones disponibles | Todas las hojas creadas |
| **4** | Objects | Elementos adicionales | Horizontal, Vertical, Text, Image, etc. |

---

## 115. Ajustar Tamaño del Dashboard

### **Opciones de Tamaño:**

**Paso 1: Abrir Selector de Tamaño**

En el panel izquierdo (área 1), clic en **"Size"** dropdown:

```
┌────────────────────────────┐
│ Size:                      │
│ ┌────────────────────────┐ │
│ │ Automatic          ▼   │ │ ⭐ Recomendado
│ └────────────────────────┘ │
│                            │
│ Other options:             │
│ • Desktop (1366 x 768)     │
│ • Laptop (1024 x 768)      │
│ • Tablet (768 x 1024)      │
│ • Phone (320 x 568)        │
│ • Custom                   │
└────────────────────────────┘
```

**Paso 2: Seleccionar "Automatic"**

**Ventajas:**
```
✅ Automatic (Pantalla completa):
   • Se adapta al tamaño de pantalla del usuario
   • Funciona en desktop, tablet, móvil
   • Tableau ajusta elementos automáticamente
   • Mejor para dashboards públicos

❌ Fixed (Tamaño fijo):
   • 1366 x 768 (desktop estándar)
   • 1024 x 768 (laptop)
   • No se adapta a otras pantallas
   • Puede requerir scroll
```

**Resultado:**
```
Automatic:
┌──────────────────────────┐  ← Pantalla grande
│                          │
│    Dashboard completo    │
│                          │
└──────────────────────────┘

┌────────────┐              ← Pantalla pequeña
│ Dashboard  │
│  ajustado  │
└────────────┘
```

---

## 116. Objetos de Contenedor (Containers)

### **Tipos de Contenedores:**

```
HORIZONTAL [H]:             VERTICAL [V]:
┌──────────────────┐        ┌──────────────┐
│ [1]  [2]  [3]    │        │     [1]      │
└──────────────────┘        ├──────────────┤
                            │     [2]      │
Elementos lado a lado      ├──────────────┤
                            │     [3]      │
                            └──────────────┘
                            
                            Elementos apilados
```

### **Crear Estructura del Dashboard:**

**Objetivo:** Dividir dashboard en 3 secciones (Superior, Central, Inferior)

**Paso 1: Agregar Contenedor Vertical**

1. En área de **Objects** (4), selecciona **"Vertical"**
2. Arrastra al área de edición (2)
3. Repite para agregar segundo contenedor

**Resultado:**
```
┌────────────────────────────┐
│   Contenedor Vertical 1    │ ← Superior (Header)
├────────────────────────────┤
│   Contenedor Vertical 2    │ ← Central (Main)
├────────────────────────────┤
│   Contenedor Vertical 3    │ ← Inferior (Details)
└────────────────────────────┘
```

**Indicadores Visuales:**
```
Cuando arrastras un objeto, Tableau muestra:

┌────────────────────────────┐
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░ │ ← Área gris = zona de drop
├────────────────────────────┤
│                            │
│                            │
└────────────────────────────┘

Zonas de drop:
• Arriba: inserta encima
• Abajo: inserta debajo
• Izquierda: inserta a la izquierda
• Derecha: inserta a la derecha
```

---

## 117. Agregar Hojas al Dashboard

### **Paso 1: Agregar Gráfico Principal**

1. En lista de **Sheets** (área 3), selecciona **"Población"**
2. Arrastra al **contenedor central**

**Resultado:**
```
┌────────────────────────────────┐
│  [Vacío]                       │ ← Superior
├────────────────────────────────┤
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │
│ ▓▓  GRÁFICO DE POBLACIÓN   ▓▓ │ ← Central (lleno)
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │
├────────────────────────────────┤
│  [Vacío]                       │ ← Inferior
└────────────────────────────────┘
```

### **Paso 2: Agregar Gráficos de Detalle**

Para la sección inferior, necesitamos **2 gráficos lado a lado**.

**Método:**

1. Arrastra **"% Población"** al contenedor inferior
2. Arrastra **"Urbano vs Rural"** al contenedor inferior **a la derecha**

**Importante:** Observa las zonas de drop:
```
Zona de drop CORRECTA (lado a lado):
┌─────────────┬─────────────┐
│ % Población │   [drop]    │ ← Soltar aquí (derecha)
└─────────────┴─────────────┘

Zona de drop INCORRECTA (uno encima del otro):
┌─────────────────────────┐
│    % Población          │
├─────────────────────────┤ ← NO soltar aquí (abajo)
│      [drop]             │
└─────────────────────────┘
```

**Resultado:**
```
┌────────────────────────────────────┐
│  [Vacío]                           │
├────────────────────────────────────┤
│ ▓▓▓ GRÁFICO DE POBLACIÓN ▓▓▓▓▓▓▓▓ │
├──────────────────┬─────────────────┤
│ % POBLACIÓN      │ URBANO VS RURAL │ ← Lado a lado
└──────────────────┴─────────────────┘
```

---

## 118. Limpiar Leyendas Innecesarias

### **Problema: Leyendas Duplicadas**

Cuando agregas hojas, Tableau **automáticamente agrega leyendas**:

```
ANTES DE LIMPIAR:
┌────────────────────────────────────┐
│ GRÁFICO                ┌─────────┐ │
│                        │ LEYENDA │ │ ← Innecesaria
│                        │ China   │ │
│                        │ India   │ │
│                        │ USA     │ │
│                        └─────────┘ │
└────────────────────────────────────┘
```

### **Eliminar Leyendas:**

**Paso 1: Identificar Leyenda**

Pasa el cursor sobre la leyenda. Aparecerá borde gris.

**Paso 2: Abrir Menú**

Clic en **triángulo** (▼) en la esquina superior derecha de la leyenda:

```
┌─────────────────────┐
│ Country          ▼  │ ← Click aquí
├─────────────────────┤
│ • Floating          │
│ • Remove from...    │ ⭐ Seleccionar
│ • Edit title        │
└─────────────────────┘
```

**Paso 3: Eliminar**

Selecciona **"Remove from Dashboard"**

**Resultado:**
```
DESPUÉS DE LIMPIAR:
┌────────────────────────────────────┐
│ GRÁFICO                            │
│                                    │ ← Sin leyenda
│                                    │    (más espacio)
│                                    │
│                                    │
└────────────────────────────────────┘
```

**⚠️ Cuándo NO Eliminar Leyendas:**

```
✅ ELIMINAR cuando:
   • Colores son obvios (países en mapa)
   • Etiquetas directas en el gráfico
   • Múltiples leyendas idénticas

❌ MANTENER cuando:
   • Colores no son intuitivos
   • Muchas categorías sin etiquetas
   • Categorías deben ser identificables
```

---

## 119. Editar Ejes

### **Problema: Nombres de Ejes Confusos**

Tableau a veces genera nombres automáticos poco claros:

```
MALO:
    Año del año
    │
    │  ▓▓▓
    │  ▓▓
    └──────────────
    
"Año del año" es redundante
```

### **Editar Nombre del Eje:**

**Paso 1: Clic Derecho en Eje**

Clic derecho en el **eje horizontal** del gráfico:

```
┌────────────────────────────┐
│ • Edit Axis...         ⭐  │
│ • Format...                │
│ • Add Reference Line       │
│ • Show Header              │
└────────────────────────────┘
```

**Paso 2: Cambiar Título**

En ventana de edición:

```
┌───────────────────────────────────┐
│ Edit Axis [YEAR(Year)]            │
├───────────────────────────────────┤
│ General                           │
│ ┌───────────────────────────────┐ │
│ │ Title: Año del año            │ │
│ └───────────────────────────────┘ │
│                                   │
│ Cambiar a: "Año"                  │
│                                   │
│ [ ] Include zero                  │
│ [✓] Automatic                     │
│                                   │
│                    [  OK  ] [ X ] │
└───────────────────────────────────┘
```

**Paso 3: Aplicar**

Cerrar ventana con **X** (cambios se guardan automáticamente)

**Resultado:**
```
BUENO:
    Año
    │
    │  ▓▓▓
    │  ▓▓
    └──────────────
    
Claro y conciso ✅
```

**Paso 4: Repetir para Todos los Gráficos**

Hacer lo mismo en:
- Gráfico de población (eje X)
- Gráfico de % población (eje X)
- Gráfico urbano vs rural (eje X)

**Ejes Y también pueden editarse:**
- "SUM(Population)" → "Población (millones)"
- "% of Total" → "Porcentaje"

---

## 120. Agregar Título al Dashboard

### **Paso 1: Agregar Contenedor Superior**

Necesitamos espacio para el título.

1. Arrastra **"Vertical"** container al **tope** del dashboard
2. Asegúrate que quede ENCIMA de todo

**Estructura:**
```
┌────────────────────────────────┐
│  [Nuevo contenedor - vacío]    │ ← Para título + filtro
├────────────────────────────────┤
│  GRÁFICO POBLACIÓN             │
├──────────────────┬─────────────┤
│  % POBLACIÓN     │ URBANO/RURAL│
└──────────────────┴─────────────┘
```

### **Paso 2: Agregar Objeto de Texto**

1. En área de **Objects**, selecciona **"Text"** (icono con "Abc")
2. Arrastra al contenedor superior

**Ventana de Edición:**
```
┌─────────────────────────────────────┐
│ Edit Text                           │
├─────────────────────────────────────┤
│ ┌─────────────────────────────────┐ │
│ │                                 │ │
│ │  [Escribe aquí]                 │ │
│ │                                 │ │
│ └─────────────────────────────────┘ │
│                                     │
│ [B] [I] [U]  Font: ▼  Size: 12 ▼   │
│                                     │
│               [  OK  ]  [ Cancel ]  │
└─────────────────────────────────────┘
```

### **Paso 3: Configurar Título**

**Texto:** `Dashboard de Población Mundial`

**Formato:**
- **Font:** Arial o Tableau Book
- **Size:** 16 pt (grande y legible)
- **Style:** Bold (negrita) [B]
- **Alignment:** Center (centrado)

**Resultado:**
```
┌────────────────────────────────────┐
│                                    │
│  Dashboard de Población Mundial    │ ← Grande, negrita
│                                    │
├────────────────────────────────────┤
│  GRÁFICO POBLACIÓN                 │
│  ...                               │
└────────────────────────────────────┘
```

---

## 121. Agregar Filtros Interactivos

### **¿Qué son Filtros de Dashboard?**

Controles que permiten al usuario **filtrar TODAS las visualizaciones** a la vez.

**Ventaja:**
```
Sin Filtro de Dashboard:       Con Filtro de Dashboard:
Usuario debe filtrar           Usuario filtra UNA VEZ
cada gráfico por separado      y TODOS se actualizan

Gráfico 1: Año ▼               [Año: 2020 ▼]
Gráfico 2: Año ▼               
Gráfico 3: Año ▼               Gráfico 1 ✅
                               Gráfico 2 ✅
❌ Tedioso                     Gráfico 3 ✅
                               
                               ✅ Eficiente
```

### **Agregar Filtro:**

**Paso 1: Seleccionar Hoja**

Clic en **cualquier gráfico** del dashboard (ej: "Población")

**Paso 2: Abrir Menú de Filtros**

Clic en **triángulo (▼)** en la esquina superior derecha:

```
┌────────────────────────────┐
│ Población               ▼  │
├────────────────────────────┤
│ • Fit                      │
│ • Filters              ►   │ ⭐ Seleccionar
│ • Parameters               │
│ • Legends                  │
└────────────────────────────┘
```

**Paso 3: Seleccionar Campo**

En submenu **"Filters"**, selecciona **"Year"** (o el campo de fecha):

```
Filters ►  ┌───────────────────┐
           │ • Year         ⭐  │
           │ • Country          │
           │ • Population Type  │
           └───────────────────┘
```

**Resultado:**
```
┌────────────────────────────────────┐
│ Year                            ▼  │ ← Filtro aparece
│ ○ 1950  ○ 1960  ○ 1970  ○ 1980    │    en el dashboard
│ ○ 1990  ● 2000  ○ 2010  ○ 2020    │
└────────────────────────────────────┘
```

### **Paso 4: Posicionar Filtro**

Arrastra el filtro al **contenedor superior**, a la derecha del título:

```
┌────────────────────────────────────────┐
│ Dashboard de Población Mundial  [Year▼]│ ← Título + Filtro
├────────────────────────────────────────┤
│  GRÁFICO POBLACIÓN                     │
│  ...                                   │
└────────────────────────────────────────┘
```

---

## 122. Modo de Presentación y Publicación

### **Activar Modo de Presentación:**

**Método 1:** Botón en la barra superior
```
[File] [Data] [Dashboard] [🖥️] ← Click aquí
                        ↑
                 Presentation Mode
```

**Método 2:** Atajo de teclado
- `F7` (Windows)
- `Cmd + F7` (Mac)

**Resultado:**
```
MODO NORMAL:                MODO PRESENTACIÓN:
┌────────────────┐          ┌──────────────────────────┐
│ [File][Edit]   │          │                          │
│ Dashboard      │          │    DASHBOARD             │
│ ┌────────────┐ │          │    (pantalla completa)   │
│ │ Graphs     │ │          │                          │
│ └────────────┘ │          │                          │
└────────────────┘          └──────────────────────────┘
                            
Con barras y paneles        Sin distracciones ✅
```

### **Salir del Modo de Presentación:**

- Presiona `Esc`
- O presiona `F7` nuevamente

### **Guardar Dashboard:**

**File → Save** o `Ctrl + S`

Guarda como `.twbx` (Tableau Packaged Workbook) para incluir datos.

---

## 123. Conclusión y Resumen del Sprint 12

### **🎉 ¡Felicidades! Has Completado el Sprint 12 - Automatización**

---

## **RESUMEN GENERAL DEL SPRINT**

Este sprint cubrió **3 áreas fundamentales** para el análisis de datos profesional:

```
┌────────────────────────────────────────────────┐
│           SPRINT 12: AUTOMATIZACIÓN            │
├────────────────────────────────────────────────┤
│                                                │
│  1. DATA PIPELINES (ETL)                       │
│     └─ Automatización de procesos de datos    │
│                                                │
│  2. DASHBOARDS CON DASH (Python)               │
│     └─ Visualizaciones interactivas web       │
│                                                │
│  3. TABLEAU PUBLIC                             │
│     └─ Business Intelligence profesional       │
│                                                │
└────────────────────────────────────────────────┘
```

---

## **PARTE 1: DATA PIPELINES Y ETL**

### **¿Qué Aprendimos?**

**Concepto de ETL:**
```
Extract  →  Transform  →  Load
   ↓           ↓           ↓
Recopilar   Procesar    Guardar
  datos       datos      datos
```

**Habilidades Desarrolladas:**

✅ **Conexión a Bases de Datos con SQLAlchemy**
```python
from sqlalchemy import create_engine

# PostgreSQL
engine = create_engine('postgresql://user:pass@host:port/db')

# SQLite (más simple)
engine = create_engine('sqlite:///games.db')

# Leer datos
df = pd.io.sql.read_sql(query, con=engine)

# Guardar datos
df.to_sql('tabla', con=engine, if_exists='append')
```

✅ **Creación de Pipelines Automatizados**
- Scripts que se ejecutan en horarios programados
- Extracción de datos de múltiples fuentes
- Transformación y limpieza automática
- Carga a bases de datos centrales

✅ **Caso Práctico:**
- Pipeline del Ministerio de Salud de Chile
- Consolidación de archivos CSV anuales
- Manejo de caracteres especiales (ñ, ó)
- Validación de datos y prevención de duplicados

**Conceptos Clave:**
- `getopt` para parámetros de línea de comandos
- `if_exists='replace'` vs `if_exists='append'`
- Queries SQL con DELETE para limpiar datos antiguos
- Conversión de tipos de datos (fechas, números)

---

## **PARTE 2: DASHBOARDS CON DASH (PYTHON)**

### **¿Qué Aprendimos?**

**Librería Dash:**
```python
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
```

### **Estructura de un Dashboard Dash:**

```python
app = dash.Dash(__name__)

# 1. LAYOUT (Diseño)
app.layout = html.Div([
    html.H1('Título'),
    dcc.Graph(id='grafico1'),
    dcc.DatePickerRange(id='filtro_fecha')
])

# 2. CALLBACK (Lógica/Interactividad)
@app.callback(
    Output('grafico1', 'figure'),
    Input('filtro_fecha', 'start_date')
)
def update_graph(start_date):
    # Lógica para actualizar el gráfico
    return figure

# 3. RUN SERVER
if __name__ == '__main__':
    app.run_server()
```

### **Tipos de Gráficos que Dominamos:**

| Tipo | Código | Uso |
|------|--------|-----|
| **Líneas** | `go.Scatter(mode='lines')` | Tendencias temporales |
| **Áreas Apiladas** | `go.Scatter(stackgroup='one')` | Composición temporal |
| **Barras** | `go.Bar(barmode='stack'/'group')` | Comparaciones categóricas |
| **Circulares** | `go.Pie(labels, values)` | Proporciones |
| **Dispersión** | `go.Scatter(mode='markers')` | Correlaciones |
| **Caja y Bigotes** | `go.Box(y=values)` | Distribuciones |
| **Tablas** | `go.Table(header, cells)` | Datos tabulares |

### **Controles Interactivos:**

✅ **Filtros de Fecha:**
```python
dcc.DatePickerRange(
    id='dt_selector',
    start_date='2016-01-01',
    end_date='2020-12-31'
)
```

✅ **Selectores de Modo:**
```python
dcc.RadioItems(
    options=[
        {'label': 'Valores Absolutos', 'value': 'abs'},
        {'label': 'Valores Relativos', 'value': 'rel'}
    ],
    value='abs'
)
```

✅ **Selectores Múltiples:**
```python
dcc.Dropdown(
    options=[{'label': x, 'value': x} for x in genres],
    value=genres,
    multi=True
)
```

### **Sistema de Grid (12 Columnas):**

```python
html.Div([
    html.Div([...], className='eight columns'),  # 66%
    html.Div([...], className='four columns'),   # 33%
], className='row')
```

**Combinaciones Comunes:**
- `twelve columns` = 100% (ancho completo)
- `six columns` + `six columns` = 50/50
- `eight columns` + `four columns` = 66/33
- `four columns` + `four columns` + `four columns` = 33/33/33

### **Callbacks Avanzados:**

```python
@app.callback(
    [Output('graph1', 'figure'),
     Output('graph2', 'figure')],
    [Input('date', 'start_date'),
     Input('mode', 'value'),
     Input('genre', 'value')]
)
def update_figures(start_date, mode, genres):
    # 1. Filtrar datos
    filtered = df.query('date >= @start_date')
    filtered = filtered.query('genre in @genres')
    
    # 2. Calcular valores relativos (si necesario)
    if mode == 'relative':
        total = filtered.groupby('year').agg({'value': 'sum'})
        filtered = filtered.join(total)
        filtered['value'] = filtered['value'] / filtered['total']
    
    # 3. Crear gráficos
    data = []
    for genre in genres:
        data += [go.Scatter(...)]
    
    # 4. Retornar figuras
    return figure1, figure2
```

### **Proyecto Final Dash:**

Dashboard interactivo de videojuegos con:
- 4 visualizaciones simultáneas
- Filtros por fecha, género y plataforma
- Modo absoluto/relativo
- Gráficos de áreas, barras, circular y dispersión
- Diseño responsive con grid de 12 columnas

---

## **PARTE 3: TABLEAU PUBLIC**

### **¿Qué Aprendimos?**

**Instalación y Configuración:**
- Descarga e instalación de Tableau Public (gratuito)
- Diferencias: Tableau Public vs Desktop vs Server
- Creación de cuenta para publicar dashboards

### **Preparación de Datos:**

✅ **Formato Correcto (Row-Oriented):**
```
INCORRECTO (Cross-tab):        CORRECTO (Row-oriented):
Country | 1950 | 1960 | 1970   Country | Year | Population
China   | 500M | 600M | 700M   China   | 1950 | 500M
USA     | 150M | 180M | 200M   China   | 1960 | 600M
                                China   | 1970 | 700M
                                USA     | 1950 | 150M
                                USA     | 1960 | 180M
                                USA     | 1970 | 200M
```

✅ **Función `melt()` para Transformar:**
```python
df_melted = df.melt(
    id_vars=['Country'],
    value_vars=['1950', '1960', '1970'],
    var_name='Year',
    value_name='Population'
)
```

### **Interface de Tableau:**

```
┌─────────────────────────────────────────────┐
│ [File] [Data] [Worksheet]                   │
├──────────┬──────────────────────────────────┤
│ Data     │                                  │
│ ────     │     CANVAS (Área de trabajo)     │
│ □ Tables │                                  │
│ □ Dim.   │         [Arrastra campos]        │
│ □ Meas.  │                                  │
│          │                                  │
│ ────     ├──────────────────────────────────┤
│ Analytics│ Columns: [           ]           │
│ ────     │ Rows:    [           ]           │
│ Show Me  ├──────────────────────────────────┤
│          │ Marks:                           │
│          │ • Color  • Size  • Label         │
│          │ • Detail • Tooltip               │
└──────────┴──────────────────────────────────┘
```

**Áreas Clave:**
1. **Data Pane:** Dimensiones y Medidas
2. **Canvas:** Área de visualización principal
3. **Shelves:** Columns, Rows, Filters, Pages
4. **Marks Card:** Color, Size, Label, Detail, Tooltip
5. **Show Me:** Panel con tipos de gráficos

### **Dimensiones vs Medidas:**

```
DIMENSIONES (Azul):           MEDIDAS (Verde):
• Categóricas                 • Numéricas
• País, Año, Género           • Población, Ventas, Score
• No se agregan               • Se agregan (SUM, AVG, etc.)
• Definen el "qué"            • Definen el "cuánto"
```

### **Tipos de Gráficos en Tableau:**

| Categoría | Tipos | Cuándo Usar |
|-----------|-------|-------------|
| **Temporales** | Line, Area, Dual Line | Tendencias en el tiempo |
| **Comparativos** | Bar, Stacked Bar | Comparar categorías |
| **Distribución** | Box Plot, Histogram | Análisis estadístico |
| **Proporciones** | Pie Chart, Treemap | Partes del todo |
| **Correlación** | Scatter Plot | Relaciones entre variables |
| **Geográficos** | Symbol Map, Filled Map | Análisis espacial |
| **Especiales** | Bullet Chart, Gantt | KPIs y cronogramas |
| **Datos** | Highlight Table, Table | Tablas detalladas |

### **Campos Calculados:**

**Crear Nueva Medida:**
```
Name: Population (Millions)
Formula: SUM([Population]) / 1000000
```

**Crear Nueva Dimensión:**
```
Name: Countries 150M+
Formula: IF [Country] IN ['China', 'India', 'USA'] 
         THEN [Country] 
         ELSE 'Other' 
         END
```

**Quick Table Calculations:**
- Percent of Total
- Running Total
- Difference
- Percent Difference
- Moving Average

### **Niveles de Cálculo:**

```
COMPUTE USING:

Table (across) → Calcula horizontalmente
Table (down)   → Calcula verticalmente ⭐
Cell           → Por cada celda individual
Pane (across)  → Por panel horizontal
Pane (down)    → Por panel vertical
```

**Ejemplo Práctico:**
```
% of Total + Table (down):
Year | China | India | USA  | Total
2020 | 18.5% | 17.8% | 4.3% | 100%
2010 | 19.2% | 17.5% | 4.5% | 100%

Cada año suma 100% ✅
```

### **Gráficos Temporales:**

**Granularidad de Fechas:**
- **Year** → 2020, 2021, 2022
- **Quarter** → Q1 2020, Q2 2020
- **Month** → Jan 2020, Feb 2020
- **Day** → 01/01/2020
- **Exact Date** ⭐ → 2020-01-01 (continuo)

**Tipos Avanzados:**
```
1. Line Chart Simple
   └─ 1 medida temporal

2. Multiple Lines
   └─ Desglose por categoría

3. Dual Lines
   └─ 2 medidas diferentes (eje Y dual)

4. Dual Combination
   └─ Línea + Barras (eje Y dual sincronizado)

5. Stacked Area
   └─ Composición temporal
```

### **Gráficos Especiales:**

**1. Mapas:**
```
Symbol Map:                Filled Map:
   ●  ●                      ▓▓▓  ▒▒▒
  ●   ●                      ▓▓   ▒▒
 ●  ●  ●                    ░░░  ▓▓▓

Puntos geográficos         Regiones coloreadas
```

**2. Bullet Charts (KPIs):**
```
┌────────────────────────────┐
│ Jack    [████████]    110% │ ✅ Cumplió
│ Sarah   [█████░░░]     70% │ ❌ No cumplió
└────────────────────────────┘
```

**3. Gantt Charts (Cronogramas):**
```
Tarea 1  [████████]
Tarea 2      [██████]
Tarea 3          [████]
         Jan Feb Mar Apr
```

### **Highlight Tables:**

```
┌──────────┬──────┬──────┬──────┐
│          │ 2018 │ 2019 │ 2020 │
├──────────┼──────┼──────┼──────┤
│ China    │ 🔴   │ 🔴   │ 🔴   │ Alto
│ India    │ 🔴   │ 🔴   │ 🔴   │ Alto
│ USA      │ 🟡   │ 🟡   │ 🟡   │ Medio
│ Brazil   │ 🟢   │ 🟢   │ 🟢   │ Bajo
└──────────┴──────┴──────┴──────┘

Color intenso = Valores altos
```

### **Construcción de Dashboards:**

**Proceso Completo:**

```
1. PLANIFICACIÓN (Wireframe)
   ┌────────────────────┐
   │ Título    [Filtro] │ 10%
   ├────────────────────┤
   │ GRÁFICO PRINCIPAL  │ 50%
   ├──────────┬─────────┤
   │ Detalle1 │ Detalle2│ 40%
   └──────────┴─────────┘

2. PREPARACIÓN
   • Crear todas las hojas
   • Nombrar descriptivamente
   • Configurar tooltips
   • Probar filtros

3. CONSTRUCCIÓN
   • New Dashboard
   • Size: Automatic
   • Contenedores Vertical/Horizontal
   • Arrastrar hojas
   • Limpiar leyendas

4. INTERACTIVIDAD
   • Agregar filtros
   • Apply to All Worksheets
   • Configurar display styles

5. PRESENTACIÓN
   • Modo presentación (F7)
   • Guardar como .twbx
   • Publicar en Tableau Public
```

### **Filtros en Tableau:**

**Tipos de Display:**
```
1. Single Value (List)     - Radio buttons
2. Single Value (Dropdown) - Dropdown compacto ⭐
3. Single Value (Slider)   - Slider continuo
4. Multiple Values (List)  - Checkboxes
5. Multiple Values (Drop)  - Multi-select
6. Wildcard Match         - Búsqueda por texto
```

**Aplicar a Hojas:**
- Only This Worksheet
- Selected Worksheets...
- **All Using This Data Source** ⭐ (recomendado)

### **Publicación:**

```
Server → Tableau Public → Save to Tableau Public

URL generada:
https://public.tableau.com/profile/usuario#!/vizhome/Dashboard

Opciones:
• Compartir link directo
• Embeber en sitio web (iframe)
• Descargar como imagen/PDF
• Editar descripción y tags
```

---

## **HABILIDADES COMPLETAS ADQUIRIDAS**

### **🔧 Técnicas:**

```
✅ Automatización de Procesos
   └─ Pipelines ETL con SQLAlchemy
   └─ Scripts programables con getopt
   └─ Conexión a múltiples BD

✅ Visualización Web Interactiva
   └─ Dashboards con Dash/Plotly
   └─ Callbacks reactivos
   └─ Diseño responsive con grid

✅ Business Intelligence
   └─ Tableau Public completo
   └─ Gráficos avanzados (14+ tipos)
   └─ Dashboards profesionales
   └─ Publicación online
```

### **📊 Gráficos Dominados:**

**Python (Dash/Plotly):**
1. ✅ Líneas (`go.Scatter`)
2. ✅ Áreas apiladas (`stackgroup`)
3. ✅ Barras (`go.Bar`)
4. ✅ Circulares (`go.Pie`)
5. ✅ Dispersión (`markers`)
6. ✅ Caja y bigotes (`go.Box`)
7. ✅ Tablas (`go.Table`)

**Tableau:**
1. ✅ Line Charts (simple, múltiple, dual)
2. ✅ Area Charts (simple, stacked)
3. ✅ Bar Charts (simple, stacked, grouped)
4. ✅ Pie Charts
5. ✅ Scatter Plots
6. ✅ Box Plots
7. ✅ Highlight Tables
8. ✅ Heat Maps
9. ✅ Symbol Maps
10. ✅ Filled Maps
11. ✅ Bullet Charts
12. ✅ Gantt Charts
13. ✅ Circle Views
14. ✅ Tables

### **🎯 Proyectos Completados:**

```
1. Pipeline ETL - Ministerio de Salud Chile
   • Consolidación de archivos CSV
   • Limpieza de datos
   • Carga a SQLite
   • Validación automática

2. Dashboard Interactivo - Videojuegos (Dash)
   • 4 visualizaciones
   • Filtros múltiples
   • Modo absoluto/relativo
   • Grid responsive

3. Dashboard Profesional - Población Mundial (Tableau)
   • 3 hojas integradas
   • Filtro temporal
   • Cálculos de tabla
   • Publicado online
```

---

## **COMPARACIÓN: DASH VS TABLEAU**

| Aspecto | Dash (Python) | Tableau Public |
|---------|---------------|----------------|
| **Lenguaje** | Python (código) | Visual (drag & drop) |
| **Curva de aprendizaje** | Alta (programación) | Baja (intuitivo) |
| **Flexibilidad** | Máxima (todo customizable) | Media (limitado por UI) |
| **Velocidad** | Lenta (escribir código) | Rápida (arrastrar) |
| **Control** | Total | Limitado |
| **Compartir** | Deployment manual | Un click (Tableau Public) |
| **Costo** | Gratis (Open Source) | Gratis (Public) |
| **Mejor para** | Desarrolladores, proyectos custom | Analistas, prototipado rápido |
| **Data Science** | Integración perfecta | Básico |
| **Producción** | Requiere servidor | Automático en cloud |

---

## **MEJORES PRÁCTICAS APRENDIDAS**

### **📋 Data Pipelines:**

```
✅ Usa parámetros para fechas (start_dt, end_dt)
✅ Valida existencia de datos antes de cargar
✅ Implementa try/except para errores
✅ Registra logs de ejecución
✅ Usa if_exists='append' para incremental
✅ DELETE datos antiguos antes de INSERT
```

### **📊 Dashboards (General):**

```
✅ Regla del 5: Máximo 5 visualizaciones
✅ Jerarquía visual: Principal (50%) > Detalles (25%)
✅ Espacio en blanco: No apretar elementos
✅ Consistencia: Mismos colores/fuentes
✅ Filtros: Aplicar a todas las hojas
✅ Títulos: Claros y descriptivos
```

### **🎨 Diseño:**

```
✅ Colores accesibles (no solo rojo-verde)
✅ Alto contraste para legibilidad
✅ Fuentes mínimo 10pt
✅ Tooltips informativos
✅ Leyendas solo si necesarias
✅ Ejes con nombres claros
```

### **🔧 Técnico:**

```
✅ Guarda como .twbx (incluye datos)
✅ Usa "Automatic" size para dashboards
✅ Prueba en modo presentación
✅ Documenta fuentes de datos
✅ Comenta código (Dash)
✅ Usa nombres descriptivos
```

---

## **ATAJOS DE TECLADO CLAVE**

### **Tableau:**

| Acción | Windows | Mac |
|--------|---------|-----|
| Nuevo Dashboard | `Ctrl + M` | `Cmd + M` |
| Duplicar Hoja | `Ctrl + D` | `Cmd + D` |
| Presentación | `F7` | `Cmd + F7` |
| Guardar | `Ctrl + S` | `Cmd + S` |
| Deshacer | `Ctrl + Z` | `Cmd + Z` |
| Siguiente Hoja | `Alt + →` | `Opt + →` |
| Hoja Anterior | `Alt + ←` | `Opt + ←` |

---

## **RECURSOS Y REFERENCIAS**

### **Documentación Oficial:**

```
Dash:
• https://dash.plot.ly/
• https://plotly.com/python/

Tableau:
• https://public.tableau.com/
• https://help.tableau.com/

SQLAlchemy:
• https://www.sqlalchemy.org/
```

### **Galería de Ejemplos:**

```
Dash:
• https://dash-gallery.plotly.host/Portal/

Tableau:
• https://public.tableau.com/gallery/
```

---

## **PRÓXIMOS PASOS SUGERIDOS**

### **Para Profundizar:**

```
1. Dash Avanzado:
   ✓ Dash Bootstrap Components
   ✓ Dash DataTable interactivo
   ✓ Deployment en Heroku/AWS

2. Tableau Avanzado:
   ✓ Tableau Desktop (versión de pago)
   ✓ Parámetros calculados
   ✓ LOD Expressions
   ✓ Tableau Server

3. Otras Herramientas:
   ✓ Power BI (Microsoft)
   ✓ Looker (Google)
   ✓ Streamlit (más simple que Dash)
   ✓ D3.js (JavaScript avanzado)
```

### **Proyectos de Práctica:**

```
1. Dashboard de Ventas Personal
   • Conectar a tu propia BD
   • KPIs principales
   • Análisis temporal
   • Publicar online

2. Pipeline ETL Completo
   • Múltiples fuentes
   • Transformaciones complejas
   • Scheduled con cron/Task Scheduler
   • Notificaciones de errores

3. Dashboard Interactivo Complejo
   • 10+ visualizaciones
   • Filtros cruzados
   • Drill-down
   • Exportar a PDF
```

---

## **CHECKLIST DE DOMINIO**

### **¿Dominaste el Sprint 12?**

Marca ✅ lo que puedas hacer **sin consultar documentación**:

**Data Pipelines:**
- [ ] Conectar a PostgreSQL con SQLAlchemy
- [ ] Leer datos de BD a DataFrame
- [ ] Guardar DataFrame en BD
- [ ] Crear script con parámetros de fecha
- [ ] Implementar try/except para errores
- [ ] Usar DELETE + INSERT en pipeline

**Dash:**
- [ ] Crear app básica de Dash
- [ ] Agregar gráfico de líneas
- [ ] Agregar gráfico de barras apiladas
- [ ] Implementar callback simple
- [ ] Implementar callback con múltiples inputs
- [ ] Usar grid de 12 columnas
- [ ] Agregar filtro de fechas
- [ ] Calcular valores relativos

**Tableau:**
- [ ] Importar datos CSV/Excel
- [ ] Transformar datos con melt()
- [ ] Crear gráfico de líneas
- [ ] Crear gráfico de áreas apiladas
- [ ] Crear campo calculado
- [ ] Usar Quick Table Calculation
- [ ] Crear highlight table
- [ ] Crear mapa (symbol o filled)
- [ ] Construir dashboard con 3+ hojas
- [ ] Agregar filtro interactivo
- [ ] Publicar en Tableau Public

**Si marcaste 15+ ítems:** ¡Dominas el sprint! 🎉  
**Si marcaste 10-14:** Buen nivel, repasa áreas débiles  
**Si marcaste < 10:** Repasa secciones específicas

---

## **IMPACTO EN TU CARRERA**

### **Con estas habilidades puedes:**

```
✅ Automatizar Reportes
   → Ahorrar 10+ horas/semana en reportes manuales

✅ Crear Dashboards Profesionales
   → Presentar insights a stakeholders ejecutivos

✅ Construir ETL Pipelines
   → Integrar múltiples fuentes de datos

✅ Analizar Datos en Tiempo Real
   → Dashboards que se actualizan automáticamente

✅ Comunicar con Visualizaciones
   → Convertir datos complejos en historias claras

✅ Trabajar con Herramientas Enterprise
   → Tableau es estándar en Fortune 500
```

### **Roles que Ahora Puedes Aplicar:**

```
• Data Analyst
• Business Intelligence Analyst
• Dashboard Developer
• Data Visualization Specialist
• ETL Developer
• Junior Data Engineer
```

---

## **REFLEXIÓN FINAL**

### **Lo Que Lograste:**

```
ANTES del Sprint 12:
❌ Reportes estáticos en Excel
❌ Análisis manual repetitivo
❌ Visualizaciones básicas
❌ Sin automatización

DESPUÉS del Sprint 12:
✅ Dashboards interactivos web
✅ Pipelines automatizados
✅ Visualizaciones profesionales
✅ Procesos 100% automatizados
✅ Análisis en tiempo real
✅ Herramientas enterprise-level
```

### **Recuerda:**

> "Los dashboards no son el fin, son el medio.  
> El objetivo es **tomar mejores decisiones** basadas en datos."

### **Cita de Reflexión:**

> "In God we trust. All others must bring data."  
> — W. Edwards Deming

---

## **🎓 CERTIFICACIÓN DE CONOCIMIENTOS**

**Has completado exitosamente:**

```
┌─────────────────────────────────────────────┐
│                                             │
│    SPRINT 12 - AUTOMATIZACIÓN               │
│         Data Pipelines & Dashboards         │
│                                             │
│  ✓ Data Pipelines (ETL)                     │
│  ✓ SQLAlchemy & Databases                   │
│  ✓ Dash & Plotly                            │
│  ✓ Tableau Public                           │
│  ✓ Dashboard Design                         │
│  ✓ Data Visualization                       │
│                                             │
│  Bootcamp: TripleTen                        │
│  Total Horas: 40+                           │
│  Proyectos: 3 Completos                     │
│                                             │
└─────────────────────────────────────────────┘
```

---

## **TABLA DE CONTENIDOS COMPLETA DEL SPRINT**

**Secciones 1-123:**

1. **Introducción a la Automatización** (1-5)
2. **Data Pipelines y ETL** (6-15)
3. **SQLAlchemy y Bases de Datos** (16-25)
4. **Introducción a Dash** (26-35)
5. **Gráficos Básicos en Dash** (36-50)
6. **Gráficos Avanzados en Dash** (51-65)
7. **Interactividad y Callbacks** (66-80)
8. **Diseño de Dashboards en Dash** (81-88)
9. **Introducción a Tableau** (89-95)
10. **Preparación de Datos en Tableau** (96-100)
11. **Gráficos en Tableau** (101-105)
12. **Campos Calculados y Filtros** (106-108)
13. **Gráficos Especiales en Tableau** (109-120)
14. **Construcción de Dashboards en Tableau** (121-122)
15. **Conclusión y Resumen** (123)

**Total:** 123 secciones, 2,900+ líneas de documentación

---

## **CONTACTO Y SOPORTE**

**Para consultas sobre este material:**
- Bootcamp: TripleTen
- Sprint: 12 - Automatización
- Fecha: Noviembre 2025

**Recursos adicionales:**
- Comunidad Tableau Public
- Stack Overflow (tags: dash, plotly, tableau)
- GitHub (proyectos open source)

---

**¡Felicidades por completar el Sprint 12! 🎉**

**Estás listo para construir dashboards profesionales y automatizar procesos de datos.**

---

**Última actualización:** Sprint 12 - Automatización (COMPLETO)  
**Bootcamp:** TripleTen  
**Líneas de Documentación:** 2,900+  
**Secciones:** 123  
**Proyectos Prácticos:** 3

