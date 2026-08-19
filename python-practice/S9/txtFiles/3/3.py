with open("simple.txt", "r") as f:
    sentence = f.read().split()

    counts = {}
    for word in sentence:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    for word, count in counts.items():
        print(word, count) 