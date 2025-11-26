# Sprint 10 - Proyecto: Análisis A/B y Priorización de Hipótesis

## Descripción
Proyecto de análisis de datos para una tienda online que incluye:
- Priorización de hipótesis usando frameworks ICE y RICE
- Análisis completo de test A/B
- Detección de anomalías
- Pruebas de significancia estadística

## Configuración del entorno

### 1. Activar el entorno virtual
```bash
source venv/bin/activate
```

### 2. Instalar dependencias (si aún no están instaladas)
```bash
pip install -r requirements.txt
```

### 3. Iniciar Jupyter Notebook
```bash
jupyter notebook
```

## Estructura del proyecto
```
Sprint 10/
├── proyecto_sprint10.ipynb    # Notebook principal del análisis
├── datasets/                   # Datos del proyecto
│   ├── hypotheses_us.csv      # Hipótesis a priorizar
│   ├── orders_us.csv          # Pedidos del test A/B
│   └── visits_us.csv          # Visitas del test A/B
├── requirements.txt           # Dependencias Python
├── config.env                 # Configuración del entorno
├── memoria.mdc               # Notas teóricas del curso
└── README.md                 # Este archivo
```

## Librerías utilizadas
- **pandas**: Manipulación y análisis de datos
- **numpy**: Operaciones numéricas
- **matplotlib**: Visualización de datos
- **scipy**: Pruebas estadísticas
- **jupyter**: Entorno de notebooks interactivos

## Uso
1. Abre `proyecto_sprint10.ipynb` en Jupyter
2. Ejecuta las celdas secuencialmente
3. Los resultados y gráficos se generarán automáticamente

## Autor
Raúl - TripleTen Bootcamp

