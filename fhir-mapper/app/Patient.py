from fhir.resources.STU3.patient import (Patient as PatientSTU3)
from fhir.resources.patient import (Patient as PatientR4)
from fhir.resources.meta import Meta
import app.InlineTransform

def transform_patient_3to4(json_data):
    patient_3 = PatientSTU3.parse_obj(json_data)
    patient_3 = patient_3.dict()
    patient_4 = PatientR4.construct()
    patient_4.id = patient_3.get('id', None)
    meta = patient_3.get('meta', None)
    if meta == None:
        pass
    else:
        meta_profile = meta.get('profile', None)
        if meta_profile == None:
            pass
        else:
            meta = Meta.construct()
            meta.source = meta_profile[0]
            patient_4.meta = meta
    patient_4.text = patient_3.get('text', None)
    contained_resources_3 = patient_3.get('contained', None)
    if contained_resources_3 == None:
        pass
    else:
        contained_resources_4 = []
        for contained_resource_3 in contained_resources_3:
            contained_resource_4 = app.InlineTransform.transform_inline_resource(contained_resource_3)
            contained_resources_4.append(contained_resource_4)
        patient_4.contained = contained_resources_4
    patient_4.extension = patient_3.get('extension', None)
    patient_4.modifierExtension = patient_3.get('modifierExtension', None)
    patient_4.identifier = patient_3.get('identifier', None)
    patient_4.active = patient_3.get('active', None)
    patient_4.name = patient_3.get('name', None)
    patient_4.telecom = patient_3.get('telecom', None)
    patient_4.gender = patient_3.get('gender', None)
    patient_4.birthDate = patient_3.get('birthDate', None)
    patient_4.deceasedBoolean = patient_3.get('deceasedBoolean', None)
    patient_4.deceasedDateTime = patient_3.get('deceasedDateTime', None)
    patient_4.address = patient_3.get('address', None)
    patient_4.maritalStatus = patient_3.get('maritalStatus', None)
    patient_4.multipleBirthBoolean = patient_3.get('multipleBirthBoolean', None)
    patient_4.multipleBirthInteger = patient_3.get('multipleBirthInteger', None)
    patient_4.photo = patient_3.get('photo', None)
    patient_4.contact = patient_3.get('contact', None)
    patient_4.communication = patient_3.get('communication', None)
    patient_4.generalPractitioner = patient_3.get('generalPractitioner', None)
    patient_4.managingOrganization = patient_3.get('managingOrganization', None)
    patient_4.link = patient_3.get('link', None)
    return patient_4

