from fhir.resources.STU3.observation import (Observation as ObservationSTU3)
from fhir.resources.observation import (Observation as ObservationR4)
from fhir.resources.meta import Meta
from fhir.resources.annotation import Annotation
import app.InlineTransform

observation = {
    "resourceType": "Observation",
    "status": "final",
    "code": {
        "coding": [
            {
            "system": "example",
            "code": "example"
            }
        ]
    }
}

def transform_observation_3to4(json_data):
    observation_3 = ObservationSTU3.parse_obj(json_data)
    observation_3 = observation_3.dict()
    observation_4 = ObservationR4.parse_obj(observation)
    observation_4.id = observation_3.get('id', None)
    meta = observation_3.get('meta', None)
    if meta == None:
        pass
    else:
        meta_profile = meta.get('profile', None)
        if meta_profile == None:
            pass
        else:
            meta = Meta.construct()
            meta.source = meta_profile[0]
            observation_4.meta = meta
    observation_4.text = observation_3.get('text', None)
    contained_resources_3 = observation_3.get('contained', None)
    if contained_resources_3 == None:
        pass
    else:
        contained_resources_4 = []
        for contained_resource_3 in contained_resources_3:
            contained_resource_4 = app.InlineTransform.transform_inline_resource(contained_resource_3)
            contained_resources_4.append(contained_resource_4)
        observation_4.contained = contained_resources_4
    observation_4.extension = observation_3.get('extension', None)
    observation_4.modifierExtension = observation_3.get('modifierExtension', None)
    observation_4.identifier = observation_3.get('identifier', None)
    observation_4.basedOn = observation_3.get('basedOn', None)
    observation_4.status = observation_3.get('status', None)
    observation_4.category = observation_3.get('category', None)
    observation_4.code = observation_3.get('code', None)
    observation_4.subject = observation_3.get('subject', None)
    observation_4.encounter = observation_3.get('context', None)
    observation_4.effectiveDateTime = observation_3.get('effectiveDateTime', None)
    observation_4.effectivePeriod = observation_3.get('effectivePeriod', None)
    observation_4.issued = observation_3.get('issued', None)
    observation_4.performer = observation_3.get('performer', None)
    observation_4.valueQuantity = observation_3.get('valueQuantity', None)
    observation_4.valueCodeableConcept = observation_3.get('valueCodeableConcept', None)
    observation_4.valueString = observation_3.get('valueString', None)
    observation_4.valueBoolean = observation_3.get('valueBoolean', None)
    observation_4.valueRange = observation_3.get('valueRange', None)
    observation_4.valueRatio = observation_3.get('valueRatio', None)
    observation_4.valueSampledData = observation_3.get('valueSampledData', None)
    observation_4.valueTime = observation_3.get('valueTime', None)
    observation_4.valueDateTime = observation_3.get('valueDateTime', None)
    observation_4.valuePeriod = observation_3.get('valuePeriod', None)
    observation_4.dataAbsentReason = observation_3.get('dataAbsentReason', None)
    interpretation = observation_3.get('interpretation', None)
    if interpretation == None:
        pass
    else:
        observation_4.interpretation = [interpretation]
    comment = observation_3.get('comment', None)
    if comment == None:
        pass
    else:
        note = Annotation.construct()
        note.text = comment
        observation_4.note = [note]
    observation_4.bodySite = observation_3.get('bodySite', None)
    observation_4.method = observation_3.get('method', None)
    observation_4.specimen = observation_3.get('specimen', None)
    observation_4.device = observation_3.get('device', None)
    observation_4.referenceRange = observation_3.get('referenceRange', None)
    related_resources = observation_3.get('related', None)
    if related_resources == None:
        pass
    else:
        members = []
        derived = []
        for related_resource in related_resources:
            if related_resource.get('type') == 'has-member':
                target = related_resource.get('target')
                members.append(target)
            elif related_resource.get('type') == 'derived-from':
                target = related_resource.get('target')
                derived.append(target)
        if not members:
            pass
        else:
            observation_4.hasMember = members
        if not derived:
            pass
        else:
            observation_4.derivedFrom = derived
    observation_4.component = observation_3.get('component', None)
    return observation_4

