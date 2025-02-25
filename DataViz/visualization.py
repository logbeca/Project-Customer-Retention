import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

# Exemplo: gráfico de custo de anúncios por canal
def plot_ad_cost_by_channel(ad_cost_data):
    df = pd.DataFrame([ad.dict() for ad in ad_cost_data])  # Transformar AdCost em DataFrame
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='channel', y='ad_cost')
    plt.title("Custo de Anúncios por Canal")
    plt.xlabel("Canal")
    plt.ylabel("Custo do Anúncio")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Exemplo: gráfico de visitas por dispositivo
def plot_visits_by_device(visits_data):
    df = pd.DataFrame([visit.dict() for visit in visits_data])  # Transformar Visits em DataFrame
    device_counts = df['device'].value_counts()
    device_counts.plot(kind='bar', figsize=(10, 6))
    plt.title("Visitas por Dispositivo")
    plt.xlabel("Dispositivo")
    plt.ylabel("Número de Visitas")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
