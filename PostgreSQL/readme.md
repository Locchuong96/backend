### postgreSQL

**What is database**
- Store data
- Manipulate data
- Retrieve data

**postgreSQL and relational database**
- postgres is SQL-engine
- SQL meaning `Structured Qeury Language` is a programming language, delevoped in 1974 `SELECT first_name FROM person`,SQL use for:
- Manage data held in a relational database
- Easy to learn
- Very powerful

**How data stored**
- Stores in the table
- Form by 2 thing column-row

|id|first_name|last_name|gender|age|
|---|---|---|---|---|
|1|Anne|Smith|female|44|
|2|Jake|Jones|male|21|
|3|Andrew|Jacob|male|19|
|4|Julia|Bravo|female|34|

**Relational database**
|id|first_name|last_name|gender|age|car_id|
|---|---|---|---|---|---|
|1|Anne|Smith|female|44||
|2|Jake|Jones|male|21|24|
|3|Andrew|Jacob|male|19||
|4|Julia|Bravo|female|34|313|

|id|make|model|price|
|---|---|---|---|
|24|Anne|Smith|44|
|313|Jake|Jones|21|

#### References

[Learn PostgreSQL Tutorial - Full Course for Beginners](https://www.youtube.com/watch?v=qw--VYLpxG4)

#### postgreSQL-python

- install postgres in python: `pip install psycopg2`

