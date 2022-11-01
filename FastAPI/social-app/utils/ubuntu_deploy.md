## Create Linux virtual machine 

### Create virtual machine by virtualbox

- download and install [VirtualBox](https://phoenixnap.com/kb/install-virtualbox-on-ubuntu)

- download [ubuntu release](https://releases.ubuntu.com/)


### Run by docker Ubuntu image

- list all container is running `docker rm -f $(docker ps -a -q)`

- pull ubuntu image: `docker pull ubuntu`

- run docker imgae interactive mode `sudo docker run -t -p 8000:8000 [your image name]`

- start the container `sudo docker container start [container id]`

- stop the container `docker stop [container_id or name]`

- delete all container `docker rm -f [container_id or name]`

- open terminal inside container `docker exec -it [container id] /bin/sh`

- jump out the container termial `exit`

## Update packages

- update packages `sudo apt update`

- update and upgrade `sudo apt update && upgrade -y`

- install text vim-editor `sudo apt install vim` or nano-editor `sudo apt install nano`

## Install Python

- check python version `python3 --version`

- install python3 `sudo apt-get install python3`

- check pip3 version `pip3 --version`

- install pip version `sudo apt install python3-pip`

- check pip3 list `pip3 list`

- install  virtualenv package by pip `sudo pip3 install virtualenv`

## Run postgresql container

- create postgresql container map internal port 5432 to external port 5431: `sudo docker run --name pgsql-dev -e POSTGRES_PASSWORD=pass123 -p 5431:5432 postgres`

- This command will start an interactive terminal inside the container. Next, you can start the PostgreSQL by running the following command on the same terminal. `docker exec -it pgsql-dev bash`

- start the postgres-container `sudo docker start 8121bd993540`

- you can access postgres docker-container with  address `172.0.0.1` port `5431`

## Install Postgres & setup password On virtual machine

- check your user role `whoami`

- install postgres `-y` (yes option as default) `sudo apt install postgresql-15.0 postgresql-contrib-15.0 -y`

- remove postgres `sudo apt-get remove --purge postgres*`

- access postgres on your machine and get help `psql --help` ,check version `psql --version`

- check the list of all user on your machine `sudo cat /etc/passwd`

- change the name of user `su - postgres`

- login to the database `postgres` exit your role and go back to root role `exit`

- go to default database `psql -U -postgres -d postgres`

## Postgres Config

- to to postgres installation floder `cd /etc/postgresql`

- go to main `cd /etc/postgresql/14/main`

		conf.d	     pg_ctl.conf  pg_ident.conf    start.conf
		environment  pg_hba.conf  postgresql.conf

- edit `postgresql.conf`: `vi postgresql.conf`

		#------------------------------------------------------------------------------
		# CONNECTIONS AND AUTHENTICATION
		#------------------------------------------------------------------------------
		# - Connection Settings -
		#listen_addresses = 'localhost'         # what IP address(es) to listen on;
		                                        # comma-separated list of addresses;
		                                        # defaults to 'localhost'; use '*' for all

edit the `listen_addresses` to access remotely

		#------------------------------------------------------------------------------
		# CONNECTIONS AND AUTHENTICATION
		#------------------------------------------------------------------------------
		# - Connection Settings -
		listen_addresses = '*' # your ip addresses , * allow access from any where
		#listen_addresses = 'localhost'         # what IP address(es) to listen on;
		                                        # comma-separated list of addresses;
		                                        # defaults to 'localhost'; use '*' for all

- edit `pg_hba.conf`

		# Database administrative login by Unix domain socket
		local   all             postgres                                peer
		# TYPE  DATABASE        USER            ADDRESS                 METHOD
		# "local" is for Unix domain socket connections only
		local   all             all                                     peer
		# IPv4 local connections:
		host    all             all             127.0.0.1/32            scram-sha-256
		# IPv6 local connections:
		host    all             all             ::1/128                 scram-sha-256

to 

		# Database administrative login by Unix domain socket
		local   all             postgres                                md5
		# TYPE  DATABASE        USER            ADDRESS                 METHOD
		# "local" is for Unix domain socket connections only
		local   all             all                                     md5
		# IPv4 local connections:
		host    all             all             0.0.0.0/0            	md5
		# IPv6 local connections:
		host    all             all             ::/0                 	md5
 
- restart to save change `systemctl restart postgresql`

## Create new user and setup python environment

- create new user `adduser admin` pass `pass123`

- change to new user role `su - admin`

- from root role give admin sudo permission `usermod -aG sudo admin`

- go to your home `cd ~`

- create directory app `mkdir app` and cd to it `cd app`

- create virtualenv `virtualenv env`

- activate and deactivate virtualenv `source env/bin/activate` and `deactivate`

- create src directory `mkdir src` and go to it `cd src`

- clone repo but without create directory name `git clone https://github.com/iteam1/social-app.git .
` 

## Environment Variables

- assign env-var `export MY_VAR = 123`

- clear env-var `unset MY_VAR = 123`

- go back home directory `cd ~`

- create .env file `touch .env` and open it `nano .env`, list hidden file `ls -la`

- set all env-vars `source .env`

- check all env-vars `printenv`
 
- export env-vars `set -o allexport; source /home/admin/.env; set +o allexport`

- list hidden file and find .procfile in home directory, then copy the export command and save it, the set env-vars will run automaticlly.

		export DATABASE_USERNAME=postgres
		export DATABASE_PASSWORD=pass123
		export DATABASE_NAME=fastapi
		export DATABASE_PORT=5432
		export DATABASE_HOSTNAME=172.17.0.2
		export ALGORITHM=HS256
		export SECRET_KEY=09c47fdd132bc4c948adf7dac546c2213ab91cbdd572addbfb844aab6167d295
		export ACCESS_TOKEN_EXPIRE_MINUTES=30

## Alembic migrations on production database

- generate database by alembic `alembic uprade head`

*Note* when you run app-container and postgres-container with map port, therse containers are in the same docker internal network, so you can access database postgres on app-container by port 5432 but when you go outside, port 5432 in the container will mapp to 5431 and access via ip 172.17.0.1

## Gunicorn

- run app listen on any ip-address `uvicorn --host 0.0.0.0 app.main:app`

- run by gunicorn setup 2 workers `gunicorn -w 2 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000
`
- check working `ps -aef | grep -i gunicorn`

## Creating a Systemd service

- run app when reboot in background

- check service `cd /etc/systemd/system/`

- create service `nano <your-service-name>.service` with content

		[Unit]
		Description=demo fastapi application
		After=network.target
		[Service]
		User=admin
		Group=admin
		WorkingDirectory=/home/admin/app/src/
		Environment="PATH=/home/admin/app/env/bin"
		EnvironmentFile=/home/amdin/.env
		ExecStart=/home/admin/app/env/bin/gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000
		[Install]
		WantedBy=multi-user.target

- start service `systemctl start <your-service-name>`

- check service serivce `systemctl start <your-service-name>`

- restart your service `systemctl start <your-service-name>`

- enable autostart when reboot `sudo systemctl enable <your-service-name>`
	
**NGINX**

**Setting up Domain name**

**SSL/HTTPS**

**NGINX enable**

**Firewall**

**Pushing code changes to Production**