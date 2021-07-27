from flask import Flask, render_template, redirect,request,url_for

app = Flask(__name__)

users = ['Loc','JohnnyDang','Eminem','VuongPham']

@app.route("/success/<username>")
def hello(username):
    return "<h4> Wellcome {} </h4>".format(username)

@app.route("/login", methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        #name = request.form['username']
        name = request.form.get('username')
        if name in users:
            return redirect(url_for('hello',username = name))
        else:
            return redirect(url_for('login'))
    else:
        return render_template('login_page.html')

if __name__ =="__main__":
    app.run(debug = True)