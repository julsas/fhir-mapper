from app.Bundle import transform_bundle_3to4
from app.Composition import transform_composition_3to4
from app.Immunization import transform_immunization_3to4
from app.ImagingStudy import transform_imaging_study_3to4
from app.DiagnosticReport import transform_diagnostic_report_3to4
from app.DeviceUseStatement import transform_device_use_statement_3to4
from app.Device import transform_device_3to4
from app.AllergyIntolerance import transform_allergy_intolerance_3to4
from app.Media import transform_media_3to4
from app.MedicationStatement import transform_medication_statement_3to4
from app.CapabilityStatement import create_capabiliy_statement
from app.Observation import transform_observation_3to4
from app.Condition import transform_condition_3to4
from app.Organization import transform_organization_3to4
from app.Patient import transform_patient_3to4
from app.ArbitraryMapper import transform_arbitrary_resource
from app.Medication import transform_medication_3to4
from app.Practitioner import transform_practitioner_3to4
from app.PractitionerRole import transform_practitioner_role_3to4
from app.Procedure import transform_procedure_3to4
from app.Specimen import transform_specimen_3to4
from flask import Flask, request
from flask_restful import Api, Resource, Headers
from logging import FileHandler, WARNING

app = Flask(__name__)

api = Api(app)

file_handler = FileHandler('log.txt')
file_handler.setLevel(WARNING)

app.logger.addHandler(file_handler)

headers = Headers()
headers.add('Accept', 'application/fhir+json; fhirVersion=4.0')
headers.add('Content-Type', 'application/fhir+json; fhirVersion=4.0')

class CapabilityStatement(Resource):
    def get(self):
        resource = create_capabiliy_statement()
        response = app.response_class(
            response=resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json, fhirVersion=4.0'
        )
        return response

class Patient(Resource):
    def post(self):
        resource = request.get_json()
        transformed_resource = transform_patient_3to4(resource)
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json; fhirVersion=4.0'
        )
        return response

class Medication(Resource):
    def post(self):
        resource = request.get_json()
        transformed_resource = transform_medication_3to4(resource)
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
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
            headers=headers,
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
            headers=headers,
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
            headers=headers,
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
            headers=headers,
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
            headers=headers,
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
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class DiagnosticReport(Resource):
    def post(self):
        resource = request.get_json()
        transformed_resource = transform_diagnostic_report_3to4(resource)
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class ImagingStudy(Resource):
    def post(self):
        resource = request.get_json()
        transformed_resource = transform_imaging_study_3to4(resource)
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class Immunization(Resource):
    def post(self):
        resource = request.get_json()
        transformed_resource = transform_immunization_3to4(resource)
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class Media(Resource):
    def post(self):
        resource = request.get_json()
        transformed_resource = transform_media_3to4(resource)
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class Organization(Resource):
    def post(self):
        resource = request.get_json()
        transformed_resource = transform_organization_3to4(resource)
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class PractitionerRole(Resource):
    def post(self):
        resource = request.get_json()
        transformed_resource = transform_practitioner_role_3to4(resource)
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class Composition(Resource):
    def post(self):
        resource = request.get_json()
        transformed_resource = transform_composition_3to4(resource)
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class Practitioner(Resource):
    def post(self):
        resource = request.get_json()
        transformed_resource = transform_practitioner_3to4(resource)
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class Procedure(Resource):
    def post(self):
        resource = request.get_json()
        transformed_resource = transform_procedure_3to4(resource)
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class Specimen(Resource):
    def post(self):
        resource = request.get_json()
        transformed_resource = transform_specimen_3to4(resource)
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class Bundle(Resource):
    def post(self):
        resource = request.get_json()
        transformed_resource = transform_bundle_3to4(resource)
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
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
            headers=headers,
            mimetype='application/fhir+json; fhirVersion=4.0'
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
api.add_resource(DiagnosticReport, "/DiagnosticReport")
api.add_resource(ImagingStudy, "/ImagingStudy")
api.add_resource(Immunization, "/Immunization")
api.add_resource(Media, "/Media")
api.add_resource(Organization, "/Organization")
api.add_resource(PractitionerRole, "/PractitionerRole")
api.add_resource(Composition, "/Composition")
api.add_resource(Practitioner, "/Practitioner")
api.add_resource(Procedure, "/Procedure")
api.add_resource(Bundle, "/Bundle")
api.add_resource(ArbitraryEndpoint, "/ArbitraryResource")

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)

    