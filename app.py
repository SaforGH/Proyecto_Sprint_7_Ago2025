#Se importan las librerías a utilizar en el proyecto
import pandas as pd 
import plotly.graph_objects as go  
import streamlit as st  

# Leer los datos del archivo CSV. Se utiliza el decorador @st.cache_data proporcionado por 
# sreamlit para evitar leer el archivo repetidamente
@st.cache_data  
def load_data():  
    return pd.read_csv('vehicles_us.csv')  

car_data = load_data()  

# Encabezado para la aplicación  
st.header("Análisis de Datos de Vehículos")  

# Casillas de verificación para seleccionar el tipo de gráfico a desarrollar y mostrar
show_histogram = st.checkbox("Mostrar Histograma")  
show_scatter = st.checkbox("Mostrar Diagrama de Dispersión")  

# Lógica para generar gráficos según casilla seleccionada  
if show_histogram:  
    st.write('Creando un histograma para el conjunto de datos de anuncios de venta de coches.')  

    # Crear un histograma utilizando  
    fig = go.Figure(data=[go.Histogram(x=car_data['model_year'], nbinsx=30)])  

    # Etiquetas del gráfico  
    fig.update_layout(  
        title_text='Distribución del año del modelo',  
        xaxis_title='model_year',  
        yaxis_title='Frecuencia'  
    )  

    # Mostrar el gráfico Plotly interactivo con Streamlit  
    st.plotly_chart(fig, use_container_width=True)  

if show_scatter:  
    st.write('Creando un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches.')  

    # Verificar que las columnas necesarias estén disponibles  
    if 'model_year' in car_data.columns and 'price' in car_data.columns:  
        # Crear un diagrama de dispersión  
        fig = go.Figure(data=go.Scatter(x=car_data['model_year'], y=car_data['price'], mode='markers'))  

        # Actualizar el diseño del gráfico  
        fig.update_layout(  
            title_text='Diagrama de Dispersión: Año del Modelo vs Precio',  
            xaxis_title='Modelo Año',  
            yaxis_title='Precio (USD)',  
        )  

        # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit  
        st.plotly_chart(fig, use_container_width=True)  
    else:  
        st.error("Las columnas 'odometer' y 'price' no están disponibles en los datos.")  