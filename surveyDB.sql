SELECT '-------------surveyDB.sql file has been accessed-------';


CREATE DATABASE surveyDB;

--- here I want to create a table for the MATH csv file data to go into
---  I think I'll also need to specify some things in the table creation.
--CREATE TABLE mathTB


--- here I want to create a table for the READING csv file data to go into
---  I think I'll also need to specify some things in the table creation.
--CREATE TABLE readingTB


--- once the tables are created, I'll need to import the csv file data into respective files
---   possibly using the folowing lines

---BULK INSERT mathTB
---FROM <filename>

----- ^^ The above methods would require me to build the schema manually first
-----    which I could do, but I'll try using csvkit first.

------------------------------------ SETUP: ---------------------------------------------------------

-- docker build -t mysql_db .

-- docker run -d mysql_db
-- ^^ -d so that it doesn't take up the terminal

------ then list the containers so I can get the <containerID>
-- docker container ls

-- docker exec -it <containerID> /bin/bash

------ now should be running inside container, now you can cd into the dir created in the dockerfile 
------   and now we can access mysql:

-- cd docker-entrypoint-initdb.d
-- mysql -proot

-------- now we can show databases and see that the database in the sql file was created.

-- use surveyDB
-- show tables
----- ^^ now we can see the tables in the database

------------------------ create tables from csv files ---------------------------------

-- csvsql --dialect mysql --snifflimit 100000 math_survey_results.csv > math_table.sql
-- csvsql --dialect mysql --snifflimit 100000 reading_survey_results.csv > reading_table.sql

-- show tables

-- SELECT * from  <tablename>
----^ do this with math and reading tables to check that they were created and populated correctly

---------------------------------------------------------------------------------------------------



