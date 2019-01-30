#%% Development
from pathlib import Path
import json
import pytest
from jsonschema.exceptions import ValidationError
from jsonschema import validate
from pprint import pprint
#%%
import jsonschema
# Select the latest schema path here
PATH_SCHEMA_DIR = Path().cwd() / 'schemas'
PATH_LATEST_SCHEMA = PATH_SCHEMA_DIR / 'schema_v190118.json'
# PATH_LATEST_SCHEMA = PATH_SCHEMA_DIR / 'supersimple.json'
# PATH_LATEST_SCHEMA = PATH_SCHEMA_DIR / 'test.json'
# PATH_LATEST_SCHEMA = PATH_SCHEMA_DIR / 'simple.json'
assert PATH_LATEST_SCHEMA.exists()

PATH_SAMPLES_DIR = Path().cwd() / 'samples'
PATH_SAMPLE_METADATA = PATH_SAMPLES_DIR / 'metadata UK weather.json'
# PATH_SAMPLE_METADATA = PATH_SAMPLES_DIR / 'supersimple.json'
# PATH_SAMPLE_METADATA = PATH_SAMPLES_DIR / 'test.json'
# PATH_SAMPLE_METADATA = PATH_SAMPLES_DIR / 'simple.json'
assert PATH_SAMPLE_METADATA.exists()

#%%
with open(PATH_LATEST_SCHEMA) as json_file:
    schema = json.load(json_file)
print("Loaded schema:", PATH_LATEST_SCHEMA)

with open(PATH_SAMPLE_METADATA) as json_file:
    sample = json.load(json_file)
print("Loaded sample:", PATH_SAMPLE_METADATA)


#%%
# sample_metadata_dict['base'].pop('name',None)

# validator = Draft7Validator(schema_dict)
# assert validator.is_valid(sample_metadata_dict) == False
# 'name' in sample_metadata_dict[]
# validate(instance=sample_metadata_dict, schema=schema_dict)

validate(instance=sample, schema=schema)
#%%
# del sample['productId']
del sample['metadata']['base']['price']
pprint(sample)
with pytest.raises(ValidationError) as e_info:
    validate(instance=sample, schema=schema)
    assert e_info

validate(sample,schema)
