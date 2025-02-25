# Dockerfile para o frontend (Streamlit)

# Usar a imagem base do Python
FROM python:3.9

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar as dependências para dentro do container
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar o restante dos arquivos do projeto
COPY . /app

# Comando para rodar o Streamlit
CMD ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
