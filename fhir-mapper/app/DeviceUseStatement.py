from fhir.resources.STU3.deviceusestatement import (DeviceUseStatement as DeviceUseStatementSTU3)
from fhir.resources.deviceusestatement import (DeviceUseStatement as DeviceUseStatementR4)
from fhir.resources.meta import (Meta)
import app.InlineTransform

device_use_statement = {
  "resourceType": "DeviceUseStatement",
  "status": "active",
  "subject": {
    "reference": "Patient/example"
  },
  "device": {
    "reference": "Device/example"
  }
}

def transform_device_use_statement_3to4(json_data):
    device_use_statement_3 = DeviceUseStatementSTU3.parse_obj(json_data)
    device_use_statement_3 = device_use_statement_3.dict()
    device_use_statement_4 = DeviceUseStatementR4.parse_obj(device_use_statement)
    device_use_statement_4.id = device_use_statement_3.get('id', None)
    meta = device_use_statement_3.get('meta', None)
    if meta == None:
        pass
    else:
        meta_profile = meta.get('profile', None)
        if meta_profile == None:
            pass
        else:
            meta = Meta.construct()
            meta.source = meta_profile[0]
            device_use_statement_4.meta = meta
    device_use_statement_4.text = device_use_statement_3.get('text', None)
    contained_resources_3 = device_use_statement_3.get('contained', None)
    if contained_resources_3 == None:
        pass
    else:
        contained_resources_4 = []
        for contained_resource_3 in contained_resources_3:
            contained_resource_4 = app.InlineTransform.transform_inline_resource(contained_resource_3)
            contained_resources_4.append(contained_resource_4)
        device_use_statement_4.contained = contained_resources_4
    device_use_statement_4.extension = device_use_statement_3.get('extension', None)
    device_use_statement_4.modifierExtension = device_use_statement_3.get('modifierExtension', None)
    device_use_statement_4.identifier = device_use_statement_3.get('identifier', None)
    device_use_statement_4.status = device_use_statement_3.get('status', None)
    device_use_statement_4.subject = device_use_statement_3.get('subject', None)
    device_use_statement_4.timingTiming = device_use_statement_3.get('timingTiming', None)
    device_use_statement_4.timingPeriod = device_use_statement_3.get('timingPeriod', None)
    device_use_statement_4.timingDateTime = device_use_statement_3.get('timingDateTime', None)
    device_use_statement_4.recordedOn = device_use_statement_3.get('recordedOn', None)
    device_use_statement_4.source = device_use_statement_3.get('source', None)
    device_use_statement_4.device = device_use_statement_3.get('device', None)
    device_use_statement_4.reasonCode = device_use_statement_3.get('indication', None)
    device_use_statement_4.bodySite = device_use_statement_3.get('bodySite', None)
    device_use_statement_4.note = device_use_statement_3.get('note', None)
    return device_use_statement_4