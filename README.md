# spring_7_project
Construcción y despliegue de un panel de control de una aplicación web en un servicio en la nube.
# Aplicación Web: Análisis de Datos de Vehículos Usados

Esta aplicación web ha sido desarrollada con **Streamlit**, **pandas** y **plotly-express**. Permite a los usuarios explorar un conjunto de datos de vehículos usados en EE.UU. de forma visual e interactiva.

### Funcionalidades principales:
- Visualizacion de los Datos de los coches
- Visualización de un **Grafico** que muestra la cantidad de vehiculos por fabricante
isualización de un **Histograma** que muestra la condicion del vehiculo vs año del modelo
- Generación de un **gráfico de dispersión** entre `model_year` y `price`, que permite observar la relación entre el año de fabricacion y el precio del vehículo.
- Interfaz simple y clara con botones o casillas de verificación para generar las gráficas dinámicamente.

### Cómo ejecutar:
1. Abre una terminal.
2. Ejecuta el siguiente comando:

```bash
streamlit run app.py