import json

def count_colors(json_string):
    data = json.loads(json_string)
    counts = {}
    for item in data:
        color = item["color"]

        if color in counts:
            counts[color] += 1
        else:
            counts[color] = 1
    return counts


json_data = '[{"color": "red"}, {"color": "red"}, {"color": "green"}]'

print(count_colors(json_data))