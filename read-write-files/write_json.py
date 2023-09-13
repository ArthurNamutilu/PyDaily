#!/usr/bin/python3
""" This module writes Python data to JSON """

data = {
    "name": "Gg",
    "age": 30,
    "city": "New York"
}


import json
with open("file.json", 'w') as json_file:
    json.dump(data, json_file)
