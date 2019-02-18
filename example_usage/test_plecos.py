from pathlib import Path
import plecos

path_to_json = Path("~/ocn/Plecos/plecos/samples/metadata_local.json").expanduser()
path_to_broken_json = Path("~/ocn/Plecos/plecos/samples/metadata_local_broken.json").expanduser()
path_to_schema = Path("~/ocn/Plecos/plecos/schemas/metadata_190218.json").expanduser()

result = plecos.validate(path_to_json)

# Validation should return None if everything is valid
assert not result
print(result)

# You can validate against a chosen shema file with the optional parameter
result = plecos.validate(path_to_json, schema_file=path_to_schema)
assert not result

# Alternatively, you can return True/False with the .is_valid function
result = plecos.is_valid(path_to_json, path_to_schema)
assert result

# If you load an invalid json, the validator will return an error
# result = plecos.validate(path_to_broken_json)

# Or return a False boolean using is_valid
result = plecos.plecos.is_valid(path_to_broken_json, path_to_schema)
assert not result

# A summary of errors can be listed with .list_errors()
plecos.list_errors(path_to_broken_json, path_to_schema)


