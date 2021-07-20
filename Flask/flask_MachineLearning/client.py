import requests 
import json 

url = "http://127.0.0.1:5000/api/"

data = [[14.34, 1.68, 2.7, 25.0, 98.0, 2.8, 1.31, 0.53, 2.7, 13.0, 0.57, 1.96, 660.0]]

j_data = json.dumps(data)
print(type(j_data))
headers = {'content-type':'application/json','Accept-Charset':'UTF-8'}
r = requests.post(url,data =j_data, headers = headers)

print("Your result: \n",r,r.text)