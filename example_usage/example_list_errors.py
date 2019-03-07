from pathlib import Path
import plecos
import json
print(plecos.__version__)
#%%
path_to_json_local = Path("~/ocn/Plecos/plecos/samples/sample_metadata_local.json").expanduser()
path_to_json_remote = Path("~/ocn/Plecos/plecos/samples/sample_metadata_remote.json").expanduser()
path_to_broken_json = Path("~/ocn/Plecos/plecos/samples/metadata_local_broken.json").expanduser()
path_to_schema_local = Path("~/ocn/Plecos/plecos/schemas/metadata_local_v0_1.json").expanduser()
path_to_schema_remote = Path("~/ocn/Plecos/plecos/schemas/metadata_remote_v0_1.json").expanduser()

# Select remote or local metadata
LOCAL=False

if LOCAL:
    path_json_file = path_to_json_local
    path_schema_file = path_to_schema_local

    with open(path_to_json_local) as f:
        json_dict = json.load(f)

else:
    path_json_file = path_to_json_remote
    path_schema_file = path_to_schema_remote

    with open(path_to_json_remote) as f:
        json_dict = json.load(f)

print("Json file:", path_json_file)
print("Schema file:", path_schema_file)
#%%



# json_dict['base']['EXTRA ATTRIB!'] = 0
# json_dict['base']['files'][0]['EXTRA_ATTR'] = "????"
# json_dict['base']['price'] = "A string is not allowed!"
errors = plecos.list_errors(json_dict, path_schema_file)

if errors:
    print("ERRORS:")
    for e in errors:
        print(e)
else:
    print("No errors")

raise
#%%


json_dict = {
  "base": {
    "name": "10 Monkey Species Small",
    "author": "Mario",
    "license": "CC0: Public Domain",
    "contentType": "jpg/txt",
    "price": 5,
    "categories": [
      "image"
    ],
    "tags": [
      "image data",
      " animals"
    ],
    "type": "dataset",
    "description": "Example description",
    "copyrightHolder": "",
    "encoding": "",
    "compression": "",
    "workExample": "",
    "inLanguage": "en",
    "files": [
      {
        "url": "https://s3.amazonaws.com/datacommons-seeding-us-east/10_Monkey_Species_Small/assets/training.zip"
      },
      {
        "url": "https://s3.amazonaws.com/datacommons-seeding-us-east/10_Monkey_Species_Small/assets/monkey_labels.txt"
      },
      {
        "url": "https://s3.amazonaws.com/datacommons-seeding-us-east/10_Monkey_Species_Small/assets/validation.zip"
      }
    ],
    "links": [
      {
        "url": "https://s3.amazonaws.com/datacommons-seeding-us-east/10_Monkey_Species_Small/links/sample/sample.zip",
        "name": "sample.zip",
        "type": "sample"
      },
      {
        "url": "https://github.com/slothkong/CNN_classification_10_monkey_species",
        "name": "example code",
        "type": "example code"
      },
      {
        "url": "https://s3.amazonaws.com/datacommons-seeding-us-east/10_Monkey_Species_Small/links/discovery/n5151.jpg",
        "name": "n5151.jpg",
        "type": "discovery"
      }
    ],
    "checksum": "0",
  },

}

#%%
path_to_schema_local = Path("~/ocn/Plecos/plecos/schemas/metadata_local_190305.json").expanduser()
errors = plecos.list_errors(json_dict, path_to_schema_local)

if errors:
    print("ERRORS:")
    for e in errors:
        print(e)
else:
    print("No errors")