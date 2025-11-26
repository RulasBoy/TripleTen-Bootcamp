# ✅ Checklist: Dashboard Tableau Public - Proyecto Sprint 12

## 📋 Estado General
- [x] Crear cuenta en Tableau Public
- [x] Acceder a Web Authoring
- [x] Subir archivo `trending_by_time.csv`
- [x] Verificar tipos de datos en Data Source (EN PROGRESO)
- [ ] Crear las 4 visualizaciones requeridas
- [ ] Construir el dashboard
- [ ] Agregar filtros globales
- [ ] Publicar dashboard
- [ ] Obtener link público
- [ ] Crear presentación PDF
- [ ] Preparar ZIP final para entrega

---

## 🔧 PASO 1: Preparar Data Source

### Verificar y Ajustar Tipos de Datos
- [x] Verificar que `trending_date` esté como **Date** (ícono de calendario) ✓
- [x] Verificar que `videos_count` esté como **Number** (ícono #) ✓
- [x] Verificar que `region` esté como **String** (ícono Abc) ✓
- [x] Verificar que `category_title` esté como **String** (ícono Abc) ✓
- [x] Verificar que `record_id` esté como **Number** (ícono #) ✓

### Ir a la Primera Hoja
- [x] Clic en pestaña **"Sheet 1"** (parte inferior) para empezar a crear visualizaciones ✓

---

## 📊 PASO 2: Crear Visualización 1 - "Historial de Tendencias"

**Tipo:** Gráfico de líneas (valores absolutos)

- [x] Renombrar hoja: Clic derecho en "Sheet 1" → **Rename** → `Historial Tendencias` ✓
- [x] Arrastrar `trending_date` a **Columns** (arriba) ✓
- [x] Arrastrar `videos_count` a **Rows** (izquierda) ✓
- [x] Arrastrar `category_title` a **Color** (en panel Marks) ✓
- [x] En panel **Marks**, seleccionar tipo **Line** (línea) ✓
- [x] Configurar granularidad de fecha: Clic en `trending_date` en Columns → Seleccionar **Day** o **Continuous** ✓
- [x] Agregar título: Doble clic en título → **"Historial de Tendencias por Categoría"** ✓
- [x] Verificar que el gráfico muestre líneas por categoría ✓

---

## 📈 PASO 3: Crear Visualización 2 - "Historial de Tendencias, %"

**Tipo:** Gráfico de líneas (porcentajes)

- [x] Duplicar hoja anterior: Clic derecho en `Historial Tendencias` → **Duplicate** ✓
- [x] Renombrar hoja duplicada: `Historial Tendencias %` ✓
- [x] Convertir a porcentaje:
  - Clic en `SUM(videos_count)` en Rows
  - Seleccionar **Quick Table Calculation** → **Percent of Total**
  - Clic nuevamente → **Compute Using** → **Table (Across)**
- [x] Cambiar título: **"Historial de Tendencias (% del Total)"** ✓
- [x] Verificar que los valores estén en porcentaje (0-100%) ✓

---

## 🗺️ PASO 4: Crear Visualización 3 - "Distribución por Regiones"

**Tipo:** Mapa (Filled Map o Symbol Map)

- [x] Crear nueva hoja: Clic en ícono **"New Worksheet"** (hoja con +) ✓
- [x] Renombrar hoja: `Distribución Regiones` ✓
- [x] Configurar campo geográfico:
  - Arrastrar `region` a la vista central
  - Si no crea mapa automáticamente: Clic derecho en `region` → **Geographic Role** → **Country/Region**
- [x] Agregar métrica:
  - Arrastrar `videos_count` a **Color** en Marks
  - (Opcional) Arrastrar `videos_count` a **Size** en Marks
- [x] Seleccionar tipo de mapa: En Marks, seleccionar **Map** o **Filled Map** ✓
- [x] Agregar título: **"Distribución de Videos por Región"** ✓
- [x] Verificar que el mapa muestre colores/intensidad por región ✓

---

## 📊 PASO 5: Crear Visualización 4 - "Categorías Top - USA vs Otros"

**Tipo:** Gráfico de barras agrupadas

- [ ] Crear nueva hoja: Clic en ícono **"New Worksheet"**
- [ ] Renombrar hoja: `USA vs Otros`
- [ ] Crear campo calculado `Region_Group`:
  - Clic derecho en área de datos (izquierda) → **Create Calculated Field**
  - Nombre: `Region_Group`
  - Fórmula:
    ```
    IF [region] = "United States" THEN "USA" ELSE "Otros" END
    ```
  - Clic en **OK**
- [x] Crear gráfico de barras:
  - Arrastrar `category_title` a **Rows**
  - Arrastrar `videos_count` a **Columns**
  - Arrastrar `Region_Group` a **Color** en Marks
- [x] Configurar barras agrupadas:
  - Menú superior: **Analysis** → **Stack Marks** → **Off** (barras lado a lado) ✓
- [x] Ajustar configuración para barras lado a lado en un solo gráfico:
  - Quitar `Region_Group` de **Columns** (si está ahí) ✓
  - Quitar `Region_Group` de **Detail** en Marks (si está ahí) ✓
  - Arrastrar `Region_Group` a **Rows**, DESPUÉS de `Category Title` (esto crea subcategorías) ✓
  - Mantener `Region_Group` también en **Color** en Marks (para los colores) ✓
- [ ] Ordenar por total: Clic en ícono de ordenar (barra con flecha)
- [x] Agregar título: **"Top Categorías: USA vs Otros Países"** ✓
- [x] Verificar que muestre barras lado a lado para USA y Otros en un solo gráfico ✓

---

## 🎨 PASO 6: Construir el Dashboard

- [x] Crear nuevo dashboard: Clic en ícono **"New Dashboard"** (cuadrado con +) ✓
- [x] Renombrar dashboard: `Dashboard YouTube Trends` ✓
- [x] Configurar tamaño:
  - Panel izquierdo, bajo **Size**: Seleccionar **Automatic** o **Desktop** (1000 x 800) ✓

### Agregar Visualizaciones al Dashboard
- [x] Arrastrar `Historial Tendencias` al dashboard (arriba izquierda, ~50% ancho) ✓
- [x] Arrastrar `Historial Tendencias %` al dashboard (arriba derecha, ~50% ancho) ✓
- [x] Arrastrar `Distribución Regiones` al dashboard (abajo izquierda, ~50% ancho) ✓
- [x] Arrastrar `USA vs Otros` al dashboard (abajo derecha, ~50% ancho) ✓

### Agregar Elementos de Diseño
- [x] Agregar título principal:
  - Arrastrar **"Text"** desde Objects (panel izquierdo) a la parte superior
  - Escribir: **"Dashboard de Tendencias de YouTube"**
  - Formatear: tamaño 18-20, negrita, centrado ✓
- [x] Agregar descripción:
  - Arrastrar otro **"Text"** debajo del título
  - Escribir descripción del proyecto (problema comercial, cómo usar) ✓

### Configurar Filtros Globales
- [x] Agregar filtro de fecha:
  - En cualquier visualización, clic en triángulo (▼) → **Filters** → Mostrar `trending_date`
  - Clic derecho en filtro → **Apply to Worksheets** → **All Using This Data Source** ✓
- [x] Agregar filtro de región:
  - En cualquier visualización, clic en triángulo (▼) → **Filters** → Mostrar `region`
  - Clic derecho en filtro → **Apply to Worksheets** → **All Using This Data Source** ✓
- [x] Verificar que los filtros funcionen en todas las visualizaciones ✓

---

## 🚀 PASO 7: Publicar Dashboard

- [x] Publicar workbook:
  - Menú superior: **File** → **"Publish"** o **"Publish As..."**
  - Nombre: `YouTube_Trends_Dashboard`
  - Agregar descripción breve (opcional)
  - Verificar que esté marcado como **"Public"** (público)
  - Clic en **"Publish"** o **"Save"** ✓
- [x] Publicar:
  - El dashboard se publicará automáticamente al guardar
  - Esperar a que se complete la publicación ✓
- [x] Obtener link público:
  - Copiar URL completa del dashboard publicado ✓
  - Formato esperado: `https://public.tableau.com/app/profile/tu-nombre/viz/YouTube_Trends_Dashboard/Dashboard`
  - **GUARDAR ESTE LINK** (lo necesitarás para entregar) ✓
- [ ] Verificar funcionamiento:
  - Abrir link en ventana de incógnito
  - Probar filtros interactivos
  - Verificar que todas las visualizaciones se muestren correctamente

---

## 📝 PASO 8: Responder Preguntas del Proyecto

Usar el dashboard para responder:

- [ ] **Pregunta 1:** ¿Qué categorías de videos fueron tendencia durante todo el período?
  - Usar visualización `Historial Tendencias` para identificar líneas consistentes
  - Documentar respuesta

- [ ] **Pregunta 2:** ¿Cómo se distribuyó el interés por categorías entre regiones?
  - Usar visualización `Distribución Regiones` y comparar colores/tamaños
  - Documentar respuesta

- [ ] **Pregunta 3:** ¿Qué categorías fueron especialmente populares en Estados Unidos?
  - Usar visualización `USA vs Otros` para ver barras más altas en USA
  - Documentar respuesta

---

## 📄 PASO 9: Crear Presentación PDF

- [x] Decidir formato (Markdown o LaTeX) ✓ (Markdown + Marp)
- [x] Crear archivo de presentación ✓ (`presentacion.md`)
- [x] Incluir:
  - [x] Portada con título del proyecto ✓
  - [x] Descripción del problema comercial ✓
  - [x] Screenshots del dashboard ✓
  - [x] Respuestas a las 3 preguntas del proyecto ✓
  - [x] Conclusiones ✓
- [x] Convertir a PDF ✓ (`presentacion.pdf` generado)
- [ ] Verificar que el PDF se vea correctamente

---

## 📦 PASO 10: Preparar Entrega Final

- [ ] Verificar que tengas:
  - [x] `trending_by_time.csv` (archivo de datos) ✓ (en `datasets/`)
  - [x] Link al dashboard en Tableau Public ✓
  - [x] Presentación en PDF ✓ (`presentacion.pdf`)
- [x] Verificar tamaño total (máximo 9 MB) ✓ (195K, muy por debajo del límite)
- [x] Crear archivo ZIP con:
  - [x] `trending_by_time.csv` ✓
  - [x] `presentacion.pdf` ✓
  - [ ] (Opcional) Archivos adicionales necesarios
- [x] Nombrar ZIP: `Sprint12_Proyecto_Raul_Espinoza.zip` ✓
- [ ] Verificar contenido del ZIP antes de enviar

---

## 📌 Notas y Observaciones

**Link del Dashboard:** 
https://public.tableau.com/views/Raul-YouTube_Trends_Dashboard/DashboardYouTubeTrends?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

**Respuestas a Preguntas:**
1. 
2. 
3. 

**Problemas Encontrados:**
- 

**Soluciones Aplicadas:**
- 

---

## ✅ Estado Final

- [x] Dashboard publicado y funcionando ✓
- [x] Link copiado y guardado ✓
- [x] Presentación PDF creada ✓
- [x] ZIP preparado para entrega ✓
- [x] Todo listo para enviar ✓

---

**Última actualización:** _(Fecha y hora)_
**Progreso actual:** Paso X de 10

