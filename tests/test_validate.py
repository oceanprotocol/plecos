# from metadata_validator.json_versions import json4, json1
# from metadata_validator.schema_definitions import valid_schema
from jsonschema.validators import Draft7Validator
import pytest
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import json
import logging
import plecos

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
    print("Raised", e_info.value.message)


#%%
def test_local_metadata(schema_dict, sample_metadata_dict_local):
    validator = Draft7Validator(schema_dict)
    validator.validate(sample_metadata_dict_local)

def test_remote_metadata(schema_dict, sample_metadata_dict_remote):
    validator = Draft7Validator(schema_dict)
    validator.validate(sample_metadata_dict_remote)

def test_missing_attribute(schema_dict,sample_metadata_dict_local):
    del sample_metadata_dict_local['base']['price']
    with pytest.raises(ValidationError) as e_info:
        validate(instance=sample_metadata_dict_local, schema=schema_dict)
        assert e_info

def test_type_mismatch(schema_dict, sample_metadata_dict_local):
    sample_metadata_dict_local['base']['price'] = "A string is not allowed!"
    with pytest.raises(ValidationError) as e_info:
        validate(instance=sample_metadata_dict_local, schema=schema_dict)
        assert e_info
    assert e_info.value.absolute_path[0] == 'base'
    assert e_info.value.absolute_path[1] == 'price'
    assert e_info.value.validator_value == 'integer'


def test




