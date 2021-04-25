from fhir.resources.STU3.organization import (Organization as OrganizationSTU3)
from fhir.resources.organization import (Organization as OrganizationR4)
from fhir.resources.meta import Meta

def transform_organization_3to4(json_data):
    organization_3 = OrganizationSTU3.parse_obj(json_data)
    organization_3 = organization_3.dict()
    organization_4 = OrganizationR4.construct()
    organization_4.id = organization_3.get('id', None)
    meta = organization_3.get('meta', None)
    if meta == None:
        pass
    else:
        meta_profile = meta.get('profile', None)
        if meta_profile == None:
            pass
        else:
            meta = Meta.construct()
            meta.source = meta_profile[0]
            organization_4.meta = meta
    organization_4.text = organization_3.get('text', None)
    organization_4.contained = organization_3.get('contained', None)
    organization_4.extension = organization_3.get('extension', None)
    organization_4.modifierExtension = organization_3.get('modifierExtension', None)
    organization_4.identifier = organization_3.get('identifier', None)
    organization_4.active = organization_3.get('active', None)
    organization_4.type = organization_3.get('type', None)
    organization_4.name = organization_3.get('name', None)
    organization_4.alias = organization_3.get('alias', None)
    organization_4.telecom = organization_3.get('telecom', None)
    organization_4.address = organization_3.get('address', None)
    organization_4.partOf = organization_3.get('partOf', None)
    organization_4.contact = organization_3.get('contact', None)
    organization_4.endpoint = organization_3.get('endpoint', None)
    return organization_4