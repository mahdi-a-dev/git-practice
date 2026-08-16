#1
def my_len(l):
    counter = 0
    for _ in l:
        counter += 1
    return counter

#2
def my_min(*args):
    minimum = float("inf")
    for i in args:
        if i < minimum:
            minimum = i
    return minimum

#3
def my_sum(*args):
    s = 0
    for i in args:
        s += i
    return s

#4
def square(n):
    for i in range(1, n):
        if n == (i ** 2):
            return True
    return False

#5
def discount(price, rate):
    discount_rate = ((price * rate) / 100)
    return price - discount_rate

#6
def func(ch):
    if 48 <= ord(ch) <= 57:
        return "is number"
    elif 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122:
        return "is letter"
    return"Others!"

print(func("!"))