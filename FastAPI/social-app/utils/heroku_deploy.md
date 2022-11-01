- install `heroku` on ubuntu `sudo snap install heroku --classic` or install heroku CLI `curl https://cli-assets.heroku.com/install.sh | sh`

- check install version `heroku --version`

- get help `heroku --help`

- login heroku `heroku login`

- create `runtime.txt` for specify python version `python-3.9.15` for heroku detect version python

- If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key. heroku login create repo on heroku `heroku create`

- define how to run your app with Procfile `touch Profile`

		web: uvicorn main:app --host=0.0.0.0 --port=${PORT:-5000}

- connect git with heroku `heroku git:remote -a <your-heroku-app-name>`

- commit changes with git

		git add .
		git commit -am "make it better"
		deploy repo on heroku git push heroku main

- Check logs `heroku --tail`

*Note* python verison 3.6.9 is not supported on heroku

- create heroku-postgres instance `heroku addons:create heroku-postgresql:hobby-dev`

- check heroku add-ons `heroku addons`

		Host ec2-52-21-136-176.compute-1.amazonaws.com
		
		Database d5ad61t359skrn
		
		User nekwrrutkwqrwf
		
		Port 5432
		
		Password 39e13b566681abaa3219819dcccb0d1fc3e3e0b432046c92a19b6b6ddf3a5438
		
		URI postgres://nekwrrutkwqrwf:39e13b566681abaa3219819dcccb0d1fc3e3e0b432046c92a19b6b6ddf3a5438@ec2-52-2
		1-136-176.compute-1.amazonaws.com:5432/d5ad61t359skrn
		
		Heroku CLI heroku pg:psql postgresql-colorful-79271 --app tranquil-cliffs-83883

- restart app `heroku ps:restart`

- view logs-tail `heroku logs -t`

- get heroku app info `heroku app`

- Alembic migrations on Heroku Postgres instance `heroku run "alembic upgrade head"`