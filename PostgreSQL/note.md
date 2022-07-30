**Familiar**

- get help `help`

- get help psql `\?`

- get help for SQL `\l`

- exit `exit`

- connect to the other `\c`

- quit `\q`

- create database: `CREATE DATABASE test`

- delete database: `DROP DATABASE test`

- create table without constrains

		CREATE TABLE person (
			id int,
			first_name VARCHAR(50),
			last_name VARCHAR(50),
			gender VARCHAR(6),
			date_of_birth DATE
		);

- create table with constrains

		CREATE TABLE person (
			id BIGSERIAL NOT NULL PRIMARY KEY,
			first_name VARCHAR(50) NOT NULL,
			last_name VARCHAR(50) NOT NULL,
			gender VARCHAR(8) NOT NULL,
			date_of_birth DATE NOT NULL
		);

- drop table `DROP TABLE [table_name];` 

- view all tables `\d`

- view specific tables `\d [table_name]` or `\d test`

- insert value into table:

		INSERT INTO person (
			first_name,
			last_name,
			gender,
			date_of_birth
			)
		VALUES ('Anne','Smith','FEMALE',DATE '1988-01-09');

- list main-table `\dt`

- select row from the table `SELECT * FROM person`

- insert sql-file: `\i /Users/PC/Desktop/postgresql/postgresql16/person.sql`

- select all and print it out: `SELECT * FROM person;`

- select the table: `SELECT FROM person;`

- select specific column `SELECT first_name FROM person;`

- select multi columns `SELECT first_name,last_name FROM person;`

- select all order by specific column `SELECT * FROM person ORDER BY [column_name] DESC`

- select some columns order by specific column `SELECT [column1],[column2] FROM person ORDER BY [column3] DESC`

- select some columns order some specific columns `SELECT [column1],[column2] FROM person ORDER BY [column3],[column4] DESC`

- sort a column other by itself will give you the repeated values ex `SELECT country_of_birth FROM person ORDER BY country_of_birth;`

- get unqiue value by `DISTINCT`: `SELECT DISTINCT country_of_birth FROM person ORDER BY country_of_birth;`

`SELECT * FROM person WHERE gender = 'Male';`

`SELECT * FROM person WHERE gender = 'Male' AND country_of_birth = 'Poland'`

`SELECT * FROM person WHERE gender = 'Male' OR 'country_of_birth = 'Poland'`

`SELECT * FROM person WHERE gender = 'Male' AND (country_of_birth = 'Poland' OR country_of_birth ='China') AND last_name = 'Pietersma'`

- check equal: `SELECT 1 = 2;`

- check smaller `SELECT 1 < 2;`

- check greater or equal `SELECT 1 >= 2;`

- check not equal `SELECT 1 <> 2;`

- select every first 10 rows on the table `SELECT * FROM person LIMIT 10;`	

- select first 10 rows but offset 5 row first `SELECT * FROM person OFFSET 5 LIMIT 10;`

- select all but start from row 5th `SELECT * FROM person OFFSET 5;`

- select from row 5th take 10 rows `SELECT * FROM person OFFSET 5 FETCH 10 ROW ONLY;`

- select the first row `SELECT * FROM person OFFSET 5 FETCH FIRST 1 ROW ONLY;`

- select the first row `SELECT * FROM person OFFSET 5 FETCH FIRST ROW ONLY;`

- you can use `IN` as a list values: `SELECT * FROM person WHERE country_of_birth IN ('China','France','Brazil')`

- you can select rows follow value of a column between a min and max: `SELECT * FROM person WHERE date_of_birth BETWEEN DATE '2000-12-31' AND ''2011-01-01;`

- select rows where the value of specific column likely a value: `SELECT * FROM person WHERE email LIKE '%.com';` or `SELECT * FROM person WHERE email LIKE '%bloomberg.com';` 

- ilike ignore lower and upper case `SELECT * FROM person WHERE gender ILIKE 'female'`

- select follow `%`: `SELECT * FROM person WHERE email LIKE '%google.%'`

- select follow number of charater`_`: `SELECT * FROM person WHERE email LIKE '%_____@%'`

- count rows follow a column: `SELECT country_of_birth ,COUNT(*) FROM person GROUP BY contry_of_birth;`

- count rows follow a column sort by order: `SELECT country_of_birth ,COUNT(*) FROM person GROUP BY contry_of_birth ORDER BY country_of_birth;`

- Group by having meaning you can give a condition: `SELECT country_of_birth,COUNT(*) FROM person GROUP BY country_of_birth HAVING COUNT(*) > 2 ORDER BY country_of_birth`

- get all: `SELECT * FROM car;`

- get max value: `SELECT MAX(price) FROM car;`

- get min value: `SELECT MIN(price) FROM car;`

- get average value: `SELECT AVG(price) FROM car;`

- get average value: `SELECT ROUND(AVG(price)) FROM car;`

- get min or max value from a group by table: `SELECT make,model,MIN(price) FROM car GROUP BY make,model;`

- sum a column `SELECT SUM(price) FROM car`

- sum `SELECT make,SUM(price) FROM car GROUP BY make;`

- `+` : `SELECT 10 + 2;`

- `-` : `SELECT 10 - 2;`

- `*` : `SELECT 10 * 2;`

- `/` : `SELECT 10 / 2;`

- factorial: `5!`

- `%` reminder: `10 % 3`

- query all rows: `SELECT id,make,model,price FROM car;`

- query and create new column `price*.10`: `SELECT id,make,model,price,price*0.10 FROM car;`

- round the query: `SELECT id,make,model,price,ROUND(price*0.10) FROM car;`

- round the query with 2 decimal: `SELECT id,make,model,price,ROUND(price*0.10,2) FROM car;`

- discount `10%`: `SELECT id,make,model,price,ROUND(price - price*0.1,2) FROM car;`

- you can you `alias` keyword to give the new column a new, or rename a column: `SELECT id,make,price AS original_price,ROUND(price - price*0.1) AS discount_price FROM car;`

- `SELECT COALESCE(1);`

- `SELECT COALESCE(1) AS number;`

- `SELECT COALESCE(1,null) AS number;` -> 1

- `SELECT COALESCE(1,2) AS number;` -> 2

- `SELECT COALESCE(null,1,null) AS number;` -> 2

- you can use `COALESCE` to give a default value: `SELECT COALESCE(email,'NO EMAIL') FROM car;`

- Return the first element if the 2 element is not equal `SELECT NULLIF(100,10);` -> 100

- Return null if they are equal `SELECT NULLIF(100,100);` -> null

- `SELECT 10 / NULLIF(0,0);` -> null 

- `SELECT COALESCE(10 / NULLIF(0,0),0);` -> 0

- get the timestamp `SELECT NOW();`

- get the date `SELECT NOW()::DATE;`

- get time `SELECT NOW()::TIME;`

- substract 1 year: `SELECT NOW() - INTERVAL '1 YEAR';`

- add 10 month: `SELECT NOW() + INERVAL '10 MONTH';`

- subtract 100 day: `SELECT NOW() - INTERVAL '100 DAYS';`

- add 100 days: `SELECT (NOW() + INTERVAL '100' DAYS)::DATE;`

- extracting year in timestamp: `SELECT EXTRACT(YEAR FROM NOW());`

- extracting month in timestamp: `SELECT EXTRACT(MONTH FROM NOW());`

- extracting day in timestamp: `SELECT EXTRACT(DAY FROM NOW());`

- extracting day in week in timestamp: `SELECT EXTRACT(DOW FROM NOW());`

- extracting century in timstamp: `SELECT EXTRACT(CENTURY FROM NOW());`

- find the age: `SELECT first_name,last_name,gender,AGE(NOW(),date_of_birth) AS age  from person`

- drop the contrain unique value `ALTER TABLE person DROP CONSTRAINT person_pkey;`

- delete row by id `DELETE FROM person WHERE id = 1;`

- add constrain into table, you can choice multi column to become primary key: `ALTER FROM person PRIMARY KEY (id);`

`SELECT email,COUNT(*) FROM person GROUP BY email;`

`SELECT email,COUNT(*) FROM person GROUP BY email HAVING COUNT(*) > 1;`

- add unique constrain for a column or multi column: `ALTER TABLE [name_of_table] ADD CONSTRAINT [name_of_constrain] UNIQUE ([column1],[column2])` example: `ALTER TABLE person ADD CONSTRAINT unique_email_address UNIQUE(email);`

- the other way to ad constrain: `ALTER TABLE person UNIQUE(email);`

- delete conflict `DELETE FROM person WHERE email = 'gweaving@wisc.edu';`

- delete the constraint `ALTER TABLE person DROP CONSTRAINT unique_email_address;`

- check constraints make sure there nothing else but given value in a row: `ALTER TABLE person ADD CONSTRAINT gender_constraint CHECK (gender ILIKE 'female' OR gender ILIKE 'male');`

- delete all: `DELETE FROM person;`

- delete by where clause: `DELETE FROM person WHERE first_name = 'Omar'`

- delete by where clause with multi condition: `DELETE FROM person WHERE gender = 'Female' AND country_of_birth = 'England';`

- update all: `UPDATE person SET email = 'mymail@gmail,com';`

- update with where clause `UPDATE person SET email = 'mymail@gmail.com' WHERE id = 2011;`

- update multi column `UPDATE person SET first_name = 'Colyn',last_name = 'Berlyn' WHERE id = 99;`

- full command: `INSERT INTO person (id,first_name,last_name,gender,email) VALUES (20,'Tim','Cook','male','mytim@email.com') ON CONFLICT (id) DO NOTHING;`

- you can use `DO UPDATE` if there is and conflict of id, like this: `INSERT INTO person (id,first_name,last_name,gender,email) VALUES (20,'Tim','Cook','male','mytim@email.gov') ON CONFLICT (id) DO UPDATE SET email = EXCLUDED.email;`

- multi excluded: `INSERT INTO person (id,first_name,last_name,gender,email) VALUES (20,'Tim','Cook','male','mytim@email.gov') ON CONFLICT (id) DO UPDATE SET email = EXCLUDED.email, first_name = EXCLUDED.first_name,last_name = EXCLUDED.last_name;`

- join by forgein key: `SELECT * FROM person JOIN car ON person.car_id = car.id;`

- expand view `\c`

- join by forgein key: `SELECT * FROM person JOIN car ON person.car_id = car.id;`

- expand view ON/OFF `\x`

- select specific column form the table `SELECT person.first_name,person.last_name,person.gender, car.make,car.model FROM person JOIN car ON person.card_id = car.id;`

- left join `SELECT * FROM person LEFT JOIN car ON car.id = peron.car_id;`

- find the different part: `SELECT * FROM person LEFT JOIN car ON person.car_id = car.id WHERE car.id = null;`or `WHERE car.* IS NULL;`

- export to csv: `\copy (Query) TO Path DELIMITER ',' CSV HEADER;`

- example: `\copy (SELECT * FROM person LEFT JOIN car ON car.id = person.car_id) TO '/Users/PC/Desktop/postgresql/postgresql55/person.csv' DELIMITER ',' CSV HEADER;`

- if you call this function the value will auto increase `SELECT * FROM nextval('person_id_seq'::regclass);`

- restart the value count of sequences table: `ALTER SEQUENCE person_id_seq RESTART WITH 10;`

- view extensions `SELECT * FROM pg_available_extensions;`

- install extension `CREATE EXTENSTION IF NOT EXISTS "[name_of_extension]";` example: `CREATE EXTENSTION IF NOT EXISTS "[name_of_extension]";`

- check extensions `\df`

- call a function `SELECT [your_function];`