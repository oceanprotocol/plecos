from json_versions import json2, json4, meta_data_links
from schema_definitions import valid_schema
import requests

from jsonschema import validate, ErrorTree, exceptions
from jsonschema.validators import Draft4Validator


# %%
# Define validator and use pre-defined schema
validator = Draft4Validator(valid_schema)


# %%
# parse urls in  and return list which contains metadata as json
def get_json_from_links(meta_list):
    list_meta_2 = []
    for i in meta_list:
        i = requests.get(i)

        if i.status_code != 200:
            continue
        elif i.status_code == 200:
            list_meta_2.append(i.json())

    print(list_meta_2)

    # for x in list_meta_2:
      # print(x)


get_json_from_links(meta_data_links)


# %%
# Return errors in a list
def validate_single_json(data):
    error_list = []
    error_path_list = []


    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
    for error in errors:

        # error = error.message
        error = error.path

        error_list.append(error)
        # error_path_list.append(error_path)

    print(error_list)
    # print(error_path_list)


# validate_json_1(json4)


# %%
# validate multiple assets within a list
def validate_multiple_json(link_list):
    list_meta_2 = []
    for i in link_list:
        i = requests.get(i)

        if i.status_code != 200:
            continue
        elif i.status_code == 200:
            list_meta_2.append(i.json())

    for x in list_meta_2:
        error_list = []
        error_path_list = []
        errors = sorted(validator.iter_errors(x), key=lambda e: e.path)
        # print(errors)
        for error in errors:
            error = error.message

            error_list.append(error)

        print(error_list)

        for error_path in errors:

            error_path = error_path.path

            error_path_list.append(error_path)

        print(error_path_list)
        print("check out https://s3.eu-central-1.amazonaws.com/trilobite/Humpback_identification/metadata.json for reference \n")


# validate_multiple_json(meta_data_links)



