FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=root

COPY ./surveyDB.sql /docker-entrypoint-initdb.d/
