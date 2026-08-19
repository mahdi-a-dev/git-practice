with open("output.txt", "w") as f:
    while (x := input("Enter sentence (or type exit): ").lower()) != "exit":
        f.write(x + "\n")

