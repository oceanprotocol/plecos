#%%
import jsonschema
from pathlib import Path
import pkg_resources

# DATA_PATH = pkg_resources.resource_filename('plecos', 'schemas/')
SCHEMA_FILE = Path(pkg_resources.resource_filename('plecos', 'schemas/metadata_v190118.json'))
assert SCHEMA_FILE.exists(), "Can't find schema file {}".format(SCHEMA_FILE)

# Select the latest schema path here
# PATH_SCHEMA_DIR = Path().cwd() / 'plecos' / 'schemas'
# print(PATH_SCHEMA_DIR)
# PATH_LATEST_SCHEMA = PATH_SCHEMA_DIR / 'metadata_v190118.json'
# PATH_LATEST_SCHEMA = PATH_SCHEMA_DIR / 'supersimple.json'
# PATH_LATEST_SCHEMA = PATH_SCHEMA_DIR / 'test.json'
# assert PATH_LATEST_SCHEMA.exists(), "Path not found: {}".format(PATH_LATEST_SCHEMA)

# PATH_SAMPLES_DIR = Path().cwd() / 'samples'
# PATH_SAMPLE_METADATA = PATH_SAMPLES_DIR / 'metadata sample publisher.json'
# PATH_SAMPLE_METADATA = PATH_SAMPLES_DIR / 'squid_example.json'
# PATH_SAMPLE_METADATA = PATH_SAMPLES_DIR / 'supersimple.json'
# PATH_SAMPLE_METADATA = PATH_SAMPLES_DIR / 'test.json'
# assert PATH_SAMPLE_METADATA.exists(), "Path not found: {}".format(PATH_SAMPLE_METADATA)

#%%