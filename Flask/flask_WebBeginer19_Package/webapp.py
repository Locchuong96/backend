from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blog1.db"

db = SQLAlchemy(app)
from models import User, Post

if __name__ == "__main__":
    app.run(debug =True)

    