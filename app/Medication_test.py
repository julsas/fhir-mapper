# %%
import json
from pydantic.json import pydantic_encoder
from fhir.resources.STU3.medication import (Medication as MedicationSTU3)
from fhir.resources.medication import (Medication as MedicationR4, MedicationIngredient as MedicationIngredientR4, MedicationBatch as MedicationBatchR4)

# %%
with open('./../data/Medication-stu3-2.json') as json_file:
    json_data = json.load(json_file)

print(json_data)
#%%
medication_3 = MedicationSTU3.parse_obj(json_data)
print(medication_3)

#%%
medication_3 = medication_3.dict()

for key, value in medication_3.items():
    print(key)

# %%
medication_4 = MedicationR4.construct()

medication_4.id = medication_3.get('id', None)
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

# %%
print(medication_4.json(indent=4))
# %%
