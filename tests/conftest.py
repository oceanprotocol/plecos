import pytest
import json
from pathlib import Path

import logging

# Select the latest schema path here
PATH_SCHEMA_DIR = Path().cwd() / 'schemas'
PATH_LATEST_SCHEMA = PATH_SCHEMA_DIR / 'schema_v190118.json'
# PATH_LATEST_SCHEMA = PATH_SCHEMA_DIR / 'supersimple.json'
# PATH_LATEST_SCHEMA = PATH_SCHEMA_DIR / 'test.json'
assert PATH_LATEST_SCHEMA.exists()

PATH_SAMPLES_DIR = Path().cwd() / 'samples'
PATH_SAMPLE_METADATA = PATH_SAMPLES_DIR / 'metadata UK weather.json'
# PATH_SAMPLE_METADATA = PATH_SAMPLES_DIR / 'supersimple.json'
# PATH_SAMPLE_METADATA = PATH_SAMPLES_DIR / 'test.json'
assert PATH_SAMPLE_METADATA.exists()


# @pytest.fixture
# def test1():
#     def this_function():
#         print("hello")
#         print("asdfasd;lfk")
#     return this_function

@pytest.fixture
def schema_dict():
    with open(PATH_LATEST_SCHEMA) as json_file:
        this_json = json.load(json_file)
    print("Loaded schema:", PATH_LATEST_SCHEMA)
    return this_json

@pytest.fixture
def sample_metadata_dict():
    with open(PATH_SAMPLE_METADATA) as json_file:
        this_json = json.load(json_file)
    print("Loaded sample:", PATH_SAMPLE_METADATA)
    return this_json