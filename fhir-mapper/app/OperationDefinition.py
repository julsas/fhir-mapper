from fhir.resources.operationdefinition import (OperationDefinition, OperationDefinitionParameter)
from fhir.resources.bundle import (Bundle, BundleEntry)
import datetime

dateTime = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()
dateTime = str(dateTime)

bundle_example = {
  "resourceType": "Bundle",
  "type": "transaction"
}

operation_definition_example = {
  "resourceType": "OperationDefinition",
  "url": "http://h7.org/fhir/OperationDefinition/example",
  "name": "Populate Questionnaire",
  "status": "draft",
  "kind": "operation",
  "code": "populate",
  "system": False,
  "type": False,
  "instance": True
}

parameter_example = {
      "name": "subject",
      "use": "in",
      "min": 1,
      "max": "1"
    }

supported_resources = [    
    "AllergyIntolerance",
    "Bundle",
    "Composition",
    "Condition",
    "Device",
    "DeviceUseStatement",
    "DiagnosticReport",
    "ImagingStudy",
    "Immunization",
    "Media",
    "Medication",
    "MedicationStatement",
    "Observation",
    "Organization",
    "Patient",
    "Practitioner",
    "PractitionerRole", 
    "Procedure", 
    "Specimen"
    ]

def create_operation_definition_3to4():
    operation_transform_3to4 = OperationDefinition.parse_obj(operation_definition_example)
    operation_transform_3to4.id = 'transform-3to4'
    operation_transform_3to4.url = 'https://hpi.de/fhir/OperationDefinition/transform-3to4'
    operation_transform_3to4.version = '1.0'
    operation_transform_3to4.name = 'Resource Transformation STU3 to R4'
    operation_transform_3to4.title = 'OperationDefinition Transform Resource STU3 to R4'
    operation_transform_3to4.status = 'active'
    operation_transform_3to4.kind = 'operation'
    operation_transform_3to4.date = '2021-05-01'
    operation_transform_3to4.publisher = 'Hasso Plattner Institute for Digital Health'
    operation_transform_3to4.description = 'A FHIR resource in version STU3 is transformed to FHIR R4. A resource to be transformed is provided to the server via a POST request. The transformed resource will be returned, or an OperationOutcome with an error message.'
    operation_transform_3to4.code = 'transform-3to4'
    operation_transform_3to4.resource = supported_resources
    operation_transform_3to4.system = False
    operation_transform_3to4.type = True
    operation_transform_3to4.instance = True

    parameters = []

    input_parameter = OperationDefinitionParameter.parse_obj(parameter_example)
    input_parameter.name = 'input'
    input_parameter.use = 'in'
    input_parameter.min = 1
    input_parameter.max = '1'
    input_parameter.type = 'Resource'
    parameters.append(input_parameter)

    output_parameter = OperationDefinitionParameter.parse_obj(parameter_example)
    output_parameter.name = 'return'
    output_parameter.use = 'out'
    output_parameter.min = 1
    output_parameter.max = '1'
    output_parameter.type = 'Resource'
    parameters.append(output_parameter)

    operation_transform_3to4.parameter = parameters

    return operation_transform_3to4

def create_operation_definition_translate_3to4():
    operation_transform_translate_3to4 = OperationDefinition.parse_obj(operation_definition_example)
    operation_transform_translate_3to4.id = 'transform-and-translate-3to4'
    operation_transform_translate_3to4.url = 'https://hpi.de/fhir/OperationDefinition/transform-and-translate-3to4'
    operation_transform_translate_3to4.version = '1.0'
    operation_transform_translate_3to4.name = 'Resource Transformation and Terminology Translation STU3 to R4'
    operation_transform_translate_3to4.title = 'OperationDefinition Transform and Translate Resource STU3 to R4'
    operation_transform_translate_3to4.status = 'active'
    operation_transform_translate_3to4.kind = 'operation'
    operation_transform_translate_3to4.date = '2021-05-18'
    operation_transform_translate_3to4.publisher = 'Hasso Plattner Institute for Digital Health'
    operation_transform_translate_3to4.description = 'A FHIR resource in version STU3 is transformed to FHIR R4. Plus the engine will connect to a terminology server and try to translate the coded information to a standard terminology. A resource to be transformed is provided to the server via a POST request. The transformed resource will be returned, or an OperationOutcome with an error message.'
    operation_transform_translate_3to4.code = 'transform-and-translate-3to4'
    operation_transform_translate_3to4.resource = ['Medication']
    operation_transform_translate_3to4.system = False
    operation_transform_translate_3to4.type = True
    operation_transform_translate_3to4.instance = True

    parameters = []

    input_parameter = OperationDefinitionParameter.parse_obj(parameter_example)
    input_parameter.name = 'input'
    input_parameter.use = 'in'
    input_parameter.min = 1
    input_parameter.max = '1'
    input_parameter.type = 'Resource'
    parameters.append(input_parameter)

    output_parameter = OperationDefinitionParameter.parse_obj(parameter_example)
    output_parameter.name = 'return'
    output_parameter.use = 'out'
    output_parameter.min = 1
    output_parameter.max = '1'
    output_parameter.type = 'Resource'
    parameters.append(output_parameter)

    operation_transform_translate_3to4.parameter = parameters

    return operation_transform_translate_3to4

def create_operation_definition_bundle():
    return_bundle = Bundle.parse_obj(bundle_example)
    return_bundle.type = 'searchset'
    return_bundle.timestamp = dateTime
    return_bundle.total = 1

    entries = []

    transform_operation_entry = BundleEntry.construct()
    transform_operation_entry.resource = create_operation_definition_3to4()
    entries.append(transform_operation_entry)

    transform_translate_operation_entry = BundleEntry.construct()
    transform_translate_operation_entry.resource = create_operation_definition_translate_3to4()
    entries.append(transform_translate_operation_entry)

    return_bundle.entry = entries

    return return_bundle