import json, csv, io

def json_to_csv(json_string):
    data = json.loads(json_string)
    output = io.StringIO()
    csv_data = csv.DictWriter(output, fieldnames=data[0].keys())
    csv_data.writeheader()
    csv_data.writerows(data)
    return output.getvalue()

data = '[{"name": "mohammadreza", "age": 21}, {"name": "ali", "age": 15}]'

print(json_to_csv(data))


