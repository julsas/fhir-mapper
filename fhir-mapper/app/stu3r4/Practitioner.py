from fhir.resources.STU3.practitioner import (Practitioner as PractitionerSTU3)
from fhir.resources.practitioner import (Practitioner as PractitionerR4)
from fhir.resources.meta import Meta
import app.stu3r4.InlineTransform

def transform_practitioner_3to4(json_data):
    practitioner_3 = PractitionerSTU3.parse_obj(json_data)
    practitioner_3 = practitioner_3.dict()
    practitioner_4 = PractitionerR4.construct()
    practitioner_4.id = practitioner_3.get('id', None)
    meta = practitioner_3.get('meta', None)
    if meta == None:
        pass
    else:
        meta_profile = meta.get('profile', None)
        if meta_profile == None:
            pass
        else:
            meta = Meta.construct()
            meta.source = meta_profile[0]
            practitioner_4.meta = meta
    practitioner_4.text = practitioner_3.get('text', None)
    contained_resources_3 = practitioner_3.get('contained', None)
    if contained_resources_3 == None:
        pass
    else:
        contained_resources_4 = []
        for contained_resource_3 in contained_resources_3:
            contained_resource_4 = app.InlineTransform.transform_inline_resource(contained_resource_3)
            contained_resources_4.append(contained_resource_4)
        practitioner_4.contained = contained_resources_4
    practitioner_4.extension = practitioner_3.get('extension', None)
    practitioner_4.modifierExtension = practitioner_3.get('modifierExtension', None)
    practitioner_4.identifier = practitioner_3.get('identifier', None)
    practitioner_4.active = practitioner_3.get('active', None)
    practitioner_4.name = practitioner_3.get('name', None)
    practitioner_4.telecom = practitioner_3.get('telecom', None)
    practitioner_4.address = practitioner_3.get('address', None)
    practitioner_4.gender = practitioner_3.get('gender', None)
    practitioner_4.birthDate = practitioner_3.get('birthDate', None)
    practitioner_4.photo = practitioner_3.get('photo', None)
    practitioner_4.qualification = practitioner_3.get('qualification', None)
    practitioner_4.communication = practitioner_3.get('communication', None)
    return practitioner_4