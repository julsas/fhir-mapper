from datetime import (date, datetime)
from fhir.resources.fhirtypes import (Date)
from fhir.resources.capabilitystatement import (CapabilityStatement, CapabilityStatementSoftware, CapabilityStatementImplementation, CapabilityStatementRest, CapabilityStatementRestResource, CapabilityStatementRestResourceInteraction, CapabilityStatementRestResourceOperation)

# needed to initialize resource and bypass validation bug when constructing resource object
json_data = {
    "resourceType": "CapabilityStatement",
    "status": "active",
    "date": "2021-02-11T15:59:20+10:00",
    "kind": "instance",
    "software": {
        "name": "FHIR Mapper",
        "version": "0.9",
        "releaseDate": "2021-02-11T00:00:00+01:00"
    },
    "implementation": {
        "description": "FHIR mapper instance",
        "url": "http://127.0.0.1:5000/"
    },
    "fhirVersion": "4.0.1",
    "format": [
        "application/fhir+json"
    ],
    "rest": [
        {
            "mode": "server",
            "resource": [
                {
                    "type": "Medication",
                    "profile": "http://hl7.org/fhir/StructureDefinition/Medication"
                }
            ],
            "operation": [
                {
                    "name": "transform-3to4",
                    "definition": "https://hpi.de/fhir/OperationDefinition/transform-3to4"
                }
            ]
        }
    ]
}

operation_example = {
    "name": "transform-3to4",
    "definition": "https://hpi.de/fhir/OperationDefinition/transform-3to4"
}

implemented_resource_types = {
    "AllergyIntolerance": "http://hl7.org/fhir/StructureDefinition/AllergyIntolerance",
    "Bundle": "http://hl7.org/fhir/StructureDefinition/Bundle",
    "Composition": "http://hl7.org/fhir/StructureDefinition/Composition",
    "Condition": "http://hl7.org/fhir/StructureDefinition/Condition",
    "Device": "http://hl7.org/fhir/StructureDefinition/Device",
    "DeviceUseStatement": "http://hl7.org/fhir/StructureDefinition/DeviceUseStatement",
    "DiagnosticReport": "http://hl7.org/fhir/StructureDefinition/DiagnosticReport",
    "ImagingStudy": "http://hl7.org/fhir/StructureDefinition/ImagingStudy",
    "Immunization": "http://hl7.org/fhir/StructureDefinition/Immunization",
    "Media": "http://hl7.org/fhir/StructureDefinition/Media",
    "Medication": "http://hl7.org/fhir/StructureDefinition/Medication",
    "MedicationStatement": "http://hl7.org/fhir/StructureDefinition/MedicationStatement",
    "Observation": "http://hl7.org/fhir/StructureDefinition/Observation",
    "Organization": "http://hl7.org/fhir/StructureDefinition/Organization",
    "Patient": "http://hl7.org/fhir/StructureDefinition/Patient",
    "Practitioner": "http://hl7.org/fhir/StructureDefinition/Practitioner",
    "PractitionerRole": "http://hl7.org/fhir/StructureDefinition/PractitionerRole", 
    "Procedure": "http://hl7.org/fhir/StructureDefinition/Procedure", 
    "Specimen": "http://hl7.org/fhir/StructureDefinition/Specimen"
    }

def create_capabiliy_statement():
    capability_statement = CapabilityStatement.parse_obj(json_data)
    capability_statement.url = "https://hpi.de/fhir/mapping-server/metadata"
    capability_statement.name = "FHIR-conformance-statement-for-mapping-server"
    capability_statement.title = "FHIR conformance statement for mapping server"
    capability_statement.status = "active"
    capability_statement.experimental = "true"
    capability_statement.date = Date(year=2021, month=5, day=1)
    capability_statement.publisher = "Hasso Plattner Institute for Digital Health"
    capability_statement.kind = "instance"
    capability_statement_software = CapabilityStatementSoftware.construct()
    capability_statement_software.name = "Janus App"
    capability_statement_software.version = "1.0"
    capability_statement_software.releaseDate = Date(year=2021, month=5, day=1)
    capability_statement.software = capability_statement_software
    capability_statement_implementation = CapabilityStatementImplementation.construct()
    capability_statement_implementation.description = "Janus app instance"
    capability_statement_implementation.url = "http://127.0.0.1:5000/"
    capability_statement.implementation = capability_statement_implementation
    capability_statement.fhirVersion = "4.0.1"
    capability_statement.format = ["application/fhir+json"]
    capability_statement_rest = CapabilityStatementRest.construct()
    capability_statement_rest.mode = "server"
    capability_statement_rest_resources = []
    for resource_type, canonical in implemented_resource_types.items():
        capability_statement_rest_resource = CapabilityStatementRestResource.construct()
        capability_statement_rest_resource.type = resource_type
        capability_statement_rest_resource.profile = canonical
        capability_statement_rest_resource_interaction = CapabilityStatementRestResourceInteraction.construct()
        capability_statement_rest_resource_interaction.code = "operation"
        capability_statement_rest_resource.interaction = [capability_statement_rest_resource_interaction]
        capability_statement_rest_resource_operation = CapabilityStatementRestResourceOperation.parse_obj(operation_example)
        capability_statement_rest_resource_operation.name = 'transform-3to4'
        capability_statement_rest_resource_operation.definition = 'https://hpi.de/fhir/OperationDefinition/transform-3to4'
        capability_statement_rest_resource.operation = [capability_statement_rest_resource_operation]
        capability_statement_rest_resources.append(capability_statement_rest_resource)
    capability_statement_rest.resource = capability_statement_rest_resources
    capability_statement.rest = [capability_statement_rest]
    return capability_statement





