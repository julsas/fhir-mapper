from fhir.resources.STU3.medication import (Medication as MedicationSTU3)
from fhir.resources.medication import (Medication as MedicationR4, MedicationIngredient as MedicationIngredientR4, MedicationBatch as MedicationBatchR4)
from fhir.resources.meta import Meta
import app.stu3r4.InlineTransform
from app.settings import headers, terminology_server
import requests

def transform_medication_3to4(json_data, translate=False):
    medication_3 = MedicationSTU3.parse_obj(json_data)
    medication_3 = medication_3.dict()
    medication_4 = MedicationR4.construct()
    medication_4.id = medication_3.get('id', None)
    meta = medication_3.get('meta', None)
    if meta == None:
        pass
    else:
        meta_profile = meta.get('profile', None)
        if meta_profile == None:
            pass
        else:
            meta = Meta.construct()
            meta.source = meta_profile[0]
            medication_4.meta = meta
    medication_4.text = medication_3.get('text', None)
    contained_resources_3 = medication_3.get('contained', None)
    if contained_resources_3 == None:
        pass
    else:
        contained_resources_4 = []
        for contained_resource_3 in contained_resources_3:
            contained_resource_4 = app.InlineTransform.transform_inline_resource(contained_resource_3)
            contained_resources_4.append(contained_resource_4)
        medication_4.contained = contained_resources_4
    medication_4.extension = medication_3.get('extension', None)
    medication_4.modifierExtension = medication_3.get('modifierExtension', None)
    if translate:
        medication_code = medication_3.get('code', None)
        if medication_code != None:
            medication_4.code = translate_coding(code=medication_code, terminology_server=terminology_server, headers=headers)
    elif not translate:
        medication_4.code = medication_3.get('code', None)
    medication_4.status = medication_3.get('status', None)
    medication_4.manufacturer = medication_3.get('manufacturer', None)
    medication_4.form = medication_3.get('form', None)
    ingredients_3 = medication_3.get('ingredient', None)
    if ingredients_3 == None:
        pass
    else:
        ingredient_4 = MedicationIngredientR4.construct()
        ingredients_4 = []
        for ingredient in ingredients_3:
            ingredient_4.itemCodeableConcept = ingredient.get('itemCodeableConcept', None)
            ingredient_4.itemReference = ingredient.get('itemReference', None)
            ingredient_4.isActive = ingredient.get('isActive', None)
            ingredient_4.strength = ingredient.get('amount', None)
            ingredients_4.append(ingredient_4)
        medication_4.ingredient = ingredients_4
    if 'package' in medication_3.items():     
        batch_3 = medication_3.get('package', None).get('batch', None)
        if batch_3 == None:
            pass
        else:
            batch_4 = MedicationBatchR4.construct()
            for batch in batch_3:
                batch_4.expirationDate = batch.get('expirationDate', None)
                batch_4.lotNumber = batch.get('lotNumber', None)
        medication_4.batch = batch_4
    return medication_4

def translate_coding(code, terminology_server, headers):
    if 'coding' in code.keys():
        code_coding = code.get('coding', None)
        for coding in code_coding:
            if coding.get('system') == 'http://www.whocc.no/atc':
                coding_code = coding.get('code')
                response = requests.get(f'{terminology_server}/ConceptMap/$translate?url=https://hpi.de/fhir/ConceptMap/atc-snomed&code={coding_code}&system=http://www.whocc.no/atc&target=http://snomed.info/sct', headers = headers)
                operation_outcome = response.json()
                if operation_outcome.get('resourceType') != 'Parameters':
                    pass
                else:
                    for parameter in operation_outcome.get('parameter'):
                        if parameter.get('name') == 'result':
                            result = parameter.get('valueBoolean')
                            if result != True:
                                return code
                            else:
                                for parameter in operation_outcome.get('parameter'):
                                    if parameter.get('name') == 'match':
                                        parts = parameter.get('part')
                                        for part in parts:
                                            if part.get('name') == 'concept':
                                                value_coding = part.get('valueCoding')
                                                code_coding.append(value_coding)
                                                code['coding'] = code_coding
                                                return code
    else:
        return code