from source import app, db, ma

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200),nullable = False)
    date = db.Column(db.String(100),nullable = False)
    complete = db.Column(db.Boolean, nullable = False)

    def __repr__(self):
        return f"('{self.id}','{self.title}','{self.date}','{self.complete}')"

class ToDo_Schema(ma.SQLAlchemySchema):
    
    class Meta:
        model = ToDo
    
    id = ma.auto_field()
    title =ma.auto_field()
    date = ma.auto_field()
    complete = ma.auto_field()

todo_schema = ToDo_Schema()
todos_schema = ToDo_Schema(many = True)
