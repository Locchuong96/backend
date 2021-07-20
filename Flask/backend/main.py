import pandas as pd 
from flask import Flask,jsonify

df = pd.read_excel('data.xlsx')

y = []
for i in range(len(df)):
    x = {'imageLink': df.iloc[i]['imageLink'],
          'totalPrice': df.iloc[i]['totalPrice'],
          'squarePrice': df.iloc[i]['squarePrice'],
          'mainTitle': df.iloc[i]['mainTitle'],
          'mainAddress': df.iloc[i]['mainAddress'],
          'bathNumber': df.iloc[i]['bathNumber'],
          'bedNumber': df.iloc[i]['bedNumber'],
          'mainSquare': df.iloc[i]['mainSquare'],
          'mainOrientation': df.iloc[i]['mainOrientation'],
          'detailPage': df.iloc[i]['detailPage'], 
          'mainID': df.iloc[i]['mainID'],
          'latitude': df.iloc[i]['latitude'],
          'longitude': df.iloc[i]['longitude']}
    y.append(x)

app = Flask(__name__)

@app.route('/')
def data_backend():
    return 'Hello World!'

@app.route('/data',methods = ['GET'])
def get():
    return jsonify({'data':y})

if __name__ == "__main__":
    app.run(debug = True)