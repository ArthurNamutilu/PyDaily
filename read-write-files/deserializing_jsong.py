#!/usr/bin/python3
import json

json_data = '{"name": "John", "age": 30, "city": "New York"}'
# json.loads() conver json string back into a python object
py_dict = json.loads(json_data)
print(py_dict)
