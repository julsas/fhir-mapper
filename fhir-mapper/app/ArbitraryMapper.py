from app.Immunization import transform_immunization_3to4
from app.ImagingStudy import transform_imaging_study_3to4
from app.DiagnosticReport import transform_diagnostic_report_3to4
from app.DeviceUseStatement import transform_device_use_statement_3to4
from app.Device import transform_device_3to4
from app.AllergyIntolerance import transform_allergy_intolerance_3to4
from app.Condition import transform_condition_3to4
from app.Media import transform_media_3to4
from app.Organization import transform_organization_3to4
from app.Patient import transform_patient_3to4
from app.Observation import transform_observation_3to4
from app.Medication import transform_medication_3to4
from app.MedicationStatement import transform_medication_statement_3to4

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
        