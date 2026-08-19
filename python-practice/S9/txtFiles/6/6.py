with open("numbers.txt", "r") as f:
    sum = 0
    l = 0
    for line in f:
        sum += int(line)
        l += 1
    print(f"sum: {sum}\navg: {sum / l}")