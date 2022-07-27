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

**postgres's advantages**
- Object-relational database management system
- Modern
- Open Source
- Other database engines: `ORACLE-Database`,`MySQL`,`Microsoft SQL Server`,etc.

**install postgresSQL**

[postgresql-installation](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)

-install postgreSQL on linux

    sudo apt-get update
    sudo apt-get install postgresql
    sudo apt-get install postgresql postgresql-contrib
    ls /etc/postgresql/10/main
  
- inside postgresql installation

      conf.d       pg_ctl.conf  pg_ident.conf    start.conf
      environment  pg_hba.conf  postgresql.conf

- check postgresql `service postgresql`
  
  Usage: /etc/init.d/postgresql {start|stop|restart|reload|force-reload|status} [version ..]

- `postgres` create a user account on your os-system, to switch to this account `sudo su postgres`

- go to postgresql command line tool `psql`

      service postgresql start
      sudo su postgres
      psql

- check database `\l`
- Close `Ctrl` + `Z`
- Exit `exit`

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

**superuser postgresql**
pass: pass123 -port 5432

#### References

[Learn PostgreSQL Tutorial - Full Course for Beginners](https://www.youtube.com/watch?v=qw--VYLpxG4)

#### postgreSQL-python

- install postgres in python: `pip install psycopg2`

