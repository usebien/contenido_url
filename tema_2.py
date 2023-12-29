

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px

st.markdown("## Tema_2")
st.markdown("### Selección: Una variable cualitativa") 

dataset = st.container()
toggle1 = st.container()
toggle2 = st.container()

with dataset:
    url = "https://raw.githubusercontent.com/usebien/data/main/uno/airline_500.csv"
    data = pd.read_csv(url)
    st.write(data.head(4))

with toggle1:
    on = st.toggle('Selección aleatoria de 10 elementos según Gender')
if on:
    a =  data['Gender'].sample(n=10)
    st.write(a)
    st.markdown("Frecuencia")
    b = a.value_counts()
    st.write(b)
    fig = px.pie(values=b)
    st.plotly_chart(fig.update_traces(textposition='inside', textfont_size=24), theme="streamlit") 

with toggle2:
    on = st.toggle('Selección aleatoria de 20 elementos según Class')
if on:
    a =  data['Class'].sample(n=20)
    st.write(a)
    st.markdown("Frecuencia")
    b = a.value_counts()
    st.write(b)
    fig = px.pie(values=b)
    st.plotly_chart(fig.update_traces(textposition='inside', textfont_size=24), theme="streamlit") 