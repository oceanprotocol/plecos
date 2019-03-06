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
if 1:
    path_json_file = path_to_json_local
    path_schema_file = path_to_schema_local

    with open(path_to_json_local) as f:
        json_dict = json.load(f)
else:
    path_json_file = path_to_json_remote
    path_schema_file = path_to_json_remote
    with open(path_to_json_remote) as f:
        json_dict = json.load(f)


#%%
result = plecos.validate_file_local(path_json_file)

# Validation should return None if everything is valid
assert not result
print(result)

# Alternatively, you can return True/False with the .is_valid function
result = plecos.is_valid_file(path_to_json)
assert result

# If you load an invalid json, the validator will return an error
# result = plecos.validate(path_to_broken_json)

# Or return a False boolean using is_valid
result = plecos.plecos.is_valid_file(path_to_broken_json, path_to_schema)
assert not result

# A summary of errors can be listed with .list_errors()
plecos.list_errors_file(path_to_broken_json, path_to_schema)


