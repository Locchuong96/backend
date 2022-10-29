## Install PostgreSQL Pgadmin

### Install PostgreSQL

- insall postgresql this command `sudo apt install postgresql`

- switch over to the postgres account on your server `sudo -i -u postgres`

- then you can access the postgres prompt by running `psql`

- to exit postgresql prompt `\q`

- to go back the linux command prompt `exit`

### Set root user credentials

- Login to Postgresql shell `sudo -u postgres psql`

- Then set root user credentials using the command `ALTER USER postgres PASSWORD '<password>';` (pass: `admin123`)

- Henceforth you can login to the PostgreSQL shell using the command `psql -U postgres -h localhost`

### Create multiple users (optional)

- You can create user using the command `CREATE USER <username> WITH CREATEDB LOGIN ENCRYPTED PASSWORD '<password>';`

- You can grant access to existing databases to the user using the command `GRANT ALL PRIVILEGES ON DATABASE codingpub TO <username>;`

### Install PgAdminv4

- Create the repository configuration file:

		curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg

- Create the repository configuration file:

		sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'

- Install for desktop mode only: `sudo apt install pgadmin4-desktop` 
	
	- pass in `admin123` (the same as super user)
	- pass to create server with username `postgres`: admin123

- Install for both desktop and web modes: `sudo apt install pgadmin4`

- Install for web mode only:  `sudo apt install pgadmin4-web`

To configure web mode, run the command: `sudo /usr/pgadmin4/bin/setup-web.sh`

### Remove PostgreSQL and Pgadmin4

- remove postgres `sudo apt-get --purge remove postgresql postgresql-*`

- remove pgadminv4 `sudo apt-get --purge remove pgadmin*`

### Install Postgres Adapter 

On Ubuntu: `pip install psycopg2-binary`