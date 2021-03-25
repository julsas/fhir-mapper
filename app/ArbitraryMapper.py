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
        


