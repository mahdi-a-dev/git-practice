def is_file_exists(path: str) -> None:
    try:
        with open(path, "r") as f:
            print(f.read())

    except FileNotFoundError:
        print("File not found!")

is_file_exists("test.txt")