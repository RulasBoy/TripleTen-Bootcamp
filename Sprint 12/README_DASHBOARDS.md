# Dashboards con Dash - Sprint 12

## 📋 Archivos Creados

He creado **3 ejemplos de dashboards** con diferentes niveles de complejidad:

### 1. `dashboard_ejemplo_simple.py`
**Nivel:** Básico  
**Contenido:**
- Dashboard simple con función lineal
- Un solo gráfico
- Estructura básica de Dash
- Ideal para aprender la estructura

### 2. `dashboard_ejemplo_multiple.py`
**Nivel:** Intermedio  
**Contenido:**
- Múltiples gráficos en el mismo dashboard
- Funciones lineales y cuadráticas
- Gráfico de barras
- Layout con columnas
- Uso de estilos CSS

### 3. `dashboard_con_datos.py`
**Nivel:** Avanzado  
**Contenido:**
- Dashboard completo de análisis de videojuegos
- Métricas clave (KPIs)
- Gráfico de áreas apiladas
- Gráfico de líneas con tendencia
- Datos simulados (años 2000-2020)
- Diseño profesional con estilos

---

## 🚀 Cómo Ejecutar los Dashboards

### Paso 1: Instalar Dependencias

```bash
pip install -r requirements.txt
```

O instalar individualmente:
```bash
pip install dash dash-core-components dash-html-components plotly pandas numpy
```

### Paso 2: Ejecutar un Dashboard

Elige uno de los tres scripts y ejecútalo:

```bash
# Opción 1: Dashboard simple
python dashboard_ejemplo_simple.py

# Opción 2: Dashboard con múltiples gráficos
python dashboard_ejemplo_multiple.py

# Opción 3: Dashboard completo con datos
python dashboard_con_datos.py
```

### Paso 3: Abrir en el Navegador

Una vez que el servidor esté ejecutándose, verás un mensaje como:
```
Dash is running on http://0.0.0.0:3000/
```

Abre tu navegador y ve a:
```
http://localhost:3000
```

### Paso 4: Detener el Dashboard

Para detener el servidor, presiona en la terminal:
```
Ctrl + C
```

---

## 📊 Estructura de un Dashboard Dash

### Componentes Básicos:

```python
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

# 1. Crear la aplicación
app = dash.Dash(__name__)

# 2. Definir el layout (diseño)
app.layout = html.Div(children=[
    html.H1('Título'),           # Encabezado
    dcc.Graph(...)               # Gráfico
])

# 3. Ejecutar el servidor
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=3000)
```

---

## 🎨 Componentes HTML Disponibles

| Componente | Uso | Ejemplo |
|------------|-----|---------|
| `html.H1()` | Encabezado nivel 1 | `html.H1('Título')` |
| `html.H2()` | Encabezado nivel 2 | `html.H2('Subtítulo')` |
| `html.Div()` | Contenedor | `html.Div(children=[...])` |
| `html.P()` | Párrafo | `html.P('Texto')` |
| `html.Br()` | Salto de línea | `html.Br()` |

---

## 📈 Tipos de Gráficos con Plotly

### 1. Gráfico de Líneas (Scatter)
```python
go.Scatter(
    x=datos_x,
    y=datos_y,
    mode='lines',          # 'lines', 'markers', 'lines+markers'
    name='Nombre'
)
```

### 2. Gráfico de Barras
```python
go.Bar(
    x=categorias,
    y=valores,
    name='Nombre'
)
```

### 3. Gráfico de Áreas Apiladas
```python
go.Scatter(
    x=datos_x,
    y=datos_y,
    mode='lines',
    stackgroup='one',      # Apilar gráficos
    fillcolor='rgba(52, 152, 219, 0.7)'
)
```

### 4. Gráfico de Dispersión
```python
go.Scatter(
    x=datos_x,
    y=datos_y,
    mode='markers',
    marker=dict(size=10, color='blue')
)
```

---

## 🎨 Personalización con Estilos

### Estilos Inline:
```python
html.Div(
    children='Contenido',
    style={
        'textAlign': 'center',
        'color': '#2c3e50',
        'backgroundColor': '#ecf0f1',
        'padding': 20,
        'marginBottom': 30,
        'borderRadius': 10
    }
)
```

### Colores Recomendados:
- **Azul:** `#3498db`
- **Rojo:** `#e74c3c`
- **Verde:** `#2ecc71`
- **Naranja:** `#f39c12`
- **Morado:** `#9b59b6`
- **Gris oscuro:** `#2c3e50`
- **Gris claro:** `#ecf0f1`

---

## 🔧 Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'dash'"
**Solución:** Instalar dependencias
```bash
pip install dash plotly
```

### Error: "Address already in use"
**Solución:** El puerto 3000 está ocupado
```bash
# Cambiar el puerto en el código:
app.run_server(host='0.0.0.0', port=3001)  # Usar puerto 3001
```

### El dashboard no se actualiza
**Solución:** Reiniciar el servidor
1. Presionar Ctrl + C en la terminal
2. Volver a ejecutar el script

---

## 📚 Recursos Adicionales

- [Documentación oficial de Dash](https://dash.plotly.com/)
- [Galería de ejemplos de Plotly](https://plotly.com/python/)
- [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)

---

## 💡 Próximos Pasos

1. ✅ Ejecutar los tres ejemplos para familiarizarte
2. ✅ Modificar los datos y ver cómo cambian los gráficos
3. ✅ Experimentar con diferentes tipos de gráficos
4. ✅ Agregar tus propios datos
5. ✅ Crear tu propio dashboard personalizado

---

**Autor:** Sprint 12 - Automatización  
**Bootcamp:** TripleTen

