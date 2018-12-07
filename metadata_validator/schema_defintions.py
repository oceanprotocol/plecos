valid_schema = {
    "properties": {
        "base": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "type": {"type": "string"},
                "size": {"type": "number"},
                "dateCreated": {"type": "string",
                                "format": "date-time"},
                "description": {"type": "string"},
                "author": {"type": "string"},
                "license": {"type": "string"},
                "copyrightHolder": {"type": "string"},
                "compression": {"type": "string"},
                "contentType": {"type": "string"},
                "workExample": {"type": "string"},
                "contentUrls": {
                    "type": "array",
                    "description": "ContentUrls",
                    "items": [
                        {"type": "string",
                         "format": "uri"}
                    ]
                },
                "links": {
                    "type": "array",
                    "description": "ContentUrls",
                    "items": [
                        {"type": "string"},
                    ]
                },
                "inLanguage": {"type": "string"},
                "tags": {"type": "string"},
                "price": {"type": "number"},
                },
            "required": ["name", "type", "description", "size", "author", "license", "contentType", "contentUrls", "links", "inLanguage", "price", "tags"]
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



