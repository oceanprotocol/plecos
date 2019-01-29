valid_schema = {
    "properties": {
        "base": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "dateCreated": {"type": "string",
                                "format": "date-time"},
                "author": {"type": "string"},
                "license": {"type": "string"},
                "contentType": {"type": "string"},
                "price": {"type": "number"},

                "links": {
                    "type": "array",
                    "description": "files",
                    "items": [
                        {"type": "string",
                         "format": "uri"},
                    ]
                },


                "size": {"type": "string"},
                "description": {"type": "string"},
                "copyrightHolder": {"type": "string"},
                "compression": {"type": "string"},

                "workExample": {"type": "string"},
                "contentUrls": {
                    "type": "array",
                    "description": "ContentUrls",
                    "items": [
                        {"type": "string",
                         "format": "uri"}
                    ]
                },

                "inLanguage": {"type": "string"},
                "tags": {"type": "string"},
                },
            "required": ["name", "type", "description", "size", "author", "license", "contentType",
                         "inLanguage", "price", "tags"]  # put contentURLs and links back in as required
            },
        "curation": {
            "type": "object",
            "properties": {
                "rating": {"type": "number"},
                "numVotes": {"type": "number"},
                "schema": {"type": "string"}
                },
            "required": ["rating", "numVotes", "schema"]
        },
    },
"required": ["base", "curation"]
}



