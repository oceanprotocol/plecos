[![banner](https://raw.githubusercontent.com/oceanprotocol/art/master/github/repo-banner%402x.png)](https://oceanprotocol.com)

# Plecos

An [Ocean Protocol](https://oceanprotocol.com) utility library to validate asset metadata.

___"🌊 Plecos are fish which mostly eat green surface algae and are excellent window cleaners."___

![photo](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Ancistrus_sp._%28aka%29.jpg/1920px-Ancistrus_sp._%28aka%29.jpg)

> Hypostomus plecostomus, the suckermouth catfish or common pleco, ('hypo' = under, 'stoma' = mouth, 'pleco'= pleated) is a tropical fish belonging to the armored catfish family (Loricariidae), named for the armor-like longitudinal rows of scutes that cover the upper parts of the head and body. Hypostomus plecostomus is named for its sucker-like mouth, which allows it to adhere to a surface, as well as to hold and rasp at food. This omnivorous species feeds on algae, aquatic plants, and small crustaceans.
-[Wikipedia](https://en.wikipedia.org/wiki/Hypostomus_plecostomus)

**🐲🦑 THERE BE DRAGONS AND SQUIDS. This is in alpha state and you can expect running into problems. If you run into them, please open up [a new issue](https://github.com/oceanprotocol/brizo/issues). 🦑🐲**

---

## Table of Contents

- [Features](#features)
- [Get Started](#getstarted)
- [License](#license) 

---

## Features

Plecos contains functions that validate metadata formatted as JSON according to [OEP-8](https://github.com/oceanprotocol/OEPs/tree/master/8).
You can validate a single JSON containing metadata or a list with with multiple links which contain metadata.

## Get Started

The following online tools are useful when working with JSON and JSON schemas:

- https://www.jsonschema.net/
- https://jsonlint.com/
- http://jsonviewer.stack.hu/

### Quickstart

After installing and importing the package, call the `.is_valid_file(YOUR_JSON_PATH, JSON_SCHEMA_PATH)` function to check a JSON file against the latest [OEP-8 schema](https://github.com/oceanprotocol/OEPs/tree/master/8).

```python
from pathlib import Path
import plecos

# Check if valid, if not - list the error in a summary form
if not plecos.is_valid_file_local('metadata.json'):
    errors = plecos.list_errors_file('metadata.json')
if errors:
    for e in errors:
        print(e)
```

A dictionary object can also be checked against the schema, using `.is_valid_dict(python_dictionary)`.

```python
import plecos
import json

# Load it into a dictionary
with open('metadata.json') as json_file:
    this_json_dict = json.load(json_file)

# Check if valid, if not - list the error in a summary form
if not plecos.is_valid_dict_local(this_json_dict):
    errors = plecos.list_errors_dict(this_json_dict)
if errors:
    for e in errors:
        print(e)
```

### Summary of Functions

Several convenience functions are defined for validated against "local" or "remote" metadata. 

- Wrapping [jschema.Draft7Validator.validate()](https://python-jsonschema.readthedocs.io/en/latest/validate/#jsonschema.IValidator.validate)
  - validate_dict(json_dict, schema_path)
    - validate_dict_local(json_dict)
    - validate_dict_remote(json_dict)
  - validate_file(json_path, schema_path)
    - validate_file_local(json_path)
    - validate_file_remote(json_path)

- Wrapping [jschema.Draft7Validator.is_valid()](https://python-jsonschema.readthedocs.io/en/latest/validate/#jsonschema.IValidator.is_valid)
  - is_valid_dict(json_dict, schema_path)
    - is_valid_dict_local(json_dict)
    - is_valid_dict_remote(json_dict)
  - is_valid_file(json_path, schema_path)
    - is_valid_file_local(json_path)
    - is_valid_file_remote(json_path)

- Wrapping [jschema.Draft7Validator.iter_errors()](https://python-jsonschema.readthedocs.io/en/latest/validate/#jsonschema.IValidator.iter_errors)
  - list_errors(json_dict, schema_path)
    - list_errors_dict_remote(json_dict)
    - list_errors_dict_remote(json_dict)
    - list_errors_file_local(json_path)
    - list_errors_file_remote(json_path)

`list_errors` returns a tuple containing a short summary of the error (the json path), and the full error object.

*LOCAL_SCHEMA_FILE_* points to the latest OEP-8 schema for local metadata. Older versions are included in the package.

*REMOTE_SCHEMA_FILE_* points to the latest OEP-8 schema for remote metadata. Older versions are included in the package.

*LOCAL_SCHEMA_FILE* and *REMOTE_SCHEMA_FILE_* can be replaced with your own file path to your own schema.

### Publishing to pypi
To publish a new version to pypi, first bump the version number using `./bumpversion.sh`, then do the following from the console:

```bash
# Assuming we are already in the "plecos" directory
python setup.py install
python setup.py bdist_wheel
twine upload --repository-url https://upload.pypi.org/legacy/  dist/*
```

## License

```text
Copyright 2018 Ocean Protocol Foundation Ltd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
