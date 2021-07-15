"""
The server needs uniform time units that are indepdent of the location of each user
typically Coordinated Universal Time (UTC) is useds
open source library written in JavaScript that renders dates and times in the browser called Moment.js
flask-moment is an extension for Flask applications that makes the integration of Momment,js into JinJa2 templates easy
"""
from flask import Flask, render_template #Create a app 
from flask_moment import Moment #Create a moment object
from datetime import datetime

app = Flask(__name__)

moment = Moment(app)

@app.route("/")
def base():
    return render_template('base.html',current_time = datetime.utcnow())

if __name__ == "__main__": 
    app.run(debug = True)
