from app.OperationDefinition import create_operation_definition_3to4, create_operation_definition_bundle
from app.stu3r4.Bundle import transform_bundle_3to4
from app.stu3r4.Composition import transform_composition_3to4
from app.stu3r4.Immunization import transform_immunization_3to4
from app.stu3r4.ImagingStudy import transform_imaging_study_3to4
from app.stu3r4.DiagnosticReport import transform_diagnostic_report_3to4
from app.stu3r4.DeviceUseStatement import transform_device_use_statement_3to4
from app.stu3r4.Device import transform_device_3to4
from app.stu3r4.AllergyIntolerance import transform_allergy_intolerance_3to4
from app.stu3r4.Media import transform_media_3to4
from app.stu3r4.MedicationStatement import transform_medication_statement_3to4
from app.CapabilityStatement import create_capabiliy_statement
from app.stu3r4.Observation import transform_observation_3to4
from app.stu3r4.Condition import transform_condition_3to4
from app.stu3r4.OperationOutcome import error_handler, operation_type_not_supported
from app.stu3r4.Organization import transform_organization_3to4
from app.stu3r4.Patient import transform_patient_3to4
from app.stu3r4.ArbitraryMapper import transform_arbitrary_resource
from app.stu3r4.Medication import transform_medication_3to4
from app.stu3r4.Practitioner import transform_practitioner_3to4
from app.stu3r4.PractitionerRole import transform_practitioner_role_3to4
from app.stu3r4.Procedure import transform_procedure_3to4
from app.stu3r4.Specimen import transform_specimen_3to4
from flask import Flask, request
from flask_restful import Api, Resource, Headers
from logging import FileHandler, WARNING
from dotenv import load_dotenv
import os

load_dotenv()

ENV_PORT = os.getenv('PORT')

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

class OperationDefinition(Resource):
    def get(self, id=None):
        if request.endpoint != 'instance':
            resource = create_operation_definition_bundle()
        elif id == 'transform-3to4':
            resource = create_operation_definition_3to4()
        response = app.response_class(
            response=resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json, fhirVersion=4.0'
        )
        return response

class Patient(Resource):
    def post(self, operation):
        resource = request.get_json()
        if operation == '$transform-3to4':
            try:
                transformed_resource = transform_patient_3to4(resource)
            except Exception as e:
                transformed_resource = error_handler(e)
        else:
            transformed_resource = operation_type_not_supported()
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json; fhirVersion=4.0'
        )
        return response

class Medication(Resource):
    def post(self, operation):
        resource = request.get_json()
        if operation == '$transform-3to4':
            try:
                transformed_resource = transform_medication_3to4(resource)
            except Exception as e:
                transformed_resource = error_handler(e)
        elif operation == '$transform-and-translate-3to4':
            try:
                transformed_resource = transform_medication_3to4(resource, translate=True)
            except Exception as e:
                transformed_resource = error_handler(e)
        else:
            transformed_resource = operation_type_not_supported()
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class MedicationStatement(Resource):
    def post(self, operation):
        resource = request.get_json()
        if operation == '$transform-3to4':
            try:
                transformed_resource = transform_medication_statement_3to4(resource)
            except Exception as e:
                transformed_resource = error_handler(e)
        else:
            transformed_resource = operation_type_not_supported()
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class Observation(Resource):
    def post(self, operation):
        resource = request.get_json()
        if operation == '$transform-3to4':
            try:
                transformed_resource = transform_observation_3to4(resource)
            except Exception as e:
                transformed_resource = error_handler(e)
        else:
            transformed_resource = operation_type_not_supported()
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class Condition(Resource):
    def post(self, operation):
        resource = request.get_json()
        if operation == '$transform-3to4':
            try:
                transformed_resource = transform_condition_3to4(resource)
            except Exception as e:
                transformed_resource = error_handler(e)
        else:
            transformed_resource = operation_type_not_supported()
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class AllergyIntolerance(Resource):
    def post(self, operation):
        resource = request.get_json()
        if operation == '$transform-3to4':
            try:
                transformed_resource = transform_allergy_intolerance_3to4(resource)
            except Exception as e:
                transformed_resource = error_handler(e)
        else:
            transformed_resource = operation_type_not_supported()
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class Device(Resource):
    def post(self, operation):
        resource = request.get_json()
        if operation == '$transform-3to4':
            try:
                transformed_resource = transform_device_3to4(resource)
            except Exception as e:
                transformed_resource = error_handler(e)
        else:
            transformed_resource = operation_type_not_supported()
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class DeviceUseStatement(Resource):
    def post(self, operation):
        resource = request.get_json()
        if operation == '$transform-3to4':
            try:
                transformed_resource = transform_device_use_statement_3to4(resource)
            except Exception as e:
                transformed_resource = error_handler(e)
        else:
            transformed_resource = operation_type_not_supported()
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class DiagnosticReport(Resource):
    def post(self, operation):
        resource = request.get_json()
        if operation == '$transform-3to4':
            try:
                transformed_resource = transform_diagnostic_report_3to4(resource)
            except Exception as e:
                transformed_resource = error_handler(e)
        else:
            transformed_resource = operation_type_not_supported()
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class ImagingStudy(Resource):
    def post(self, operation):
        resource = request.get_json()
        if operation == '$transform-3to4':
            try:
                transformed_resource = transform_imaging_study_3to4(resource)
            except Exception as e:
                transformed_resource = error_handler(e)
        else:
            transformed_resource = operation_type_not_supported()
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class Immunization(Resource):
    def post(self, operation):
        resource = request.get_json()
        if operation == '$transform-3to4':
            try:
                transformed_resource = transform_immunization_3to4(resource)
            except Exception as e:
                transformed_resource = error_handler(e)
        else:
            transformed_resource = operation_type_not_supported()
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class Media(Resource):
    def post(self, operation):
        resource = request.get_json()
        if operation == '$transform-3to4':
            try:
                transformed_resource = transform_media_3to4(resource)
            except Exception as e:
                transformed_resource = error_handler(e)
        else:
            transformed_resource = operation_type_not_supported()
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class Organization(Resource):
    def post(self, operation):
        resource = request.get_json()
        if operation == '$transform-3to4':
            try:
                transformed_resource = transform_organization_3to4(resource)
            except Exception as e:
                transformed_resource = error_handler(e)
        else:
            transformed_resource = operation_type_not_supported()
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class PractitionerRole(Resource):
    def post(self, operation):
        resource = request.get_json()
        if operation == '$transform-3to4':
            try:
                transformed_resource = transform_practitioner_role_3to4(resource)
            except Exception as e:
                transformed_resource = error_handler(e)
        else:
            transformed_resource = operation_type_not_supported()
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class Composition(Resource):
    def post(self, operation):
        resource = request.get_json()
        if operation == '$transform-3to4':
            try:
                transformed_resource = transform_composition_3to4(resource)
            except Exception as e:
                transformed_resource = error_handler(e)
        else:
            transformed_resource = operation_type_not_supported()
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class Practitioner(Resource):
    def post(self, operation):
        resource = request.get_json()
        if operation == '$transform-3to4':
            try:
                transformed_resource = transform_practitioner_3to4(resource)
            except Exception as e:
                transformed_resource = error_handler(e)
        else:
            transformed_resource = operation_type_not_supported()
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class Procedure(Resource):
    def post(self, operation):
        resource = request.get_json()
        if operation == '$transform-3to4':
            try:
                transformed_resource = transform_procedure_3to4(resource)
            except Exception as e:
                transformed_resource = error_handler(e)
        else:
            transformed_resource = operation_type_not_supported()
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class Specimen(Resource):
    def post(self, operation):
        resource = request.get_json()
        if operation == '$transform-3to4':
            try:
                transformed_resource = transform_specimen_3to4(resource)
            except Exception as e:
                transformed_resource = error_handler(e)
        else:
            transformed_resource = operation_type_not_supported()
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class Bundle(Resource):
    def post(self, operation):
        resource = request.get_json()
        if operation == '$transform-3to4':
            try:
                transformed_resource = transform_bundle_3to4(resource)
            except Exception as e:
                transformed_resource = error_handler(e)
        else:
            transformed_resource = operation_type_not_supported()
        response = app.response_class(
            response=transformed_resource.json(),
            status=200,
            headers=headers,
            mimetype='application/fhir+json'
        )
        return response

class ArbitraryEndpoint(Resource):
    def post(self, operation):
        resource = request.get_json()
        if operation == '$transform-3to4':
            try:
                transformed_resource = transform_arbitrary_resource(resource)
            except Exception as e:
                transformed_resource = error_handler(e)
        else:
            transformed_resource = operation_type_not_supported()
        response = app.response_class(
            response=transformed_resource,
            status=200,
            headers=headers,
            mimetype='application/fhir+json; fhirVersion=4.0'
        )
        return response

@app.route("/")
def home():
    return "This is the base url of a FHIR server. Get started with the CapabilityStatement with GET {base-url}/metadata."

api.add_resource(CapabilityStatement, "/metadata")
api.add_resource(OperationDefinition, "/OperationDefinition", endpoint="search")
api.add_resource(OperationDefinition, "/OperationDefinition/<id>", endpoint="instance")
api.add_resource(Patient, "/Patient/<operation>")
api.add_resource(Medication, "/Medication/<operation>")
api.add_resource(MedicationStatement, "/MedicationStatement/<operation>")
api.add_resource(Observation, "/Observation/<operation>")
api.add_resource(Condition, "/Condition/<operation>")
api.add_resource(AllergyIntolerance, "/AllergyIntolerance/<operation>")
api.add_resource(Device, "/Device/<operation>")
api.add_resource(DeviceUseStatement, "/DeviceUseStatement/<operation>")
api.add_resource(DiagnosticReport, "/DiagnosticReport/<operation>")
api.add_resource(ImagingStudy, "/ImagingStudy/<operation>")
api.add_resource(Immunization, "/Immunization/<operation>")
api.add_resource(Media, "/Media/<operation>")
api.add_resource(Organization, "/Organization/<operation>")
api.add_resource(PractitionerRole, "/PractitionerRole/<operation>")
api.add_resource(Composition, "/Composition/<operation>")
api.add_resource(Practitioner, "/Practitioner/<operation>")
api.add_resource(Procedure, "/Procedure/<operation>")
api.add_resource(Bundle, "/Bundle/<operation>")
api.add_resource(ArbitraryEndpoint, "/ArbitraryResource/<operation>")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    #app.run(debug=True)
    #app.run()

    