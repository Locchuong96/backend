# social-app
FastAPI framework

[Example on Heroku](https://tranquil-cliffs-83883.herokuapp.com/docs)

### Guides

*Note: Run the command on your terminal*

- create virtual enviroment `virtualenv env`
- activate virtual enviroment `source env/bin/activate`
- deactivate virtual enviroment `deactivate`
- export packages in virtual enviroment `pip3 freeze > requirements.txt`
- install packages as requirements: `pip3 install -r requirements.txt`
- install FastAPI full (all flag) `pip3 install fastapi[all]`
- run app (app instance from main) `uvicorn app.main:app`
- view api-doc `http://127.0.0.1:8000/docs` or `http://127.0.0.1:8000/redoc`
- reload web app automaticly if changing happen `uvicon app.main:app --reload`
- switch over to the postgres account on your server `sudo -i -u postgres`
- then you can access the postgres prompt by running `psql`
- to exit postgresql prompt `\q`
- to go back the linux command prompt `exit`
- check linux enviroment variables `set`
- check specific linux variable `echo "$HOME"`
- set a enviroment variable `export POSTGRES_HOST=localhost`
- left join query: `SELECT * FROM posts LEFT JOIN users ON posts.owner_id = users.id;` (add more info)
- left join specific column from specific table: `SELECT posts.id,email FROM posts LEFT JOIN users ON posts.owner_id = users.id;`

- left join specific column from specific table: `SELECT posts.* FROM posts LEFT JOIN users ON posts.owner_id = users.id;`

- group by `SELECT users.id , COUNT(posts.id) FROM posts LEFT JOIN users ON posts.owner_id = users.id  group by users.id;`

- group by `SELECT users.id , COUNT(posts.id) FROM posts RIGHT JOIN users ON posts.owner_id = users.id  group by users.id;`

- group by and rename `SELECT users.id , COUNT(posts.id) as users_post_count FROM posts LEFT JOIN users ON
posts.owner_id = users.id  group by users.id;`

- count vote follow posts `SELECT posts.id,COUNT(*) AS vote_count FROM posts LEFT JOIN votes ON
posts.id = votes.post_id GROUP BY posts.id;`

- count vote follow posts count user_id column `SELECT posts.id, COUNT(votes.user_id) AS vote_count FROM posts LEFT JOIN votes ON posts.id = votes.post_id GROUP BY posts.id;`

- count vote with WHERE condition `SELECT posts.*, COUNT(votes.post_id) AS vote_count FROM posts LEFT JOIN votes ON posts.id = votes.post_id  WHERE posts.id = 7 GROUP BY posts.id;`

- install `heroku` on ubuntu `sudo snap install heroku --classic`
- check install version `heroku --version`
- get help `heroku --help`
- check git remote `git remote`
- run pytest `pytest` or you can run `pytest <your_specific_file>.py` or `pytest -v` or `pytest -v -s` example `pytest --disable-warnings -v -s tests/test_users.py`
- run pytest and stop in the first test fail `pytest --disable-warnings -v -s -x tests/test_users.py`
- run pytest and store result `pytest --disable-warnings -v -x tests/test_users.py > tests/test_votes.txt
`

## Dependenices

- install automaticly `pip3 install -r requirements.txt`

- install FastAPI full `pip3 install fastapi[all]`

- install python - postgresql driver `pip3 install psycopg2-binary`

- install sqlalchemy `pip3 install sqlalchemy`

- install jose-authentication `pip3 install python-jose`

- install `passlib` package `pip3 install passlib`

- install `bcrypt` package `pip3 install bcrypt`

- install alembic package `pip3 install alembic`

- install pytest package `pip3 install pytest` (pytest run every file name *_test.py or test_*.py) 

### Course contents

<details><summary>Click to expand</summary>
<p>

**Section 1: Intro**

- [Intro](https://github.com/iteam1/social-app/tree/v1)

- [Project Overview](https://github.com/iteam1/social-app/tree/v1)

- [Mac Python Installation](https://github.com/iteam1/social-app/tree/v1)

**Section 2: Setup & installation**

- [Mac VS Code install and setup](https://github.com/iteam1/social-app/tree/v1)

- [Windows Python Installation](https://github.com/iteam1/social-app/tree/v1)

- [Windows VS Code install and setup](https://github.com/iteam1/social-app/tree/v1)

- [Python virtual Env Basics](https://github.com/iteam1/social-app/tree/v1)

- [Virtual Env on windows](https://github.com/iteam1/social-app/tree/v1)

- [Virtual Env on Mac](https://github.com/iteam1/social-app/tree/v1)

**Section 3: FastAPI**

- [Install dependencies w/ pip](https://github.com/iteam1/social-app/tree/v1)

- [Starting FastAPI](https://github.com/iteam1/social-app/tree/v1)

- [Path Operations](https://github.com/iteam1/social-app/tree/v2)

- [Intro Postman](https://github.com/iteam1/social-app/tree/v2)

- [HTTP Requests](https://github.com/iteam1/social-app/tree/v2)

- [Schema Validation with Pydantic](https://github.com/iteam1/social-app/tree/v3)

- [CRUD Operations](https://github.com/iteam1/social-app/tree/v4)

- [Storing in Array](https://github.com/iteam1/social-app/tree/v4)

- [Creating](https://github.com/iteam1/social-app/tree/v4)

- [Postman Collections & saving requests](https://github.com/iteam1/social-app/tree/v4)

- [Retrieve One](https://github.com/iteam1/social-app/tree/v4)

- [Path order Matters](https://github.com/iteam1/social-app/tree/v4)

- [Changing response Status Codes](https://github.com/iteam1/social-app/tree/v5)

- [Deleting](https://github.com/iteam1/social-app/tree/v5)

- [Updating](https://github.com/iteam1/social-app/tree/v5)

- [Automatic Documentation](https://github.com/iteam1/social-app/tree/v5)

- [Python packages](https://github.com/iteam1/social-app/tree/v6)

**Section 4: Databases**

- [Database Intro](https://github.com/iteam1/social-app/tree/v6)

- [Postgres Windows Install](https://github.com/iteam1/social-app/tree/v6)

- [Postgres Mac Install](https://github.com/iteam1/social-app/tree/v6)

- [Database Schema & Tables](https://github.com/iteam1/social-app/tree/v6)

- [Managing Postgres with PgAdmin GUI](https://github.com/iteam1/social-app/tree/v6)

- [Your first SQL Query](https://github.com/iteam1/social-app/tree/v6)

- [Filter results with "where"](https://github.com/iteam1/social-app/tree/v6)

- [SQL Operators](https://github.com/iteam1/social-app/tree/v6)

- [IN](https://github.com/iteam1/social-app/tree/v6)

- [Pattern matching with LIKE](https://github.com/iteam1/social-app/tree/v6)

- [Ordering Results](https://github.com/iteam1/social-app/tree/v6)

- [LIMIT & OFFSET](https://github.com/iteam1/social-app/tree/v6)

- [Modifying Data](https://github.com/iteam1/social-app/tree/v6)

**Section 5: Python + Raw SQL**

- [Setup App Database](https://github.com/iteam1/social-app/tree/v7)

- [Connecting to database w/ Python](https://github.com/iteam1/social-app/tree/v7)

- [Database CRUD](https://github.com/iteam1/social-app/tree/v7)

**Section 6: ORMs**

- [ORM intro](https://github.com/iteam1/social-app/tree/v8)

- [SQLALCHEMY setup](https://github.com/iteam1/social-app/tree/v8)

- [Adding CreatedAt Column](https://github.com/iteam1/social-app/tree/v8)

- [Get All](https://github.com/iteam1/social-app/tree/v8)

- [Create](https://github.com/iteam1/social-app/tree/v8)

- [Get by ID](https://github.com/iteam1/social-app/tree/v8)

- [Delete](https://github.com/iteam1/social-app/tree/v8)

- [Update](https://github.com/iteam1/social-app/tree/v8)

**Section 7: Pydantic Models**

- [Pydantic vs ORM Models](https://github.com/iteam1/social-app/tree/v9)

- [Pydantic Models Deep Dive](https://github.com/iteam1/social-app/tree/v9)

- [Response Model](https://github.com/iteam1/social-app/tree/v9)

**Section 8: Authentication & Users**

- [Creating Users Table](https://github.com/iteam1/social-app/tree/v9)

- [User Registration Path Operation](https://github.com/iteam1/social-app/tree/v9)

- [Hashing Passwords](https://github.com/iteam1/social-app/tree/v9)

- [Refractor Hashing Logic](https://github.com/iteam1/social-app/tree/v9)

- [Get User by ID](https://github.com/iteam1/social-app/tree/v9)

- [FastAPI Routers](https://github.com/iteam1/social-app/tree/v10)

- [Router Prefix](https://github.com/iteam1/social-app/tree/v11)

- [Router Tags](https://github.com/iteam1/social-app/tree/v11)

- [JWT Token Basics](https://github.com/iteam1/social-app/tree/v12)

- [Login Process](https://github.com/iteam1/social-app/tree/v12)

- [Creating Token](https://github.com/iteam1/social-app/tree/v12)

- [OAuth2 PasswordRequestForm](https://github.com/iteam1/social-app/tree/v13)

- [Verify user is Logged In](https://github.com/iteam1/social-app/tree/v13)

- [Fixing Bugs](https://github.com/iteam1/social-app/tree/v13)

- [Protecting Routes](https://github.com/iteam1/social-app/tree/v13)

- [Test Expired Token](https://github.com/iteam1/social-app/tree/v13)

- [Fetching User in Protected Routes](https://github.com/iteam1/social-app/tree/v13)

- [Postman advanced Features](https://github.com/iteam1/social-app/tree/v13)

**Section 9: Relationships**

- [SQL Relationship Basics](https://github.com/iteam1/social-app/tree/v14)

- [Postgres Foreign Keys](https://github.com/iteam1/social-app/tree/v14)

- [SQLAlchemy Foreign Keys](https://github.com/iteam1/social-app/tree/v14)

- [Update Schema to include User](https://github.com/iteam1/social-app/tree/v14)

- [Assigning Owner id when creating new](https://github.com/iteam1/social-app/tree/v14)

- [Delete and Update only your own](https://github.com/iteam1/social-app/tree/v14)

- [Only Retrieving Logged in User's](https://github.com/iteam1/social-app/tree/v14)

- [Sqlalchemy Relationships](https://github.com/iteam1/social-app/tree/v14)

- [Query Parameters](https://github.com/iteam1/social-app/tree/v14)

- [Cleanup our main.py file](https://github.com/iteam1/social-app/tree/v14)

- [Env Variables](https://github.com/iteam1/social-app/tree/v15)

**Section 10: Vote/Like System**

- [Vote/Like Theory](https://github.com/iteam1/social-app/tree/v15)

- [Votes Table](https://github.com/iteam1/social-app/tree/v15)

- [Votes Sqlalchemy](https://github.com/iteam1/social-app/tree/v15)

- [Votes Route](https://github.com/iteam1/social-app/tree/v15)

- [SQL Joins](https://github.com/iteam1/social-app/tree/v15)

- [Joins in SqlAlchemy](https://github.com/iteam1/social-app/tree/v15)

- [Get One with Joins](https://github.com/iteam1/social-app/tree/v15)

**Section 11: Database Migration w/ Alembic**

- [What is a database migration tool](https://github.com/iteam1/social-app/tree/v16)

- [Alembic Setup](https://github.com/iteam1/social-app/tree/v16)

- [Disable SqlAlchemy create Engine](https://github.com/iteam1/social-app/tree/v16)

**Section 12: Pre Deployment Checklist**

- [What is CORS?](https://github.com/iteam1/social-app/tree/v17)

- [Git PreReqs](https://github.com/iteam1/social-app/tree/v17)

- [Git Install](https://github.com/iteam1/social-app/tree/v17)

- [Github](https://github.com/iteam1/social-app/tree/v17)

**Section 13: Deployment Heroku**

- [Heroku intro](https://github.com/iteam1/social-app/tree/v18)

- [Create Heroku App](https://github.com/iteam1/social-app/tree/v18)

- [Heroku procfile](https://github.com/iteam1/social-app/tree/v18)

- [Adding a Postgres database](https://github.com/iteam1/social-app/tree/v18)

- [Env Variables in Heroku](https://github.com/iteam1/social-app/tree/v18)

- [Alembic migrations on Heroku Postgres instance](https://github.com/iteam1/social-app/tree/v18)

- [Pushing changed to production](https://github.com/iteam1/social-app/tree/v18)

**Section 14: Deployment Ubuntu**

- [Create an Ubuntu VM](https://github.com/iteam1/social-app/tree/v19)

- [Update packages](https://github.com/iteam1/social-app/tree/v19)

- [Install Python](https://github.com/iteam1/social-app/tree/v19)

- [Install Postgres & setup password](https://github.com/iteam1/social-app/tree/v19)

- [Postgres Config](https://github.com/iteam1/social-app/tree/v19)

- [Create new user and setup python evironment](https://github.com/iteam1/social-app/tree/v19)

- [Env Variables](https://github.com/iteam1/social-app/tree/v19)

- [Alembic migrations on production database](https://github.com/iteam1/social-app/tree/v19)

- [Gunicorn](https://github.com/iteam1/social-app/tree/v19)

- [Creating a Systemd service](https://github.com/iteam1/social-app/tree/v19)

- [NGINX](https://github.com/iteam1/social-app/tree/v19)

- [Setting up Domain name](https://github.com/iteam1/social-app/tree/v19)

- [SSL/HTTPS](https://github.com/iteam1/social-app/tree/v19)

- [NGINX enable](https://github.com/iteam1/social-app/tree/v19)

- [Firewall](https://github.com/iteam1/social-app/tree/v19)

- [Pushing code changes to Production](https://github.com/iteam1/social-app/tree/v19)

**Section 15: Docker**

- [Dockerfile](https://github.com/iteam1/social-app/tree/v20)

- [Docker Compose](https://github.com/iteam1/social-app/tree/v20)

- [Postgres Container](https://github.com/iteam1/social-app/tree/v20)

- [Bind Mounts](https://github.com/iteam1/social-app/tree/v20)

- [Dockerhub](https://github.com/iteam1/social-app/tree/v20)

- [Production vs Development](https://github.com/iteam1/social-app/tree/v20)

**Section 16: Testing**

- [Testing Intro](https://github.com/iteam1/social-app/tree/v21)

- [Writing your first test](https://github.com/iteam1/social-app/tree/v21)

- [The -s & -v flags](https://github.com/iteam1/social-app/tree/v21)

- [Testing more functions](https://github.com/iteam1/social-app/tree/v21)

- [Parametrize](https://github.com/iteam1/social-app/tree/v21)

- [Testing Classes](https://github.com/iteam1/social-app/tree/v21)

- [Fixtures](https://github.com/iteam1/social-app/tree/v21)

- [Combining Fixtures + Parametrize](https://github.com/iteam1/social-app/tree/v21)

- [Testing Exceptions](https://github.com/iteam1/social-app/tree/v21)

- [FastAPI TestClient](https://github.com/iteam1/social-app/tree/v21)

- [Pytest flags](https://github.com/iteam1/social-app/tree/v21)

- [Test create user](https://github.com/iteam1/social-app/tree/v21)

- [Setup testing database](https://github.com/iteam1/social-app/tree/v21)

- [Create & destroy database after each test](https://github.com/iteam1/social-app/tree/v21)

- [More Fixtures to handle database interaction](https://github.com/iteam1/social-app/tree/v22)

- [Trailing slashes in path](https://github.com/iteam1/social-app/tree/v22)

- [Fixture scope](https://github.com/iteam1/social-app/tree/v22)

- [Test user fixture](https://github.com/iteam1/social-app/tree/v22)

- [Test/validate token](https://github.com/iteam1/social-app/tree/v22)

- [Conftest.py](https://github.com/iteam1/social-app/tree/v22)

- [Testing](https://github.com/iteam1/social-app/tree/v22)

**Section 17: CI/CD pipeline**

- [CI/CD intro](https://github.com/iteam1/social-app/tree/v23)

- [Github Actions](https://github.com/iteam1/social-app/tree/v23)

- [Creating Jobs](https://github.com/iteam1/social-app/tree/v23)

- [setup python/dependencies/pytest](https://github.com/iteam1/social-app/tree/v23)

- [Env variables](https://github.com/iteam1/social-app/tree/v23)

- [Github Secrets](https://github.com/iteam1/social-app/tree/v23)

- [Testing database](https://github.com/iteam1/social-app/tree/v23)

- [Building Docker images](https://github.com/iteam1/social-app/tree/v23)

- [Deploy to heroku](https://github.com/iteam1/social-app/tree/v23)

- [Failing tests in pipeline](https://github.com/iteam1/social-app/tree/v23)

- [Deploy to Ubuntu](https://github.com/iteam1/social-app/tree/v23)

</p>
</details>

### References

[Python API Development - Comprehensive Course for Beginners](https://www.youtube.com/watch?v=0sOvCWFmrtA)

[fastapi-course](https://github.com/Sanjeev-Thiyagarajan/fastapi-course)

[FastAPI official document](https://fastapi.tiangolo.com/tutorial/)

[HTTP methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

[download Postman](https://www.postman.com/downloads/)

[pydantic](https://pydantic-docs.helpmanual.io/)

[HTTP Status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

[PostgreSQL Tutorial](https://www.postgresqltutorial.com/)

[ubuntu-install-postgresql-and-pgadmin](https://codingpub.dev/ubuntu-install-postgresql-and-pgadmin/)

[Ubuntu: Install PostgreSQL and pgAdmin](https://www.pgadmin.org/download/pgadmin-4-apt/)

[Postgres Datatype](https://www.postgresql.org/docs/current/datatype.html)

[PostgreSQL Python driver](https://www.psycopg.org/docs/)

[Sqlalchemy](https://www.sqlalchemy.org/)

[Python Typing - Type Hints & Annotations](https://www.youtube.com/watch?v=QORvB-_mbZ0)

[Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/)

[JSON Web Token Builder](http://jwtbuilder.jamiekurtz.com/)

[Online JWT Generator](https://www.javainuse.com/jwtgenerator)

[OAuth2 with Password (and hashing), Bearer with JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

[Decode token online tool](http://calebb.net/)

[Alembic](https://alembic.sqlalchemy.org/en/latest/)

[CORS (Cross-Origin Resource Sharing)](https://fastapi.tiangolo.com/tutorial/cors/)

[Heroku *Free*](https://www.heroku.com/)

[Heroku-Postgres](https://devcenter.heroku.com/articles/heroku-postgresql)

[DigitalOcean](https://www.digitalocean.com/)

[VirtualBox](https://phoenixnap.com/kb/install-virtualbox-on-ubuntu)

[Creating a Linux Virtual Machine with VirtualBox](https://www.youtube.com/watch?v=Fy0MuysJU5Q)

[ubuntu release](https://releases.ubuntu.com/)

[Xubuntu](https://xubuntu.org/)

[postgresql-docker](https://www.sqlshack.com/getting-started-with-postgresql-on-docker/)

[nginx](https://www.nginx.com/)

[namecheap](https://www.namecheap.com/)

[certbot](https://certbot.eff.org/)

[dockerhub](https://hub.docker.com/)

[pytest](https://docs.pytest.org/en/7.2.x/)

[FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/)

[Mock-data mockaroo](https://www.mockaroo.com/)

[github-action](https://docs.github.com/en/actions)

[github marketplace](https://github.com/marketplace?type=)