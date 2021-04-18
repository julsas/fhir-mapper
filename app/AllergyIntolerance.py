from fhir.resources.STU3.allergyintolerance import (AllergyIntolerance as AllergyIntoleranceSTU3)
from fhir.resources.allergyintolerance import (AllergyIntolerance as AllergyIntoleranceR4)
from fhir.resources.codeableconcept import (CodeableConcept)
from fhir.resources.coding import (Coding)
from fhir.resources.meta import Meta

def transform_allergy_intolerance_3to4(json_data):
    allergy_intolerance_3 = AllergyIntoleranceSTU3.parse_obj(json_data)
    allergy_intolerance_3 = allergy_intolerance_3.dict()
    allergy_intolerance_4 = AllergyIntoleranceR4.construct()
    allergy_intolerance_4.id = allergy_intolerance_3.get('id', None)
    meta = allergy_intolerance_3.get('meta', None)
    if meta == None:
        pass
    else:
        meta_profile = meta.get('profile', None)
        if meta_profile == None:
            pass
        else:
            meta = Meta.construct()
            meta.source = meta_profile[0]
            allergy_intolerance_4.meta = meta
    allergy_intolerance_4.text = allergy_intolerance_3.get('text', None)
    allergy_intolerance_4.contained = allergy_intolerance_3.get('contained', None)
    allergy_intolerance_4.extension = allergy_intolerance_3.get('extension', None)
    allergy_intolerance_4.modifierExtension = allergy_intolerance_3.get('modifierExtension', None)
    allergy_intolerance_4.identifier = allergy_intolerance_3.get('identifier', None)
    clinical_status_3 = allergy_intolerance_3.get('clinicalStatus', None)
    if clinical_status_3 == None:
        pass
    else:
        clinical_status = CodeableConcept.construct()
        clinical_status_coding = Coding.construct()
        clinical_status_coding.system = 'http://terminology.hl7.org/CodeSystem/allergyintolerance-clinical'
        clinical_status_coding.code = clinical_status_3
        clinical_status.coding = [clinical_status_coding]
        allergy_intolerance_4.clinicalStatus = clinical_status
    verification_status_3 = allergy_intolerance_3.get('verificationStatus', None)
    if verification_status_3 == None:
        pass
    else:
        verification_status = CodeableConcept.construct()
        verification_status_coding = Coding.construct()
        verification_status_coding.system = 'http://terminology.hl7.org/CodeSystem/allergyintolerance-verification'
        verification_status_coding.code = verification_status_3
        verification_status.coding = [verification_status_coding]
        allergy_intolerance_4.verificationStatus = verification_status
    allergy_intolerance_4.type = allergy_intolerance_3.get('type', None)
    allergy_intolerance_4.category = allergy_intolerance_3.get('category', None)
    allergy_intolerance_4.criticality = allergy_intolerance_3.get('criticality', None)
    allergy_intolerance_4.code = allergy_intolerance_3.get('code', None)
    allergy_intolerance_4.patient = allergy_intolerance_3.get('patient', None)
    allergy_intolerance_4.onsetDateTime = allergy_intolerance_3.get('onsetDateTime', None)
    allergy_intolerance_4.onsetAge = allergy_intolerance_3.get('onsetAge', None)
    allergy_intolerance_4.onsetPeriod = allergy_intolerance_3.get('onsetPeriod', None)
    allergy_intolerance_4.onsetRange = allergy_intolerance_3.get('onsetRange', None)
    allergy_intolerance_4.onsetString = allergy_intolerance_3.get('onsetString', None)
    allergy_intolerance_4.recordedDate = allergy_intolerance_3.get('assertedDate', None)
    allergy_intolerance_4.recorder = allergy_intolerance_3.get('recorder', None)
    allergy_intolerance_4.asserter = allergy_intolerance_3.get('asserter', None)
    allergy_intolerance_4.lastOccurrence = allergy_intolerance_3.get('lastOccurrence', None)
    allergy_intolerance_4.reaction = allergy_intolerance_3.get('reaction', None)
    return allergy_intolerance_4