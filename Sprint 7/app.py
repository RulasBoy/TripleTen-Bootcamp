# Importar librerías
import streamlit as st
import pandas as pd
import plotly_express as px

# Configuración de la página
st.set_page_config(
    page_title="Dashboard de Vehículos",
    page_icon="🚗",
    layout="wide"
)

# Título principal
st.title("🚗 Dashboard de Análisis de Vehículos")
st.markdown("---")

# Cargar datos
@st.cache_data
def load_data():
    return pd.read_csv('datasets/vehicles_us.csv')

try:
    car_data = load_data()
    st.success(f"Datos cargados exitosamente: {len(car_data)} vehículos")
except FileNotFoundError:
    st.error("No se pudo encontrar el archivo 'datasets/vehicles_us.csv'")
    st.stop()

# Información básica del dataset
st.header("📊 Información General del Dataset")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total de Vehículos", len(car_data))
with col2:
    st.metric("Precio Promedio", f"${car_data['price'].mean():.0f}")
with col3:
    st.metric("Año Promedio", f"{car_data['model_year'].mean():.0f}")
with col4:
    st.metric("Kilometraje Promedio", f"{car_data['odometer'].mean():.0f}")

st.markdown("---")

# Sección de filtros
st.header("🔧 Filtros de Datos")

# Crear filtros en columnas
filter_col1, filter_col2, filter_col3 = st.columns(3)

with filter_col1:
    # Filtro por rango de precios
    price_range = st.slider(
        "Rango de Precios ($)",
        min_value=int(car_data['price'].min()),
        max_value=int(car_data['price'].max()),
        value=(int(car_data['price'].min()), int(car_data['price'].max())),
        step=1000
    )

with filter_col2:
    # Filtro por tipo de vehículo
    vehicle_types = ['Todos'] + list(car_data['type'].dropna().unique())
    selected_type = st.selectbox("Tipo de Vehículo", vehicle_types)

with filter_col3:
    # Filtro por condición
    conditions = ['Todos'] + list(car_data['condition'].dropna().unique())
    selected_condition = st.selectbox("Condición", conditions)

# Aplicar filtros
filtered_data = car_data[
    (car_data['price'] >= price_range[0]) & 
    (car_data['price'] <= price_range[1])
]

if selected_type != 'Todos':
    filtered_data = filtered_data[filtered_data['type'] == selected_type]

if selected_condition != 'Todos':
    filtered_data = filtered_data[filtered_data['condition'] == selected_condition]

st.info(f"Mostrando {len(filtered_data)} vehículos después de aplicar filtros")

st.markdown("---")

# Sección de gráficos
st.header("📈 Visualizaciones")

# Crear pestañas para diferentes tipos de gráficos
tab1, tab2, tab3, tab4 = st.tabs(["Histogramas", "Gráficos de Dispersión", "Gráficos de Barras", "Datos"])

with tab1:
    st.subheader("Histogramas")
    
    # Selectores para histogramas
    hist_col1, hist_col2 = st.columns(2)
    
    with hist_col1:
        hist_column = st.selectbox(
            "Selecciona la columna para el histograma:",
            ["price", "odometer", "model_year", "days_listed"]
        )
    
    with hist_col2:
        hist_bins = st.slider("Número de bins:", 10, 100, 30)
    
    # Checkbox para mostrar histograma
    show_histogram = st.checkbox("Mostrar Histograma")
    
    if show_histogram:
        st.write(f'Histograma de {hist_column}')
        fig_hist = px.histogram(
            filtered_data, 
            x=hist_column,
            nbins=hist_bins,
            title=f'Distribución de {hist_column.title()}',
            labels={hist_column: hist_column.replace('_', ' ').title()}
        )
        fig_hist.update_layout(showlegend=False)
        st.plotly_chart(fig_hist, use_container_width=True)

with tab2:
    st.subheader("Gráficos de Dispersión")
    
    # Selectores para gráfico de dispersión
    scatter_col1, scatter_col2, scatter_col3 = st.columns(3)
    
    with scatter_col1:
        x_axis = st.selectbox(
            "Eje X:",
            ["price", "odometer", "model_year", "days_listed"]
        )
    
    with scatter_col2:
        y_axis = st.selectbox(
            "Eje Y:",
            ["odometer", "price", "model_year", "days_listed"]
        )
    
    with scatter_col3:
        color_by = st.selectbox(
            "Colorear por:",
            ["Ninguno", "condition", "type", "fuel", "transmission"]
        )
    
    # Checkbox para mostrar gráfico de dispersión
    show_scatter = st.checkbox("Mostrar Gráfico de Dispersión")
    
    if show_scatter:
        st.write(f'Gráfico de dispersión: {x_axis} vs {y_axis}')
        
        # Crear el gráfico
        if color_by == "Ninguno":
            fig_scatter = px.scatter(
                filtered_data, 
                x=x_axis, 
                y=y_axis,
                title=f'{x_axis.title()} vs {y_axis.title()}',
                labels={
                    x_axis: x_axis.replace('_', ' ').title(),
                    y_axis: y_axis.replace('_', ' ').title()
                }
            )
        else:
            fig_scatter = px.scatter(
                filtered_data, 
                x=x_axis, 
                y=y_axis,
                color=color_by,
                title=f'{x_axis.title()} vs {y_axis.title()} (por {color_by.title()})',
                labels={
                    x_axis: x_axis.replace('_', ' ').title(),
                    y_axis: y_axis.replace('_', ' ').title(),
                    color_by: color_by.replace('_', ' ').title()
                }
            )
        
        st.plotly_chart(fig_scatter, use_container_width=True)

with tab3:
    st.subheader("Gráficos de Barras")
    
    # Selector para gráfico de barras
    bar_column = st.selectbox(
        "Selecciona la columna categórica:",
        ["condition", "type", "fuel", "transmission", "paint_color"]
    )
    
    # Checkbox para mostrar gráfico de barras
    show_bar = st.checkbox("Mostrar Gráfico de Barras")
    
    if show_bar:
        st.write(f'Distribución por {bar_column}')
        
        # Contar valores y crear gráfico
        bar_data = filtered_data[bar_column].value_counts().reset_index()
        bar_data.columns = [bar_column, 'count']
        
        fig_bar = px.bar(
            bar_data, 
            x=bar_column, 
            y='count',
            title=f'Distribución por {bar_column.title()}',
            labels={
                bar_column: bar_column.replace('_', ' ').title(),
                'count': 'Cantidad'
            }
        )
        fig_bar.update_layout(showlegend=False)
        st.plotly_chart(fig_bar, use_container_width=True)

with tab4:
    st.subheader("Vista de Datos")
    
    # Mostrar estadísticas descriptivas
    show_stats = st.checkbox("Mostrar Estadísticas Descriptivas")
    if show_stats:
        st.write("Estadísticas Descriptivas:")
        st.dataframe(filtered_data.describe())
    
    # Mostrar datos filtrados
    show_data = st.checkbox("Mostrar Datos Filtrados")
    if show_data:
        st.write("Datos Filtrados:")
        st.dataframe(filtered_data)
    
    # Opción para descargar datos
    if st.button("Preparar Descarga de Datos Filtrados"):
        csv = filtered_data.to_csv(index=False)
        st.download_button(
            label="Descargar CSV",
            data=csv,
            file_name='vehiculos_filtrados.csv',
            mime='text/csv'
        )

# Pie de página
st.markdown("---")
st.markdown("*Dashboard creado con Streamlit y Plotly*")