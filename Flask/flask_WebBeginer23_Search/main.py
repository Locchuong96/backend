from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///database.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Books(db.Model):
    book_id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(100),nullable = True)
    title = db.Column(db.String(100),nullable = False)
    price = db.Column(db.Float,nullable = False)

    def __repr__(self):
        return f"Book('{self.book_id}','{self.author}','{self.title}','{self.price}')"

class Book_Schema(ma.SQLAlchemySchema):
    class Meta:
        model = Books
        #_include_sqlalchemy = True
    
    book_id = ma.auto_field()
    author = ma.auto_field()
    title = ma.auto_field()
    price = ma.auto_field()

book_schema = Book_Schema()
books_schema = Book_Schema(many = True)

@app.route("/books",methods = ['GET'])
def search():
    return render_template('search.html')

@app.route("/books",methods = ['POST'])
def bookresult():
    
    author = request.form.get('author')
    title = request.form.get('title')
    price = request.form.get('price')
    result = []
    all_row = Books.query.all()
    
    for row in all_row:
        if title.lower() in row.title.lower():
            result.append(row)

    return  render_template('bookresult.html',count = len(result) ,result = result)

if __name__ == "__main__":
    app.run(debug = True)
     