from flask import Flask, abort
from flasgger import Swagger, Schema, fields
from marshmallow.validate import Length, OneOf

app = Flask(__name__)
Swagger(app)

swag = {"swag": True,
        "tags": ["demo"],
        "responses": {200: {"description": "Success request"},
                      400: {"description": "Validation error"}}}


class Body(Schema):
    color = fields.List(fields.String(), required=True, validate=Length(max=5), example=["white", "blue", "red"])

    def swag_validation_function(self, data, main_def):
        self.load(data)

    def swag_validation_error_handler(self, err, data, main_def):
        abort(400, err)


class Query(Schema):
    color = fields.String(required=True, validate=OneOf(["white", "blue", "red"]))

    def swag_validation_function(self, data, main_def):
        self.load(data)

    def swag_validation_error_handler(self, err, data, main_def):
        abort(400, err)

    swag_in = "query"


@app.route("/color/<id>/<name>", methods=["POST"], **swag)
def index(body: Body, query: Query, id: int, name: str):
    return {"body": body, "query": query, "id": id, "name": name}

if __name__ == "__main__":
    app.run(debug=True)