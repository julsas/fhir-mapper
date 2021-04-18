from app.DeviceUseStatement import transform_device_use_statement_3to4
from app.Device import transform_device_3to4
from app.AllergyIntolerance import transform_allergy_intolerance_3to4
from app.MedicationStatement import transform_medication_statement_3to4
from app.CapabilityStatement import create_capabiliy_statement
from app.Observation import transform_observation_3to4
from app.Condition import transform_condition_3to4
from app.Patient import transform_patient_3to4
from app.ArbitraryMapper import transform_arbitrary_resource
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

class Patient(Resource):
    def post(self):
        resource = request.get_json()
        transformed_resource = transform_patient_3to4(resource)
        response = app.response_class(
            response=transformed_resource.json(),
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

class Observation(Resource):
    def post(self):
        resource = request.get_json()
        transformed_resource = transform_observation_3to4(resource)
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            mimetype='application/fhir+json'
        )
        return response

class Condition(Resource):
    def post(self):
        resource = request.get_json()
        transformed_resource = transform_condition_3to4(resource)
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            mimetype='application/fhir+json'
        )
        return response

class AllergyIntolerance(Resource):
    def post(self):
        resource = request.get_json()
        transformed_resource = transform_allergy_intolerance_3to4(resource)
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            mimetype='application/fhir+json'
        )
        return response

class Device(Resource):
    def post(self):
        resource = request.get_json()
        transformed_resource = transform_device_3to4(resource)
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            mimetype='application/fhir+json'
        )
        return response

class DeviceUseStatement(Resource):
    def post(self):
        resource = request.get_json()
        transformed_resource = transform_device_use_statement_3to4(resource)
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            mimetype='application/fhir+json'
        )
        return response

class ArbitraryEndpoint(Resource):
    def post(self):
        resource = request.get_json()
        transformed_resource = transform_arbitrary_resource(resource)
        response = app.response_class(
            response=transformed_resource,
            status=200,
            mimetype='application/fhir+json'
        )
        return response

api.add_resource(CapabilityStatement, "/metadata")
api.add_resource(Patient, "/Patient")
api.add_resource(Medication, "/Medication")
api.add_resource(MedicationStatement, "/MedicationStatement")
api.add_resource(Observation, "/Observation")
api.add_resource(Condition, "/Condition")
api.add_resource(AllergyIntolerance, "/AllergyIntolerance")
api.add_resource(Device, "/Device")
api.add_resource(DeviceUseStatement, "/DeviceUseStatement")
api.add_resource(ArbitraryEndpoint, "/ArbitraryResource")

if __name__ == "__main__":
    app.run(debug=True)

    