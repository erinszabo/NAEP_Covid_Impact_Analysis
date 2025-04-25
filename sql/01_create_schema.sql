
CREATE DATABASE
IF NOT EXISTS surveyDB;

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
    Question VARCHAR(1000)
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
    Question VARCHAR(1000)

);
