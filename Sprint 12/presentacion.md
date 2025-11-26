---
marp: true
theme: default
paginate: true
header: 'Dashboard de Tendencias de YouTube - Sprint 12'
footer: 'TripleTen Bootcamp - Raul A. Espinoza'
---

# Dashboard de Tendencias de YouTube

## Proyecto Sprint 12 - Automatización

**Bootcamp:** TripleTen  
**Sprint:** 12 - Automatización  
**Estudiante:** Raul A. Espinoza

---

## 📋 Contexto del Proyecto

### Problema Identificado

**Situación:**
- Analizamos tendencias de videos en YouTube manualmente
- Cada semana, Melanie y Ashok hacen las mismas 3 preguntas
- 6 semanas respondiendo manualmente → **Necesidad de automatización**

**Preguntas Recurrentes:**
1. ¿Qué categorías estaban en tendencias la semana pasada?
2. ¿Cómo se distribuyeron en diversas regiones?
3. ¿Qué categorías fueron particularmente populares en Estados Unidos?

---

## 🎯 Solución Implementada

### Dashboard Interactivo en Tableau Public

**Objetivo:**
Crear un dashboard automatizado que permita a Melanie y Ashok consultar los datos por sí mismos, eliminando la necesidad de consultas manuales semanales.

**Herramienta:** Tableau Public (Web Authoring)

**Link del Dashboard:**
https://public.tableau.com/views/Raul-YouTube_Trends_Dashboard/DashboardYouTubeTrends

---

## 📊 Visualizaciones del Dashboard

### 1. Historial de Tendencias por Categoría
- **Tipo:** Gráfico de líneas (valores absolutos)
- **Muestra:** Evolución temporal del número de videos en tendencia por categoría
- **Utilidad:** Identificar categorías que mantienen tendencia constante

### 2. Historial de Tendencias (% del Total)
- **Tipo:** Gráfico de líneas (porcentajes)
- **Muestra:** Proporción de cada categoría respecto al total de videos en tendencia
- **Utilidad:** Entender la distribución relativa de interés por categoría

---

## 📊 Visualizaciones del Dashboard (Cont.)

### 3. Distribución de Videos por Región
- **Tipo:** Mapa de símbolos (Symbol Map)
- **Muestra:** Concentración geográfica de videos en tendencia
- **Utilidad:** Identificar regiones con mayor actividad y distribución geográfica

### 4. Top Categorías: USA vs Otros Países
- **Tipo:** Gráfico de barras agrupadas
- **Muestra:** Comparación directa de categorías populares entre USA y resto del mundo
- **Utilidad:** Identificar preferencias específicas del mercado estadounidense

---

## 🎛️ Controles Interactivos

### Filtros Globales

**Filtro de Fecha:**
- Permite seleccionar rango de fechas específico
- Afecta a todas las visualizaciones simultáneamente

**Filtro de Región:**
- Permite seleccionar países/regiones específicas
- Afecta a todas las visualizaciones simultáneamente

**Beneficio:** Análisis dinámico y personalizado según necesidades del momento

---

## 📝 Respuesta a Pregunta 1

### ¿Qué categorías de videos fueron tendencia durante todo el período?

**Respuesta:**

Claramente se puede ver en la gráfica que fueron los de **"Entertainment" (Entretenimiento)**.

**Análisis Detallado:**
- La categoría "Entertainment" muestra una línea consistente y prominente a lo largo de todo el período
- Mantiene niveles altos de videos en tendencia de manera constante (entre 2,500 y 3,500 videos)
- Es la categoría dominante en términos de volumen absoluto de videos
- Otras categorías con presencia constante pero menor: "Education", "Nonprofits & Activism", "News & Politics"

**Visualización:** Historial de Tendencias por Categoría

---

## 📝 Respuesta a Pregunta 2

### ¿Cómo se distribuyó el interés por categorías entre regiones?

**Respuesta:**

Excluyendo a Japón, el interés se mantuvo bastante alto y estable, entre los **70 y 80k videos**.

**Análisis Detallado:**
- Las regiones principales (Estados Unidos, Francia, India, Reino Unido) muestran niveles consistentes de actividad
- El mapa muestra círculos grandes y oscuros en estas regiones, indicando alta concentración de videos (rango: 36,762 - 80,758 videos)
- Estados Unidos presenta el mayor volumen con aproximadamente 80,758 videos
- Francia, India y Reino Unido muestran niveles similares entre 70k-75k videos
- Japón muestra un volumen significativamente menor comparado con otras regiones
- La distribución es relativamente uniforme entre las principales regiones, con variaciones menores

**Visualización:** Distribución de Videos por Región (Mapa)

---

## 📝 Respuesta a Pregunta 3

### ¿Qué categorías fueron especialmente populares en Estados Unidos?

**Respuesta:**

De las categorías especiales para USA se pueden destacar:
- **Entertainment (Entretenimiento)** - ~45,000 videos en USA
- **Music (Música)** - ~12,000 videos en USA
- **Howto & Style** - ~8,000 videos en USA

**Análisis Detallado:**
- Estas categorías muestran barras naranjas (USA) relativamente más altas comparadas con otras categorías
- Aunque ninguna supera a "Otros" en términos absolutos, estas tres muestran una proporción más equilibrada entre USA y resto del mundo
- **Entertainment** es la categoría más popular en USA, con aproximadamente 45,000 videos, aunque "Otros" tiene 70,000
- **Music** muestra una diferencia menor: USA tiene 12,000 vs 22,000 de "Otros"
- **Howto & Style** tiene 8,000 en USA vs 12,000 en "Otros", mostrando un interés relativamente alto en el mercado estadounidense
- Indican preferencias específicas del mercado estadounidense para contenido educativo/práctico y entretenimiento

**Visualización:** Top Categorías: USA vs Otros Países

---

## ✅ Beneficios del Dashboard

### Para Melanie y Ashok:
- ✅ **Autonomía:** Pueden consultar datos sin depender del analista
- ✅ **Tiempo real:** Acceso inmediato a información actualizada
- ✅ **Interactividad:** Filtros permiten análisis personalizados
- ✅ **Visualización clara:** Información presentada de forma intuitiva

### Para la Agencia:
- ✅ **Eficiencia:** Eliminación de consultas manuales semanales
- ✅ **Escalabilidad:** Fácil agregar nuevas métricas o visualizaciones
- ✅ **Toma de decisiones:** Información accesible para decisiones estratégicas

---

## 🎯 Conclusiones

### Logros del Proyecto:
1. ✅ Dashboard funcional publicado en Tableau Public
2. ✅ 4 visualizaciones interactivas implementadas
3. ✅ Filtros globales configurados correctamente
4. ✅ Respuestas claras a las 3 preguntas recurrentes

### Impacto:
- **Automatización completa** del proceso de análisis semanal
- **Reducción de tiempo** en consultas manuales
- **Mejora en la toma de decisiones** basada en datos

---

## 📚 Recursos y Enlaces

**Dashboard Publicado:**
https://public.tableau.com/views/Raul-YouTube_Trends_Dashboard/DashboardYouTubeTrends

**Datos Utilizados:**
- Archivo: `trending_by_time.csv`
- Período: Noviembre 2017
- Regiones: USA, Francia, India, Japón, Reino Unido

**Herramientas:**
- Tableau Public (Web Authoring)
- Visualizaciones: Líneas, Mapa, Barras agrupadas

---

## 🙏 Gracias

### Preguntas y Comentarios

**Contacto:**
- Estudiante: Raul A. Espinoza
- Bootcamp: TripleTen
- Sprint: 12 - Automatización

---

