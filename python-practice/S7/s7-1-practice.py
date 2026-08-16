# 1
print("---------1---------")
if len((text := input("Enter text: "))) > 10:
    print(text)

# 2
print("---------2---------")
if len((list := input("Enter list: ").split(","))) > 5:
    print(int(list[0]) + int(list[1]))

# 3
print("---------3---------")
s = 0
while (number := input("Enter numbers: ")) != " ":
    s += int(number)
print(s)


# 4
print("---------4---------")
if "5" in (list := input("Enter list: ").split(",")):
    print(list.index("5"))

# 5
print("---------5---------")
from random import randint
c = 0
while (r := randint(1, 100)) < 80:
    c += 1
    print(r)
print(f"count: {c}")

# 6
print("---------6---------")
print(len((text := input("Enter text: ").split(" "))))
