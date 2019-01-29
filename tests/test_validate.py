# from metadata_validator.json_versions import json4, json1
# from metadata_validator.schema_definitions import valid_schema
from jsonschema.validators import Draft7Validator
import pytest
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import logging

# %%

def test_validator_simple():
    # A sample schema, like what we'd get from json.load()
    schema = {
        "type" : "object",
        "properties" : {
            "price" : {"type" : "number"},
            "name" : {"type" : "string"},
        },
        "required": ["price", "name"]
    }

    # If no exception is raised by validate(), the instance is valid.
    validate(instance={"name" : "Eggs", "price" : 34.99}, schema=schema)

    with pytest.raises(ValidationError) as e_info:
        validate(instance={"name" : "Eggs", "price" : "Invalid"}, schema=schema, )
    print("Raised", e_info.value.message)

    with pytest.raises(ValidationError) as e_info:
        validate(instance={"name" : "Eggs", }, schema=schema, )
        assert e_info
    print("Raised",e_info.value.message)

def test_base_metadata(schema_dict,sample_metadata_dict):
    """
    Test the valid metadata file
    """
    validator = Draft7Validator(schema_dict)
    validator.validate(sample_metadata_dict)
    # assert validator.is_valid(sample_metadata_dict)

def test_missing_name(schema_dict,sample_metadata_dict):
    # sample_metadata_dict['base'].pop('name',None)
    del sample_metadata_dict['productId']
    # validator = Draft7Validator(schema_dict)
    # assert validator.is_valid(sample_metadata_dict) == False
    # 'name' in sample_metadata_dict[]
    # validate(instance=sample_metadata_dict, schema=schema_dict)
    with pytest.raises(ValidationError) as e_info:
        validate(instance=sample_metadata_dict, schema=schema_dict)
        assert e_info

    # validator.validate(sample_metadata_dict)

