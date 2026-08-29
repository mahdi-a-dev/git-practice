def found_key(dictionary, key):
    try:
        value = dictionary[key]
    except KeyError:
        print("key not found!")
    else:
        return value

print(found_key({"name": "ali", "age": 20}, "age"))