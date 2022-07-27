**Create table without constrains**

		CREATE TABLE person (
			id int,
			first_name VARCHAR(50),
			last_name VARCHAR(50),
			gender VARCHAR(6),
			date_of_birth DATE,
		);

- view all tables `\d`

- view specific tables `\d [table_name]` or `\d test`

- drop table `DROP TABLE [table_name];` ex: `DROP TABLE person;`