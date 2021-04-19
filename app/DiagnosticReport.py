from fhir.resources.STU3.diagnosticreport import (DiagnosticReport as DiagnosticReportSTU3)
from fhir.resources.diagnosticreport import (DiagnosticReport as DiagnosticReportR4)
from fhir.resources.meta import (Meta)

diagnostic_report = {
  "resourceType": "DiagnosticReport",
  "status": "final",
  "code": {
    "coding": [
      {
        "system": "http://snomed.info/sct",
        "code": "429858000",
        "display": "Computed tomography (CT) of head and neck"
      }
    ]
  }
}

def transform_diagnostic_report_3to4(json_data):
    diagnostic_report_3 = DiagnosticReportSTU3.parse_obj(json_data)
    diagnostic_report_3 = diagnostic_report_3.dict()
    diagnostic_report_4 = DiagnosticReportR4.parse_obj(diagnostic_report)
    diagnostic_report_4.id = diagnostic_report_3.get('id', None)
    meta = diagnostic_report_3.get('meta', None)
    if meta == None:
        pass
    else:
        meta_profile = meta.get('profile', None)
        if meta_profile == None:
            pass
        else:
            meta = Meta.construct()
            meta.source = meta_profile[0]
            diagnostic_report_4.meta = meta
    diagnostic_report_4.text = diagnostic_report_3.get('text', None)
    diagnostic_report_4.contained = diagnostic_report_3.get('contained', None)
    diagnostic_report_4.extension = diagnostic_report_3.get('extension', None)
    diagnostic_report_4.modifierExtension = diagnostic_report_3.get('modifierExtension', None)
    diagnostic_report_4.identifier = diagnostic_report_3.get('identifier', None)
    diagnostic_report_4.basedOn = diagnostic_report_3.get('basedOn', None)
    diagnostic_report_4.status = diagnostic_report_3.get('status', None)
    diagnostic_report_4.category = diagnostic_report_3.get('category', None)
    diagnostic_report_4.code = diagnostic_report_3.get('code', None)
    diagnostic_report_4.subject = diagnostic_report_3.get('subject', None)
    diagnostic_report_4.encounter = diagnostic_report_3.get('context', None)
    diagnostic_report_4.effectiveDateTime = diagnostic_report_3.get('effectiveDateTime', None)
    diagnostic_report_4.effectivePeriod = diagnostic_report_3.get('effectivePeriod', None)
    diagnostic_report_4.issued = diagnostic_report_3.get('issued', None)
    performer_3 = diagnostic_report_3.get('performer', None)
    if performer_3 == None:
        pass
    else:
        performer_4 = []
        for performer in performer_3:
            actor_3 = performer.get('actor', None)
            performer_4.append(actor_3)
            diagnostic_report_4.performer = performer_4
    diagnostic_report_4.specimen = diagnostic_report_3.get('specimen', None)
    diagnostic_report_4.result = diagnostic_report_3.get('result', None)
    diagnostic_report_4.imagingStudy = diagnostic_report_3.get('imagingStudy', None)
    diagnostic_report_4.media = diagnostic_report_3.get('image', None)
    diagnostic_report_4.conclusion = diagnostic_report_3.get('conclusion', None)
    diagnostic_report_4.conclusionCode = diagnostic_report_3.get('codedDiagnosis', None)
    diagnostic_report_4.presentedForm = diagnostic_report_3.get('presentedForm', None)
    return diagnostic_report_4