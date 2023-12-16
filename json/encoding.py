""" encoding """
import json

data = {"name": "John", "age": 30, "city": "New York"}

# serialize to JSON
json_data = json.dumps(data)
print(json_data)