
from flask import Flask,request,jsonify
import numpy as np 
import pickle
import json 

app = Flask(__name__)

@app.route("/")
def homepage():
    return '<h1> I am a Machine Learning Web</h1>'

@app.route('/api/',methods =['POST'])
def makecalc():
    data       = request.get_json()
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)

if __name__ =="__main__":
    modelfile = 'flask_MachineLearning/final_prediction.pickle'
    model     = pickle.load(open(modelfile,'rb'))
    app.run(debug = True,host = '127.0.0.1')
