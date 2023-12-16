""" Deserialization """
import json

encoded_data = '{"name": "John", "age": 30, "city": "New York"}'
decoded_data = json.loads(encoded_data)
print(decoded_data)
