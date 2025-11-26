# RESPUESTA A LA PREGUNTA DEL PROYECTO
## Sprint 12 - Automatización

**Bootcamp:** TripleTen  
**Pregunta:** Parte 1 - Reunir requisitos técnicos

---

## 📋 **CONTEXTO DE LA PREGUNTA**

**Situación:**
- Trabajas en agencia Sterling & Draper
- Analizas tendencias de YouTube manualmente
- Cada semana Melanie y Ashok preguntan lo mismo:
  1. ¿Qué categorías estaban en tendencias?
  2. ¿Cómo se distribuyeron por regiones?
  3. ¿Qué categorías populares en Estados Unidos?
- Llevas 6 semanas → Momento de **AUTOMATIZAR**

---

## ❓ **LA PREGUNTA**

### **¿Qué pasos deben tomarse para diseñar y crear el dashboard?**

Se presentan **4 opciones**:

---

## **ANÁLISIS DE CADA OPCIÓN**

### **OPCIÓN 1:** ❌ **INCORRECTA**

> "Hablar con los administradores de la base de datos y preguntar qué datos recolectan. Entonces, trabajar con los ingenieros de datos para diseñar tablas de agregación y la estructura de tubería y esperar a que la desarrollen. Después de eso, crear el dashboard. Por último, anunciarles solemnemente a Melanie y Ashok que pueden analizar los datos por su cuenta."

**❌ ERRORES:**
```
1. Comienza con TECNOLOGÍA en lugar de REQUISITOS
   → No pregunta a los usuarios qué necesitan

2. Orden incorrecto del proceso
   → BD Admins → Ingenieros → Dashboard → Usuarios
   → DEBERÍA SER: Usuarios → BD → Ingenieros → Dashboard

3. No valida que el dashboard resuelva el problema real
   → Asume qué datos mostrar

4. Comunicación inapropiada
   → "Anunciar solemnemente" es arrogante

5. Proceso burocrático
   → Demasiado tiempo, posible sobre-ingeniería
```

**Consecuencia:** Dashboard que NO cumple requisitos de los usuarios.

---

### **OPCIÓN 2:** ❌ **INCORRECTA**

> "Necesitas crear el código del dashboard de inmediato. Debe aceptar datos brutos directamente. Sin tablas de agregación ni pipelines. Así le ahorraremos tiempo a los ingenieros de datos. Cuando el dashboard esté listo, avisa a Melanie y Ashok."

**❌ ERRORES:**
```
1. NO recopila requisitos con usuarios
   → ¿Qué necesitan? ¿Qué visualizaciones prefieren?

2. Ignora MEJORES PRÁCTICAS
   → Datos brutos = Dashboard LENTO
   → Sin agregación = Consultas pesadas

3. Falsa economía
   → "Ahorrar tiempo a ingenieros" vs "Dashboard eficiente"
   → Prioriza mal

4. No consulta al equipo técnico
   → ¿Los datos existen? ¿Son accesibles?

5. No es escalable
   → Funcionará MAL con volúmenes grandes
```

**Consecuencia:** Dashboard extremadamente lento e ineficiente.

---

### **OPCIÓN 3:** ❌ **INCORRECTA**

> "Necesitas hablar con Melanie y Ashok para saber de dónde obtener los datos y en cuáles bases almacenar la información de agregación. Tú te encargarás de diseñar los elementos del dashboard. No se necesita hablar con los administradores de la base ni con los ingenieros, ellos no saben de problemas analíticos."

**❌ ERRORES:**
```
1. Ignora COMPLETAMENTE al equipo técnico
   → BD Admins y Engineers son ESENCIALES

2. Asume que USUARIOS conocen infraestructura
   → Melanie y Ashok NO saben de BD, pipelines, etc.
   → Esa NO es su responsabilidad

3. Falsa afirmación
   → "Ellos no saben de problemas analíticos" = FALSO
   → Conocen desde perspectiva técnica

4. No valida viabilidad técnica
   → ¿Datos accesibles? ¿Permisos? ¿Rendimiento?

5. Trabajo en SILO
   → Sin colaboración = Solución no viable
```

**Consecuencia:** Dashboard no implementable (datos inaccesibles).

---

### **OPCIÓN 4:** ✅ **CORRECTA**

> "Necesitas hablar con Melanie y Ashok sobre los contenidos de los dashboards, su diseño y los datos que se deben presentar. Luego, habla con los administradores de la base de datos y los ingenieros para saber de dónde y cómo se recolectan los datos necesarios y cómo se pueden transformar. No olvides preguntarles dónde almacenar las tablas de agregación. Por último, crea el pipeline y el dashboard."

**✅ CORRECTO:**
```
1. Comienza con REQUISITOS DE USUARIOS ✅
   → ¿Qué problema resolver?
   → ¿Qué métricas necesitan?
   → ¿Qué diseño prefieren?

2. Valida VIABILIDAD TÉCNICA ✅
   → Consulta con BD Admins
   → ¿De dónde vienen los datos?
   → ¿Cómo acceder a ellos?

3. Diseña INFRAESTRUCTURA ✅
   → Trabaja con ingenieros
   → Pipeline ETL eficiente
   → Tablas de agregación

4. Implementa SOLUCIÓN ✅
   → Crea pipeline
   → Construye dashboard
   → Valida con usuarios
```

---

## ✅ **RESPUESTA CORRECTA: OPCIÓN 4**

### **Proceso Correcto Paso a Paso:**

```
┌───────────────────────────────────────────────────┐
│ FASE 1: REQUISITOS DE NEGOCIO                     │
├───────────────────────────────────────────────────┤
│ → Hablar con Melanie y Ashok                      │
│                                                   │
│   Preguntar:                                      │
│   ├─ ¿Qué problema resolver?                      │
│   │  → Eliminar consultas manuales semanales      │
│   ├─ ¿Qué métricas necesitan?                     │
│   │  → Categorías, regiones, USA específico       │
│   ├─ ¿Qué diseño prefieren?                       │
│   │  → Barras, mapas, tablas                      │
│   ├─ ¿Con qué frecuencia lo usarán?               │
│   │  → Semanalmente                               │
│   └─ ¿Qué filtros necesitan?                      │
│      → Semana, región                             │
└───────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────┐
│ FASE 2: VALIDACIÓN TÉCNICA - BD                   │
├───────────────────────────────────────────────────┤
│ → Hablar con Administradores de Base de Datos    │
│                                                   │
│   Preguntar:                                      │
│   ├─ ¿De dónde provienen los datos?               │
│   │  → API YouTube, data lake, etc.               │
│   ├─ ¿Qué tablas/campos están disponibles?        │
│   │  → youtube_trending_raw con campos X, Y, Z    │
│   ├─ ¿Qué permisos tengo?                          │
│   │  → READ en raw, WRITE en analytics            │
│   ├─ ¿Dónde almacenar agregaciones?                │
│   │  → Schema analytics.youtube_trending_agg      │
│   └─ ¿Con qué frecuencia se actualizan?            │
│      → Diariamente a las 2:00 AM                  │
└───────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────┐
│ FASE 3: DISEÑO DE INFRAESTRUCTURA                 │
├───────────────────────────────────────────────────┤
│ → Hablar con Ingenieros de Datos                  │
│                                                   │
│   Discutir:                                       │
│   ├─ ¿Cómo diseñar el pipeline ETL?                │
│   │  → Script Python + SQLAlchemy                 │
│   ├─ ¿Qué transformaciones hacer?                  │
│   │  → Agrupar por week, region, category         │
│   ├─ ¿Con qué frecuencia ejecutar?                 │
│   │  → Diariamente después de actualización raw   │
│   ├─ ¿Cómo manejar errores?                        │
│   │  → Logs, alertas, reintentos                  │
│   └─ ¿Cómo validar calidad de datos?               │
│      → Tests automáticos, comparación totales     │
└───────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────┐
│ FASE 4: IMPLEMENTACIÓN                            │
├───────────────────────────────────────────────────┤
│ → Crear Pipeline y Dashboard                      │
│                                                   │
│   Pasos:                                          │
│   ├─ 1. Desarrollar script ETL                     │
│   │     └─ Extract → Transform → Load             │
│   ├─ 2. Crear tablas de agregación                 │
│   │     └─ youtube_trending_agg                   │
│   ├─ 3. Configurar ejecución automática            │
│   │     └─ Cron job diario                        │
│   ├─ 4. Exportar datos para Tableau                │
│   │     └─ trending_by_time.csv                   │
│   ├─ 5. Construir dashboard en Tableau             │
│   │     └─ 3 visualizaciones + filtros            │
│   ├─ 6. Publicar en Tableau Public                 │
│   │     └─ URL compartible                        │
│   ├─ 7. Validar con Melanie y Ashok                │
│   │     └─ ¿Responde las 3 preguntas?             │
│   └─ 8. Iterar según feedback                      │
│       └─ Ajustes y mejoras                        │
└───────────────────────────────────────────────────┘
```

---

## 🎯 **POR QUÉ LA OPCIÓN 4 ES CORRECTA**

### **1. Sigue las Mejores Prácticas del Sprint:**

Recuerda la **Sección 11** del Sprint:

> **Detalles a Aclarar ANTES de Construir el Dashboard:**
> 1. Problema comercial
> 2. Frecuencia de uso
> 3. Estructura de datos
> 4. Fuentes de datos
> 5. Base de datos
> 6. Frecuencia de actualización
> 7. Gráficos
> 8. Controles

La **Opción 4** cubre TODOS estos puntos.

---

### **2. Proceso Colaborativo:**

```
EQUIPOS INVOLUCRADOS:

Usuarios (Melanie & Ashok):
├─ Conocen el PROBLEMA DE NEGOCIO
├─ Saben QUÉ necesitan ver
├─ Definen REQUISITOS funcionales
└─ NO conocen infraestructura técnica

BD Admins:
├─ Conocen las FUENTES DE DATOS
├─ Saben CÓMO acceder a ellos
├─ Definen PERMISOS y seguridad
└─ NO conocen requisitos de negocio

Ingenieros de Datos:
├─ Diseñan PIPELINES eficientes
├─ Implementan TRANSFORMACIONES
├─ Garantizan CALIDAD de datos
└─ NO conocen requisitos de negocio

Analista (TÚ):
├─ PUENTE entre negocio y técnica
├─ Traduce requisitos a soluciones
├─ Diseña VISUALIZACIONES
└─ Implementa DASHBOARD

→ TODOS SON NECESARIOS ✅
```

---

### **3. Orden Lógico:**

```
INCORRECTO:
Tecnología → Solución → Usuarios
❌ Riesgo: Dashboard que nadie usa

CORRECTO:
Usuarios → Tecnología → Solución ✅
✅ Garantiza: Dashboard útil y usado
```

---

### **4. Eficiencia Técnica:**

```
SIN AGREGACIÓN (Opción 2):
├─ Dashboard consulta datos BRUTOS
├─ Millones de registros por consulta
├─ Tiempo de carga: 30-60 segundos
└─ Experiencia de usuario: PÉSIMA ❌

CON AGREGACIÓN (Opción 4):
├─ Dashboard consulta datos AGREGADOS
├─ Miles de registros (ya resumidos)
├─ Tiempo de carga: 1-3 segundos
└─ Experiencia de usuario: EXCELENTE ✅
```

---

## 📊 **TABLA COMPARATIVA FINAL**

| Criterio | Opción 1 | Opción 2 | Opción 3 | **Opción 4** ✅ |
|----------|----------|----------|----------|-----------------|
| **Comienza con usuarios** | ❌ | ❌ | ✅ | ✅ |
| **Consulta BD Admins** | ✅ | ❌ | ❌ | ✅ |
| **Consulta Ingenieros** | ✅ | ❌ | ❌ | ✅ |
| **Orden lógico** | ❌ | ❌ | ❌ | ✅ |
| **Usa agregación** | ✅ | ❌ | ⚠️ | ✅ |
| **Valida requisitos** | ❌ | ❌ | ⚠️ | ✅ |
| **Colaborativo** | ⚠️ | ❌ | ❌ | ✅ |
| **Escalable** | ✅ | ❌ | ❌ | ✅ |
| **Eficiente** | ⚠️ | ❌ | ❌ | ✅ |
| **Implementable** | ⚠️ | ⚠️ | ❌ | ✅ |
| **Cumple requisitos** | ❌ | ❌ | ❌ | ✅ |

---

## 💡 **LECCIONES CLAVE**

### **Memoriza este Proceso:**

```
1️⃣ USUARIOS PRIMERO
   → ¿Qué problema resolver?
   → ¿Qué necesitan ver?

2️⃣ VALIDACIÓN TÉCNICA
   → ¿Datos disponibles?
   → ¿Cómo acceder?

3️⃣ DISEÑO DE INFRAESTRUCTURA
   → Pipeline ETL
   → Agregación

4️⃣ IMPLEMENTACIÓN
   → Dashboard
   → Validación
   → Iteración
```

### **Principio Fundamental:**

> **"La tecnología existe para servir al negocio,  
> no el negocio para justificar la tecnología."**

---

## ✅ **RESUMEN EJECUTIVO**

**Pregunta:** ¿Qué pasos seguir para diseñar y crear el dashboard?

**Respuesta Correcta:** **OPCIÓN 4**

**Razón:**
1. Comienza con **requisitos de usuarios** ✅
2. Valida **viabilidad técnica** ✅
3. Diseña **infraestructura eficiente** ✅
4. Implementa **solución validada** ✅

**Proceso:**
```
Melanie & Ashok → BD Admins → Ingenieros → Pipeline + Dashboard
(Requisitos)      (Datos)     (ETL)        (Implementación)
```

**Este es el proceso estándar en la industria** para proyectos de Business Intelligence y Data Analytics.

---

**Autor:** Documentación Sprint 12  
**Bootcamp:** TripleTen  
**Tema:** Automatización - Proyecto Final

