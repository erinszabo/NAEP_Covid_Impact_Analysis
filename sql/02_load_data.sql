USE surveyDB;


LOAD DATA INFILE '/var/lib/mysql-files/math_survey_results.csv' 
INTO TABLE mathTB
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(
    NAEPID,
    AccNum,
    Category,
    CategoryL,
    sPercent,
    @PCT_SE,
    @Avg_score,
    @ScoreSE,
    Question
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
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(
    NAEPID,
    AccNum,
    Category,
    CategoryL,
    sPercent,
    @PCT_SE,
    @Avg_score,
    @ScoreSE,
    Question
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
