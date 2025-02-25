import pandas as pd
from sqlalchemy import create_engine
from models import AdCost, Visits

# Configuração do banco de dados
DATABASE_URL = "postgresql://postgres:1234@localhost/mydatabase"

# Criar engine de conexão com o banco
engine = create_engine(DATABASE_URL)

# Função para carregar dados de AdCost do banco
def load_ad_cost_data():
    query = """
    SELECT date_ad, channel, ad_cost, impressions, clicks, conversion
    FROM ad_cost_table
    """
    df = pd.read_sql(query, engine)
    ad_cost_data = [AdCost(**row) for row in df.to_dict(orient="records")]
    return ad_cost_data

# Função para carregar dados de Visits do banco
def load_visits_data():
    query = """
    SELECT user_id, date_time, session_id, device, location, source, pages_visited, time_on_site, events, transaction
    FROM visits_table
    """
    df = pd.read_sql(query, engine)
    visits_data = [Visits(**row) for row in df.to_dict(orient="records")]
    return visits_data
