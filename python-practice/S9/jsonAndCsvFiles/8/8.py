import csv

def sum_column(path, name):
    total = 0
    with open(path, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            total += float(row[name])

    return total

result = sum_column("data.csv", "age")
print(result)