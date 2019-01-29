from metadata_validator.json_versions import json4, json1
# from metadata_validator.schema_definitions import valid_schema
from jsonschema.validators import Draft7Validator

import json

import logging

# def test_load_schema():
#     pass



# %%

# def test_fixtures(test1):
#     test1()

# test links in list
def test_base_metadata(schema_dict,sample_metadata_dict):
    """
    Test the valid metadata file
    """
    validator = Draft7Validator(schema_dict)
    assert validator.is_valid(schema_dict)

def test_missing_name(schema_dict,sample_metadata_dict):
    # schema_dict[''].pop('name',None)
    validator = Draft7Validator(schema_dict)
    assert validator



