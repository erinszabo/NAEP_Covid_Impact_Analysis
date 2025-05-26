
SELECT 'Running transform script...' AS status;

USE surveyDB;

/*
-- Main tables
---- Keeping the SE values to find z scores
---- Removing IDs
---- Removing rows with missing or null values
*/

CREATE TABLE math_TB AS
SELECT
    Category,
    CategoryL,
    PercentA,
    PCT_SE,
    Avg_score,
    ScoreSE,
    Question
FROM mathTB
WHERE Question NOT LIKE '%MISSING%'
    AND CategoryL NOT LIKE '%MISSING%';

CREATE TABLE reading_TB AS
SELECT
    Category,
    CategoryL,
    PercentA,
    PCT_SE,
    Avg_score,
    ScoreSE,
    Question
FROM readingTB
WHERE Question NOT LIKE '%MISSING%'
    AND CategoryL NOT LIKE '%MISSING%';




-- Trimmed versions of the tables for my own veiwing

CREATE TABLE reading_trimmed AS
SELECT
    Category,
    CategoryL,
    PercentA,
    Avg_score,
    Question
FROM readingTB
WHERE Question NOT LIKE '%MISSING%'
    AND CategoryL NOT LIKE '%MISSING%';

CREATE TABLE math_trimmed AS
SELECT
    Category,
    CategoryL,
    PercentA,
    Avg_score,
    Question
FROM readingTB
WHERE Question NOT LIKE '%MISSING%'
    AND CategoryL NOT LIKE '%MISSING%';
