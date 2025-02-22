import streamlit as st
import plotly.express as px
import pandas as pd

# Crear el DataFrame con los datos de ejemplo
data = {
    'Volumen de Producción': [1000, 500, 1500, 800, 1200, 900, 1100, 650, 1400, 2000],
    'Técnica de Cultivo': ['Riego por goteo', 'Tradicional', 'Riego por goteo', 'Sist. Hidropónico', 
                           'Tradicional', 'Sist. Hidropónico', 'Riego por goteo', 'Tradicional', 
                           'Riego por goteo', 'Sist. Hidropónico'],
    'Campesino Asociado': ['Juan Pérez', 'María López', 'Carlos García', 'Ana Ruiz', 
                           'Luis Hernández', 'Elena Díaz', 'José Martínez', 'Sofía Torres', 
                           'Miguel Sánchez', 'Laura Fernández'],
    'Género': ['Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino', 
               'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino'],
    'Edad': [45, 38, 50, 32, 41, 29, 54, 27, 36, 41],
    'Año': [2021, 2021, 2022, 2022, 2023, 2023, 2022, 2023, 2021, 2021]  # Año de producción
}

# Crear el DataFrame
df = pd.DataFrame(data)

# Título del dashboard
st.title("Dashboard de Producción Agrícola")

# Crear un gráfico de barras para el Volumen de Producción
fig1 = px.bar(df, x="Campesino Asociado", y="Volumen de Producción", 
              title="Volumen de Producción por Campesino", 
              labels={"Campesino Asociado": "Campesino", "Volumen de Producción": "Volumen de Producción"})

# Crear un gráfico de barras para la Técnica de Cultivo
fig2 = px.bar(df, x="Campesino Asociado", y="Técnica de Cultivo", 
              title="Técnica de Cultivo por Campesino", 
              labels={"Campesino Asociado": "Campesino", "Técnica de Cultivo": "Técnica de Cultivo"})

# Mostrar los gráficos
st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)
