with open("notes.txt", "a") as f:
    while (text := input("Enter text (leave empty for exit):")) != "":
        f.write(text + "\n")