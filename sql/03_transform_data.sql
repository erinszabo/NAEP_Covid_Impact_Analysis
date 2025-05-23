
SELECT 'Running transform script...' AS status;

USE surveyDB;

-- to reduce size and ensure only high confidence (hc) data, only consider rows with high SE scores
-- remove rows with missing information


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
WHERE ScoreSE < 3 AND PCT_SE < 3
    AND Question NOT LIKE '%MISSING%'
    AND CategoryL NOT LIKE '%MISSING%';

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
WHERE ScoreSE < 3 AND PCT_SE < 3
    AND Question NOT LIKE '%MISSING%'
    AND CategoryL NOT LIKE '%MISSING%';



-- tables with only the information I want to analyze

CREATE TABLE reading_trimmed AS
SELECT
    Category,
    CategoryL,
    sPercent,
    Avg_score,
    Question
FROM readingTB
WHERE Question NOT LIKE '%MISSING%'
    AND CategoryL NOT LIKE '%MISSING%';

CREATE TABLE math_trimmed AS
SELECT
    Category,
    CategoryL,
    sPercent,
    Avg_score,
    Question
FROM readingTB
WHERE Question NOT LIKE '%MISSING%'
    AND CategoryL NOT LIKE '%MISSING%';
