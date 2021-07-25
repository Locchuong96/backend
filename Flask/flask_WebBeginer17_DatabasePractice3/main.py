from flask import Flask, jsonify 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///site.db"

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Author(db.Model):
    id = db.Column(db.Integer,primary_key =True)
    name = db.Column(db.String(255))
    books = db.relationship("Book",backref = "author")

    def __repr__(self):
        return f"Author('{self.id}','{self.name}')"

class Book(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    author_id = db.Column(db.Integer,db.ForeignKey("author.id"))
    #author =db.relationship("Author",backref = "books")

    def __repr__(self):
        return f"Book('{self.id}','{self.title}','{self.author_id}')"

class Author_Schema(ma.SQLAlchemySchema):
    class Meta:
        model = Author
        _include_sqlalchemy = True

    name = ma.auto_field()
    books = ma.auto_field()

author_schema = Author_Schema()
authors_schema = Author_Schema(many = True)

class Book_Schema(ma.SQLAlchemySchema):
    class Meta:
        model = Book
        _include_sqlalchemy = True
    
    title = ma.auto_field()
    author_id = ma.auto_field()
    author = ma.auto_field() # You can do it bacause _include_sqlalchemy

book_schema = Book_Schema()
books_schema = Book_Schema(many = True)

@app.route("/authors",methods  = ['GET'])
def get_author():
    authors = Author.query.all()
    return  authors_schema.jsonify(authors)

@app.route("/books",methods  = ['GET'])
def get_book():
    books = Book.query.all()
    return  books_schema.jsonify(books)

if __name__ == "__main__":
    app.run(debug = True)
