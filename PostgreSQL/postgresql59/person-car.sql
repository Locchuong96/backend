/*We have to create car first because person table have references into car table*/

CREATE TABLE car (
	car_uid UUID NOT NULL PRIMARY KEY,
	make VARCHAR(100) NOT NULL,
	model VARCHAR(100) NOT NULL,
	price NUMERIC(19,2) NOT NULL
);


CREATE TABLE person(
	person_uid UUID NOT NULL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	gender VARCHAR(7) NOT NULL,
	email VARCHAR(100),
	date_of_birth DATE NOT NULL,
	country_of_birth VARCHAR(50) NOT NULL,
	car_uid UUID REFERENCES car(car_uid),
	UNIQUE(car_uid),
	UNIQUE(email)
);

INSERT INTO person (person_uid,first_name,last_name,gender,email,date_of_birth,country_of_birth) VALUES (uuid_generate_v4(),'Anne','Smith','Female',null,'1990-02-03','USA');
INSERT INTO person (person_uid,first_name,last_name,gender,email,date_of_birth,country_of_birth) VALUES (uuid_generate_v4(),'Jake','Jones','Male','jake@email.com','1892-12-22','USA');
INSERT INTO person (person_uid,first_name,last_name,gender,email,date_of_birth,country_of_birth) VALUES (uuid_generate_v4(),'Andrew','Jacob','Male','andrew1@email.com','1995-05-06','USA');
INSERT INTO person (person_uid,first_name,last_name,gender,email,date_of_birth,country_of_birth) VALUES (uuid_generate_v4(),'Julia','Bravo','Female',null,'1850-07-11','USA');

INSERT INTO car (car_uid,make,model,price) VALUES (uuid_generate_v4(),'BWM','Red',12400.65);
INSERT INTO car (car_uid,make,model,price) VALUES (uuid_generate_v4(),'Kia','Blue',3310.43);
INSERT INTO car (car_uid,make,model,price) VALUES (uuid_generate_v4(),'Honda','Yellow',5400.85);
