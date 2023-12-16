""" Deserialization """
import json

encoded_data = '{"name": "John", "age": 30, "city": "New York"}'
dencoded_data = json.loads(encoded_data)
print(dencoded_data)
