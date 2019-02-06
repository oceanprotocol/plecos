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
def load_serial_data_file_path(file_path):
    file_path_obj = Path(file_path)
    assert Path(file_path_obj).exists(), "File path {} does not exist".format(file_path)

    assert file_path_obj.is_file()
    # file_name = file_path_obj.name

    if file_path_obj.suffix == '.json':
        with open(file_path_obj) as fp:
           json_dict  = json.load(fp)
        return json_dict
    if file_path_obj.suffix in ['.yaml', '.yml']:
        with open(file_path_obj) as fp:
            json_dict = json.load(fp)
        return json_dict

def validate_against(this_json_file, schema_file):
    """
    """
    logging.info("Schema: {}".format(schema_file))
    this_json_schema_dict = load_serial_data_file_path(schema_file)
    logging.info("Json to validate: {}".format(this_json_file))
    this_json_dict = load_serial_data_file_path(this_json_file)
    # assert Path(schema_file).exists(), "Schema file path {} does not exist".format(schema_file)
    # with open(schema_file) as f_schema:
    #     this_json_schema_dict = json.load(f_schema)


    # assert Path(this_json_file).exists(), "Json file path {} does not exist".format(this_json_file)
    # with open(this_json_file) as f_json:
    #     this_json = json.load(f_json)

    validator = jschema.validators.Draft7Validator(this_json_schema_dict)
    return validator.validate(this_json_dict)

    # logging.info("Schema: {}".format(schema_file))
    # logging.info("Json to validate: {}".format(json_file))
    # print(type(schema_file))
    # json_file_path = Path.cwd() / json_file
    # assert json_file_path.exists(), "Json file path {} does not exist".format(json_file_path)
    # schema_file_path = Path.cwd() / schema_file
    # assert schema_file_path.exists()

def is_valid(json_file_abs_path, schema_file=SCHEMA_FILE):
    logging.info("Schema: {}".format(schema_file))
    this_json_schema_dict = load_serial_data_file_path(schema_file)
    logging.info("Json to validate: {}".format(json_file_abs_path))
    this_json_dict = load_serial_data_file_path(json_file_abs_path)

    validator = jschema.validators.Draft7Validator(this_json_schema_dict)
    # validator = jschema.validators.Draft7Validator(this_json_schema_dict)
    return validator.is_valid(this_json_dict)


def validate(json_file_abs_path, schema_file=SCHEMA_FILE):
    """ Wrapper around validate_against

    TODO: This function should handle default schemas for DDO and MetaData

    :param json_file_abs_path:
    :param schema_file:
    :return:
    """
    return validate_against(json_file_abs_path, schema_file)

def list_errors(json_file_abs_path, schema_file=SCHEMA_FILE):
    """ Iterate over the validation errors, print to log.warn

    :param json_file_abs_path:
    :param schema_file:
    :return:
    """
    logging.info("Schema: {}".format(schema_file))
    this_json_schema_dict = load_serial_data_file_path(schema_file)
    logging.info("Json to validate: {}".format(json_file_abs_path))
    this_json_dict = load_serial_data_file_path(json_file_abs_path)

    validator = jschema.Draft4Validator(this_json_schema_dict)
    logging.info("Instantiated validator {}".format(validator))

    errors = sorted(validator.iter_errors(this_json_dict), key=lambda e: e.path)
    for i,err in enumerate(errors):
        stack_path = list(err.relative_path)
        stack_path = [str(p) for p in stack_path]
        logging.warning("Error {} at {}".format(i,"/".join(stack_path)))
        logging.warning("\t" + err.message)

