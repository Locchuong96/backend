# This requests use arguments to query, GET method

from flask import Flask, request

app = Flask(__name__)

@app.route('/query')

def query():

	language = request.args.get('language')
	framework = request.args['framework'] # you will get the error if you dont get the framework arg in your path
	website = request.args.get('website')

	# print(request.args) # This is a imutableDict

	return '''<h1> Your languge is {0} </h1>
				<h2> The framework is {1} </h2>
					<h3> The website is {2} </h3>'''.format(language,framework,website) # http://127.0.0.1:5000/query?language=English&number=Arabic

if __name__ == "__main__":

	app.run(debug = True,port = 5000)