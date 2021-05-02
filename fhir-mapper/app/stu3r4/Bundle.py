from fhir.resources.STU3.bundle import (Bundle as BundleSTU3)
from fhir.resources.bundle import (Bundle as BundleR4, BundleEntry)
from fhir.resources.meta import Meta
from fhir.resources.extension import (Extension)
from fhir.resources.fhirprimitiveextension import (FHIRPrimitiveExtension)
from app.stu3r4.InlineTransform import transform_inline_resource
import datetime

dateTime = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()
dateTime = str(dateTime)

bundle_example = {
  "resourceType": "Bundle",
  "type": "transaction"
}

def transform_bundle_3to4(json_data):
    bundle_3 = BundleSTU3.parse_obj(json_data)
    bundle_3 = bundle_3.dict()
    bundle_4 = BundleR4.parse_obj(bundle_example)
    bundle_4.id = bundle_3.get('id', None)
    meta = bundle_3.get('meta', None)
    if meta == None:
        pass
    else:
        meta_profile = meta.get('profile', None)
        if meta_profile == None:
            pass
        else:
            meta = Meta.construct()
            meta.source = meta_profile[0]
            bundle_4.meta = meta
    bundle_4.identifier = bundle_3.get('identifier', None)
    bundle_type = bundle_3.get('type', None)
    bundle_4.type = bundle_type
    if bundle_type == 'document':
        bundle_4.timestamp = dateTime
    else:
        data_absent_reason = Extension.construct()
        data_absent_reason.url = 'http://hl7.org/fhir/StructureDefinition/data-absent-reason'
        data_absent_reason.valueCode = 'unknown'
        data_absent_reason_ex = FHIRPrimitiveExtension.construct()
        data_absent_reason_ex.extension = [data_absent_reason]
        bundle_4.timestamp__ext = data_absent_reason_ex
    bundle_4.total = bundle_3.get('total', None)
    bundle_4.link = bundle_3.get('link', None)
    entries_3 = bundle_3.get('entry', None)
    if entries_3 == None:
        pass
    else:
        entries_4 = []
        for entry in entries_3:
            entry_4 = BundleEntry.construct()
            entry_4.link = entry.get('link', None)
            entry_4.fullUrl = entry.get('fullUrl', None)
            resource_3 = entry.get('resource', None)
            if resource_3 == None:
                pass
            else:
                resource_4 = transform_inline_resource(resource_3)
                entry_4.resource = resource_4
            entry_4.search = entry.get('search', None)
            entry_4.request = entry.get('request', None)
            entry_4.response = entry.get('response', None)
            entries_4.append(entry_4)
        bundle_4.entry = entries_4
    bundle_4.signature = bundle_3.get('signature', None)
    return bundle_4
