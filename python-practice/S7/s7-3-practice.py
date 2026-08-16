#1
print("---------1---------")
text = "!Hello, World"
encoded = text.encode("utf-8")
print(encoded)

#2
print("---------2---------")
data = b"My name is M\xc3\xb6bius"
decoded = data.decode("utf-8")
print(decoded)

#3
print("---------3---------")
chars = ["A", "B", "C", "a", "b", "c"]
ascii_list = [ord(char) for char in chars]
print(ascii_list)

#3
print("---------3---------")
text = input("Enter a sentence: ")
total = sum(ord(char) for char in text)
print(total)

#4
print("---------4---------")
unicode_points = [1024, 5679, 234, 987]
text = ""
for number in unicode_points:
    text += chr(number)
encoded = text.encode("utf-8")
print(encoded)

#5
#print("---------5---------")
#data = b"\xff\xfeM\x00y\x00\x00N\x00a\x00m\x00e\x00"
#decoded = data.decode("utf-16")
#print(decoded)

#6
print("---------6---------")
def utf_hex(text):
    encoded = text.encode("utf-8")
    return encoded.hex()

text = input("enter a string: ")
result = utf_hex(text)
print(result)