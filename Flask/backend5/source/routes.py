from source import app, db
from source.models import Realestate
from source.models import realestate_schema, realestates_schema

@app.route("/")
def index():
    result = Realestate.query.all()
    return realestates_schema.jsonify(result)