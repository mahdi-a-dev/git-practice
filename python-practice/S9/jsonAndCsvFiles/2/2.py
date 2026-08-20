import json

def get_value(s, key):
    data = json.loads(s)
    return data[key] 

json_data = '{"name": "ali", "age": "21"}'

print(get_value(json_data, "name"))
print(get_value(json_data, "age"))