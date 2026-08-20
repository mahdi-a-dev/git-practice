import json 

def merge_json(json1, json2):
    data1 = json.loads(json1)
    data2 = json.loads(json2)
    data1.update(data2)
    return json.dumps(data1)


data = '{"name": "mohammadreza"}'
data1 = '{"age": 21}'

print(merge_json(data, data1))