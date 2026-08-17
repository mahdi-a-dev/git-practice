# 1
print("----------1----------")
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
for i in range(min(num1, num2) + 1, max(num1, num2)):
    print(i)

# 2
print("----------2----------")
x = int(input("x: "))
y = int(input("y: "))
min_ = min(x, y)
for i in range(1, min_ +1):
    if x % i == 0 and y % i == 0:
        print(i)

# 3
print("----------3----------")
x = int(input("x: "))
y = int(input("y: "))
min_ = min(x, y)
for i in range(min_, 0, -1):
    if x % i == 0 and y % i == 0:
        print(i)
        break

# 4
print("----------4----------")
x = int(input("x: "))
y = int(input("y: "))
min_ = min(x, y)
max_ = max(x, y)

i = max_
while i % min_ != 0:
    i += max_
print(i)


# 5
print("----------5----------")
x = int(input("x: "))

i = 0
while x > 0:
    x //= 10
    i += 1
print(i)

# 6
print("----------6----------")
n = int(input("n: "))
for i in range(1, n +1):
    print(" " * (n-1), end="")
    print("*" * i)

# 7
print("----------7----------")
from random import choice
names = ["mohammadreza", "ali", "reza", "javad", "mohammad", "sara", "morteza"]
while True:
    ch = choice(names)
    answer = input(f"is this your guess, {ch}? (y/n): ").lower()
    if "y" in answer:
        print("you win!")
        break
    names.remove(ch)