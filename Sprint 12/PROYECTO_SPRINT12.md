# PROYECTO SPRINT 12 - AUTOMATIZACIÓN
## Dashboard de Tendencias de YouTube

**Bootcamp:** TripleTen  
**Sprint:** 12 - Automatización  
**Fecha:** Noviembre 2025

---

## 📋 DESCRIPCIÓN DEL PROYECTO

### **Contexto:**

Trabajas como **analista de vídeos publicitarios** en la agencia de publicidad **Sterling & Draper**.

**Situación actual:**
- Analizas tendencias de vídeos en YouTube manualmente
- Determinas qué contenido merece atención para mercadotecnia
- Cada semana, Melanie y Ashok te hacen las mismas preguntas

**Problema:**
```
Cada semana, Melanie y Ashok preguntan:
├─ ¿Qué categorías estaban en tendencias la semana pasada?
├─ ¿Cómo se distribuyeron en diversas regiones?
└─ ¿Qué categorías fueron particularmente populares en Estados Unidos?

Llevas 6 semanas respondiendo manualmente → Es hora de AUTOMATIZAR
```

**Solución:**
Crear un **dashboard automatizado** para que Melanie y Ashok puedan consultar los datos por sí mismos.

---

## 🎯 OBJETIVOS DEL PROYECTO

### **Objetivo Principal:**
Crear un dashboard interactivo en **Tableau Public** que responda automáticamente a las preguntas recurrentes sobre tendencias de YouTube.

### **Objetivos Específicos:**

```
1. Automatizar el análisis de tendencias
   └─ Eliminar consultas manuales semanales

2. Visualizar categorías en tendencia
   └─ Por semana, región y país

3. Análisis específico de Estados Unidos
   └─ Categorías más populares

4. Dashboard autoservicio
   └─ Melanie y Ashok pueden explorar datos sin ayuda
```

---

## 📊 DATOS DEL PROYECTO

### **Características de los Datos:**

**Cada video tiene:**
- ✅ Categoría específica (entretenimiento, música, noticias, política, etc.)
- ✅ Región geográfica
- ✅ Fecha en que se hace tendencia

**Comportamiento:**
```
Un video puede estar en tendencias durante VARIOS días seguidos

Ejemplo:
Video: "Amazing Cat Tricks"
├─ Categoría: Entretenimiento
├─ Región: Estados Unidos
└─ Tendencia:
    ├─ Día 1: 2024-01-15
    ├─ Día 2: 2024-01-16
    ├─ Día 3: 2024-01-17
    └─ Día 4: 2024-01-18
```

### **Archivo de Datos:**

**Nombre:** `trending_by_time.csv`

**Estructura esperada:**
```
Columnas probables:
├─ video_id         : ID único del video
├─ title            : Título del video
├─ category         : Categoría (Music, Entertainment, News, etc.)
├─ region           : Región geográfica (US, GB, CA, etc.)
├─ trending_date    : Fecha en que estuvo en tendencia
├─ views            : Número de visualizaciones
├─ likes            : Número de likes
└─ comments         : Número de comentarios
```

---

## ✅ PREGUNTA CLAVE DEL PROYECTO

### **¿Qué pasos deben tomarse para diseñar y crear el dashboard?**

**Opciones proporcionadas:**

#### **Opción 1:** ❌ INCORRECTA
```
Hablar con administradores de BD → Trabajar con ingenieros → 
Diseñar tablas de agregación → Esperar desarrollo → 
Crear dashboard → Anunciar a Melanie y Ashok

❌ Problemas:
   • Demasiado burocrático
   • No consulta con usuarios finales (Melanie y Ashok)
   • Orden incorrecto de pasos
```

#### **Opción 2:** ❌ INCORRECTA
```
Crear código del dashboard de inmediato → Aceptar datos brutos → 
Sin tablas de agregación ni pipelines → Avisar a Melanie y Ashok

❌ Problemas:
   • No recopila requisitos de usuarios
   • Ignora mejores prácticas (agregación)
   • Sin consulta con equipo técnico
   • Dashboard ineficiente (datos brutos)
```

#### **Opción 3:** ❌ INCORRECTA
```
Hablar con Melanie y Ashok → Diseñar elementos del dashboard →
No hablar con administradores ni ingenieros

❌ Problemas:
   • Ignora al equipo técnico
   • No verifica disponibilidad de datos
   • Asume que los datos existen y son accesibles
   • Posible solución no implementable
```

#### **Opción 4:** ✅ CORRECTA
```
1. Hablar con Melanie y Ashok
   └─ Contenidos del dashboard
   └─ Diseño requerido
   └─ Datos necesarios

2. Hablar con administradores de BD
   └─ De dónde se recolectan los datos
   └─ Cómo se pueden transformar
   └─ Dónde almacenar tablas de agregación

3. Hablar con ingenieros de datos
   └─ Confirmar viabilidad técnica
   └─ Diseñar pipeline
   └─ Implementar transformaciones

4. Crear pipeline y dashboard
   └─ Desarrollo técnico
   └─ Testing
   └─ Deployment

✅ Este es el PROCESO CORRECTO según las mejores prácticas
```

---

## 🔄 PROCESO CORRECTO PASO A PASO

### **FASE 1: Recopilación de Requisitos (Usuarios)**

**Hablar con Melanie y Ashok:**

```
Preguntas clave:
├─ ¿Qué problema comercial resuelve el dashboard?
├─ ¿Con qué frecuencia lo usarán?
├─ ¿Qué métricas específicas necesitan?
│  ├─ Categorías en tendencia
│  ├─ Distribución por región
│  └─ Popularidad en Estados Unidos
├─ ¿Qué filtros necesitan?
│  ├─ Rango de fechas (semanal)
│  ├─ Región/País
│  └─ Categoría
├─ ¿Valores absolutos o relativos?
└─ ¿Qué tipo de gráficos prefieren?
```

**Resultado esperado:**
```
Documento de requisitos:
├─ Problema: Responder 3 preguntas semanales
├─ Frecuencia de uso: Semanal
├─ Métricas:
│  ├─ Número de videos en tendencia por categoría
│  ├─ Distribución geográfica
│  └─ Top categorías en USA
├─ Filtros:
│  ├─ Semana (date picker)
│  ├─ Región (dropdown)
│  └─ Categoría (opcional)
└─ Gráficos:
   ├─ Barras apiladas (categorías por semana)
   ├─ Mapa (distribución geográfica)
   └─ Top 10 (categorías en USA)
```

---

### **FASE 2: Consulta Técnica (Administradores de BD)**

**Hablar con administradores de BD:**

```
Preguntas clave:
├─ ¿De dónde provienen los datos de YouTube?
│  └─ API de YouTube, scraping, data lake, etc.
├─ ¿Qué datos están disponibles actualmente?
│  └─ Verificar campos necesarios
├─ ¿Dónde almacenar tablas de agregación?
│  ├─ PostgreSQL
│  ├─ MySQL
│  └─ SQLite (si es pequeño)
├─ ¿Con qué frecuencia se actualizan los datos?
│  └─ Diario, semanal, tiempo real
└─ ¿Permisos de lectura/escritura?
   └─ Credenciales para acceder
```

**Resultado esperado:**
```
Especificaciones técnicas:
├─ Fuente: API de YouTube
├─ Frecuencia: Actualización diaria
├─ Base de datos: PostgreSQL
├─ Tabla origen: youtube_trending_raw
├─ Tabla agregada: youtube_trending_agg
├─ Usuario: analyst_user
└─ Permisos: READ en raw, WRITE en agg
```

---

### **FASE 3: Diseño de Pipeline (Ingenieros de Datos)**

**Hablar con ingenieros de datos:**

```
Discutir:
├─ Diseño del pipeline ETL
│  ├─ Extract: De dónde leer datos
│  ├─ Transform: Qué agregaciones hacer
│  └─ Load: Dónde guardar resultado
├─ Frecuencia de ejecución
│  └─ Diaria, semanal, tiempo real
├─ Manejo de errores
│  └─ Logs, alertas, reintentos
└─ Testing y validación
   └─ Cómo asegurar calidad de datos
```

**Pipeline ETL propuesto:**

```python
# Pseudocódigo del pipeline

def youtube_trending_pipeline(start_date, end_date):
    """
    Pipeline para agregar datos de YouTube Trending
    """
    # 1. EXTRACT
    engine = create_engine('postgresql://user:pass@host/db')
    query = """
        SELECT 
            video_id,
            category,
            region,
            trending_date,
            views,
            likes
        FROM youtube_trending_raw
        WHERE trending_date BETWEEN %(start)s AND %(end)s
    """
    df = pd.read_sql(query, engine, params={
        'start': start_date,
        'end': end_date
    })
    
    # 2. TRANSFORM
    # Agregar por categoría, región y semana
    df['week'] = pd.to_datetime(df['trending_date']).dt.to_period('W')
    
    agg_data = df.groupby(['week', 'region', 'category']).agg({
        'video_id': 'count',    # Número de videos
        'views': 'sum',         # Total de visualizaciones
        'likes': 'sum'          # Total de likes
    }).reset_index()
    
    agg_data.rename(columns={
        'video_id': 'videos_trending'
    }, inplace=True)
    
    # 3. LOAD
    # Borrar datos antiguos
    engine.execute("""
        DELETE FROM youtube_trending_agg
        WHERE week BETWEEN %(start)s AND %(end)s
    """, {'start': start_date, 'end': end_date})
    
    # Insertar datos nuevos
    agg_data.to_sql(
        'youtube_trending_agg',
        engine,
        if_exists='append',
        index=False
    )
    
    print(f"Pipeline completado: {len(agg_data)} registros cargados")
```

---

### **FASE 4: Creación del Dashboard (Tableau)**

**Pasos en Tableau:**

#### **4.1. Preparar Datos**

```python
# Exportar datos agregados para Tableau
query = """
    SELECT 
        week,
        region,
        category,
        videos_trending,
        views,
        likes
    FROM youtube_trending_agg
    ORDER BY week DESC, region, category
"""
df = pd.read_sql(query, engine)
df.to_csv('trending_by_time.csv', index=False)
```

#### **4.2. Conectar Datos a Tableau**

```
1. Abrir Tableau Public
2. Connect → Text file
3. Seleccionar trending_by_time.csv
4. Verificar tipos de datos:
   ├─ week: Date
   ├─ region: String (Dimension)
   ├─ category: String (Dimension)
   ├─ videos_trending: Number (Measure)
   ├─ views: Number (Measure)
   └─ likes: Number (Measure)
```

#### **4.3. Crear Visualizaciones**

**Hoja 1: Categorías en Tendencia por Semana**
```
Tipo: Stacked Bar Chart (Barras apiladas)
├─ Columns: WEEK(week)
├─ Rows: SUM(videos_trending)
├─ Color: category
├─ Label: category
└─ Filtro: region (opcional)

Responde: ¿Qué categorías estaban en tendencias la semana pasada?
```

**Hoja 2: Distribución Geográfica**
```
Tipo: Symbol Map o Filled Map
├─ Geo: region
├─ Size: SUM(videos_trending)
├─ Color: SUM(videos_trending)
├─ Tooltip: region, category, videos_trending
└─ Filtro: week, category

Responde: ¿Cómo se distribuyeron en diversas regiones?
```

**Hoja 3: Top Categorías en Estados Unidos**
```
Tipo: Horizontal Bar Chart (Top 10)
├─ Rows: category (sorted descending)
├─ Columns: SUM(videos_trending)
├─ Filtro: region = 'US'
├─ Filtro: week
└─ Top 10: category by videos_trending

Responde: ¿Qué categorías fueron particularmente populares en USA?
```

#### **4.4. Construir Dashboard**

```
Layout del Dashboard:
┌────────────────────────────────────────────────┐
│ Tendencias de YouTube    [Semana: ▼] [US ✓]   │ 10%
├────────────────────────────────────────────────┤
│                                                │
│  CATEGORÍAS EN TENDENCIA POR SEMANA            │ 40%
│  (Barras apiladas)                             │
│                                                │
├──────────────────────┬─────────────────────────┤
│ DISTRIBUCIÓN         │ TOP 10 CATEGORÍAS       │
│ GEOGRÁFICA           │ EN ESTADOS UNIDOS       │ 50%
│ (Mapa)               │ (Barras horizontales)   │
└──────────────────────┴─────────────────────────┘

Elementos:
├─ Título: "Dashboard de Tendencias de YouTube"
├─ Filtro de semana: Date picker
├─ Filtro de región: Dropdown (All, US, GB, CA, etc.)
├─ 3 visualizaciones principales
└─ Tooltips informativos en cada gráfico
```

---

## 📦 ENTREGABLES DEL PROYECTO

### **Archivos Requeridos:**

```
proyecto_sprint12.zip
├─ trending_by_time.csv          # Datos agregados
├─ presentacion.pdf              # Presentación del proyecto
├─ link_tableau_public.txt       # URL del dashboard publicado
└─ readme.txt (opcional)         # Instrucciones de ejecución
```

**Límite:** Máximo 9 MB total

---

## 📄 CONTENIDO DE CADA ENTREGABLE

### **1. trending_by_time.csv**

```csv
week,region,category,videos_trending,views,likes
2024-W01,US,Music,45,12500000,850000
2024-W01,US,Entertainment,38,9800000,720000
2024-W01,US,News & Politics,22,5400000,320000
2024-W01,GB,Music,32,7800000,540000
...
```

**Requisitos:**
- ✅ Datos agregados (no datos brutos)
- ✅ Columnas necesarias para el dashboard
- ✅ Formato CSV válido
- ✅ Encodig UTF-8

---

### **2. presentacion.pdf**

**Estructura de la Presentación:**

```
Diapositiva 1: PORTADA
├─ Título: Dashboard de Tendencias de YouTube
├─ Nombre: Tu nombre
├─ Bootcamp: TripleTen
└─ Sprint: 12 - Automatización

Diapositiva 2: PROBLEMA EMPRESARIAL
├─ Contexto: Agencia Sterling & Draper
├─ Situación actual: Consultas manuales semanales
├─ Usuarios: Melanie y Ashok
└─ Preguntas recurrentes (3)

Diapositiva 3: SOLUCIÓN PROPUESTA
├─ Dashboard interactivo en Tableau Public
├─ Actualización automática
├─ Autoservicio para usuarios
└─ Elimina consultas manuales

Diapositiva 4: PROCESO DE DESARROLLO
├─ Fase 1: Requisitos con usuarios
├─ Fase 2: Consulta técnica con BD
├─ Fase 3: Diseño de pipeline ETL
└─ Fase 4: Creación del dashboard

Diapositiva 5: FUENTE DE DATOS
├─ Origen: API de YouTube / Data Lake
├─ Frecuencia: Actualización diaria
├─ Pipeline ETL: Python + SQLAlchemy
└─ Agregación: Por semana, región, categoría

Diapositiva 6: DASHBOARD - VISTA GENERAL
├─ Screenshot del dashboard completo
├─ Destacar 3 secciones principales
└─ Filtros disponibles

Diapositiva 7: VISUALIZACIÓN 1
├─ Categorías en tendencia por semana
├─ Tipo: Barras apiladas
├─ Screenshot
└─ Responde: ¿Qué categorías en tendencia?

Diapositiva 8: VISUALIZACIÓN 2
├─ Distribución geográfica
├─ Tipo: Mapa
├─ Screenshot
└─ Responde: ¿Distribución por regiones?

Diapositiva 9: VISUALIZACIÓN 3
├─ Top categorías en USA
├─ Tipo: Barras horizontales (Top 10)
├─ Screenshot
└─ Responde: ¿Categorías populares en USA?

Diapositiva 10: INSIGHTS CLAVE
├─ Insight 1: Categoría más popular
├─ Insight 2: Región más activa
├─ Insight 3: Tendencias temporales
└─ Insight 4: Patrones identificados

Diapositiva 11: IMPACTO Y BENEFICIOS
├─ Ahorro de tiempo: 2-3 horas/semana
├─ Autoservicio: Usuarios independientes
├─ Actualización automática
└─ Escalable a más usuarios

Diapositiva 12: RECOMENDACIONES
├─ Monitorear uso del dashboard
├─ Recopilar feedback de usuarios
├─ Posibles mejoras futuras
└─ Expandir a otras regiones/métricas

Diapositiva 13: CONCLUSIONES
├─ Dashboard cumple objetivos
├─ Proceso correcto seguido
├─ Usuarios empoderados
└─ Proceso automatizado exitosamente
```

---

### **3. link_tableau_public.txt**

**Contenido:**

```txt
DASHBOARD DE TENDENCIAS DE YOUTUBE
===================================

Autor: [Tu nombre]
Bootcamp: TripleTen
Sprint: 12 - Automatización

URL del Dashboard:
https://public.tableau.com/profile/[tu_usuario]/#!/vizhome/YouTubeTrending/Dashboard

Descripción:
Dashboard interactivo que muestra tendencias de videos de YouTube
por categoría, región y tiempo. Permite a los usuarios explorar
qué categorías están en tendencia, cómo se distribuyen geográficamente
y qué categorías son más populares en Estados Unidos.

Filtros disponibles:
- Semana (date picker)
- Región (dropdown)

Visualizaciones:
1. Categorías en tendencia por semana (barras apiladas)
2. Distribución geográfica (mapa)
3. Top 10 categorías en USA (barras horizontales)

Instrucciones de uso:
1. Seleccionar semana de interés en el filtro superior
2. Opcionalmente filtrar por región específica
3. Explorar las 3 visualizaciones para obtener insights
4. Hacer hover sobre elementos para ver detalles en tooltips
```

---

### **4. readme.txt (OPCIONAL)**

**Contenido:**

```txt
INSTRUCCIONES DE EJECUCIÓN
==========================

ARCHIVOS INCLUIDOS:
-------------------
1. trending_by_time.csv      - Datos agregados del pipeline
2. presentacion.pdf          - Presentación del proyecto
3. link_tableau_public.txt   - URL del dashboard publicado
4. pipeline_etl.py           - Script del pipeline (opcional)

REQUISITOS:
-----------
- Tableau Public 2023.3 o superior
- Navegador web moderno (Chrome, Firefox, Safari)
- Conexión a internet para acceder al dashboard

CÓMO VISUALIZAR EL DASHBOARD:
------------------------------
1. Abrir link_tableau_public.txt
2. Copiar la URL
3. Pegar en navegador
4. Explorar el dashboard interactivo

DATOS:
------
Archivo: trending_by_time.csv
Período: [Indicar rango de fechas]
Regiones incluidas: US, GB, CA, DE, FR, etc.
Categorías: Music, Entertainment, News & Politics, etc.

PIPELINE ETL (si se incluye):
-----------------------------
Lenguaje: Python 3.7+
Librerías requeridas:
- pandas
- sqlalchemy
- psycopg2 (para PostgreSQL)

Para ejecutar el pipeline:
1. Instalar dependencias: pip install -r requirements.txt
2. Configurar credenciales de BD en config.py
3. Ejecutar: python pipeline_etl.py --start-date 2024-01-01 --end-date 2024-12-31

CONTACTO:
---------
Autor: [Tu nombre]
Email: [Tu email]
Bootcamp: TripleTen - Sprint 12
```

---

## ✅ CRITERIOS DE EVALUACIÓN

### **El Proyecto Será Aprobado Si:**

```
✅ Requisitos Técnicos:
   ├─ Archivo trending_by_time.csv incluido
   ├─ Datos correctamente agregados
   ├─ Dashboard publicado en Tableau Public
   ├─ Link funcional al dashboard
   └─ Presentación en PDF incluida

✅ Dashboard:
   ├─ Responde las 3 preguntas de negocio
   ├─ Visualizaciones apropiadas y claras
   ├─ Filtros funcionales
   ├─ Diseño profesional y organizado
   └─ Tooltips informativos

✅ Presentación:
   ├─ Explica el problema empresarial
   ├─ Describe el proceso seguido
   ├─ Muestra screenshots del dashboard
   ├─ Incluye insights clave
   └─ Formato profesional

✅ Proceso:
   ├─ Siguió el proceso correcto (Opción 4)
   ├─ Consultó requisitos con usuarios
   ├─ Consideró aspectos técnicos
   └─ Documentó decisiones
```

---

## 🎯 MEJORES PRÁCTICAS PARA EL PROYECTO

### **Dashboard:**

```
✅ DO (Hacer):
   • Usar títulos descriptivos y claros
   • Implementar filtros interactivos
   • Colores consistentes por categoría
   • Tooltips con información útil
   • Diseño limpio y organizado
   • Probar en modo presentación (F7)

❌ DON'T (No hacer):
   • Demasiados gráficos (máx 5)
   • Colores muy saturados
   • Texto muy pequeño (< 10pt)
   • Gráficos sin títulos
   • Leyendas innecesarias
   • Layout desorganizado
```

### **Presentación:**

```
✅ DO (Hacer):
   • Contar una historia clara
   • Screenshots de buena calidad
   • Resaltar insights clave
   • Explicar decisiones de diseño
   • Formato profesional y limpio

❌ DON'T (No hacer):
   • Solo texto sin imágenes
   • Screenshots borrosos
   • Demasiadas diapositivas (< 15)
   • Información técnica excesiva
   • Faltas de ortografía
```

---

## 🔄 CICLO DE REVISIÓN

### **Proceso de Evaluación:**

```
1. Subir proyecto inicial
   └─ ZIP < 9 MB

2. Esperar feedback (48 horas)
   └─ Revisor evaluará el proyecto

3. Recibir comentarios
   └─ Posibles áreas de mejora

4. Hacer correcciones
   └─ Implementar sugerencias

5. Reenviar proyecto
   └─ Segunda evaluación

6. Repetir si es necesario
   └─ Ciclos normales de revisión

7. Aprobación final
   └─ ¡Proyecto completado! 🎉
```

**Nota:** Es común pasar por varios ciclos. ¡No te desanimes!

---

## 💡 CONSEJOS FINALES

### **Para el Dashboard:**

```
1. Simplicidad primero
   → Enfócate en responder las 3 preguntas clave

2. Prueba con usuarios
   → Pide a alguien que lo use sin explicaciones

3. Optimiza el performance
   → Usa datos agregados, no datos brutos

4. Documenta tus decisiones
   → Explica por qué elegiste cada visualización

5. Itera basado en feedback
   → La primera versión rara vez es perfecta
```

### **Para la Presentación:**

```
1. Cuenta una historia
   → Problema → Proceso → Solución → Impacto

2. Usa visuales
   → Screenshots > Texto

3. Destaca insights
   → ¿Qué aprendiste de los datos?

4. Sé conciso
   → 10-15 diapositivas máximo

5. Revisa ortografía
   → Usa corrector antes de enviar
```

---

## 🎓 CONCLUSIÓN

Este proyecto te permite demostrar que dominas:

```
✅ Recopilación de requisitos
✅ Diseño de pipelines ETL
✅ Análisis de datos
✅ Visualización en Tableau
✅ Comunicación de resultados
✅ Pensamiento analítico
✅ Trabajo con stakeholders
```

**¡Éxito en tu proyecto!** 🚀

---

## 🎨 PARTE 2: CREAR EL DASHBOARD

### **Borrador del Dashboard:**

**Estructura del Dashboard (según imagen proporcionada):**

```
┌────────────────────────────────────────────────────────────┐
│  Tendencias de YouTube                                     │
│  [Filtro Fecha] [Filtro País]                             │ ← Header (10%)
├────────────────────────────────────────────────────────────┤
│                                                            │
│  HISTORIAL DE TENDENCIAS                                   │
│  (Gráfico de líneas/áreas - videos_count vs tiempo)       │ ← Main (30%)
│                                                            │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  HISTORIAL DE TENDENCIAS, %                                │
│  (Gráfico de áreas apiladas - porcentajes vs tiempo)      │ ← Second (30%)
│                                                            │
├───────────────────────────┬────────────────────────────────┤
│ DISTRIBUCIÓN POR          │  CATEGORÍAS TOP EN USA         │
│ REGIONES                  │  (Comparación USA vs Otros)    │ ← Details (30%)
│ (Mapa o gráfico regional) │  (Barras comparativas)         │
└───────────────────────────┴────────────────────────────────┘
```

### **Especificaciones Técnicas del Dashboard:**

#### **Filtros Globales:**

```
1. Filtro de Fecha/Tiempo:
   ├─ Tipo: Date Range Picker
   ├─ Campo: trending_date o week
   ├─ Aplicar a: TODAS las visualizaciones
   └─ Posición: Header superior izquierda

2. Filtro de País:
   ├─ Tipo: Dropdown (multi-select)
   ├─ Campo: country o region
   ├─ Opciones: US, GB, CA, DE, FR, etc.
   ├─ Aplicar a: TODAS las visualizaciones
   └─ Posición: Header superior derecha
```

#### **Visualización 1: Historial de Tendencias (Absolutos)**

```
Nombre: "Historial de Tendencias"
Tipo: Line Chart o Area Chart

Configuración:
├─ Eje X: trending_date (Exact Date o agregado por día/semana)
├─ Eje Y: SUM(videos_count)
├─ Color: category (opcional, para mostrar por categoría)
├─ Label: Valores en puntos clave
└─ Filtros afectan: Sí (fecha y país)

Objetivo: Mostrar cuántos videos estuvieron en tendencia a lo largo del tiempo
```

#### **Visualización 2: Historial de Tendencias, % (Relativos)**

```
Nombre: "Historial de Tendencias, %"
Tipo: Stacked Area Chart (100%)

Configuración:
├─ Eje X: trending_date (Exact Date o agregado)
├─ Eje Y: % of Total (Quick Table Calculation)
│  └─ Compute Using: Table (down) para % por fecha
├─ Color: category
├─ Stackgroup: Apilado al 100%
└─ Filtros afectan: Sí (fecha y país)

Objetivo: Mostrar la composición porcentual de categorías en cada período
```

#### **Visualización 3: Distribución por Regiones**

```
Nombre: "Distribución por Regiones"
Tipo: Symbol Map o Filled Map

Configuración:
├─ Geo: country o region
├─ Size/Color: SUM(videos_count)
├─ Label: Nombre del país + valor
├─ Tooltip: Detalles (país, categorías, count)
└─ Filtros afectan: Sí (fecha principalmente)

Objetivo: Mostrar qué regiones tienen más videos en tendencia
```

#### **Visualización 4: Categorías Top - USA vs Otros**

```
Nombre: "Categorías Populares: USA vs Otros"
Tipo: Grouped Bar Chart (barras agrupadas)

Configuración:
├─ Filas: category (ordenado por total descendente)
├─ Columnas: SUM(videos_count)
├─ Color: Segmento (USA vs Otros)
│  └─ Crear campo calculado:
│      IF [Country] = 'US' THEN 'USA' ELSE 'Otros' END
├─ Barmode: Group (lado a lado)
├─ Top 10: Mostrar solo top 10 categorías
└─ Filtros afectan: Sí (fecha)

Objetivo: Comparar qué categorías son populares en USA vs resto del mundo
```

---

## 📝 INSTRUCCIONES DETALLADAS

### **Paso 1: Preparar Datos en Tableau**

#### **1.1. Conectar Datos**

```
1. Abrir Tableau Public
2. Connect → Text file
3. Seleccionar: trending_by_time.csv
4. Verificar preview de datos
```

#### **1.2. Verificar Tipos de Datos**

```
Columna              Tipo Correcto       Rol
────────────────────────────────────────────────
trending_date        Date                 -
country/region       String               Dimension (Geographic)
category             String               Dimension
videos_count         Number (whole)       Measure
views (si existe)    Number (whole)       Measure
likes (si existe)    Number (whole)       Measure
```

**Si los tipos están mal:**
```
Clic en icono de tipo → Seleccionar tipo correcto
```

#### **1.3. Crear Campo Calculado (si necesario)**

**Campo: "Segmento"** (para USA vs Otros)

```
Clic derecho en Data pane → Create Calculated Field

Name: Segmento
Formula:
IF [Country] = 'US' THEN 'USA'
ELSE 'Otros'
END
```

---

### **Paso 2: Crear Visualizaciones**

#### **Hoja 1: Historial de Tendencias (Absolutos)**

```
Pasos:
1. Nueva hoja → Renombrar: "Historial Tendencias"

2. Arrastrar campos:
   ├─ Columns: trending_date
   │  └─ Cambiar a: Exact Date o Week
   ├─ Rows: SUM(videos_count)
   └─ Color: category (opcional)

3. Tipo de gráfico:
   └─ Show Me → Line Chart o Area Chart

4. Configurar eje Y:
   ├─ Clic derecho → Edit Axis
   └─ Title: "Número de Videos en Tendencia"

5. Configurar eje X:
   ├─ Clic derecho → Edit Axis
   └─ Title: "Fecha"

6. Agregar etiquetas (opcional):
   └─ Arrastra videos_count a Label
```

**Resultado esperado:**
```
Videos
  |
600|    ╱╲
500|   ╱  ╲    ╱╲
400|  ╱    ╲  ╱  ╲
300| ╱      ╲╱    ╲
  |___________________ Fecha
   Jan  Feb  Mar  Apr
```

---

#### **Hoja 2: Historial de Tendencias, %**

```
Pasos:
1. Duplicar hoja anterior:
   └─ Clic derecho en "Historial Tendencias" → Duplicate

2. Renombrar: "Historial Tendencias %"

3. Cambiar a porcentajes:
   ├─ Clic derecho en SUM(videos_count) en Rows
   ├─ Quick Table Calculation → Percent of Total
   └─ Compute Using → Table (down)
      (para que cada fecha sume 100%)

4. Cambiar a Stacked Area:
   ├─ Show Me → Area Chart
   └─ Asegurar que category está en Color

5. Configurar para 100%:
   └─ Analysis → Percentage Of → Table (down)

6. Ajustar eje Y:
   ├─ Clic derecho → Edit Axis
   └─ Title: "Porcentaje de Videos (%)"

7. Verificar stackgroup:
   └─ Todas las áreas deben sumar 100% en cada fecha
```

**Resultado esperado:**
```
100%|████████████████████ Music
 80%|██████████████░░░░░░ Entertainment
 60%|████████░░░░░░░░░░░░ News & Politics
 40%|██░░░░░░░░░░░░░░░░░░ Gaming
  0%|____________________ Other
     Jan  Feb  Mar  Apr
```

---

#### **Hoja 3: Distribución por Regiones**

```
Pasos:
1. Nueva hoja → Renombrar: "Distribución Regional"

2. Arrastrar campos:
   ├─ Double-click en country (si es geo, genera mapa automático)
   │  O arrastrar country a área de visualización
   └─ Arrastra videos_count a Size y Color

3. Seleccionar tipo de mapa:
   └─ Show Me → Symbol Map (círculos)
      O Filled Map (regiones coloreadas)

4. Configurar tooltip:
   ├─ Clic en Tooltip en Marks
   └─ Editar:
      <b><Country></b>
      Videos en Tendencia: <SUM(videos_count)>
      
5. Ajustar colores:
   ├─ Clic en Color
   └─ Edit Colors → Seleccionar paleta apropiada

6. Agregar etiquetas (opcional):
   └─ Arrastra country a Label
```

**Resultado esperado:**
```
       MAPA MUNDIAL
   ┌────────────────────┐
   │   ●●●         ●●   │  US (grande)
   │      ●    ●         │  GB, DE
   │  ●      ●           │
   │    ●                │
   └────────────────────┘
   
   Tamaño = Cantidad de videos
```

---

#### **Hoja 4: USA vs Otros**

```
Pasos:
1. Nueva hoja → Renombrar: "USA vs Otros"

2. Crear campo calculado "Segmento":
   IF [Country] = 'US' THEN 'USA' ELSE 'Otros' END

3. Arrastrar campos:
   ├─ Rows: category
   ├─ Columns: SUM(videos_count)
   └─ Color: Segmento

4. Seleccionar tipo:
   └─ Show Me → Horizontal Bar Chart

5. Configurar barras agrupadas:
   └─ Asegurar que barras estén lado a lado (grouped)

6. Ordenar por total:
   ├─ Clic en eje de categorías
   └─ Sort → Sort by: Field → SUM(videos_count) → Descending

7. Top 10 (opcional):
   ├─ Arrastra category a Filters
   └─ Top → By field → Top 10 by SUM(videos_count)

8. Ajustar colores:
   ├─ USA: Azul (#1f77b4)
   └─ Otros: Naranja (#ff7f0e)
```

**Resultado esperado:**
```
Music             ████████████ USA
                  ████████ Otros

Entertainment     ██████████ USA
                  ████████████ Otros

Gaming            ██████ USA
                  ████████ Otros

News & Politics   ████████ USA
                  ██████ Otros
```

---

### **Paso 3: Construir el Dashboard**

#### **3.1. Crear Nuevo Dashboard**

```
1. Clic en New Dashboard (icono inferior)
   O Dashboard → New Dashboard

2. Configurar tamaño:
   └─ Size: Automatic (recomendado)
      O Desktop (1366 x 768)
```

#### **3.2. Agregar Estructura**

```
1. Agregar contenedores verticales:
   ├─ Arrastra "Vertical" del área Objects
   └─ Repetir para dividir dashboard en secciones

Estructura:
┌────────────────────┐
│ Contenedor 1       │ ← Título + Filtros
├────────────────────┤
│ Contenedor 2       │ ← Historial Absolutos
├────────────────────┤
│ Contenedor 3       │ ← Historial %
├────────────────────┤
│ Contenedor 4       │ ← Mapa + USA vs Otros
└────────────────────┘
```

#### **3.3. Agregar Título**

```
1. Arrastra "Text" de Objects al contenedor superior
2. Escribir: "Dashboard de Tendencias de YouTube"
3. Formato:
   ├─ Font: Tableau Book (o Arial)
   ├─ Size: 16-18 pt
   ├─ Bold: Sí
   └─ Alignment: Center
```

#### **3.4. Agregar Filtros**

```
Filtro 1: Fecha
──────────────
1. Clic en cualquier hoja del dashboard
2. Clic en ▼ (menú) → Filters → trending_date
3. Posicionar en header, lado izquierdo
4. Configurar display:
   ├─ Edit Filter → Show
   └─ Single Value (slider) o Range of Dates

5. Aplicar a todas las hojas:
   ├─ Clic en ▼ del filtro
   ├─ Apply to Worksheets
   └─ All Using This Data Source ✅

Filtro 2: País
──────────────
1. Desde cualquier hoja → Filters → country
2. Posicionar en header, lado derecho
3. Configurar display:
   ├─ Edit Filter → Show
   └─ Multiple Values (dropdown)

4. Aplicar a todas las hojas:
   └─ Apply to Worksheets → All Using This Data Source ✅
```

#### **3.5. Agregar Hojas**

```
Orden sugerido:
1. Arrastra "Historial Tendencias" al contenedor 2
   └─ Ocupa ancho completo

2. Arrastra "Historial Tendencias %" al contenedor 3
   └─ Ocupa ancho completo

3. Para contenedor 4 (dividido):
   a. Arrastra "Horizontal" container
   b. Arrastra "Distribución Regional" a la izquierda (50%)
   c. Arrastra "USA vs Otros" a la derecha (50%)
```

#### **3.6. Limpiar Leyendas**

```
Para cada leyenda innecesaria:
├─ Hover sobre leyenda
├─ Clic en ▼
└─ Remove from Dashboard

Mantener solo leyendas útiles (ej: category)
```

#### **3.7. Ajustar Alturas**

```
Para cada visualización:
├─ Clic en gráfico
├─ Clic en ▼
└─ Fit → Entire View
   (para que se ajuste al espacio disponible)
```

---

### **Paso 4: Publicar en Tableau Public**

#### **4.1. Guardar Localmente Primero**

```
1. File → Save to Tableau Public As...
2. Login con tu cuenta de Tableau Public
3. Nombre: "YouTube_Trending_Dashboard"
```

#### **4.2. Configurar Privacidad**

```
1. En la ventana de publicación:
   └─ ✅ "Show workbook sheets as tabs"
   └─ ✅ "Allow others to see and download the workbook"

2. Click "Save"
```

#### **4.3. Verificar Accesibilidad**

```
Después de publicar:
1. Copiar URL generada
2. Abrir en navegador incógnito
3. Verificar que carga correctamente
4. Probar filtros

URLs típicas:
https://public.tableau.com/profile/[usuario]/#!/vizhome/YouTube_Trending_Dashboard/Dashboard
```

#### **4.4. Editar Detalles (Opcional)**

```
En Tableau Public online:
1. Edit Details
2. Agregar:
   ├─ Título descriptivo
   ├─ Descripción breve
   ├─ Tags: youtube, trending, analytics
   └─ Thumbnail (screenshot automático)
```

---

### **Paso 5: Responder Preguntas de Negocio**

#### **Usar el Dashboard para Responder:**

**Pregunta 1: ¿Qué categorías estuvieron en tendencia más frecuentemente?**

```
Análisis:
├─ Mirar "Historial Tendencias %" (áreas apiladas)
├─ Identificar categorías con mayor área
└─ Verificar en "Historial Tendencias" (absolutos)

Proceso:
1. Ajustar filtro de fecha: Todo el período disponible
2. Filtro de país: All (todos)
3. Observar en gráfico de %: ¿Qué colores dominan?
4. Observar en gráfico absoluto: ¿Qué líneas/áreas son más altas?

Respuesta esperada (ejemplo):
"Las categorías más frecuentes fueron:
 1. Music (25% del total)
 2. Entertainment (22%)
 3. Gaming (15%)
 4. News & Politics (12%)
 5. How-to & Style (10%)"

Evidencia: Screenshot de ambos gráficos de historial
```

**Pregunta 2: ¿Cómo se distribuyeron en las regiones?**

```
Análisis:
├─ Mirar "Distribución Regional" (mapa)
├─ Identificar países/regiones con más actividad
└─ Comparar tamaños de círculos o intensidad de colores

Proceso:
1. Filtro de fecha: Todo el período
2. Filtro de país: All
3. Observar mapa: ¿Qué regiones tienen círculos más grandes?
4. Hacer hover para ver valores exactos

Respuesta esperada (ejemplo):
"Distribución por regiones:
 1. Estados Unidos (US): 35% de los videos
 2. Reino Unido (GB): 18%
 3. Canadá (CA): 12%
 4. Alemania (DE): 10%
 5. Francia (FR): 8%
 6. Otros: 17%

Estados Unidos domina claramente con más de un tercio
de todos los videos en tendencia."

Evidencia: Screenshot del mapa con tooltips visibles
```

**Pregunta 3: ¿Categorías populares en USA? ¿Diferencias con otros lugares?**

```
Análisis:
├─ Mirar "USA vs Otros" (barras comparativas)
├─ Identificar diferencias entre barras azules (USA) y naranjas (Otros)
└─ Buscar patrones únicos de USA

Proceso:
1. Observar gráfico "USA vs Otros"
2. Identificar categorías donde USA > Otros
3. Identificar categorías donde Otros > USA
4. Buscar categorías exclusivas o muy diferentes

Respuesta esperada (ejemplo):
"Categorías populares en USA:
 
 Similares en USA y Otros:
 • Music: Popular en ambos
 • Entertainment: Popular en ambos
 • Gaming: Popular en ambos
 
 MÁS populares en USA:
 • News & Politics: 15% en USA vs 8% en Otros
 • Sports: 12% en USA vs 6% en Otros
 • How-to & Style: 10% en USA vs 7% en Otros
 
 MÁS populares en Otros:
 • Comedy: 18% en Otros vs 10% en USA
 • People & Blogs: 14% en Otros vs 8% en USA
 
 Diferencias clave:
 - USA consume más contenido de noticias y deportes
 - Resto del mundo prefiere más comedia y vlogs
 - Music y Entertainment son universales"

Evidencia: Screenshot de gráfico comparativo + tabla de valores
```

---

### **Paso 6: Crear Presentación**

#### **Estructura de la Presentación (PDF):**

```
Diapositiva 1: PORTADA
├─ Título: Dashboard de Tendencias de YouTube
├─ Subtítulo: Análisis de Categorías y Regiones
├─ Nombre: [Tu nombre]
├─ Bootcamp: TripleTen - Sprint 12
└─ Fecha: [Fecha actual]

Diapositiva 2: CONTEXTO
├─ Problema: Consultas manuales semanales
├─ Usuarios: Melanie y Ashok
├─ Preguntas recurrentes (3)
└─ Solución: Dashboard automatizado

Diapositiva 3: DASHBOARD - VISTA GENERAL
├─ Screenshot completo del dashboard
└─ Destacar 4 visualizaciones principales

Diapositiva 4: PREGUNTA 1 - CATEGORÍAS MÁS FRECUENTES
├─ Pregunta: ¿Qué categorías en tendencia más frecuentemente?
├─ Screenshot: Gráficos de historial (absoluto + %)
├─ Respuesta: Lista top 5 categorías con porcentajes
└─ Insight: Music y Entertainment dominan

Diapositiva 5: ANÁLISIS TEMPORAL
├─ Screenshot: Zoom en período específico
├─ Observación: ¿Tendencias cambian con el tiempo?
└─ Insight: Patrones estacionales o eventos específicos

Diapositiva 6: PREGUNTA 2 - DISTRIBUCIÓN REGIONAL
├─ Pregunta: ¿Cómo se distribuyeron en regiones?
├─ Screenshot: Mapa de distribución
├─ Respuesta: Ranking de países con porcentajes
└─ Insight: USA domina, seguido por países anglófonos

Diapositiva 7: PREGUNTA 3 - USA VS OTROS (Parte 1)
├─ Pregunta: ¿Categorías populares en USA?
├─ Screenshot: Gráfico comparativo USA vs Otros
├─ Respuesta: Top categorías en USA
└─ Destacar valores

Diapositiva 8: PREGUNTA 3 - DIFERENCIAS (Parte 2)
├─ Pregunta: ¿Diferencias entre USA y otros lugares?
├─ Tabla comparativa:
│  Categoría         USA    Otros   Diferencia
│  News & Politics   15%    8%      +7% USA
│  Comedy            10%    18%     +8% Otros
├─ Insight clave: USA prefiere noticias, mundo prefiere comedia
└─ Hipótesis: Diferencias culturales y eventos locales

Diapositiva 9: INSIGHTS ADICIONALES
├─ Insight 1: Music es universal (top en todos)
├─ Insight 2: Gaming creciente en ambos
├─ Insight 3: News & Politics correlaciona con eventos
└─ Insight 4: Entertainment estable a lo largo del tiempo

Diapositiva 10: RECOMENDACIONES
├─ Para Melanie y Ashok:
│  ├─ Usar dashboard semanalmente los lunes
│  ├─ Filtrar por período de interés
│  └─ Exportar datos si necesitan análisis adicional
├─ Para la agencia:
│  ├─ Enfocar campañas en Music y Entertainment (universales)
│  ├─ Adaptar contenido por región (News en USA, Comedy en Europa)
│  └─ Aprovechar tendencias estacionales
└─ Monitoreo: Revisar dashboard antes de lanzar campañas

Diapositiva 11: LIMITACIONES Y PRÓXIMOS PASOS
├─ Limitaciones actuales:
│  ├─ Datos solo de países principales
│  ├─ No incluye métricas de engagement (likes, comments)
│  └─ Sin análisis de videos específicos
├─ Próximos pasos:
│  ├─ Agregar más regiones
│  ├─ Incluir métricas de rendimiento
│  ├─ Análisis de canales top
│  └─ Predicción de tendencias
└─ Feedback bienvenido

Diapositiva 12: CONCLUSIONES
├─ Dashboard cumple objetivos
├─ Automatiza análisis semanal
├─ Responde las 3 preguntas clave
├─ Usuarios pueden explorar datos independientemente
└─ URL del dashboard: [link]

Diapositiva 13: ¿PREGUNTAS?
├─ Contacto: [Tu email]
├─ URL Dashboard: [Link a Tableau Public]
└─ Repositorio: [Si aplica]
```

---

## 📊 CHECKLIST ANTES DE ENVIAR

### **Dashboard en Tableau Public:**

```
✅ Conectado a trending_by_time.csv
✅ 4 visualizaciones creadas:
   ├─ Historial Tendencias (absoluto)
   ├─ Historial Tendencias (%)
   ├─ Distribución Regional
   └─ USA vs Otros
✅ 2 filtros globales funcionando:
   ├─ Fecha/Tiempo
   └─ País
✅ Filtros aplicados a TODAS las visualizaciones
✅ Layout organizado y profesional
✅ Títulos claros en cada gráfico
✅ Leyendas apropiadas (no excesivas)
✅ Tooltips informativos
✅ Publicado en Tableau Public
✅ URL accesible públicamente
✅ Probado en múltiples navegadores:
   ├─ Chrome
   ├─ Firefox
   └─ Safari (si disponible)
✅ Dashboard carga rápidamente (< 5 segundos)
```

### **Presentación PDF:**

```
✅ 10-13 diapositivas
✅ Portada con información completa
✅ Screenshots de calidad del dashboard
✅ 3 preguntas respondidas con evidencia
✅ Insights y recomendaciones incluidas
✅ Formato profesional y limpio
✅ Sin errores de ortografía
✅ Gráficos legibles (no pixelados)
✅ URL del dashboard incluida
✅ Conclusiones claras
```

### **Archivo ZIP:**

```
✅ Tamaño < 9 MB
✅ Contiene:
   ├─ trending_by_time.csv
   ├─ presentacion.pdf
   ├─ link_tableau_public.txt
   └─ readme.txt (opcional)
✅ Nombre del archivo: proyecto_sprint12_[tu_nombre].zip
✅ Sin archivos innecesarios (no .DS_Store, Thumbs.db, etc.)
```

---

## 💡 CONSEJOS FINALES PARA EL DASHBOARD

### **Diseño Visual:**

```
✅ DO (Hacer):
   • Colores consistentes por categoría
   • Espacio en blanco suficiente
   • Fuentes legibles (mín 10pt)
   • Títulos descriptivos
   • Leyenda solo si necesaria

❌ DON'T (No hacer):
   • Demasiados colores (máx 10)
   • Gráficos apretados
   • Texto muy pequeño
   • Animaciones excesivas
   • Leyendas duplicadas
```

### **Interactividad:**

```
✅ DO (Hacer):
   • Filtros fáciles de usar
   • Tooltips informativos
   • Hover effects claros
   • Respuesta rápida (< 2 seg)

❌ DON'T (No hacer):
   • Demasiados filtros (2-3 max)
   • Tooltips con info innecesaria
   • Delays largos al filtrar
```

### **Análisis:**

```
✅ DO (Hacer):
   • Responder las 3 preguntas claramente
   • Proporcionar evidencia visual
   • Incluir insights adicionales
   • Ser específico con números

❌ DON'T (No hacer):
   • Respuestas vagas
   • Sin evidencia
   • Solo describir sin analizar
   • Números sin contexto
```

---

**Última actualización:** Sprint 12 - Proyecto (Parte 2 - Creación del Dashboard)  
**Bootcamp:** TripleTen  
**Tipo:** Proyecto Final de Sprint

