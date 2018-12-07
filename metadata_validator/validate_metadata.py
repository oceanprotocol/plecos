
from json_versions import json2, json4
from query import requests, meta_data_links, get_assets


from schema_definitions import schema_1

from jsonschema import validate, ErrorTree, exceptions
from jsonschema.validators import Draft4Validator


# %%
validator = Draft4Validator(schema_1)


# %%
# parse urls and return list which contains metadata
# get_assets(meta_data_links)


# %%
# Return errors in a list
def validate_json_1(data):
    list = []

    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
    for error in errors:

        error = error.message
        # error = error.path

        list.append(error)
        # list_2.append(error_path)

    print(list)


# validate_json_1(json4)


# %%
# validate multiple assets within a list
def validate_json_2(link_list):
    list_meta_2 = []
    for i in link_list:
        i = requests.get(i)

        if i.status_code != 200:
            continue
        elif i.status_code == 200:
            list_meta_2.append(i.json())

    for x in list_meta_2:
        error_list = []
        errors = sorted(validator.iter_errors(x), key=lambda e: e.path)
        # print(errors)
        for error in errors:
            error = error.message
            # error = error.path

            error_list.append(error)
            # list_2.append(error_path)

        print(error_list)


# validate_json_2(meta_data_links)



