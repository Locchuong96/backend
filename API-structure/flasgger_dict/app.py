from flask import Flask, jsonify 
from flasgger import Swagger, swag_from 

app = Flask(__name__)
swagger = Swagger(app)

colors_dict = {
    "parameters":[
        {
            "name"    : "palette",
            "in"      : "path",
            "type"    : "string",
            "enum"    : ["all","rgb","cmyk"],
            "required": "true",
            "default" : "all"
        }
    ],
    "definitions":{
        "Palette":{
            "type":"object",
            "properties":{
                "palette_name":{
                    "type":"array",
                    "items":{
                        "$ref":"#/definitions/Color"
                    }
                }
            }
        },
        "Color":{
            "type":"string"
        }
    },
    "responses":{
        "200":{
            "description":"A list of colors (may be filtered by palette)",
            "schema":{
                "$ref":"#/definitions/Palette"
            },
            "examples":{
                "application/json":{"rgb":["red","green","blue"]}       
                }
            }
        }
    }

@app.route("/colors/<palette>/")
@swag_from(colors_dict)
def colors(palette):
    """
    Example endpoint returning a list of colors by palette
    In this example the specification is taken from specs_dict
    """
    all_colors = {
        "cmyk":['cian','magenta','yellow','black'],
        "rbg": ['red','green','blue']
    }
    if palette == 'all':
        result = all_colors 
    else:
        result = {palette : all_colors.get(palette)}
    
    return jsonify(result)

app.run(debug = True)