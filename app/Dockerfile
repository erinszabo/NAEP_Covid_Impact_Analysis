FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y default-mysql-client
RUN pip install -r requirements.txt
RUN chmod +x project.sh