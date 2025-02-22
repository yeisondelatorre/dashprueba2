import pandas as pd
import numpy as np

# Generar datos aleatorios
np.random.seed(42)

# Crear listas de datos
edades = np.random.randint(18, 60, size=20)  # Edades entre 18 y 59
prom_notas = np.random.uniform(5, 10, size=20).round(2)  # Notas promedio entre 5 y 10
horas_estudio = np.random.randint(5, 30, size=20)  # Horas de estudio entre 5 y 30 horas por semana
generos = np.random.choice([1, 0], size=20)  # 1 para hombre, 0 para mujer

# Crear el DataFrame
df = pd.DataFrame({
    'edad': edades,
    'prom_nota': prom_notas,
    'horas_estudio': horas_estudio,
    'genero': generos
})

# Título de la aplicación
st.title("Análisis de Datos: Edad, Promedio de Notas y Género")

# Gráfico de barras de la edad
fig1 = px.bar(df, x=df.index, y="edad", labels={"edad": "Edad", "index": "Índice"},
              title="Distribución de Edad")

# Gráfico de barras del promedio de notas
fig2 = px.bar(df, x=df.index, y="prom_nota", labels={"prom_nota": "Promedio de Notas", "index": "Índice"},
              title="Promedio de Notas de los Estudiantes")

# Gráfico de torta para el género
fig3 = px.pie(df, names="genero", title="Distribución de Género",
              labels={"genero": "Género", "0": "Femenino", "1": "Masculino"})

# Mostrar los gráficos en Streamlit
st.plotly_chart(fig1)
st.plotly_chart(fig2)
st.plotly_chart(fig3)
