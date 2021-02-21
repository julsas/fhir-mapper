from datetime import (date, datetime)
from fhir.resources.fhirtypes import (Date)
from fhir.resources.capabilitystatement import (CapabilityStatement, CapabilityStatementSoftware, CapabilityStatementImplementation, CapabilityStatementRest, CapabilityStatementRestResource, CapabilityStatementRestResourceInteraction)

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

implemented_resource_types = ["Medication"] 

def create_capabiliy_statement():
    capability_statement = CapabilityStatement.parse_obj(json_data)
    capability_statement.url = "https://hpi.de/fhir/metadata"
    capability_statement.name = "FHIR-conformance-statement-for-mapping-server"
    capability_statement.title = "FHIR conformance statement for mapping server"
    capability_statement.status = "active"
    capability_statement.experimental = "true"
    capability_statement.date = Date(year=2021, month=2, day=16)
    capability_statement.publisher = "Hasso Plattner Institute for Digital Health"
    capability_statement.kind = "instance"
    capability_statement_software = CapabilityStatementSoftware.construct()
    capability_statement_software.name = "FHIR Mapper"
    capability_statement_software.version = "0.9"
    capability_statement_software.releaseDate = Date(year=2021, month=2, day=16)
    capability_statement.software = capability_statement_software
    capability_statement_implementation = CapabilityStatementImplementation.construct()
    capability_statement_implementation.description = "FHIR mapper instance"
    capability_statement_implementation.url = "http://127.0.0.1:5000/"
    capability_statement.implementation = capability_statement_implementation
    capability_statement.fhirVersion = "4.0.1"
    capability_statement.format = ["application/fhir+json"]
    capability_statement_rest = CapabilityStatementRest.construct()
    capability_statement_rest.mode = "server"
    capability_statement_rest_resources = []
    for resource in implemented_resource_types:
        capability_statement_rest_resource = CapabilityStatementRestResource.construct()
        capability_statement_rest_resource.type = resource
        capability_statement_rest_resource_interaction = CapabilityStatementRestResourceInteraction.construct()
        capability_statement_rest_resource_interaction.code = "operation"
        capability_statement_rest_resource.interaction = [capability_statement_rest_resource_interaction]
        capability_statement_rest_resources.append(capability_statement_rest_resource)
    capability_statement_rest.resource = capability_statement_rest_resources
    return capability_statement





