from fhir.resources.STU3.device import (Device as DeviceSTU3)
from fhir.resources.device import (Device as DeviceR4, DeviceUdiCarrier, DeviceDeviceName, DeviceVersion)
from fhir.resources.meta import (Meta)
import app.InlineTransform

device_name_4 = [
        {
            "name": "name",
            "type": "udi-label-name"
        }
    ]

def transform_device_3to4(json_data):
    device_3 = DeviceSTU3.parse_obj(json_data)
    device_3 = device_3.dict()
    device_4 = DeviceR4.construct()
    device_4.id = device_3.get('id', None)
    meta = device_3.get('meta', None)
    if meta == None:
        pass
    else:
        meta_profile = meta.get('profile', None)
        if meta_profile == None:
            pass
        else:
            meta = Meta.construct()
            meta.source = meta_profile[0]
            device_4.meta = meta
    device_4.text = device_3.get('text', None)
    contained_resources_3 = device_3.get('contained', None)
    if contained_resources_3 == None:
        pass
    else:
        contained_resources_4 = []
        for contained_resource_3 in contained_resources_3:
            contained_resource_4 = app.InlineTransform.transform_inline_resource(contained_resource_3)
            contained_resources_4.append(contained_resource_4)
        device_4.contained = contained_resources_4
    device_4.extension = device_3.get('extension', None)
    device_4.modifierExtension = device_3.get('modifierExtension', None)
    device_4.identifier = device_3.get('identifier', None)
    udi = device_3.get('udi', None)
    if udi == None:
        pass
    else:
        udi_carrier = DeviceUdiCarrier.construct()
        udi_carrier.deviceIdentifier = udi.get('deviceIdentifier', None)
        name = udi.get('name', None)
        if name == None:
            pass
        else:
            device_name = DeviceDeviceName.parse_obj(device_name_4[0])
            device_name.name = name
            device_name.type = 'udi-label-name'
            device_4.deviceName = [device_name]
        udi_carrier.jurisdiction = udi.get('jurisdiction', None)
        udi_carrier.carrierHRF = udi.get('carrierHRF', None)
        udi_carrier.carrierAIDC = udi.get('carrierAIDC', None)
        udi_carrier.issuer = udi.get('issuer', None)
        udi_carrier.entryType = udi.get('entryType', None)
        device_4.udiCarrier = [udi_carrier]
    device_4.status = device_3.get('status', None)
    device_4.type = device_3.get('type', None)
    device_4.lotNumber = device_3.get('lotNumber', None)
    device_4.manufacturer = device_3.get('manufacturer', None)
    device_4.manufactureDate = device_3.get('manufacturedDate', None)
    device_4.expirationDate = device_3.get('expirationDate', None)
    device_4.modelNumber = device_3.get('model', None)
    version = device_3.get('version', None)
    if version == None:
        pass
    else:
        device_version = DeviceVersion.construct()
        device_version.value = version
        device_4.version = device_version
    device_4.patient = device_3.get('patient', None)
    device_4.owner = device_3.get('owner', None)
    device_4.contact = device_3.get('contact', None)
    device_4.location = device_3.get('location', None)
    device_4.url = device_3.get('url', None)
    device_4.note = device_3.get('note', None)
    device_4.safety = device_3.get('safety', None)
    return device_4