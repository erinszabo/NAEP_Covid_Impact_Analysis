SELECT 'Running transform script...' AS status;

USE surveyDB;

-- remove rows with missing information
CREATE TABLE math_no_missing AS
SELECT *
FROM math_hc
WHERE Question NOT LIKE '%MISSING%'
    AND CategoryL NOT LIKE '%MISSING%';


CREATE TABLE reading_no_missing AS
SELECT *
FROM reading_hc
WHERE Question NOT LIKE '%MISSING%'
    AND CategoryL NOT LIKE '%MISSING%';
