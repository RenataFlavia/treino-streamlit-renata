import streamlit as st

st.title("Aplicativo de treinamento da Renata")

valor = st.slider(
    "Escolha um número",
    min_value=0,
    max_value=100,
    value=50
)

st.write("Você escolheu:", valor)
