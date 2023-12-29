import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px

st.markdown("## Tema_1")
st.markdown("### Una variable cualitativa") 

dataset = st.container()
pie_1 = st.container()
resumen1 = st.container()
pie_2 = st.container()

with dataset:
    url = "https://raw.githubusercontent.com/usebien/data/main/uno/airline_500.csv"
    data = pd.read_csv(url)
    st.write(data.head(10))    

with pie_1, resumen1:
    fig = px.pie(data.groupby(['Gender'])['Gender'].count().reset_index(name='count'), values='count', names='Gender', title='Gender')
    st.plotly_chart(fig.update_traces(textposition='inside', textfont_size=24), theme="streamlit") 
    st.markdown("Frecuencia")   
    code = '''data['Gender'].value_counts()'''
    st.code(code, language='python')
    st.write(data['Gender'].value_counts())

with pie_2:
    fig = px.pie(data.groupby(['Class'])['Class'].count().reset_index(name='count'), values='count', names='Class', title='Class')
    st.plotly_chart(fig.update_traces(textposition='inside', textfont_size=24), theme="streamlit")    

