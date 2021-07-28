from flask import Flask 

app = Flask(__name__)

@app.route("/")
def index():
	return """
			<!doctype html>
			<html>
				<head>
					<title> Server </title>
				</head>
				<body>
					<p class = "title">Site title goes here.</p>
					<p class = "content">Site content goes here.</p>
				</body>
			</html>
			"""

if __name__ == "__main__":
	app.run(debug = True)