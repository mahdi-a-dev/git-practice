#1 string
print("----------1----------")
text = input("Enter text: ")
sentences = text.count(".") + text.count(",") + text.count("!") + text.count("?") + text.count(";")
words = text.count(" ") + 1
characters = len(text)
letters = characters - (sentences + text.count(":"))

print(f"sentences: {sentences}\nwords: {words}\ncharacters: {characters}\nletters: {letters}")

# 2 string
print("----------2----------")
ch = input("Enter chr: ")
print(ord(ch))

# 3 string
print("----------3----------")
phone = input("Enter phone: ")
print(phone.isnumeric())

# 4 dictionary
print("----------4----------")
dictionary = {}
while (word := input("Enter word (exit with q):")).lower() != "q":
    meaning = input("Enter meaning (split with , ):").split(",")
    dictionary[word] = meaning
print(dictionary)

# 5 dictionary
print("----------5----------")

while (word := input("Enter word for get meaning (exit with q):")).lower() != "q":
    print(dictionary.get(word))

# 6 list
print("----------6----------")
lst1 = ["0936", "0938", "0935"]
lst2 = ["0935", "0933", "0930"]
print(list(set(lst1 + lst2)))

# 7 numbers
print("----------7----------")
p = 3.14
r = float(input("Enter radius: "))
print(f"area: {(p * (r ** 2)):.2f}")
print(f"perimeter: {(2 * p * r):.2f}")

# 8 numbers
print("----------8----------")
number = int(input("Enter a number: "))
print(f"{number} ^ 2: {number ** 2}")
print(f"{number} ^ 3: {number ** 3}")

# 9 numbers
print("----------9----------")
num1 = float(input("num1: "))
num2 = float(input("num2: "))
print(f"{num1} ^ {num2}: {num1 ** num2}")

# 10 numbers
print("----------10----------")
x = float(input("num1: "))
y = float(input("num2: "))
z = float(input("num3: "))
print(f"avg: {(x + y + z) / 3}")
