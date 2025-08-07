import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt


car_data = pd.read_csv('vehicles_us.csv')

st.title('Visualizacion de Datos de Coches')
st.subheader('Datos:')
st.dataframe(car_data)

st.title('Tipos de vehiculos')

fabricantes = car_data['type'].value_counts().reset_index()
fabricantes.columns = ['Tipo de vehiculo', 'cantidad']

fig = px.bar(
    fabricantes,
    x='Tipo de vehiculo',
    y='cantidad',
    title='Cantidad de vehículos por fabricante',
    labels={'cantidad': 'Número de Vehículos', 'manufacturer': 'Fabricante'},
)
st.plotly_chart(fig)

st.title("Histograma: Condición del Vehículo vs Año del Modelo")
car_data1 = car_data.dropna(subset=['condition', 'model_year'])
car_data1['model_year'] = car_data1['model_year'].astype(int)

fig = px.histogram(car_data,
    x='model_year',
    color='condition',
    title='Distribución de Vehículos por Año del Modelo y Condición',
    labels={'model_year': 'Año del Modelo', 'count': 'Cantidad de Vehículos'},
    barmode='group')

st.plotly_chart(fig) 

st.title("Grafico de dispersion: Price vs Model Year")
fig = px.scatter(car_data, x="model_year", y="price") 
st.plotly_chart(fig) 

hist_button = st.button('Construir Grafico') 
     
if hist_button: 
        
    st.write('Creación de un Grafico para el conjunto de datos de anuncios de venta de coches')
         
    fig = px.histogram(car_data, x="condition", color_discrete_sequence=["#FFC0CB"])
     
    st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox('Construir un Grafico')

if build_histogram:
    st.write('Construir un grafico para la columna Condition')