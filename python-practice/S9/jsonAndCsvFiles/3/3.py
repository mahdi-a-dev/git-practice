import json

def update_json(json_string, key, value):
    data = json.loads(json_string)
    data[key] = value
    return json.dumps(data)

json_data = '{"name": "mohammadreza", "age": 45}'

result = update_json(json_data, "city", "tehran")

print(result)