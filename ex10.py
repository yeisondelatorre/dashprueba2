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

# Usar todos los datos (sin filtro de año)
filtered_df = df

# Crear un gráfico de dispersión
fig1 = px.scatter(filtered_df, x="Edad", y="Volumen de Producción", color="Técnica de Cultivo",
                  hover_name="Campesino Asociado", title="Volumen de Producción vs Edad del Campesino")

# Crear un gráfico de barras
fig2 = px.bar(filtered_df, x="Técnica de Cultivo", y="Volumen de Producción", color="Técnica de Cultivo",
              title="Volumen de Producción por Técnica de Cultivo")

# Crear un gráfico de barras para el promedio por género
fig3 = px.bar(df.groupby("Género").agg({"Volumen de Producción": "mean"}).reset_index(), x="Género", y="Volumen de Producción",
              title="Promedio de Volumen de Producción por Género")

# Mostrar los gráficos
st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)
st.plotly_chart(fig3, use_container_width=True)

