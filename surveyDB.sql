SELECT '-------------surveyDB.sql file has been accessed-------';


CREATE DATABASE surveyDB;

--- here I want to create a table for the MATH csv file data to go into
---  I think I'll also need to specify some things in the table creation.
--CREATE TABLE mathTB

--- here I want to create a table for the READING csv file data to go into
---  I think I'll also need to specify some things in the table creation.
--CREATE TABLE readingTB


------- SETUP: -------

-- docker build -t mysql_db .

-- docker run -d mysql_db
-- ^^ -d so that it doesnt take up the terminal

------ then list the containers so i can get the <containerID>
--docker container ls

-- docker exec -it <containerID> /bin/bash

------ now should be running inside container. now you can cd into the dir created in the dockerfile 
------   and now we can access mysql:

-- cd docker-entrypoint-initdb.d
-- mysql -proot

-------- now we can show databases and see that the database in the sql file was created.

-- use surveyDB
-- show tables
----- ^^ now we can see the tables in the database

--------------------------------------------------------

------ next I want to create a math table and a reading table and import the csv file data into the respective tables

---BULK INSERT math_survey_data
---FROM 'ltt-reading2022covidsurveyresults.csv'


-- SELECT * from 