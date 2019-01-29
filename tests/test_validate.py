from metadata_validator.json_versions import json4, json1
from metadata_validator.schema_definitions import valid_schema
from jsonschema.validators import Draft4Validator

import json

import logging

# def test_load_schema():
#     pass



# %%

# def test_fixtures(test1):
#     test1()

# test links in list
def test_metadata(schema_dict,sample_metadata_dict):
    """
    Test a valid as well as invalid json metadata.
    """
    # print(schema_dict)

    validator = Draft4Validator(valid_schema)
    # try:
    #     validator.validate(sample_metadata_dict)
    # except ValidationError:
    #     print("asdfasdf;lkasjdf;laskdjf")
    assert validator.validate(sample_metadata_dict)
    # print(validator.is_valid(sample_metadata_dict))
    # assert validator.is_valid(sample_metadata_dict)


# test_metadata(json1)
# test_metadata(json4)


