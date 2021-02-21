from app.MedicationStatement import transform_medication_statement_3to4
from app.CapabilityStatement import create_capabiliy_statement
#import json
from flask.json import JSONEncoder
from pydantic.json import pydantic_encoder
from app.Medication import transform_medication_3to4
from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse

#class CustomJSONEncoder(JSONEncoder):
#    def default(self, obj):
#        return json.dumps(obj, indent=4, default=pydantic_encoder)

app = Flask(__name__)
#app.json_encoder = CustomJSONEncoder
api = Api(app)

class CapabilityStatement(Resource):
    def get(self):
        resource = create_capabiliy_statement()
        response = app.response_class(
            response=resource.json(),
            status=200,
            mimetype='application/fhir+json'
        )
        return response

class Medication(Resource):
    def post(self):
        resource = request.get_json()
        transformed_resource = transform_medication_3to4(resource)
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            mimetype='application/fhir+json'
        )
        return response

class MedicationStatement(Resource):
    def post(self):
        resource = request.get_json()
        transformed_resource = transform_medication_statement_3to4(resource)
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            mimetype='application/fhir+json'
        )
        return response

api.add_resource(CapabilityStatement, "/metadata")
api.add_resource(Medication, "/Medication")
api.add_resource(MedicationStatement, "/MedicationStatement")

if __name__ == "__main__":
    app.run(debug=True)

    