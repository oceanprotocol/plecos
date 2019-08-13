# from metadata_validator.json_versions import json4, json1
# from metadata_validator.schema_definitions import valid_schema
import pytest
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonschema.validators import Draft7Validator

import plecos


# %%

def test_validator_simple():
    # A sample schema, like what we'd get from json.load()
    schema = {
        "type": "object",
        "properties": {
            "price": {"type": "number"},
            "name": {"type": "string"},
        },
        "required": ["price", "name"]
    }

    # If no exception is raised by validate(), the instance is valid.
    validate(instance={"name": "Eggs", "price": 34.99}, schema=schema)

    with pytest.raises(ValidationError) as e_info:
        validate(instance={"name": "Eggs", "price": "Invalid"}, schema=schema, )
    print("Raised", e_info.value.message)

    with pytest.raises(ValidationError) as e_info:
        validate(instance={"name": "Eggs", }, schema=schema, )
        assert e_info
    print("Raised", e_info.value.message)


# %%

def test_local_metadata_passes(schema_local_dict, sample_metadata_dict_local):
    validator = Draft7Validator(schema_local_dict)
    validator.validate(sample_metadata_dict_local)


def test_remote_metadata_passes(schema_remote_dict, sample_metadata_dict_remote):
    validator = Draft7Validator(schema_remote_dict)
    validator.validate(sample_metadata_dict_remote)


def test_fail_on_additonal_base_attribute(schema_local_dict, schema_remote_dict,
                                          sample_metadata_dict_local, sample_metadata_dict_remote):
    sample_metadata_dict_local['main']['EXTRA ATTRIB!'] = 0
    with pytest.raises(ValidationError) as e_info:
        validate(instance=sample_metadata_dict_local, schema=schema_local_dict)
        assert e_info

    sample_metadata_dict_remote['main']['EXTRA ATTRIB!'] = 0
    with pytest.raises(ValidationError) as e_info:
        validate(instance=sample_metadata_dict_remote, schema=schema_remote_dict)
        assert e_info


def test_fail_on_additonal_file_attribute(schema_local_dict, schema_remote_dict,
                                          sample_metadata_dict_local, sample_metadata_dict_remote):
    sample_metadata_dict_local['main']['files'][0]['EXTRA ATTRIB!'] = 0
    with pytest.raises(ValidationError) as e_info:
        validate(instance=sample_metadata_dict_local, schema=schema_local_dict)
        assert e_info

    sample_metadata_dict_remote['main']['files'][0]['EXTRA ATTRIB!'] = 0
    with pytest.raises(ValidationError) as e_info:
        validate(instance=sample_metadata_dict_remote, schema=schema_remote_dict)
        assert e_info


def test_fail_on_missing_file_index_attribute(schema_local_dict, schema_remote_dict,
                                              sample_metadata_dict_local,
                                              sample_metadata_dict_remote):
    del sample_metadata_dict_local['main']['files'][0]['index']
    with pytest.raises(ValidationError) as e_info:
        validate(instance=sample_metadata_dict_local, schema=schema_local_dict)
        assert e_info

    del sample_metadata_dict_remote['main']['files'][0]['index']
    with pytest.raises(ValidationError) as e_info:
        validate(instance=sample_metadata_dict_remote, schema=schema_remote_dict)
        assert e_info


def test_fail_on_missing_file_url_attribute(schema_local_dict, schema_remote_dict,
                                            sample_metadata_dict_local,
                                            sample_metadata_dict_remote):
    del sample_metadata_dict_local['main']['files'][0]['url']
    with pytest.raises(ValidationError) as e_info:
        validate(instance=sample_metadata_dict_local, schema=schema_local_dict)
        assert e_info

    with pytest.raises(KeyError) as e_info:
        print(sample_metadata_dict_remote['main']['files'][0]['url'])
        assert e_info


def test_fail_on_missing_base_attribute(schema_local_dict, schema_remote_dict,
                                        sample_metadata_dict_local, sample_metadata_dict_remote):
    del sample_metadata_dict_local['main']['price']
    with pytest.raises(ValidationError) as e_info:
        validate(instance=sample_metadata_dict_local, schema=schema_local_dict)
        assert e_info

    del sample_metadata_dict_remote['main']['price']
    with pytest.raises(ValidationError) as e_info:
        validate(instance=sample_metadata_dict_remote, schema=schema_remote_dict)
        assert e_info


def test_allow_additional_information(schema_local_dict, schema_remote_dict,
                                      sample_metadata_dict_local, sample_metadata_dict_remote):
    more = {'more info': {
        "extra": "stuff",
        "item2": 2}
    }

    # delete additionalInformation, if present
    if 'additionalInformation' in sample_metadata_dict_local:
        del sample_metadata_dict_local['additionalInformation']
    validate(instance=sample_metadata_dict_local, schema=schema_local_dict)

    if 'additionalInformation' in sample_metadata_dict_remote:
        del sample_metadata_dict_remote['additionalInformation']
    validate(instance=sample_metadata_dict_remote, schema=schema_remote_dict)

    # add additional info
    sample_metadata_dict_local['additionalInformation'] = more
    validate(instance=sample_metadata_dict_local, schema=schema_local_dict)

    sample_metadata_dict_remote['additionalInformation'] = more
    validate(instance=sample_metadata_dict_remote, schema=schema_remote_dict)


def test_fail_local_missing_file_url(schema_local_dict, schema_remote_dict,
                                     sample_metadata_dict_local, sample_metadata_dict_remote):
    del sample_metadata_dict_local['main']['files'][0]['url']
    with pytest.raises(ValidationError) as e_info:
        validate(instance=sample_metadata_dict_local, schema=schema_local_dict)
        assert e_info


def test_assert_remote_without_file_url(schema_local_dict, schema_remote_dict,
                                        sample_metadata_dict_local, sample_metadata_dict_remote):
    with pytest.raises(KeyError) as e_info:
        sample_metadata_dict_remote['main']['files'][0]['url']
        assert e_info


def test_fail_on_type_mismatches(schema_local_dict, schema_remote_dict, sample_metadata_dict_local,
                                 sample_metadata_dict_remote):
    sample_metadata_dict_local['main']['price'] = "A string is not allowed!"
    with pytest.raises(ValidationError) as e_info:
        validate(instance=sample_metadata_dict_local, schema=schema_local_dict)
        assert e_info
    assert e_info.value.absolute_path[0] == 'main'
    assert e_info.value.absolute_path[1] == 'price'
    assert e_info.value.validator_value == '^[0-9]+$'

    sample_metadata_dict_remote['main']['price'] = "A string is not allowed!"
    with pytest.raises(ValidationError) as e_info:
        validate(instance=sample_metadata_dict_remote, schema=schema_remote_dict)
        assert e_info
    assert e_info.value.absolute_path[0] == 'main'
    assert e_info.value.absolute_path[1] == 'price'
    assert e_info.value.validator_value == '^[0-9]+$'


def test_validate_file(path_sample_metadata_local):
    plecos.validate_file_local(path_sample_metadata_local)


def test_validate_dict(sample_metadata_dict_local):
    plecos.validate_dict_local(sample_metadata_dict_local)


def test_is_valid_file(path_sample_metadata_local):
    assert plecos.is_valid_file_local(path_sample_metadata_local)


def test_is_valid_dict(sample_metadata_dict_local):
    assert plecos.is_valid_dict_local(sample_metadata_dict_local)


def test_list_errors_dict(sample_metadata_dict_local):
    assert len(plecos.list_errors_dict_local(sample_metadata_dict_local)) == 0

    sample_metadata_dict_local['main']['price'] = "A string is not allowed!"
    del sample_metadata_dict_local['main']['name']
    errors = plecos.list_errors_dict_local(sample_metadata_dict_local)
    # print(errors)
    for i, err in enumerate(errors):
        stack_path = list(err[1].relative_path)
        stack_path = [str(p) for p in stack_path]
        print("Error {} at {}: {}".format(i, "/".join(stack_path), err[1].message))

    assert len(errors) == 2
