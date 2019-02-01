# %%
from pathlib import Path
import pkg_resources
import logging
import json
import jsonschema as jschema

# %%
# Here is the Schema file
SCHEMA_FILE = Path(pkg_resources.resource_filename('plecos', 'schemas/metadata_190131.json'))
assert SCHEMA_FILE.exists(), "Can't find schema file {}".format(SCHEMA_FILE)


# %%
def load_json(json_file_path):
    assert Path(json_file_path).exists(), "File path {} does not exist".format(json_file_path)
    with open(json_file_path) as fp:
       json_dict  = json.load(fp)
    return json_dict

def validate_against(this_json_file, schema_file):
    """
    """
    logging.info("Schema: {}".format(schema_file))
    this_json_schema_dict = load_json(schema_file)
    logging.info("Json to validate: {}".format(this_json_file))
    this_json_dict = load_json(this_json_file)
    # assert Path(schema_file).exists(), "Schema file path {} does not exist".format(schema_file)
    # with open(schema_file) as f_schema:
    #     this_json_schema_dict = json.load(f_schema)


    # assert Path(this_json_file).exists(), "Json file path {} does not exist".format(this_json_file)
    # with open(this_json_file) as f_json:
    #     this_json = json.load(f_json)

    validator = jschema.validators.Draft7Validator(this_json_schema_dict)
    validator.validate(this_json_dict)

    # logging.info("Schema: {}".format(schema_file))
    # logging.info("Json to validate: {}".format(json_file))
    # print(type(schema_file))
    # json_file_path = Path.cwd() / json_file
    # assert json_file_path.exists(), "Json file path {} does not exist".format(json_file_path)
    # schema_file_path = Path.cwd() / schema_file
    # assert schema_file_path.exists()


def validate(json_file_abs_path, schema_file=SCHEMA_FILE):
    """Wrapper around validate_against

    TODO: This function should handle default schemas for DDO and MetaData
    """
    validate_against(json_file_abs_path, schema_file)

def list_errors(json_file_abs_path, schema_file=SCHEMA_FILE):
    logging.info("Schema: {}".format(schema_file))
    this_json_schema_dict = load_json(schema_file)
    logging.info("Json to validate: {}".format(this_json_file))
    this_json_dict = load_json(this_json_file)

