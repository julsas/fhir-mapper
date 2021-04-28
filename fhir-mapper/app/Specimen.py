from fhir.resources.STU3.specimen import (Specimen as SpecimenSTU3)
from fhir.resources.specimen import (Specimen as SpecimenR4)
from fhir.resources.meta import Meta
import app.InlineTransform

def transform_specimen_3to4(json_data):
    specimen_3 = SpecimenSTU3.parse_obj(json_data)
    specimen_3 = specimen_3.dict()
    specimen_4 = SpecimenR4.construct()
    specimen_4.id = specimen_3.get('id', None)
    meta = specimen_3.get('meta', None)
    if meta == None:
        pass
    else:
        meta_profile = meta.get('profile', None)
        if meta_profile == None:
            pass
        else:
            meta = Meta.construct()
            meta.source = meta_profile[0]
            specimen_4.meta = meta
    specimen_4.text = specimen_3.get('text', None)
    contained_resources_3 = specimen_3.get('contained', None)
    if contained_resources_3 == None:
        pass
    else:
        contained_resources_4 = []
        for contained_resource_3 in contained_resources_3:
            contained_resource_4 = app.InlineTransform.transform_inline_resource(contained_resource_3)
            contained_resources_4.append(contained_resource_4)
        specimen_4.contained = contained_resources_4
    specimen_4.extension = specimen_3.get('extension', None)
    specimen_4.modifierExtension = specimen_3.get('modifierExtension', None)
    specimen_4.identifier = specimen_3.get('identifier', None)
    specimen_4.accessionIdentifier = specimen_3.get('accessionIdentifier', None)
    specimen_4.status = specimen_3.get('status', None)
    specimen_4.type = specimen_3.get('type', None)
    specimen_4.subject = specimen_3.get('subject', None)
    specimen_4.receivedTime = specimen_3.get('receivedTime', None)
    specimen_4.parent = specimen_3.get('parent', None)
    specimen_4.request = specimen_3.get('request', None)
    specimen_4.collection = specimen_3.get('collection', None)
    specimen_4.processing = specimen_3.get('processing', None)
    specimen_4.container = specimen_3.get('container', None)
    specimen_4.note = specimen_3.get('note', None)
    return specimen_4
