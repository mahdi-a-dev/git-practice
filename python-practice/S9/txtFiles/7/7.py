with open("document.txt", "r") as f:
    file_content = f.read()
    while (search := input("search (exit q): ").lower()) != "q":
        if search in file_content:
            print("word found!")
            reaplace = input("Reaplace it with something: ")
            file_content = file_content.replace(search, reaplace)
        else:
            print("word not found!")
    with open("update_document.txt", "w") as u:
        u.write(file_content)