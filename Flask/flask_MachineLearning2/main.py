from flask import Flask,render_template, jsonify, request 
import numpy as np 
import pickle

model = pickle.load(open("./flask_MachineLearning2/model.pkl","rb"))

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/predict",methods = ['POST'])
def predict():
    int_features = [ int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    predict_value = model.predict(final_features)
    predict_value = round(predict_value[0],2)
    predict_text = int_features
    return render_template('index.html',predict_text = "Sales should be {} $".format(predict_value))

if __name__ == "__main__":
    app.run(debug = True)
