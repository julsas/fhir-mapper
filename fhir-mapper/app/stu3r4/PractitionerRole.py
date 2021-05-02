from fhir.resources.STU3.practitionerrole import (PractitionerRole as PractitionerRoleSTU3)
from fhir.resources.practitionerrole import (PractitionerRole as PractitionerRoleR4)
from fhir.resources.meta import Meta
import app.stu3r4.InlineTransform

def transform_practitioner_role_3to4(json_data):
    practitioner_role_3 = PractitionerRoleSTU3.parse_obj(json_data)
    practitioner_role_3 = practitioner_role_3.dict()
    practitioner_role_4 = PractitionerRoleR4.construct()
    practitioner_role_4.id = practitioner_role_3.get('id', None)
    meta = practitioner_role_3.get('meta', None)
    if meta == None:
        pass
    else:
        meta_profile = meta.get('profile', None)
        if meta_profile == None:
            pass
        else:
            meta = Meta.construct()
            meta.source = meta_profile[0]
            practitioner_role_4.meta = meta
    practitioner_role_4.text = practitioner_role_3.get('text', None)
    contained_resources_3 = practitioner_role_3.get('contained', None)
    if contained_resources_3 == None:
        pass
    else:
        contained_resources_4 = []
        for contained_resource_3 in contained_resources_3:
            contained_resource_4 = app.InlineTransform.transform_inline_resource(contained_resource_3)
            contained_resources_4.append(contained_resource_4)
        practitioner_role_4.contained = contained_resources_4
    practitioner_role_4.extension = practitioner_role_3.get('extension', None)
    practitioner_role_4.modifierExtension = practitioner_role_3.get('modifierExtension', None)
    practitioner_role_4.identifier = practitioner_role_3.get('identifier', None)
    practitioner_role_4.active = practitioner_role_3.get('active', None)
    practitioner_role_4.period = practitioner_role_3.get('period', None)
    practitioner_role_4.practitioner = practitioner_role_3.get('practitioner', None)
    practitioner_role_4.organization = practitioner_role_3.get('organization', None)
    practitioner_role_4.code = practitioner_role_3.get('code', None)
    practitioner_role_4.specialty = practitioner_role_3.get('speciality', None)
    practitioner_role_4.location = practitioner_role_3.get('location', None)
    practitioner_role_4.healthcareService = practitioner_role_3.get('healthcareService', None)
    practitioner_role_4.telecom = practitioner_role_3.get('telecom', None)
    practitioner_role_4.availableTime = practitioner_role_3.get('availableTime', None)
    practitioner_role_4.notAvailable = practitioner_role_3.get('notAvailable', None)
    practitioner_role_4.availabilityExceptions = practitioner_role_3.get('availabilityExceptions', None)
    practitioner_role_4.endpoint = practitioner_role_3.get('endpoint', None)
    return practitioner_role_4
