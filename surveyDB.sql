
CREATE DATABASE surveyDB;

USE surveyDB;

CREATE TABLE mathTB
(
    NAEPID VARCHAR(7),
    AccNum VARCHAR(8),
    Category INT,
    CategoryL VARCHAR(10),
    sPercent INT,
    PCT_SE FLOAT,
    Avg_score INT,
    ScoreSE FLOAT,
    SQD VARCHAR(60),
    Flag VARCHAR(1)
);

CREATE TABLE readingTB
(
    NAEPID VARCHAR(7),
    AccNum VARCHAR(8),
    Category INT,
    CategoryL VARCHAR(10),
    sPercent INT,
    PCT_SE FLOAT,
    Avg_score INT,
    ScoreSE FLOAT,
    SQD VARCHAR(60),
    Flag VARCHAR(1)
);

LOAD DATA LOCAL INFILE '/math_survey_results.csv'
INTO TABLE mathTB
FIELDS TERMINATED BY ","
LINES TERMINATED BY "\n"
IGNORE 5 LINES;

LOAD DATA LOCAL INFILE '/reading_survey_results.csv'
INTO TABLE mathTB
FIELDS TERMINATED BY ","
LINES TERMINATED BY "\n"
IGNORE 5 LINES;
