# This requests using json, this is th POST method

# import requests  

# json = {
# 	"language": "python",
# 	"framework": "flask",
# 	"website": "scotch",
# 	"version_info": {
# 		"python": 3.7,
# 		"flask" : 1.0
# 		},
# 	"examples": ['query','form','json'],
# 	'boolean_test': True
# }

# response = requests.post('http://127.0.0.1:5000/json',json = json)
# print(response.content)
# print(response.json)

from flask import Flask, request

app = Flask(__name__)

@app.route('/json',methods = ['POST'])
def json():
	req_data = request.get_json()
	language = req_data['language']
	framework = req_data['framework']
	website = req_data['website']

	return '''
	<h1> Your language is {0} </h1>
	<h2> Your framework is {1} </h2>
	<h3> Your website is {2} <h3>
	'''.format(language,framework,website)

if __name__ == "__main__":
	app.run(debug = True,port = 5000)


