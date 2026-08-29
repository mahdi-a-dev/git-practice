def string_to_int(string: str) -> int | None:
    try:
        return int(string)
    except ValueError:
        return None

print(string_to_int("123456F"))