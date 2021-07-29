from flask import Flask, request,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
ma = Marshmallow()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100),nullable = False)
    author = db.Column(db.String(40),nullable = False)
    comment = db.Column(db.String(500),nullable = False)
    quantity = db.Column(db.Integer,nullable = False)
    price = db.Column(db.Float,nullable = False)

    def __repr__(self):
        return f"Book('{self.title}','{self.author}','{self.quantity}','{self.price}')"

class Book_Schema(ma.SQLAlchemySchema):
    class Meta:
        model = Book

    id = ma.auto_field()
    title = ma.auto_field()
    author = ma.auto_field()
    comment = ma.auto_field()
    quantity = ma.auto_field()
    price = ma.auto_field()

book_schema = Book_Schema()
books_schema = Book_Schema(many = True)

@app.route("/", methods= ['GET'])
def get_all():
    result=  Book.query.all()
    return books_schema.jsonify(result)

@app.route("/post_book", methods = ['GET','POST'])
def post_new():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        comment = request.form.get('comment')
        quantity = request.form.get('quantity')
        price = request.form.get('price')
        newbook = Book(title = title, author = author, comment=  comment, quantity = quantity, price = price)
        db.session.add(newbook)
        db.session.commit()
        return book_schema.jsonify(newbook)
    else:
        return render_template('post_page.html')

@app.route("/search_book",methods = ['GET','POST'])
def search():
    if request.method == 'POST':
        keyword = request.form['keyword']
        books = Book.query.all()
        result = []
        for book in books:
            if (keyword.lower() in book.title.lower()) or (keyword.lower() in book.author.lower()):
                result.append(book)
        count = len(result)
        return render_template('bookresult.html',count = count,result = result)
    else:
        return render_template('search_page.html')

@app.route("/update_book",methods = ['GET','POST'])
def update():
    if request.method == 'POST':
        id = request.form.get('id')
        book = Book.query.get(id)

        if request.form['title'] != "":
            book.title = request.form['title']

        if request.form['author'] != "":
            book.author = request.form['author']
        
        if request.form['comment'] != "":
            book.comment = request.form['comment']

        if request.form['quantity'] != "":
            book.quantity = request.form['quantity']
        
        if request.form['price'] != "":
            book.price = request.form['price']

        db.session.commit()

        return book_schema.jsonify(book)
    else:
        return render_template('put_page.html')

@app.route("/remove_book",methods = ['GET','POST'])
def remove():
    if request.method == 'POST':
        id = int(request.form['id'])
        book = Book.query.get(id)
        db.session.delete(book)
        db.session.commit()
        return book_schema.jsonify(book)

    else:
        return render_template('delete_page.html')

if __name__ == "__main__":
    app.run(debug = True)


