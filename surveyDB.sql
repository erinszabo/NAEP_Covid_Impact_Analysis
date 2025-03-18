
CREATE DATABASE surveyDB;

USE surveyDB;

CREATE TABLE mathTB
(
    NAEPID VARCHAR(8),
    AccNum VARCHAR(9),
    Category INT,
    CategoryL VARCHAR(11),
    sPercent INT,
    PCT_SE FLOAT,
    Avg_score INT,
    ScoreSE FLOAT,
    SQD VARCHAR(60),
    Flag VARCHAR(5)
);

CREATE TABLE readingTB
(
    NAEPID VARCHAR(8),
    AccNum VARCHAR(9),
    Category INT,
    CategoryL VARCHAR(11),
    sPercent INT,
    PCT_SE FLOAT,
    Avg_score INT,
    ScoreSE FLOAT,
    SQD VARCHAR(60),
    Flag VARCHAR(5)
);

LOAD DATA INFILE '/var/lib/mysql-files/math_survey_results.csv'
INTO TABLE mathTB
FIELDS TERMINATED BY ","
LINES TERMINATED BY "\n"
IGNORE 6 LINES;

LOAD DATA INFILE '/var/lib/mysql-files/reading_survey_results.csv'
INTO TABLE mathTB
FIELDS TERMINATED BY ","
LINES TERMINATED BY "\n"
IGNORE 6 LINES;