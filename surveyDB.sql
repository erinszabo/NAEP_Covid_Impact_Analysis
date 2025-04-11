
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
    ScoreSE FLOAT
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
    ScoreSE FLOAT
);

SET sql_mode
= 'NO_ENGINE_SUBSTITUTION';


LOAD DATA INFILE '/var/lib/mysql-files/test_math.csv' 
INTO TABLE mathTB
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
OPTIONALLY ENCLOSED BY "'"
LINES TERMINATED BY '\n'
(
    NAEPID,
    AccNum,
    Category,
    CategoryL,
    sPercent,
    @PCT_SE,
    @Avg_score,
    @ScoreSE
)
SET
    PCT_SE
=
IF(LOWER(TRIM(BOTH ' ' FROM @PCT_SE)) = 'null', NULL, NULLIF
(@PCT_SE, '')),
    Avg_score =
IF(LOWER(TRIM(BOTH ' ' FROM @Avg_score)) = 'null', NULL, NULLIF
(@Avg_score, '')),
    ScoreSE =
IF(LOWER(TRIM(BOTH ' ' FROM @ScoreSE)) = 'null' OR @ScoreSE = '', NULL, @ScoreSE);

LOAD DATA INFILE '/var/lib/mysql-files/reading_survey_results.csv' 
INTO TABLE readingTB
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
OPTIONALLY ENCLOSED BY "'"
LINES TERMINATED BY '\n'
(
    NAEPID,
    AccNum,
    Category,
    CategoryL,
    sPercent,
    @PCT_SE,
    @Avg_score,
    @ScoreSE
)
SET
    PCT_SE
=
IF(LOWER(TRIM(BOTH ' ' FROM @PCT_SE)) = 'null', NULL, NULLIF
(@PCT_SE, '')),
    Avg_score =
IF(LOWER(TRIM(BOTH ' ' FROM @Avg_score)) = 'null', NULL, NULLIF
(@Avg_score, '')),
    ScoreSE =
IF(LOWER(TRIM(BOTH ' ' FROM @ScoreSE)) = 'null' OR @ScoreSE = '', NULL, @ScoreSE);
