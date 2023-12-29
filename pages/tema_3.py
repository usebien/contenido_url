

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px

st.markdown("## Tema_3")
st.markdown("### Relación entre dos variables cualitativas") 

dataset = st.container()
resumen1 = st.container()
grafico1 = st.container()

with dataset:
    url = "https://raw.githubusercontent.com/usebien/data/main/uno/airline_500.csv"
    data = pd.read_csv(url, sep=";")
    st.write(data.head(4))

with resumen1:
    st.markdown("#### Tabla: resumiendo la relación entre dos variables cualitativas")
    st.write(pd.crosstab(index=data['Gender'], columns=data['Type of Travel'], margins=True))

with grafico1:
    tabla = pd.crosstab(index=data['Gender'], columns=data['Type of Travel'])
    fig = px.histogram(tabla, x=["Female", "Male"], y=["Business", "Personal"], 
                 barmode='group', barnorm='percent')
st.plotly_chart(fig)
