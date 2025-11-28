# Instrucciones para Ejecutar el Proyecto

## 1. Activar el Entorno Virtual

```bash
cd "/home/raul/Documents/TripleTen-Bootcamp"
source .venv/bin/activate
```

## 2. Instalar Dependencias

```bash
cd "Sprint 13"
pip install -r requirements.txt
```

## 3. Iniciar Jupyter Notebook

```bash
# Asegúrate de estar en el directorio Sprint 13
cd "Sprint 13"
jupyter notebook
```

O si prefieres JupyterLab:

```bash
jupyter lab
```

## 4. Abrir el Notebook

En el navegador que se abra, busca y abre el archivo `proyecto_churn.ipynb`

## 5. Ejecutar el Proyecto

Ejecuta las celdas del notebook en orden. El proyecto está estructurado en 5 pasos principales:

- **Paso 1:** Carga de datos
- **Paso 2:** Análisis Exploratorio de Datos (EDA)
- **Paso 3:** Modelo de Clasificación Binaria
- **Paso 4:** Clustering de Usuarios
- **Paso 5:** Conclusiones y Recomendaciones

## Notas

- Asegúrate de que el archivo `datasets/gym_churn_us.csv` esté en la ubicación correcta
- El notebook usa `random_state=42` para reproducibilidad
- Todas las visualizaciones se generan automáticamente

## Desactivar el Entorno Virtual

Cuando termines de trabajar:

```bash
deactivate
```

