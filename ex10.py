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

# Título de la aplicación
st.title("📊 Dashboard de Producción Agrícola")

# Crear un slider para seleccionar el género
genero_seleccionado = st.selectbox('Selecciona el género', df['Género'].unique())

# Crear un slider para seleccionar la técnica de cultivo
tecnica_seleccionada = st.selectbox('Selecciona la técnica de cultivo', df['Técnica de Cultivo'].unique())

# Filtrar los datos según los sliders seleccionados
filtered_df = df[(df['Género'] == genero_seleccionado) & (df['Técnica de Cultivo'] == tecnica_seleccionada)]

# Gráfico de torta (pie chart) para la distribución de género
fig1 = px.pie(df, names="Género", title="Distribución de Género", hole=0.3)

# Gráfico de barras para la distribución de edad
fig2 = px.bar(filtered_df, x="Edad", y="Volumen de Producción", title="Distribución de Edad vs Volumen de Producción")

# Gráfico de barras para la distribución de producción por técnica de cultivo
fig3 = px.bar(filtered_df, x="Técnica de Cultivo", y="Volumen de Producción", title="Volumen de Producción por Técnica de Cultivo")

# Mostrar los gráficos
st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)
st.plotly_chart(fig3, use_container_width=True)



