[![banner](https://raw.githubusercontent.com/oceanprotocol/art/master/github/repo-banner%402x.png)](https://oceanprotocol.com)

# Plecos

> Utility library to validate the Metadata of assets
> [oceanprotocol.com](https://oceanprotocol.com)

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

Plecos contains functions that validate metadata formatted as json according to OEP-8. 
You can validate a single json containg metadata or a list with with multiple links 
which contain metadata. 

## Get Started 

The following online tools are useful when working with JSON and schemas;
https://www.jsonschema.net/
https://jsonlint.com/
http://jsonviewer.stack.hu/

### Quickstart
After installing and importing the package, call the `.is_valid(YOUR_JSON_PATH)` function to check a json file against the latest [OEP8 schema](https://github.com/oceanprotocol/OEPs/tree/master/8). 
```python
from pathlib import Path
import plecos

# Get a file path to your metadata.json file
PATH_DATA_ROOT = Path("~/DATA").expanduser()
path_to_json = PATH_DATA_ROOT / 'metadata.json'

# Check if valid, if not - list the error in a summary form
if not plecos.is_valid(path_to_json):
    plecos.list_errors(path_to_json)
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

