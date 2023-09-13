#!/usr/bin/python3
import json

data = {
    "country": "Netherlands",
    "year": 2026,
    "city": "Amsterdam"
}

json_string = json.dumps(data, indent=4)  # json.dumps() convert py obj to JSON string
print(json_string)
