from fhir.resources.STU3.condition import (Condition as ConditionSTU3)
from fhir.resources.condition import (Condition as ConditionR4)
from fhir.resources.codeableconcept import (CodeableConcept)
from fhir.resources.coding import (Coding)
from fhir.resources.meta import Meta

def transform_condition_3to4(json_data):
    condition_3 = ConditionSTU3.parse_obj(json_data)
    condition_3 = condition_3.dict()
    condition_4 = ConditionR4.construct()
    condition_4.id = condition_3.get('id', None)
    meta = condition_3.get('meta', None)
    if meta == None:
        pass
    else:
        meta_profile = meta.get('profile', None)
        if meta_profile == None:
            pass
        else:
            meta = Meta.construct()
            meta.source = meta_profile[0]
            condition_4.meta = meta
    condition_4.text = condition_3.get('text', None)
    condition_4.contained = condition_3.get('contained', None)
    condition_4.extension = condition_3.get('extension', None)
    condition_4.modifierExtension = condition_3.get('modifierExtension', None)
    condition_4.identifier = condition_3.get('identifier', None)
    clinical_status_3 = condition_3.get('clinicalStatus', None)
    if clinical_status_3 == None:
        pass
    else:
        clinical_status = CodeableConcept.construct()
        clinical_status_coding = Coding.construct()
        clinical_status_coding.system = 'http://terminology.hl7.org/CodeSystem/condition-clinical'
        clinical_status_coding.code = clinical_status_3
        clinical_status.coding = [clinical_status_coding]
        condition_4.clinicalStatus = clinical_status
    verification_status_3 = condition_3.get('verificationStatus', None)
    if verification_status_3 == None:
        pass
    else:
        verification_status = CodeableConcept.construct()
        verification_status_coding = Coding.construct()
        verification_status_coding.system = 'http://terminology.hl7.org/CodeSystem/condition-ver-status'
        verification_status_coding.code = verification_status_3
        verification_status.coding = [verification_status_coding]
        condition_4.verificationStatus = verification_status
    condition_4.category = condition_3.get('category', None)
    condition_4.severity = condition_3.get('severity', None)
    condition_4.code = condition_3.get('code', None)
    condition_4.bodySite = condition_3.get('bodySite', None)
    condition_4.subject = condition_3.get('subject', None)
    condition_4.encounter = condition_3.get('context', None)
    condition_4.onsetDateTime = condition_3.get('onsetDateTime', None)
    condition_4.onsetAge = condition_3.get('onsetAge', None)
    condition_4.onsetPeriod = condition_3.get('onsetPeriod', None)
    condition_4.onsetRange = condition_3.get('onsetRange', None)
    condition_4.onsetString = condition_3.get('onsetString', None)
    condition_4.abatementDateTime = condition_3.get('abatementDateTime', None)
    condition_4.abatementAge = condition_3.get('abatementAge', None)
    condition_4.abatementPeriod = condition_3.get('abatementPeriod', None)
    condition_4.abatementRange = condition_3.get('abatementRange', None)
    condition_4.abatementString = condition_3.get('abatementString', None)
    condition_4.recordedDate = condition_3.get('assertedDate', None)
    condition_4.asserter = condition_3.get('asserter', None)
    stage_3 = condition_3.get('stage', None)
    if stage_3 == None:
        pass
    else:
        condition_4.stage = [stage_3]
    condition_4.evidence = condition_3.get('evidence', None)
    condition_4.note = condition_3.get('note', None)
    return condition_4

