from fhir.resources.STU3.procedure import (Procedure as ProcedureSTU3)
from fhir.resources.procedure import (Procedure as ProcedureR4, ProcedurePerformer)
from fhir.resources.meta import Meta

procedure_example = {
  "resourceType": "Procedure",
  "status": "completed",
  "subject": {
    "reference": "Patient/example"
  }
}

def transform_procedure_3to4(json_data):
    procedure_3 = ProcedureSTU3.parse_obj(json_data)
    procedure_3 = procedure_3.dict()
    procedure_4 = ProcedureR4.parse_obj(procedure_example)
    procedure_4.id = procedure_3.get('id', None)
    meta = procedure_3.get('meta', None)
    if meta == None:
        pass
    else:
        meta_profile = meta.get('profile', None)
        if meta_profile == None:
            pass
        else:
            meta = Meta.construct()
            meta.source = meta_profile[0]
            procedure_4.meta = meta
    procedure_4.text = procedure_3.get('text', None)
    procedure_4.contained = procedure_3.get('contained', None)
    procedure_4.extension = procedure_3.get('extension', None)
    procedure_4.modifierExtension = procedure_3.get('modifierExtension', None)
    procedure_4.identifier = procedure_3.get('identifier', None)
    procedure_4.instantiatesCanonical = procedure_3.get('instantiatesCanonical', None)
    procedure_4.instantiatesUri = procedure_3.get('instantiatesUri', None)
    procedure_4.basedOn = procedure_3.get('basedOn', None)
    procedure_4.partOf = procedure_3.get('partOf', None)
    if 'notDone' in procedure_3.items():
        not_done = procedure_3.get('notDone')
        if not_done == True:
            procedure_4.status = 'not-done'
        else:
            pass
    else:
        procedure_4.status = procedure_3.get('status')
    procedure_4.statusReason = procedure_3.get('notDoneReason', None)
    procedure_4.category = procedure_3.get('category', None)
    procedure_4.code = procedure_3.get('code', None)
    procedure_4.subject = procedure_3.get('subject', None)
    procedure_4.encounter = procedure_3.get('context', None)
    procedure_4.performedDateTime = procedure_3.get('performedDateTime', None)
    procedure_4.performedPeriod = procedure_3.get('performedPeriod', None)
    performer_3 = procedure_3.get('performer', None)
    if performer_3 == None:
        pass
    else:
        performers = []
        for performer in performer_3:
            performer_4 = ProcedurePerformer.construct()
            performer_4.function = performer.get('role', None)
            performer_4.actor = performer.get('actor', None)
            performer_4.onBehalfOf = performer.get('onBehalfOf', None)
            performers.append(performer_4)
        procedure_4.performer = performers
    procedure_4.location = procedure_3.get('location', None)
    procedure_4.reasonCode = procedure_3.get('reasonCode', None)
    procedure_4.reasonReference = procedure_3.get('reasonReference', None)
    procedure_4.bodySite = procedure_3.get('bodySite', None)
    procedure_4.outcome = procedure_3.get('outcome', None)
    procedure_4.report = procedure_3.get('report', None)
    procedure_4.complication = procedure_3.get('complication', None)
    procedure_4.complicationDetail = procedure_3.get('complicationDetail', None)
    procedure_4.followUp = procedure_3.get('followUp', None)
    procedure_4.note = procedure_3.get('note', None)
    procedure_4.focalDevice = procedure_3.get('focalDevice', None)
    procedure_4.usedReference = procedure_3.get('usedReference', None)
    procedure_4.usedCode = procedure_3.get('usedCode', None)
    return procedure_4
