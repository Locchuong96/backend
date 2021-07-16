from flask import Flask , abort 

def load_user(id):
    users = {
        "1" : "Tom"  ,
        "2" : "Jimmy",
        "3" : "Emily",
        "4" : "Daine",
        "5" : "Harry"
    }
    return users.get(id)

app = Flask(__name__)

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1> Hello {} </h1>'.format(user)

if __name__ == "__main__":
    app.run(debug = True)
    
