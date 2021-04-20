from fhir.resources.STU3.immunization import (Immunization as ImmunizationSTU3)
from fhir.resources.immunization import (Immunization as ImmunizationR4, ImmunizationPerformer, ImmunizationProtocolApplied)
from fhir.resources.meta import (Meta)
from fhir.resources.extension import (Extension)

immunization_example = {
  "resourceType": "Immunization",
  "status": "completed",
  "vaccineCode": {
    "coding": [
      {
        "system": "urn:oid:1.2.36.1.2001.1005.17",
        "code": "FLUVAX"
      }
    ],
    "text": "Fluvax (Influenza)"
  },
  "patient": {
    "reference": "Patient/example"
  },
  "occurrenceDateTime": "2013-01-10"
}

def transform_immunization_3to4(json_data):
    immunization_3 = ImmunizationSTU3.parse_obj(json_data)
    immunization_3 = immunization_3.dict()
    immunization_4 = ImmunizationR4.parse_obj(immunization_example)
    immunization_4.id = immunization_3.get('id', None)
    meta = immunization_3.get('meta', None)
    if meta == None:
        pass
    else:
        meta_profile = meta.get('profile', None)
        if meta_profile == None:
            pass
        else:
            meta = Meta.construct()
            meta.source = meta_profile[0]
            immunization_4.meta = meta
    immunization_4.text = immunization_3.get('text', None)
    immunization_4.contained = immunization_3.get('contained', None)
    immunization_4.extension = immunization_3.get('extension', None)
    immunization_4.modifierExtension = immunization_3.get('modifierExtension', None)
    immunization_4.identifier = immunization_3.get('identifier', None)
    immunization_4.status = immunization_3.get('status', None)
    not_given = immunization_3.get('notGiven', None)
    if not_given == 'false':
        pass
    else:
        immunization_4.status = 'not-done'
    immunization_4.vaccineCode = immunization_3.get('vaccineCode', None)
    immunization_4.patient = immunization_3.get('patient', None)
    immunization_4.encounter = immunization_3.get('encounter', None)
    immunization_4.occurrenceDateTime = immunization_3.get('date', None)
    immunization_4.primarySource = immunization_3.get('primarySource', None)
    immunization_4.reportOrigin = immunization_3.get('reportOrigin', None)
    immunization_4.location = immunization_3.get('location', None)
    immunization_4.manufacturer = immunization_3.get('manufacturer', None)
    immunization_4.lotNumber = immunization_3.get('lotNumber', None)
    immunization_4.expirationDate = immunization_3.get('expirationDate', None)
    immunization_4.site = immunization_3.get('site', None)
    immunization_4.route = immunization_3.get('route', None)
    immunization_4.doseQuantity = immunization_3.get('doseQuantity', None)
    practitioners_3 = immunization_3.get('practitioner', None)
    if practitioners_3 == None:
        pass
    else:
        performers = []
        for practitioner in practitioners_3:
            performer = ImmunizationPerformer.construct()
            performer.function = practitioner.get('role', None)
            performer.actor = practitioner.get('actor', None)
            performers.append(performer)
        immunization_4.performer = performers
    immunization_4.note = immunization_3.get('note', None)
    explanation = immunization_3.get('explanation', None)
    if explanation == None:
        pass
    else:
        reason_codes = []
        reasons = explanation.get('reason', None)
        if reasons == None:
            pass
        else:
            for reason in reasons:
                reason_codes.append(reason)
        reasons_not_given = explanation.get('reasonNotGiven', None)
        if reasons_not_given == None:
            pass
        else:
            for reason_not_given in reasons_not_given:
                reason_codes.append(reason_not_given)
        immunization_4.reasonCode = reason_codes
    immunization_4.reaction = immunization_3.get('reaction', None)
    vaccination_protocol = immunization_3.get('vaccinationProtocol', None)
    if vaccination_protocol == None:
        pass
    else:
        protocols_applied = []
        for protocol in vaccination_protocol:
            protocol_applied = ImmunizationProtocolApplied.construct()
            protocol_applied.series = protocol.get('series', None)
            protocol_applied.authority = protocol.get('authority', None)
            protocol_applied.targetDisease = protocol.get('targetDisease', None)
            dose_sequence = protocol.get('doseSequence', None)
            if dose_sequence == None:
                data_absent_reason = Extension.construct()
                data_absent_reason.url = 'http://hl7.org/fhir/StructureDefinition/data-absent-reason'
                data_absent_reason.valueCode = 'unknown'
                protocol_applied.doseNumberPositiveInt__ext = data_absent_reason
            else:
                protocol_applied.doseNumberPositiveInt = dose_sequence
            protocol_applied.seriesDosesPositiveInt = protocol.get('seriesDoses', None)
        protocols_applied.append(protocol_applied)
    return immunization_4