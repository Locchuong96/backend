**Connect to database**

Before go inside the database, you have to give the `psql` know these argument:

	hostname
	portname
	databasename
	username
	password of username

The connection is follow this: `[your_terminal] -> [psql] -> [your_database]`

- In os-system like Linux and Mac, you can open terminal shell with this `psql -h [
HOSTNAME] -U [USERNAME] -p [PORTNAME] [DATABASENAME]` ex `psql -h localhost -U postgres -p 5432 test`

- In Windows you can open `SQL Shell`, you have to enter these argument as the inputs.