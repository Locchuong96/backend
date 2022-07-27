### postgreSQL

⭐️ Contents ⭐️

1/[What is SQL And Relational Database]()

2/[What is PostreSQL AKA Postrgres]()

3/[PostgreSQL Installation (Mac OS)]()

4/[PostgreSQL Installation (Windows)]()

5/[GUI Clients vs Terminal/CMD Clients](/PostgreSQL/postgresql6)

6/[Setup PSQL (MAC OS)](/PostgreSQL/postgresql7)

7/[Setup PSQL (Windows)](/PostgreSQL/postgresql7)

8/[How to Create Database](/PostgreSQL/postgresq8)

9/[How to Connect to Databases](/PostgreSQL/postgresql9)

10/[A Very Dangerous Command](/PostgreSQL/postgresql10)

11/[How To Create Tables](/PostgreSQL/postgresql11)

12/[Creating Tables Without Constraints](/PostgreSQL/postgresql12)

13/[Creating Tables with Constraints](/PostgreSQL/postgresql13)

14/[Insert Into](/PostgreSQL/postgresql14)

15/[Insert Into Example](/PostgreSQL/postgresql15)

16/[Generate 1000 Rows with Mockaroo](/PostgreSQL/postgresql16)

17/[Select From](/PostgreSQL/postgresql17)

18/[Order By](/PostgreSQL/postgresql18)

19/[Distinct](/PostgreSQL/postgresql19)

20/[Where Clause and AND](/PostgreSQL/postgresql20)

21/[Comparison Operators](/PostgreSQL/postgresql21)

22/[Limit, Offset & Fetch](/PostgreSQL/postgresql22)

23/[IN](/PostgreSQL/postgresql23)

24/[Between](/PostgreSQL/postgresql24)

25/[Like And iLike](/PostgreSQL/postgresql25)

26/[Group By](/PostgreSQL/postgresql26)

27/[Group By Having](/PostgreSQL/postgresql27)

28/[Adding New Table And Data Using Mockaroo](/PostgreSQL/postgresql28)

29/[Calculating Min, Max & Average](/PostgreSQL/postgresql29)

30/[Sum](/PostgreSQL/postgresql30)

31/[Basics of Arithmetic Operators](/PostgreSQL/postgresql31)

32/[Arithmetic Operators (ROUND)]()

33/[Alias]()

34/[Coalesce]()

35/[NULLIF]()

36/[Timestamps And Dates Course]()

37/[Adding And Subtracting With Dates]()

38/[Extracting Fields From Timestamp]()

39/[Age Function]()

40/[What Are Primary Keys]()

41/[Understanding Primary Keys]()

42/[Adding Primary Key]()

43/[Unique Constraints]()

44/[Check Constraints]()

45/[How to Delete Records]()

46/[How to Update Records]()

47/[On Conflict Do Nothing]()

48/[Upsert]()

49/[What Is A Relationship/Foreign Keys]()

50/[Adding Relationship Between Tables]()

51/[Updating Foreign Keys Columns]()

52/[Inner Joins]()

53/[Left Joins]()

54/[Deleting Records With Foreign Keys]()

55/[Exporting Query Results to CSV]()

56/[Serial & Sequences]()

57/[Extensions]()

58/[Understanding UUID Data Type]()

59/[UUID As Primary Keys]()

60/[Conclusion]()

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
- Change the password `ALTER USER postgres WITH PASSWORD 'pass123'`

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

[official-document](https://www.postgresql.org/docs/)

[mockagroo-data-generation](https://www.mockaroo.com/)

#### postgreSQL-python

- install postgres in python: `pip install psycopg2`

