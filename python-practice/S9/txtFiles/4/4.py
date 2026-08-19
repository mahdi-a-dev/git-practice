with open("source.txt", "r") as s:
    with open("destination.txt", "w") as d:
        for line in s:
            d.write(line)

