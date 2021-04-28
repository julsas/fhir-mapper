from fhir.resources.STU3.composition import (Composition as CompositionSTU3)
from fhir.resources.composition import (Composition as CompositionR4, CompositionAttester)
from fhir.resources.meta import Meta
import app.InlineTransform

composition_example = {
  "resourceType": "Composition",
  "status": "final",
  "type": {
    "coding": [
      {
        "system": "http://loinc.org",
        "code": "11488-4",
        "display": "Consult note"
      }
    ]
  },
  "date": "2012-01-04T09:10:14Z",
  "author": [
    {
      "reference": "Practitioner/xcda-author",
      "display": "Harold Hippocrates, MD"
    }
  ],
  "title": "Consultation Note"
}

def transform_composition_3to4(json_data):
    composition_3 = CompositionSTU3.parse_obj(json_data)
    composition_3 = composition_3.dict()
    composition_4 = CompositionR4.parse_obj(composition_example)
    composition_4.id = composition_3.get('id', None)
    meta = composition_3.get('meta', None)
    if meta == None:
        pass
    else:
        meta_profile = meta.get('profile', None)
        if meta_profile == None:
            pass
        else:
            meta = Meta.construct()
            meta.source = meta_profile[0]
            composition_4.meta = meta
    composition_4.text = composition_3.get('text', None)
    contained_resources_3 = composition_3.get('contained', None)
    if contained_resources_3 == None:
        pass
    else:
        contained_resources_4 = []
        for contained_resource_3 in contained_resources_3:
            contained_resource_4 = app.InlineTransform.transform_inline_resource(contained_resource_3)
            contained_resources_4.append(contained_resource_4)
        composition_4.contained = contained_resources_4
    composition_4.extension = composition_3.get('extension', None)
    composition_4.modifierExtension = composition_3.get('modifierExtension', None)
    composition_4.identifier = composition_3.get('identifier', None)
    composition_4.status = composition_3.get('status', None)
    composition_4.type = composition_3.get('type', None)
    class_3 = composition_3.get('class', None)
    if class_3 == None:
        pass
    else:
        composition_4.category = [class_3]
    composition_4.subject = composition_3.get('subject', None)
    composition_4.encounter = composition_3.get('encounter', None)
    composition_4.date = composition_3.get('date', None)
    composition_4.author = composition_3.get('author', None)
    composition_4.title = composition_3.get('title', None)
    composition_4.confidentiality = composition_3.get('confidentiality', None)
    attester_3 = composition_3.get('attester', None)
    if attester_3 == None:
        pass
    else:
        attesters = []
        for attester in attester_3:
            attester_4 = CompositionAttester.construct()
            mode_3 = attester.get('mode')
            attester_4.mode = mode_3[0]
            attester_4.time = attester.get('time', None)
            attester_4.party = attester.get('party', None)
            attesters.append(attester_4)
        composition_4.attester = attesters
    composition_4.custodian = composition_3.get('custodian', None)
    composition_4.relatesTo = composition_3.get('relatesTo', None)
    composition_4.event = composition_3.get('event', None)
    composition_4.section = composition_3.get('section', None)
    return composition_4


