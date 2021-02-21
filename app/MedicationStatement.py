import json
from fhir.resources.STU3.medicationstatement import (MedicationStatement as MedicationStatementSTU3)
from fhir.resources.medicationstatement import (MedicationStatement as MedicationStatementR4)
from fhir.resources.dosage import (Dosage, DosageDoseAndRate)
from fhir.resources.timing import (Timing, TimingRepeat)

medication_statement = {
    "resourceType": "MedicationStatement",
    "status": "active",
    "medicationReference": {
        "reference": "Medication/example"
    },
    "subject": {
        "reference": "Patient/example"
    }
}

def transform_medication_statement_3to4(json_data):
    medication_statement_3 = MedicationStatementSTU3.parse_obj(json_data)
    medication_statement_3 = medication_statement_3.dict()
    medication_statement_4 = MedicationStatementR4.parse_obj(medication_statement)
    medication_statement_4.id = medication_statement_3.get('id', None)
    medication_statement_4.text = medication_statement_3.get('text', None)
    medication_statement_4.contained = medication_statement_3.get('contained', None)
    medication_statement_4.identifier = medication_statement_3.get('identifier', None)
    medication_statement_4.basedOn = medication_statement_3.get('basedOn', None)
    medication_statement_4.partOf = medication_statement_3.get('partOf', None)
    medication_statement_4.context = medication_statement_3.get('context', None)
    if 'taken' in medication_statement_3.items():
        if medication_statement_3.get('taken') not in ('n', 'unk'):
            if 'status' in medication_statement_3.items():
                medication_statement_4.status = medication_statement_3.get('status')
            else:
                medication_statement_4.status__ext = medication_statement_3.get('_status')
        elif medication_statement_3.get('taken') == 'n':
            medication_statement_4.status = 'not-taken'
        elif medication_statement_3.get('taken') == 'unk':
            medication_statement_4.status = 'unknown'
    medication_statement_4.category = medication_statement_3.get('category', None)
    medication_statement_4.medicationCodeableConcept = medication_statement_3.get('medicationCodeableConcept', None)
    medication_statement_4.medicationReference = medication_statement_3.get('medicationReference', None)
    medication_statement_4.effectiveDateTime = medication_statement_3.get('effectiveDateTime', None)
    medication_statement_4.effectivePeriod = medication_statement_3.get('effectivePeriod', None)
    medication_statement_4.dateAsserted = medication_statement_3.get('dateAsserted', None)
    medication_statement_4.informationSource = medication_statement_3.get('informationSource', None)
    medication_statement_4.subject = medication_statement_3.get('subject', None)
    medication_statement_4.derivedFrom = medication_statement_3.get('derivedFrom', None)
    if 'reasonNotTaken' in medication_statement_3.items():
        medication_statement_4.reasonCode = medication_statement_3.get('reasonNotTaken', None)
    elif 'reasonCode' in medication_statement_3.items():
        medication_statement_4.reasonCode = medication_statement_3.get('reasonCode', None)
    else:
        pass
    medication_statement_4.note = medication_statement_3.get('note', None)
    dosage_3 = medication_statement_3.get('dosage', None)
    if dosage_3 == None:
        pass
    else:
        dosage_4 = Dosage.construct()
        dosages = []
        for dosage in dosage_3:
            dosage_4.sequence = dosage.get('sequence', None)
            dosage_4.text = dosage.get('text', None)
            dosage_4.additionalInstruction = dosage.get('additionalInstruction', None)
            dosage_4.patientInstruction = dosage.get('patientInstruction', None)
            timing_3 = dosage.get('timing', None)
            if timing_3 == None:
                pass
            else:
                timing_4 = Timing.construct()
                timing_4.event = timing_3.get('event', None)
                timing_repeat_3 = timing_3.get('repeat', None)
                if timing_repeat_3 == None:
                    pass
                else:
                    timing_repeat_4 = TimingRepeat.construct()
                    timing_repeat_4.boundsDuration = timing_repeat_3.get('boundsDuration', None)
                    timing_repeat_4.boundsRange = timing_repeat_3.get('boundsRange', None)
                    timing_repeat_4.boundsPeriod = timing_repeat_3.get('boundsPeriod', None)
                    timing_repeat_4.count = timing_repeat_3.get('count', None)
                    timing_repeat_4.countMax = timing_repeat_3.get('countMax', None)
                    timing_repeat_4.duration = timing_repeat_3.get('duration', None)
                    timing_repeat_4.durationMax = timing_repeat_3.get('durationMax', None)
                    timing_repeat_4.durationUnit = timing_repeat_3.get('durationUnit', None)
                    timing_repeat_4.frequency = timing_repeat_3.get('frequency', None)
                    timing_repeat_4.frequencyMax = timing_repeat_3.get('frequencyMax', None)
                    timing_repeat_4.period = timing_repeat_3.get('period', None)
                    timing_repeat_4.periodMax = timing_repeat_3.get('periodMax', None)
                    timing_repeat_4.periodUnit = timing_repeat_3.get('periodUnit', None)
                    timing_repeat_4.dayOfWeek = timing_repeat_3.get('dayOfWeek', None)
                    timing_repeat_4.timeOfDay = timing_repeat_3.get('timeOfDay', None)
                    timing_repeat_4.when = timing_repeat_3.get('when', None)
                    timing_repeat_4.offset = timing_repeat_3.get('offset', None)
                    timing_4.repeat = timing_repeat_4
                timing_4.code = timing_3.get('code', None)
                dosage_4.timing = timing_4
            dosage_4.asNeededBoolean = dosage.get('asNeededBoolean', None)
            dosage_4.asNeededCodeableConcept = dosage.get('asNeededCodeableConcept', None)
            dosage_4.site = dosage.get('site', None)
            dosage_4.route = dosage.get('route', None)
            dosage_4.method = dosage.get('method', None)
            doseRange = dosage.get('doseRange', None)
            doseQuantity = dosage.get('doseQuantity', None)
            rateRatio = dosage.get('rateRatio', None)
            rateRange = dosage.get('rateRange', None)
            rateQuantity = dosage.get('rateQuantity', None)
            if (doseRange == None and doseQuantity == None and rateRatio == None and rateRange == None and rateQuantity == None):
                pass
            else:
                doseAndRate = DosageDoseAndRate.construct()
                doseAndRate.doseRange = doseRange
                doseAndRate.doseQuantity = doseQuantity
                doseAndRate.rateRatio = rateRatio
                doseAndRate.rateRange = rateRange
                doseAndRate.rateQuantity = rateQuantity
                dosage_4.doseAndRate = [doseAndRate]
            dosage_4.maxDosePerPeriod = dosage.get('maxDosePerPeriod', None)
            dosage_4.maxDosePerAdministration = dosage.get('maxDosePerAdministration', None)
            dosage_4.maxDosePerLifetime = dosage.get('maxDosePerLifetime', None)
            dosages.append(dosage_4)
        medication_statement_4.dosage = dosages
    return medication_statement_4