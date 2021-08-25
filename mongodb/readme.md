# mongoDB 

## Pymongo, Flask Pymongo, Flask MongoEnigne ,Mongo client all come to MongoDB server, local or online

## Use driver Pymongo 

python -m pip install 'pymongo[srv]'

## Flask MongoEngine 

pip3 install flask-mongoengine

  from flask_mongoengine import MongoEngine

  app = Flask(__name__)
  api = Api(app)

  app.config['MONGODB_SETTINGS'] = {
    'db':'todomodel',
    'host':'localhost',
    'port':27017
  }

  db = MongoEngine()

  db.init_app(app)

##  Flask Pymongo

pip3 install Flask-Pymongo

# Install Mongo Client, Mongo Compass

mongo client : sudo apt install mongo-clients | mongo 

mongo compass: mongodb-compass

