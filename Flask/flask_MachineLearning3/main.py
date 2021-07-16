from flask import Flask, render_template, jsonify, request 
import pickle 
import numpy as np

model = pickle.load(open('./flask_MachineLearning3/model.pkl',"rb"))

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('home.html')

@app.route("/predict",methods = ['POST'])
def predict():
    form_data  = request.form.values()
    number_data = [float(x) for x in form_data]
    input  = np.array([number_data])
    output = model.predict(input)
    output = round(output[0],2) 
    return render_template('home.html',predict_value = "Predict Price {} $".format(output))
if __name__ == "__main__":
    app.run(debug = True)