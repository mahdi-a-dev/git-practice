import csv

def write_csv(data):
    with open("output.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())

        writer.writeheader()
        writer.writerows(data)

data = [
    {"name": "ali", "age": 21, "city": "tehran"},
    {"name": "mohammad", "age": 34, "city": "shiraz"},
    {"name": "reza", "age": 23, "city": "tabriz"}
    ]

write_csv(data)