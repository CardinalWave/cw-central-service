# Use a imagem base do Python
FROM python:3.11-alpine

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as propriedades necessarias
RUN apk add --no-cache git build-base libffi-dev

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos os arquivos do diretório atual para o diretório de trabalho no contêiner
COPY . .

# Define variáveis de ambiente para o IP e porta do MQTT
ENV CW_AUTH_SERVICE=0.0.0.0
ENV CW_CENTRAL_SERVICE=cw-central-service
ENV CW_CENTRAL_SERVICE_IP=0.0.0.0
ENV CW_CENTRAL_SERVICE_PORT=5001
ENV CW_MESSAGE_SERVICE_IP=cw-message-service
ENV CW_MESSAGE_SERVICE_PORT=5003
ENV CW_MESSAGE_SERVICE_URL=http:/cw-message-service:5003
ENV CW_LOG_TRACE_IP=cw-log-trace
ENV CW_LOG_TRACE_PORT=5050
ENV CW_CENTRAL_DB=postgresql+psycopg2://postgres:postgres@cw_central_db:5432/cw_central_db
ENV CW_CENTRAL_DB_PASS=postgres
ENV CW_CENTRAL_DB_USER=postgres
ENV CW_CENTRAL_DB_HOST=cw_central_db
ENV CW_CENTRAL_DB_PORT=5432
ENV CW_CENTRAL_DB_NAME=postgres

# Expor a porta 5001 para o Flask
EXPOSE 5001

# Comando para executar a aplicação Flask
CMD ["python", "run.py"]