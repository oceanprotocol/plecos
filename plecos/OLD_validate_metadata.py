raise

# from json_versions import json1, json2, json4, meta_data_links
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


# get_json_from_links(meta_data_links)


# %%
# Return errors in a list
def validate_single_json(single_json):
    error_list = []
    error_path_list = []

    if validator.is_valid(single_json):
        print("is valid")

    else:
        errors = sorted(validator.iter_errors(single_json), key=lambda e: e.path)
        for error in errors:

            error = error.message
            error_list.append(error)

        print(error_list)
        # print(error_path_list)

        # this returns the error paths in a list
        for error_path in errors:
            error_path = error_path.path

            error_path_list.append(error_path)

        print(error_path_list)


# validate_single_json(json2)


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

        if validator.is_valid(x):
            print(" is valid \n ")

        else:
            error_list = []
            error_path_list = []
            errors = sorted(validator.iter_errors(x), key=lambda e: e.path)

            # this returns all validation errors in a list
            for error in errors:
                error = error.message

                error_list.append(error)

            print(error_list)

            # this returns the error paths in a list
            for error_path in errors:

                error_path = error_path.path

                error_path_list.append(error_path)

            print("{} \n".format(error_path_list))

            # TODO: if valid return true


# validate_multiple_json(meta_data_links)



