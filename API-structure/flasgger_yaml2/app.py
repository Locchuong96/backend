from flask import Flask, jsonify 
from flasgger import Swagger, swag_from 

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/colors/<palette>/')
def colors(palette):
    """
    file: colors.yml
    """
    all_colors = {
        "cmyk": ['cian','magenta','yellow','black'],
        "rgb": ['red','green','blue']
    }
    if palette == 'all':
        result = all_colors
    else:
        result = {palette: all_colors.get(palette)}

    return jsonify(result)

app.run(debug = True)

