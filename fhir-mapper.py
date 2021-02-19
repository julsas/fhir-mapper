from app.CapabilityStatement import create_capabiliy_statement
import json
from flask.json import JSONEncoder
from pydantic.json import pydantic_encoder
from app.Medication import transform_medication_3to4
from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        return json.dumps(obj, indent=4, default=pydantic_encoder)

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
api = Api(app)

class CapabilityStatement(Resource):
    def get(self):
        resource = create_capabiliy_statement()
        return jsonify(resource)

class Medication(Resource):
    def post(self):
        resource = request.get_json()
        transformed_resource = transform_medication_3to4(resource)
        return jsonify(transformed_resource)

api.add_resource(CapabilityStatement, "/metadata")
api.add_resource(Medication, "/Medication")

if __name__ == "__main__":
    app.run(debug=True)

    