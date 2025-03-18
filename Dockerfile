FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=root

COPY ./surveyDB.sql /docker-entrypoint-initdb.d/
COPY ./math_survey_results.csv /var/lib/mysql-files/
COPY ./reading_survey_results.csv /var/lib/mysql-files/

