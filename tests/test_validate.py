from metadata_validator.json_versions import json4, json1
from metadata_validator.schema_definitions import valid_schema
from jsonschema.validators import Draft4Validator




# %%
# test links in list
def test_metadata(json_data):
    """
    Test a valid as well as invalid json metadata.
    """

    validator = Draft4Validator(valid_schema)
    print(validator)
    assert validator.is_valid(json_data)


test_metadata(json1)
test_metadata(json4)


