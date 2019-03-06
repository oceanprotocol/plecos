from pathlib import Path
import plecos
import json
print(plecos.__version__)
#%%
path_to_json_local = Path("~/ocn/Plecos/plecos/samples/metadata_local.json").expanduser()
path_to_json_remote = Path("~/ocn/Plecos/plecos/samples/metadata_remote.json").expanduser()
path_to_broken_json = Path("~/ocn/Plecos/plecos/samples/metadata_local_broken.json").expanduser()
path_to_schema_local = Path("~/ocn/Plecos/plecos/schemas/metadata_local_190305.json").expanduser()
path_to_schema_remote = Path("~/ocn/Plecos/plecos/schemas/metadata_remote_190305.json").expanduser()

# Select remote or local metadata
LOCAL=True
# LOCAL=False

if LOCAL:
    path_json_file = path_to_json_local
    path_schema_file = path_to_schema_local

    with open(path_to_json_local) as f:
        json_dict = json.load(f)

else:
    path_json_file = path_to_json_remote
    path_schema_file = path_to_json_remote

    with open(path_to_json_remote) as f:
        json_dict = json.load(f)

print("Json file:", path_json_file)
print("Schema file:", path_schema_file)
#%%
result = plecos.validate_file(path_json_file, path_schema_file)

# Validation should return None if everything is valid
assert not result
# print(result)

# Alternatively, you can return True/False with the .is_valid function
result = plecos.is_valid_file(path_json_file, path_schema_file)
assert result

# If you load an invalid json, the validator will return an error
# result = plecos.validate(path_to_broken_json)

# Or return a False boolean using is_valid
result = plecos.plecos.is_valid_file(path_to_broken_json, path_schema_file)
assert not result

# # A summary of errors can be listed with .list_errors()
# errors = plecos.list_errors(path_to_broken_json, path_schema_file)

with open(path_to_json_local) as f:
    json_dict = json.load(f)

json_dict['base']['EXTRA ATTRIB!'] = 0
json_dict['base']['price'] = "A string is not allowed!"
errors = plecos.list_errors(json_dict, path_schema_file)

print("ERRORS:")
for e in errors:
    print(e)

