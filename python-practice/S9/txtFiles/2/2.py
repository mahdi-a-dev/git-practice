with open("data.txt", "r") as f:
    for line in f:
        print(" ".join(line.split()))