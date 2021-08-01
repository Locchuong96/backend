from market import app, db 

class Item(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(length = 30), nullable = False,unique = True)
    price = db.Column(db.Integer,nullable = False)
    barcode = db.Column(db.String(length = 12),nullable = False,unique = True)
    descript = db.Column(db.String(length = 1000),nullable = False,unique = True)

    def __repr__(self):
        return f"Item'{self.name}'"

