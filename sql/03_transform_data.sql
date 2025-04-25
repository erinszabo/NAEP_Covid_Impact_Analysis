
SELECT 'Running transform script...' AS status;

USE surveyDB;

-- to reduce size and ensure only high confidence (hc) data, only consider rows with high SE scores


CREATE TABLE math_hc AS
SELECT
    NAEPID,
    AccNum,
    Category,
    CategoryL,
    sPercent,
    Avg_score,
    Question
FROM mathTB
WHERE ScoreSE < 3 AND PCT_SE < 3;

CREATE TABLE reading_hc AS
SELECT
    NAEPID,
    AccNum,
    Category,
    CategoryL,
    sPercent,
    Avg_score,
    Question
FROM readingTB
WHERE ScoreSE < 3 AND PCT_SE < 3;
