# Contexto del Proyecto: Optimización de Gastos de Marketing para Showz

## Sprint 9 - Proyecto de TripleTen Bootcamp

### Descripción del Proyecto

Este es un **proyecto de análisis de negocio** donde actúas como analista de datos en prácticas en el departamento de analítica de **Showz**, una empresa de venta de entradas de eventos. Tu primera tarea es ayudar a optimizar los gastos de marketing.

**Contexto del Rol**: Has sido contratado como analista en prácticas y tu primera tarea es crucial para el departamento de marketing.

---

## Descripción General del Proyecto

**Showz** es una empresa de venta de entradas para eventos que busca optimizar sus inversiones en marketing. El proyecto analiza el comportamiento de usuarios, evalúa la rentabilidad de diferentes canales de marketing y proporciona recomendaciones sobre dónde y cuánto invertir.

### Objetivos del Proyecto

1. **Análisis de Producto**: Entender cómo los usuarios interactúan con el servicio
   - Usuarios activos diarios, semanales y mensuales (DAU, WAU, MAU)
   - Duración y frecuencia de sesiones
   - Tasa de retorno de usuarios (sticky factor)

2. **Análisis de Ventas**: Evaluar el comportamiento de compra
   - Tiempo hasta la primera conversión
   - Frecuencia de pedidos
   - Ticket promedio de compra
   - LTV (Lifetime Value) por cliente

3. **Análisis de Marketing**: Medir la eficiencia de las inversiones
   - Gastos por fuente de adquisición
   - CAC (Customer Acquisition Cost)
   - ROMI (Return on Marketing Investment)

4. **Recomendaciones**: Identificar las fuentes más rentables y sugerir estrategias de inversión

### Datos Disponibles

- **Período de análisis**: Enero 2017 - Diciembre 2018
- **visits_log_us.csv**: Registros de visitas al sitio web
- **orders_log_us.csv**: Información sobre pedidos realizados
- **costs_us.csv**: Gastos de marketing por fuente y fecha

---

## Instrucciones del Proyecto (Sprint 9)

### Paso 1: Acceder a los Datos y Prepararlos para el Análisis

**Tareas**:
- Almacenar los datos de visitas, pedidos y gastos en variables
- Optimizar los datos para el análisis
- Asegurar que cada columna contenga el tipo de datos correcto

**Rutas de archivos**:
- `/datasets/visits_log_us.csv`
- `/datasets/orders_log_us.csv`
- `/datasets/costs_us.csv`

### Paso 2: Hacer Informes y Calcular Métricas

#### A. Análisis de Visitas
1. **¿Cuántas personas lo usan cada día, semana y mes?**
   - DAU (Daily Active Users)
   - WAU (Weekly Active Users)
   - MAU (Monthly Active Users)

2. **¿Cuántas sesiones hay por día?**
   - Un usuario puede tener más de una sesión

3. **¿Cuál es la duración de cada sesión?**
   - Duración promedio de sesión (ASL)

4. **¿Con qué frecuencia los usuarios regresan?**
   - Sticky factor (DAU/WAU o DAU/MAU)

#### B. Análisis de Ventas
1. **¿Cuándo empieza la gente a comprar?**
   - Tiempo entre registro y conversión (primera compra)
   - Categorías: Conversion 0d, Conversion 1d, etc.
   - Comparar conversiones de diferentes cohortes/canales

2. **¿Cuántos pedidos hacen durante un período de tiempo dado?**
   - Frecuencia de pedidos por usuario

3. **¿Cuál es el tamaño promedio de compra?**
   - Ticket promedio (Revenue promedio por pedido)

4. **¿Cuánto dinero traen? (LTV)**
   - Lifetime Value por cliente
   - LTV por cohorte

#### C. Análisis de Marketing
1. **¿Cuánto dinero se gastó?**
   - Total de gastos
   - Gastos por fuente de adquisición
   - Gastos a lo largo del tiempo

2. **¿Cuál fue el costo de adquisición de clientes de cada fuente?**
   - CAC (Customer Acquisition Cost) por fuente

3. **¿Cuán rentables eran las inversiones?**
   - ROMI (Return on Marketing Investment) por fuente

#### Visualizaciones Requeridas
- Trazar gráficos para mostrar cómo difieren las métricas para:
  - Varios dispositivos
  - Diferentes fuentes de anuncios
  - Cómo cambian con el tiempo

### Paso 3: Escribir una Conclusión

**Recomendaciones para Expertos de Marketing**:
- ¿Cuánto dinero invertir?
- ¿Dónde invertir?
- ¿Qué fuentes/plataformas recomendar?
- Fundamentar la selección:
  - ¿En qué métricas te enfocaste?
  - ¿Por qué esas métricas?
  - ¿Qué conclusiones sacaste?

### Formato del Proyecto

- **Herramienta**: Jupyter Notebook
- **Celdas de código**: Para el código Python
- **Celdas markdown**: Para explicaciones de texto
- **Formato**: Aplicar formato y encabezados apropiados

---

## Descripción Detallada de los Datos

### Tabla: visits (visits_log_us.csv)
Registros del servidor con datos sobre las visitas al sitio web.

**Columnas**:
- `Uid`: Identificador único del usuario
- `Device`: Dispositivo del usuario (ej: desktop, mobile, touch)
- `Start Ts`: Fecha y hora de inicio de la sesión
- `End Ts`: Fecha y hora de término de la sesión
- `Source Id`: Identificador de la fuente de anuncios de la que proviene el usuario

**Formato de fechas**: AAAA-MM-DD

### Tabla: orders (orders_log_us.csv)
Datos sobre pedidos realizados.

**Columnas**:
- `Uid`: Identificador único del usuario que realiza un pedido
- `Buy Ts`: Fecha y hora del pedido
- `Revenue`: El ingreso de Showz por el pedido

### Tabla: costs (costs_us.csv)
Datos sobre gastos de marketing.

**Columnas**:
- `source_id`: Identificador de la fuente de anuncios
- `dt`: Fecha
- `costs`: Gastos en esta fuente de anuncios en este día

---

## Criterios de Evaluación del Proyecto

Tu proyecto será evaluado según estos criterios. **Léelos atentamente antes de empezar**.

### Lo que Buscan los Revisores

1. **Preparación de Datos**
   - Cómo preparas los datos para el análisis
   - Manejo de tipos de datos
   - Limpieza y transformación de datos

2. **Visualizaciones**
   - Qué gráficos trazas para las métricas
   - Calidad y claridad de las visualizaciones
   - Relevancia de los gráficos para responder las preguntas

3. **Interpretación**
   - Cómo interpretas los gráficos resultantes
   - Capacidad de extraer insights de los datos
   - Análisis crítico de los resultados

4. **Cálculo de Métricas**
   - Cómo calculas cada parámetro
   - Correctitud de los cálculos
   - Interpretación de cada métrica

5. **Recomendaciones**
   - Cómo fundamentas tus recomendaciones para los expertos de marketing
   - Qué métricas utilizas para justificar las recomendaciones
   - Claridad y acción de las recomendaciones

6. **Estructura y Organización**
   - Si sigues la estructura del proyecto
   - Mantenimiento del código ordenado
   - Uso apropiado de celdas markdown y code

7. **Conclusiones**
   - Calidad de las conclusiones a las que llegas
   - Capacidad de síntesis
   - Relevancia para el negocio

8. **Documentación**
   - Si dejas comentarios en cada paso
   - Claridad de las explicaciones
   - Documentación del proceso de análisis

### Proceso de Revisión

1. **Primera entrega**: Enviar trabajo al revisor de proyecto
2. **Feedback inicial**: Recibir opinión en 24 horas
3. **Iteración**: Realizar cambios basados en comentarios
4. **Nueva versión**: Enviar versión actualizada
5. **Ciclos adicionales**: Es normal pasar por varios ciclos de comentarios y revisiones
6. **Aprobación**: El proyecto se considera completado una vez que el revisor lo apruebe

---

## Conceptos Clave del Bootcamp

### 1. Métricas de Usuario

#### Métricas de Actividad
- **DAU** (Daily Active Users): Número de usuarios únicos diarios
- **WAU** (Weekly Active Users): Número de usuarios únicos semanales
- **MAU** (Monthly Active Users): Número de usuarios únicos mensuales
- **Sticky Factor**: Fidelidad de la audiencia al producto
  - Fórmula: `DAU/WAU` o `DAU/MAU`

#### Sesiones de Usuario
- **Sesión**: Período entre apertura y cierre de aplicación/sitio
- **ASL** (Average Session Length): Duración promedio de sesión
- **Número de sesiones mensuales por usuario**: Indicador de frecuencia de uso

#### Frameworks de Métricas
- **HEART** (Google): Happiness, Engagement, Adoption, Retention, Task success
- **AARRR** (Métricas Pirata): Acquisition, Activation, Retention, Referral, Revenue

### 2. Métricas y Embudos

#### Métricas Financieras
- **Facturación/Ingreso bruto**: Dinero que clientes pagaron a la empresa
- **Costo directo**: Dinero que la empresa gasta para obtener un producto
- **Beneficio bruto**: `Facturación - Costo directo`
- **Margen bruto**: `Beneficio bruto / Ingresos`
- **Gastos operativos**: Gastos en actividades principales
- **Beneficio operativo**: `Beneficio bruto - Gastos operativos`
- **Margen operativo**: `Beneficio operativo / Ingresos`
- **Beneficio neto**: `Beneficio operativo - Impuestos y préstamos`

#### Métricas de Inversión
- **ROI** (Return on Investment): `(Beneficio neto - Inversiones) / Inversiones`
- **ROMI** (Return on Marketing Investment): `Beneficio bruto de campaña / Gastos`

#### Embudos y Conversiones
- **Tasa de conversión**: Proporción de personas que cambian su estado
- **Embudo**: Ruta que siguen usuarios para comprar y porcentaje en cada fase
- **CTR** (Click-Through Rate): `Clics / Impresiones * 100%`
- **CR** (Conversion Rate): `Inscripciones / Clics * 100%`

### 3. Análisis de Cohortes

#### Conceptos Fundamentales
- **Cohorte**: Conjunto de personas que comparten un suceso en el mismo período temporal
- **Evento**: Caso registrado de una acción por parte de un usuario
- **Período**: Lapso de tiempo durante el cual ocurrió el evento
- **Valor absoluto**: Volumen, tamaño o magnitud de un evento
- **Valor relativo**: Relación entre otros dos valores
- **Ciclo de vida**: Métrica que indica la edad de una cohorte

#### Métricas de Cohortes
- **Tasa de retención**: `Usuarios activos en período n / Usuarios activos en período 0 * 100%`
- **Tasa de cancelación**: `Usuarios activos en período n / Usuarios activos en período (n-1) * 100%`
- **Cálculo en Python**: `cohorts.groupby(['column1'])['column2'].pct_change()`

#### Visualización
- **Mapa de calor**: Visualización de tabla donde celdas varían en color según valores
- **Código**: `sns.heatmap(dataframe, annot=True, fmt='.1f', linewidths=1, linecolor='gray')`

### 4. Economía Unitaria

#### Economía por Venta
- **Gastos variables**: Relacionados directamente con volúmenes de ventas
- **Gastos fijos**: No cambian con los ingresos
- **Objetivo**: Determinar volumen de ventas necesario para obtener beneficios

#### Economía por Cliente
- **LTV** (Lifetime Value): Cantidad total de dinero que el cliente promedio aporta a lo largo del tiempo
- **CAC** (Customer Acquisition Cost): Costo de conseguir un cliente
- **Regla de oro**: LTV > CAC para economía unitaria sólida

#### Cálculo de LTV por Cohortes
1. Encontrar fecha de primera compra de cada cliente
2. Calcular número de nuevos clientes para cada fecha
3. Añadir fecha del primer pedido a tabla de pedidos
4. Agrupar tabla y calcular ingresos
5. LTV = Ingreso acumulado de cohorte / Número de personas en cohorte

### 5. SQL como Herramienta para Trabajar con Datos

#### Conceptos Básicos
- **Base de datos**: Lugar donde se almacenan datos estructurados
- **DBMS**: Sistema de gestión de bases de datos (PostgreSQL)
- **Tabla**: Conjunto de filas y columnas
- **Campo**: Columna de tabla con características del objeto
- **Tupla/Registro**: Fila de tabla con información sobre un objeto
- **Clave primaria**: Campo o grupo de campos para identificar una tupla

#### Sintaxis SQL
```sql
-- Selección básica
SELECT column_1, column_2
FROM table_name
WHERE condition;

-- Funciones de agregación
SELECT COUNT(*) AS cnt,
       SUM(column) AS sum_column,
       AVG(column) AS avg_column,
       MIN(column) AS min_column,
       MAX(column) AS max_column
FROM table;

-- Conversión de tipos
CAST(column_name AS data_type)
column_name :: data_type
```

### 6. Funciones Avanzadas de SQL

#### Agrupación y Ordenamiento
```sql
SELECT field_1, field_2, AGGREGATE_FUNCTION(field) AS alias
FROM table_name
WHERE condition
GROUP BY field_1, field_2
HAVING AGGREGATE_FUNCTION(field) > n
ORDER BY field_1 DESC, field_2 ASC
LIMIT n;
```

#### Funciones de Fecha
```sql
-- Extraer fragmentos de fecha
SELECT EXTRACT(date_fragment FROM column) AS new_column
FROM table_with_dates;

-- Truncar fecha
SELECT DATE_TRUNC('date_fragment', column) AS new_column
FROM table_with_dates;
```

#### Subconsultas
```sql
-- En bloque FROM
SELECT SUBQUERY_1.column_name
FROM (SELECT column_name FROM table_name WHERE condition) AS SUBQUERY_1;

-- En bloque WHERE
SELECT column_name
FROM table_name
WHERE column_name IN (SELECT column_1 FROM table_name_2 WHERE condition);
```

#### Funciones de Ventana
```sql
SELECT author_id, name, 
       SUM(price) OVER (PARTITION BY author_id ORDER BY author_id 
                        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
FROM books_price;
```

### 7. Relaciones entre Tablas

#### Tipos de Relaciones
- **Una a una**: Cada fila de una tabla conectada con una sola fila de otra
- **Una a muchas**: Cada fila de una tabla coincide con varias filas de otra
- **Muchas a muchas**: Varias filas de una tabla coinciden con varias de otra

#### JOINs
```sql
-- INNER JOIN
SELECT TABLE_1.field_1, TABLE_2.field_n
FROM TABLE_1
INNER JOIN TABLE_2 ON TABLE_2.field = TABLE_1.field;

-- LEFT JOIN
SELECT TABLE_1.field_1, TABLE_2.field_n
FROM TABLE_1
LEFT JOIN TABLE_2 ON TABLE_2.field = TABLE_1.field;

-- RIGHT JOIN
SELECT TABLE_1.field_1, TABLE_2.field_n
FROM TABLE_1
RIGHT JOIN TABLE_2 ON TABLE_1.field = TABLE_2.field;

-- UNION
SELECT column_name FROM table_1
UNION
SELECT column_name FROM table_2;
```

#### Operadores Útiles
```sql
-- Valores NULL
WHERE column_name IS NULL;
WHERE column_name IS NOT NULL;

-- CASE
CASE
    WHEN condition_1 THEN result_1
    WHEN condition_2 THEN result_2
    ELSE result_3
END;

-- LIKE
WHERE column_name LIKE 'pattern';
```

### 8. Recuperación de Datos de Recursos en Línea

#### Conceptos Básicos
- **Minería web**: Proceso de buscar recursos en línea y recuperar datos
- **HTML**: Lenguaje de marcado de hipertexto
- **HTTP/HTTPS**: Protocolos de transferencia
- **API**: Interfaz de programación de aplicaciones
- **JSON**: Notación de objetos de JavaScript

#### Solicitudes HTTP con Python
```python
import requests

# Solicitud GET
req = requests.get(URL)
print(req.text)  # Contenido de la página
print(req.status_code)  # Código de estado

# Con parámetros
PARAM = {"page": "4"}
req = requests.get(URL, params=PARAM)

# Con autenticación
r = requests.get(URL, headers={'Authorization': 'OAuth {0}'.format(token)})
```

#### Expresiones Regulares
```python
import re

# Buscar
re.search(pattern, string).group()

# Dividir
re.split(pattern, string, maxsplit=num_split)

# Reemplazar
re.sub(pattern, repl, string)

# Encontrar todas
re.findall(pattern, string)
```

#### Análisis de HTML con BeautifulSoup
```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(req.text, 'lxml')

# Encontrar primera etiqueta
tag_content = soup.find(tag, attrs={"attr_name": "attr_value"})
print(tag_content.text)

# Encontrar todas las etiquetas
for tag_content in soup.find_all(tag, attrs={"attr_name": "attr_value"}):
    print(tag_content.text)
```

#### Trabajo con JSON
```python
import json

# Convertir JSON a diccionario
x = '{"Nombre": "General Slocum", "fecha": "Junio 15, 1904"}'
y = json.loads(x)
print(y['Nombre'], y['fecha'])
```

---

## Análisis de Datasets del Proyecto

### Dataset: visits_log_us.csv
- **Registros**: 359,400
- **Columnas**:
  - `Device`: Tipo de dispositivo (touch, desktop)
  - `Start Ts`: Timestamp de inicio de sesión
  - `End Ts`: Timestamp de fin de sesión
  - `Source Id`: ID de la fuente de tráfico (1-10)
  - `Uid`: ID único del usuario
- **Sin valores nulos**

### Dataset: orders_log_us.csv
- Información sobre pedidos realizados
- Contiene datos de transacciones

### Dataset: costs_us.csv
- Gastos de marketing por fuente y fecha
- Período: Enero 2017 - Diciembre 2018

---

## Metodología de Análisis

### 1. Análisis Exploratorio de Datos (EDA)
- Carga y exploración de datasets
- Identificación de valores nulos
- Estadísticas descriptivas
- Análisis de distribuciones

### 2. Análisis de Producto
- Cálculo de DAU, WAU, MAU
- Análisis de sesiones por usuario
- Cálculo de sticky factor
- Identificación de patrones de uso

### 3. Análisis de Ventas
- Cálculo de tiempo hasta primera conversión
- Análisis de frecuencia de pedidos
- Cálculo de ticket promedio
- Análisis de cohortes de compradores

### 4. Análisis de Marketing
- Cálculo de gastos por fuente
- Cálculo de CAC por fuente
- Cálculo de ROMI por fuente
- Análisis de rentabilidad por canal

### 5. Visualizaciones
- Mapas de calor para análisis de cohortes
- Gráficos de embudos de conversión
- Distribuciones de métricas clave
- Comparaciones entre fuentes de tráfico

### 6. Recomendaciones
- Identificación de fuentes más rentables
- Sugerencias de reasignación de presupuesto
- Optimización de inversiones en marketing
- Estrategias de crecimiento

---

## Herramientas y Tecnologías

### Lenguajes y Librerías
- **Python**: Lenguaje principal de análisis
- **pandas**: Manipulación de datos
- **numpy**: Operaciones numéricas
- **matplotlib**: Visualización básica
- **seaborn**: Visualización estadística avanzada
- **requests**: Solicitudes HTTP
- **BeautifulSoup**: Análisis de HTML
- **re**: Expresiones regulares

### Bases de Datos
- **PostgreSQL**: Sistema de gestión de bases de datos
- **SQL**: Lenguaje de consulta estructurada

### Conceptos de Análisis
- Análisis de cohortes
- Economía unitaria
- Métricas de usuario
- Embudos de conversión
- Análisis de rentabilidad

---

## Notas Importantes

### Detección de Anomalías
1. Recopilar datos y calcular métricas clave
2. Visualizar datos
3. Separar datos con comportamiento anómalo
4. Estudiar datos y buscar razones:
   - Comparar con otras anomalías
   - Considerar eventos externos
   - Analizar problemas de competidores
   - Verificar recopilación de datos
   - Considerar estacionalidad y lanzamientos
5. Sacar conclusiones

### Frameworks de Métricas
- **HEART**: Para valorar experiencia de usuario (UX)
- **AARRR**: Para entender tráfico de usuarios y optimizar embudo
- **Objetivos-Señales-Métricas**: Para identificar métricas clave

### Mejores Prácticas
- Siempre validar calidad de datos antes de análisis
- Documentar supuestos y limitaciones
- Visualizar resultados para facilitar interpretación
- Considerar contexto de negocio en interpretaciones
- Realizar análisis de sensibilidad cuando sea apropiado

---

## Estado Actual del Proyecto

### Contexto Completo ✅
- ✅ Descripción general del proyecto Showz
- ✅ Objetivos del proyecto claramente definidos
- ✅ Instrucciones paso a paso del Sprint 9
- ✅ Descripción detallada de los datasets
- ✅ Criterios de evaluación del proyecto
- ✅ Conceptos clave del bootcamp documentados
- ✅ Metodología de análisis definida
- ✅ Herramientas y tecnologías identificadas

### Próximos Pasos del Proyecto

1. ⏳ **Paso 1**: Carga y preparación de datos
   - Cargar visits_log_us.csv, orders_log_us.csv, costs_us.csv
   - Optimizar tipos de datos
   - Validar calidad de datos

2. ⏳ **Paso 2A**: Análisis de Visitas
   - Calcular DAU, WAU, MAU
   - Analizar sesiones por día
   - Calcular duración de sesiones (ASL)
   - Calcular sticky factor

3. ⏳ **Paso 2B**: Análisis de Ventas
   - Calcular tiempo hasta primera conversión
   - Analizar frecuencia de pedidos
   - Calcular ticket promedio
   - Calcular LTV por cohorte

4. ⏳ **Paso 2C**: Análisis de Marketing
   - Calcular gastos totales y por fuente
   - Calcular CAC por fuente
   - Calcular ROMI por fuente

5. ⏳ **Paso 2D**: Visualizaciones
   - Gráficos por dispositivo
   - Gráficos por fuente de anuncios
   - Gráficos de evolución temporal

6. ⏳ **Paso 3**: Conclusiones y Recomendaciones
   - Identificar fuentes más rentables
   - Recomendar dónde invertir
   - Fundamentar con métricas clave

---

## Notas Importantes para el Desarrollo

### Checklist de Calidad
- [ ] Cada sección tiene celdas markdown explicativas
- [ ] Código está comentado y es legible
- [ ] Todas las preguntas del proyecto son respondidas
- [ ] Visualizaciones son claras y relevantes
- [ ] Recomendaciones están fundamentadas con datos
- [ ] Conclusiones son accionables para el negocio

### Mejores Prácticas
- Documentar cada paso del análisis
- Explicar el "por qué" detrás de cada decisión
- Usar visualizaciones para comunicar insights
- Ser específico en las recomendaciones
- Considerar el contexto de negocio en interpretaciones

---

**Fecha de creación**: 2024
**Proyecto**: TripleTen Bootcamp - Sprint 9
**Tema**: Análisis de Marketing y Optimización de Inversiones
**Estado**: Contexto completo listo para iniciar desarrollo

