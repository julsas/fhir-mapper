from app.stu3r4.Bundle import transform_bundle_3to4
from app.stu3r4.Composition import transform_composition_3to4
from app.stu3r4.Immunization import transform_immunization_3to4
from app.stu3r4.ImagingStudy import transform_imaging_study_3to4
from app.stu3r4.DiagnosticReport import transform_diagnostic_report_3to4
from app.stu3r4.DeviceUseStatement import transform_device_use_statement_3to4
from app.stu3r4.Device import transform_device_3to4
from app.stu3r4.AllergyIntolerance import transform_allergy_intolerance_3to4
from app.stu3r4.Condition import transform_condition_3to4
from app.stu3r4.Media import transform_media_3to4
from app.stu3r4.OperationOutcome import resource_type_not_supported
from app.stu3r4.Organization import transform_organization_3to4
from app.stu3r4.Patient import transform_patient_3to4
from app.stu3r4.Observation import transform_observation_3to4
from app.stu3r4.Medication import transform_medication_3to4
from app.stu3r4.MedicationStatement import transform_medication_statement_3to4
from app.stu3r4.Practitioner import transform_practitioner_3to4
from app.stu3r4.PractitionerRole import transform_practitioner_role_3to4
from app.stu3r4.Procedure import transform_procedure_3to4
from app.stu3r4.Specimen import transform_specimen_3to4

def transform_arbitrary_resource(json_data):
    if json_data['resourceType'] == 'Medication':
        transformed_resource = transform_medication_3to4(json_data)
        return transformed_resource.json()
    
    elif json_data['resourceType'] == 'MedicationStatement':
        transformed_resource = transform_medication_statement_3to4(json_data)
        return transformed_resource.json()

    elif json_data['resourceType'] == 'Observation':
        transformed_resource = transform_observation_3to4(json_data)
        return transformed_resource.json()

    elif json_data['resourceType'] == 'Patient':
        transformed_resource = transform_patient_3to4(json_data)
        return transformed_resource.json()

    elif json_data['resourceType'] == 'Condition':
        transformed_resource = transform_condition_3to4(json_data)
        return transformed_resource.json()

    elif json_data['resourceType'] == 'AllergyIntolerance':
        transformed_resource = transform_allergy_intolerance_3to4(json_data)
        return transformed_resource.json()

    elif json_data['resourceType'] == 'Device':
        transformed_resource = transform_device_3to4(json_data)
        return transformed_resource.json()

    elif json_data['resourceType'] == 'DeviceUseStatement':
        transformed_resource = transform_device_use_statement_3to4(json_data)
        return transformed_resource.json()

    elif json_data['resourceType'] == 'DiagnosticReport':
        transformed_resource = transform_diagnostic_report_3to4(json_data)
        return transformed_resource.json()

    elif json_data['resourceType'] == 'ImagingStudy':
        transformed_resource = transform_imaging_study_3to4(json_data)
        return transformed_resource.json()

    elif json_data['resourceType'] == 'Immunization':
        transformed_resource = transform_immunization_3to4(json_data)
        return transformed_resource.json()

    elif json_data['resourceType'] == 'Media':
        transformed_resource = transform_media_3to4(json_data)
        return transformed_resource.json()

    elif json_data['resourceType'] == 'Organization':
        transformed_resource = transform_organization_3to4(json_data)
        return transformed_resource.json()

    elif json_data['resourceType'] == 'PractitionerRole':
        transformed_resource = transform_practitioner_role_3to4(json_data)
        return transformed_resource.json()

    elif json_data['resourceType'] == 'Composition':
        transformed_resource = transform_composition_3to4(json_data)
        return transformed_resource.json()

    elif json_data['resourceType'] == 'Practitioner':
        transformed_resource = transform_practitioner_3to4(json_data)
        return transformed_resource.json()

    elif json_data['resourceType'] == 'Procedure':
        transformed_resource = transform_procedure_3to4(json_data)
        return transformed_resource.json()

    elif json_data['resourceType'] == 'Specimen':
        transformed_resource = transform_specimen_3to4(json_data)
        return transformed_resource.json()

    elif json_data['resourceType'] == 'Bundle':
        transformed_resource = transform_bundle_3to4(json_data)
        return transformed_resource.json()

    else:
        operation_outcome = resource_type_not_supported()
        return operation_outcome.json()
        