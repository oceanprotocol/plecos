import pytest
import json
from pathlib import Path

import logging

# Select the latest schema path here
PATH_SCHEMA_DIR = Path().cwd() / 'plecos' / 'schemas'
print(PATH_SCHEMA_DIR)
PATH_LATEST_SCHEMA = PATH_SCHEMA_DIR / 'metadata_190218.json'
assert PATH_LATEST_SCHEMA.exists(), "Path not found: {}".format(PATH_LATEST_SCHEMA)

PATH_SAMPLES_DIR = Path().cwd() / 'plecos' / 'samples'
PATH_SAMPLE_METADATA_LOCAL = PATH_SAMPLES_DIR / 'metadata_local.json'
assert PATH_SAMPLE_METADATA_LOCAL.exists(), "Path not found: {}".format(PATH_SAMPLE_METADATA_LOCAL)

PATH_SAMPLES_DIR = Path().cwd() / 'plecos' / 'samples'
PATH_SAMPLE_METADATA_REMOTE = PATH_SAMPLES_DIR / 'metadata_remote.json'
assert PATH_SAMPLE_METADATA_REMOTE.exists(), "Path not found: {}".format(PATH_SAMPLE_METADATA_REMOTE)

@pytest.fixture
def schema_dict():
    with open(PATH_LATEST_SCHEMA) as json_file:
        this_json = json.load(json_file)
    print("Loaded schema:", PATH_LATEST_SCHEMA)
    return this_json

@pytest.fixture
def sample_metadata_dict_local():
    with open(PATH_SAMPLE_METADATA_LOCAL) as json_file:
        this_json = json.load(json_file)
    print("Loaded sample:", PATH_SAMPLE_METADATA_LOCAL)
    return this_json

@pytest.fixture
def sample_metadata_dict_remote():
    with open(PATH_SAMPLE_METADATA_REMOTE) as json_file:
        this_json = json.load(json_file)
    print("Loaded sample:", PATH_SAMPLE_METADATA_REMOTE)
    return this_json