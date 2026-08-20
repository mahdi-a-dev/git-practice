import json

def parse_json(s):
    return json.loads(s)

print(parse_json("[4, 5, 6, 6]"))