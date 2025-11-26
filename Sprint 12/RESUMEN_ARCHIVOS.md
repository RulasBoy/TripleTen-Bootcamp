# 📁 Resumen de Archivos - Sprint 12 Automatización

## 📚 Documentación

### 📖 `MEMORIA_SPRINT_AUTOMATIZACION.md` (Principal)
**Contenido completo del Sprint:**
- ✅ Introducción a la Automatización
- ✅ Data Pipelines (ETL)
- ✅ SQLAlchemy y conexión a bases de datos
- ✅ Scripts de pipeline completos
- ✅ Ejercicio Ministerio de Salud Chile
- ✅ Dashboards con Dash
- ✅ Componentes HTML y gráficos
- ✅ Estilos CSS
- ✅ Buenas prácticas
- ✅ 22 secciones organizadas

### 📘 `README_DASHBOARDS.md`
**Guía práctica de uso:**
- Instrucciones de instalación
- Cómo ejecutar cada dashboard
- Tipos de gráficos disponibles
- Personalización con estilos
- Solución de problemas
- Recursos adicionales

### 📄 `RESUMEN_ARCHIVOS.md` (Este archivo)
**Índice y navegación:**
- Descripción de todos los archivos
- Guía de inicio rápido
- Estructura del proyecto

---

## 🚀 Scripts de Dashboards

### 🟢 `dashboard_plantilla.py` ⭐ **RECOMENDADO PARA EMPEZAR**
**Plantilla base limpia**
- Estructura básica lista para usar
- Comentarios explicativos
- Ejemplo mínimo funcional
- **Usa este archivo para crear tus propios dashboards**

### 🔵 `dashboard_ejemplo_simple.py`
**Nivel:** ⭐ Básico
- Dashboard con función lineal simple
- Un solo gráfico
- Código minimalista
- Ideal para aprender la estructura

**Características:**
- Encabezado
- Descripción
- Gráfico de línea (y = x)

### 🟡 `dashboard_ejemplo_multiple.py`
**Nivel:** ⭐⭐ Intermedio
- Múltiples gráficos en un dashboard
- Layout con columnas
- Varios tipos de gráficos

**Características:**
- Funciones lineales (y=x, y=2x, y=-x)
- Función cuadrática (y=x²)
- Gráfico de barras
- Layout en dos columnas

### 🟣 `dashboard_con_datos.py`
**Nivel:** ⭐⭐⭐ Avanzado
- Dashboard profesional completo
- Datos simulados de videojuegos
- Diseño con estilos CSS

**Características:**
- 4 KPIs (métricas clave) en tarjetas
- Gráfico de áreas apiladas (por plataforma)
- Gráfico de líneas con tendencia
- Colores y estilos profesionales
- Datos de 2000-2020
- Análisis por plataformas (PS4, Xbox, PC, Switch)

---

## 📊 Datasets

### 📂 `datasets/`
**Contiene 3 archivos CSV del ejercicio de pipelines:**

1. `EGRE_DATOS_ABIERTOS_2018.csv`
   - Egresos hospitalarios Chile 2018
   - ~1,620,450 registros

2. `EGRE_DATOS_ABIERTOS_2019.csv`
   - Egresos hospitalarios Chile 2019
   - ~1,623,335 registros

3. `EGRE_DATOS_ABIERTOS_2020.csv`
   - Egresos hospitalarios Chile 2020
   - ~1,292,935 registros

**Uso:** Ejercicio práctico de pipelines ETL con SQLite

---

## ⚙️ Configuración

### 📋 `requirements.txt`
**Dependencias del proyecto:**
```
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
scipy>=1.10.0
statsmodels>=0.14.0
jupyter>=1.0.0
notebook>=7.0.0
ipykernel>=6.25.0
dash>=2.14.0              ← NUEVO
dash-core-components>=2.0.0  ← NUEVO
dash-html-components>=2.0.0  ← NUEVO
plotly>=5.17.0            ← NUEVO
sqlalchemy>=2.0.0         ← NUEVO
```

**Instalar todo:**
```bash
pip install -r requirements.txt
```

---

## 📓 Jupyter Notebook

### 📒 `notebook.ipynb`
Notebook para experimentación y análisis interactivo

---

## 📖 PDFs de Referencia

### 📕 `moved_Hoja_informativa_Data_pipelines_y_por_qu_utilizarlos_esp.pdf`
Hoja de referencia rápida sobre pipelines

### 📗 `moved_Resumen_del_captulo_data_pipelines_y_por_qu_utilizarlos.pdf`
Resumen detallado del capítulo de pipelines

---

## 🎯 Guía de Inicio Rápido

### Para Aprender Dashboards:

1. **Lee la teoría:**
   ```
   MEMORIA_SPRINT_AUTOMATIZACION.md
   (Secciones 10-22)
   ```

2. **Revisa los ejemplos:**
   ```bash
   # Ejemplo 1: Simple
   python dashboard_ejemplo_simple.py
   
   # Ejemplo 2: Múltiple
   python dashboard_ejemplo_multiple.py
   
   # Ejemplo 3: Avanzado
   python dashboard_con_datos.py
   ```

3. **Crea tu propio dashboard:**
   ```bash
   # Usa la plantilla
   cp dashboard_plantilla.py mi_dashboard.py
   nano mi_dashboard.py
   python mi_dashboard.py
   ```

### Para Aprender Pipelines ETL:

1. **Lee la teoría:**
   ```
   MEMORIA_SPRINT_AUTOMATIZACION.md
   (Secciones 1-9)
   ```

2. **Revisa el ejercicio resuelto:**
   ```
   Sección 7 en MEMORIA_SPRINT_AUTOMATIZACION.md
   Ejercicio del Ministerio de Salud Chile
   ```

3. **Práctica con datasets reales:**
   ```
   datasets/EGRE_DATOS_ABIERTOS_*.csv
   ```

---

## 📐 Estructura del Proyecto

```
Sprint 12/
│
├── 📚 DOCUMENTACIÓN
│   ├── MEMORIA_SPRINT_AUTOMATIZACION.md    ⭐ Documento principal
│   ├── README_DASHBOARDS.md                 Guía de dashboards
│   └── RESUMEN_ARCHIVOS.md                  Este archivo
│
├── 🚀 DASHBOARDS
│   ├── dashboard_plantilla.py               ⭐ Plantilla base
│   ├── dashboard_ejemplo_simple.py          Nivel básico
│   ├── dashboard_ejemplo_multiple.py        Nivel intermedio
│   └── dashboard_con_datos.py               Nivel avanzado
│
├── 📊 DATOS
│   └── datasets/
│       ├── EGRE_DATOS_ABIERTOS_2018.csv
│       ├── EGRE_DATOS_ABIERTOS_2019.csv
│       └── EGRE_DATOS_ABIERTOS_2020.csv
│
├── ⚙️ CONFIGURACIÓN
│   ├── requirements.txt                     Dependencias
│   └── notebook.ipynb                       Jupyter notebook
│
└── 📖 REFERENCIAS
    ├── moved_Hoja_informativa_*.pdf
    └── moved_Resumen_del_captulo_*.pdf
```

---

## 🎨 Recursos Visuales

### Colores Usados en los Ejemplos:

| Color | Código | Uso |
|-------|--------|-----|
| 🔵 Azul | `#3498db` | Información, datos |
| 🔴 Rojo | `#e74c3c` | Alertas |
| 🟢 Verde | `#2ecc71` | Éxito |
| 🟠 Naranja | `#f39c12` | Advertencias |
| 🟣 Morado | `#9b59b6` | Destacar |
| ⚫ Gris Oscuro | `#2c3e50` | Texto |
| ⚪ Gris Claro | `#ecf0f1` | Fondos |

---

## 🔧 Comandos Útiles

### Instalación:
```bash
pip install -r requirements.txt
```

### Ejecutar Dashboard:
```bash
python dashboard_ejemplo_simple.py
# Abrir en: http://localhost:3000
```

### Ver en Navegador:
```bash
# Linux/Mac
xdg-open http://localhost:3000

# Windows
start http://localhost:3000
```

### Detener Dashboard:
```
Ctrl + C (en la terminal)
```

---

## 📊 Comparación de Archivos de Dashboard

| Archivo | Líneas | Gráficos | Nivel | Tiempo |
|---------|--------|----------|-------|--------|
| `dashboard_plantilla.py` | ~60 | 1 | Base | - |
| `dashboard_ejemplo_simple.py` | ~50 | 1 | ⭐ | 5 min |
| `dashboard_ejemplo_multiple.py` | ~100 | 3 | ⭐⭐ | 10 min |
| `dashboard_con_datos.py` | ~180 | 2 + KPIs | ⭐⭐⭐ | 20 min |

---

## 💡 Recomendaciones de Uso

### Si eres principiante:
1. ✅ Lee `MEMORIA_SPRINT_AUTOMATIZACION.md` secciones 10-13
2. ✅ Ejecuta `dashboard_ejemplo_simple.py`
3. ✅ Modifica `dashboard_plantilla.py`

### Si tienes experiencia:
1. ✅ Revisa `dashboard_con_datos.py`
2. ✅ Adapta el código a tus datos
3. ✅ Agrega interactividad (callbacks)

### Para proyectos reales:
1. ✅ Usa `dashboard_plantilla.py` como base
2. ✅ Conecta a tu base de datos
3. ✅ Aplica estilos personalizados
4. ✅ Implementa filtros interactivos

---

## ✅ Checklist de Aprendizaje

### Conceptos Básicos:
- [ ] Entender qué es un dashboard
- [ ] Conocer la estructura de Dash
- [ ] Importar librerías necesarias
- [ ] Crear layout básico

### Componentes:
- [ ] Usar `html.H1()`, `html.Div()`
- [ ] Crear gráficos con `dcc.Graph()`
- [ ] Configurar `go.Scatter()`, `go.Bar()`
- [ ] Personalizar con estilos CSS

### Avanzado:
- [ ] Crear gráficos de áreas apiladas
- [ ] Diseñar KPIs visualmente
- [ ] Implementar layouts multi-columna
- [ ] Aplicar paleta de colores consistente

### Pipelines:
- [ ] Entender proceso ETL
- [ ] Usar SQLAlchemy
- [ ] Conectar a bases de datos
- [ ] Crear pipeline completo

---

## 🎓 Próximos Pasos

1. **Práctica básica:** Ejecuta los 3 ejemplos
2. **Personalización:** Modifica colores y textos
3. **Datos propios:** Usa tus propios datasets
4. **Interactividad:** Aprende callbacks de Dash
5. **Deployment:** Publica tu dashboard online

---

## 📞 Recursos de Ayuda

- **Documentación:** `MEMORIA_SPRINT_AUTOMATIZACION.md`
- **Guía práctica:** `README_DASHBOARDS.md`
- **Plantilla:** `dashboard_plantilla.py`
- **Ejemplos:** Carpeta con 3 scripts

---

**Creado:** Sprint 12 - Automatización  
**Bootcamp:** TripleTen  
**Última actualización:** 2025

