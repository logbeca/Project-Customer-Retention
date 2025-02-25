# Usar Python 3.9 como imagem base
FROM python:3.9

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar e instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante dos arquivos do projeto
COPY . .

# Executar o script que cria as tabelas
CMD ["python", "main.py"]
