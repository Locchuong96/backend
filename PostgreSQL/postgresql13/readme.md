**Create table with constrains**

- create table with constrains

- `BIGSERIAL`: auto increase by themself, it auto create a sub table `[your_table]_id_seq`
- `NOT NULL`: un accept `null` value
- `PRIMARY KEY`: unique value to identify  

		CREATE TABLE person (
			id BIGSERIAL NOT NULL PRIMARY KEY,
			first_name VARCHAR(50) NOT NULL,
			last_name VARCHAR(50) NOT NULL,
			gender VARCHAR(8) NOT NULL,
			date_of_birth DATE NOT NULL,
			email VARCHAR(200)
		);

- drop table `DROP TABLE [your_table]`

