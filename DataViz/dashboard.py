import streamlit as st
from ETL.select_data import load_ad_cost_data, load_visits_data
from visualization import plot_ad_cost_by_channel, plot_visits_by_device

st.title("Análise de Dados de Marketing e Visitas")

# Carregar dados do banco
ad_cost_data = load_ad_cost_data()
visits_data = load_visits_data()

# Seletor para mostrar diferentes gráficos
chart_option = st.selectbox("Escolha o gráfico", ["Custo de Anúncios por Canal", "Visitas por Dispositivo"])

if chart_option == "Custo de Anúncios por Canal":
    plot_ad_cost_by_channel(ad_cost_data)
elif chart_option == "Visitas por Dispositivo":
    plot_visits_by_device(visits_data)
