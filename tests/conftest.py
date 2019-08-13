import json
from pathlib import Path

import pytest

import plecos

# Select the latest schema path here
# PATH_SCHEMA_DIR = Path().cwd() / 'plecos' / 'schemas'
# print(PATH_SCHEMA_DIR)
# PATH_LATEST_SCHEMA = PATH_SCHEMA_DIR / 'metadata_190218.json'
# assert PATH_LATEST_SCHEMA.exists(), "Path not found: {}".format(PATH_LATEST_SCHEMA)

# Local sample
PATH_SAMPLES_DIR = Path().cwd() / 'plecos' / 'samples'
PATH_SAMPLE_METADATA_LOCAL = PATH_SAMPLES_DIR / 'sample_metadata_local.json'
assert PATH_SAMPLE_METADATA_LOCAL.exists(), "Path not found: {}".format(PATH_SAMPLE_METADATA_LOCAL)

# Remote sample
PATH_SAMPLES_DIR = Path().cwd() / 'plecos' / 'samples'
PATH_SAMPLE_METADATA_REMOTE = PATH_SAMPLES_DIR / 'sample_metadata_remote.json'
assert PATH_SAMPLE_METADATA_REMOTE.exists(), "Path not found: {}".format(
    PATH_SAMPLE_METADATA_REMOTE)


@pytest.fixture
def schema_local_dict():
    with open(plecos.LOCAL_SCHEMA_FILE) as json_file:
        this_json = json.load(json_file)
    print("Loaded schema:", plecos.LOCAL_SCHEMA_FILE)
    return this_json


@pytest.fixture
def schema_remote_dict():
    with open(plecos.REMOTE_SCHEMA_FILE) as json_file:
        this_json = json.load(json_file)
    print("Loaded schema:", plecos.REMOTE_SCHEMA_FILE)
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


@pytest.fixture
def path_sample_metadata_local():
    return PATH_SAMPLE_METADATA_LOCAL


@pytest.fixture
def path_sample_metadata_remote():
    return PATH_SAMPLE_METADATA_REMOTE
