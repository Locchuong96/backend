# This requests using form, This is the POST method for receive and handle the data, and the method GET for render the form in gui

from flask import Flask, request 

app = Flask(__name__)

#This route got also GET method for render the gui and POST method for handle the posted form 
@app.route('/form', methods = ['GET','POST'])
def form():
	if request.method == 'POST':
		language = request.form.get('lang')
		framework = request.form.get('frame')
		website =  request.form.get('web')

		return '''
		<h1> Your language is {0} </h1>
		<h2> Your framework is {1} </h2>
		<h3> Your website is {2} </h3>
		'''.format(language,framework,website)

	return '''
	<form action = "/form" method = 'POST'>
		Language <input type = 'text' name = 'lang'>
		Framework <input type = 'text' name = 'frame'>
		Website <input type = 'text name = 'web'>
		<button type = 'submit'>Submit</button>
	</form>
	'''

if __name__ == '__main__':
	app.run(debug = True, port = 5000)


