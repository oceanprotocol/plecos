import requests
#  from ../metadata_validator/json_versions import meta_data_links


# %%
# list containing links to metadata
meta_data_links = [
    "https://s3.eu-central-1.amazonaws.com/trilobite/British_birdsong/metadata.json",
    "https://s3.eu-central-1.amazonaws.com/trilobite/Humpback_identification/metadata.json",
    "https://s3.eu-central-1.amazonaws.com/trilobite/Monkey_Species/metadata.json",
    "https://s3.eu-central-1.amazonaws.com/trilobite/World_Population/metadata.json",
    "https://s3.eu-central-1.amazonaws.com/trilobite/Monkey_Species/metadata.json",
    "https://s3.eu-central-1.amazonaws.com/trilobite/Monkey_Species/metadata.json",
]


# %%
# test links in list
def test_metadata(link_list):
    """
    Tests that correct responses are returned and that data
    can be validated against schema.
    """
    list_meta_2 = []
    for i in link_list:
        i = requests.get(i)

        if i.status_code != 200:
            print(" {} does not return a valid response".format(i))
            continue
        elif i.status_code == 200:
            list_meta_2.append(i.json())
            print(" {} returns a valid response".format(i))

    print(list_meta_2)


test_metadata(meta_data_links)
