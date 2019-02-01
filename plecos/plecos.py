#%%
import jsonschema
from pathlib import Path
import pkg_resources
import logging
# DATA_PATH = pkg_resources.resource_filename('plecos', 'schemas/')
SCHEMA_FILE = Path(pkg_resources.resource_filename('plecos', 'schemas/metadata_v190118.json'))
assert SCHEMA_FILE.exists(), "Can't find schema file {}".format(SCHEMA_FILE)
import json
import jsonschema as jschema

# from jsonschema.validators import Draft7Validator
# from jsonschema import validate
# from jsonschema.exceptions import ValidationError


# Select the latest schema path here
# PATH_SCHEMA_DIR = Path().cwd() / 'plecos' / 'schemas'
# print(PATH_SCHEMA_DIR)
# PATH_LATEST_SCHEMA = PATH_SCHEMA_DIR / 'metadata_v190118.json'
# PATH_LATEST_SCHEMA = PATH_SCHEMA_DIR / 'supersimple.json'
# PATH_LATEST_SCHEMA = PATH_SCHEMA_DIR / 'test.json'
# assert PATH_LATEST_SCHEMA.exists(), "Path not found: {}".format(PATH_LATEST_SCHEMA)

# PATH_SAMPLES_DIR = Path().cwd() / 'samples'
# PATH_SAMPLE_METADATA = PATH_SAMPLES_DIR / 'metadata sample publisher.json'
# PATH_SAMPLE_METADATA = PATH_SAMPLES_DIR / 'squid_example.json'
# PATH_SAMPLE_METADATA = PATH_SAMPLES_DIR / 'supersimple.json'
# PATH_SAMPLE_METADATA = PATH_SAMPLES_DIR / 'test.json'
# assert PATH_SAMPLE_METADATA.exists(), "Path not found: {}".format(PATH_SAMPLE_METADATA)

#%%

def validate_against(schema_file, json_file):
    """Validates a json file according a schema file.
    Wraps the jsonschema project, see https://pypi.org/project/jsonschema/.

    Arguments:
        schema_file: the name of the schema file, found in ./schemas
        json_file: the relative (to current directory) path of the json file to validate against
    """
    logging.info("Schema: {}".format(schema_file))
    logging.info("Json to validate: {}".format(json_file))
    # print(type(schema_file))
    json_file_path = Path.cwd() / json_file
    assert json_file_path.exists(), "Json file path {} does not exist".format(json_file_path)
    # schema_file_path = Path.cwd() / schema_file
    # assert schema_file_path.exists()

def validate(json_file_abs_path):
    # print("asdfasdf")
    logging.info("Schema: {}".format(SCHEMA_FILE))
    logging.info("Json to validate: {}".format(json_file_abs_path))
    json_file_path = Path.cwd() / json_file_abs_path
    assert json_file_path.exists(), "Json file path {} does not exist".format(json_file_path)


    with open(SCHEMA_FILE) as json_file:
        this_json_schema_dict = json.load(json_file)

    with open(json_file_abs_path) as json_file:
        this_json = json.load(json_file)

    validator = jschema.validators.Draft7Validator(this_json_schema_dict)
    validator.validate(this_json)
