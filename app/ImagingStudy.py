from fhir.resources.STU3.imagingstudy import (ImagingStudy as ImagingStudySTU3)
from fhir.resources.imagingstudy import (ImagingStudy as ImagingStudyR4, ImagingStudySeries, ImagingStudySeriesInstance, ImagingStudySeriesPerformer)
from fhir.resources.meta import (Meta)
from fhir.resources.identifier import (Identifier)
from fhir.resources.codeableconcept import (CodeableConcept)
from fhir.resources.coding import (Coding)
import re

imaging_study_example = {
  "resourceType": "ImagingStudy",
  "status": "available",
  "subject": {
    "reference": "Patient/dicom"
  }
}

series_example = {
      "uid": "2.16.124.113543.6003.2588828330.45298.17418.2723805630",
      "modality": {
        "system": "http://dicom.nema.org/resources/ontology/DCM",
        "code": "CT"
      }
    }

instance_example = {
          "uid": "2.16.124.113543.6003.189642796.63084.16748.2599092903",
          "sopClass": {
            "system": "urn:ietf:rfc:3986",
            "code": "urn:oid:1.2.840.10008.5.1.4.1.1.2"
          }
        }

def transform_imaging_study_3to4(json_data):
    imaging_study_3 = ImagingStudySTU3.parse_obj(json_data)
    imaging_study_3 = imaging_study_3.dict()
    imaging_study_4 = ImagingStudyR4.parse_obj(imaging_study_example)
    imaging_study_4.id = imaging_study_3.get('id', None)
    meta = imaging_study_3.get('meta', None)
    if meta == None:
        pass
    else:
        meta_profile = meta.get('profile', None)
        if meta_profile == None:
            pass
        else:
            meta = Meta.construct()
            meta.source = meta_profile[0]
            imaging_study_4.meta = meta
    imaging_study_4.text = imaging_study_3.get('text', None)
    imaging_study_4.contained = imaging_study_3.get('contained', None)
    imaging_study_4.extension = imaging_study_3.get('extension', None)
    imaging_study_4.modifierExtension = imaging_study_3.get('modifierExtension', None)
    identifier_4 = []
    uid = imaging_study_3.get('uid', None)
    if uid == None:
        pass
    else:
        identifier = Identifier.construct()
        identifier.system = 'urn:dicom:uid'
        identifier.value = uid
        identifier_4.append(identifier)
    identifier_3 = imaging_study_3.get('identifier', None)
    if identifier_3 == None:
        pass
    else:
        for identifier in identifier_3:
            identifier_4.append(identifier)
    accession = imaging_study_3.get('accession', None)
    if accession == None:
        pass
    else:
        identifier_4.append(accession)
    if not identifier_4:
        pass
    else:
        imaging_study_4.identifier = identifier_4
    availability = imaging_study_3.get('availability', None)
    if availability == 'OFFLINE' or availability == 'UNAVAILABLE':
        imaging_study_4.status = 'registered'
    elif availability == 'ONLINE' or availability == 'NEARLINE':
        imaging_study_4.status = 'available'
    else:
        imaging_study_4.status = 'unknown'
    imaging_study_4.modality = imaging_study_3.get('modalityList', None)
    imaging_study_4.subject = imaging_study_3.get('patient', None)
    imaging_study_4.encounter = imaging_study_3.get('context', None)
    imaging_study_4.started = imaging_study_3.get('started', None)
    imaging_study_4.basedOn = imaging_study_3.get('basedOn', None)
    imaging_study_4.referrer = imaging_study_3.get('referrer', None)
    imaging_study_4.interpreter = imaging_study_3.get('interpreter', None)
    imaging_study_4.endpoint = imaging_study_3.get('endpoint', None)
    imaging_study_4.numberOfSeries = imaging_study_3.get('numberOfSeries', None)
    imaging_study_4.numberOfInstances = imaging_study_3.get('numberOfInstances', None)
    imaging_study_4.procedureReference = imaging_study_3.get('procedureReference', None)
    imaging_study_4.procedureCode = imaging_study_3.get('procedureCode', None)
    imaging_study_4.reasonCode = imaging_study_3.get('reason', None)
    imaging_study_4.description = imaging_study_3.get('description', None)
    series_3 = imaging_study_3.get('series', None)
    if series_3 == None:
        pass
    else:
        series_4 = []
        for series in series_3:
            dicom_series = ImagingStudySeries.parse_obj(series_example)
            dicom_series.uid = re.sub('^urn:oid:', '', series.get('uid'))
            dicom_series.number = series.get('number', None)
            dicom_series.modality = series.get('modality')
            dicom_series.description = series.get('description', None)
            dicom_series.numberOfInstances = series.get('numberOfInstances', None)
            dicom_series.endpoint = series.get('endpoint', None)
            dicom_series.bodySite = series.get('bodySite', None)
            dicom_series.laterality = series.get('laterality', None)
            dicom_series.started = series.get('started', None)
            performer_3 = series.get('performer', None)
            if performer_3 ==None:
                pass
            else:
                performers_4 = []
                for performer in performer_3:
                    performer_4 = ImagingStudySeriesPerformer.construct()
                    performer_function = CodeableConcept.construct()
                    performer_function_coding = Coding.construct()
                    performer_function_coding.system = 'http://terminology.hl7.org/CodeSystem/v3-ParticipationType'
                    performer_function_coding.code = 'PRF'
                    performer_function.coding = [performer_function_coding]
                    performer_4.function = performer_function
                    performer_4.actor = performer
                    performers_4.append(performer_4)
                dicom_series.performer = performers_4
            series_instance_3 = series.get('instance', None)
            if series_instance_3 == None:
                pass
            else:
                series_instances_4 = []
                for series_instance in series_instance_3:
                    series_instance_4 = ImagingStudySeriesInstance.parse_obj(instance_example)
                    series_instance_4.uid = re.sub('^urn:oid:', '', series_instance.get('uid', None))
                    sop_class = Coding.construct()
                    sop_class.system = 'urn:ietf:rfc:3986'
                    sop_class.code = series_instance.get('sopClass')
                    series_instance_4.sopClass = sop_class
                    series_instance_4.number = series_instance.get('number', None)
                    series_instance_4.title = series_instance.get('title', None)
                    series_instances_4.append(series_instance_4)
                dicom_series.instance = series_instances_4
            series_4.append(dicom_series)
        imaging_study_4.series = series_4
    return imaging_study_4