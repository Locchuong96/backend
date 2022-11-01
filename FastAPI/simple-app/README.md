# simple-app

## Repository

create a new repository on the command line

	echo "# simple-app" >> README.md
	git init
	git add README.md
	git commit -m "first commit"
	git branch -M main
	git remote add origin git@github.com:iteam1/simple-app.git
	git push -u origin main

or push an existing repository from the command line

	git remote add origin git@github.com:iteam1/simple-app.git
	git branch -M main
	git push -u origin main

## FastAPI app

install packages full `pip3 install fastapi[all]`

## Heroku deploy

create `runtime.txt` for specify python version `python-3.9.15` for heroku detect version python

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key. `heroku login`

create repo on heroku `heroku create`

define how to run your app with Procfile `touch Profile`

connect git with heroku `heroku git:remote -a mysterious-wave-91162`

commit changes with git

	git add .
	git commit -am "make it better"

deploy repo on heroku `git push heroku main`

*Note* python verison 3.6.9 is not supported on heroku

## Reference

[How to upgrade to Python 3.9.0 on Ubuntu 18.04 LTS](https://www.itsupportwale.com/blog/how-to-upgrade-to-python-3-9-0-on-ubuntu-18-04-lts/)

[ImportError: cannot import name 'sysconfig' from 'distutils'](https://askubuntu.com/questions/1292972/importerror-cannot-import-name-sysconfig-from-distutils-usr-lib-python3-9)