#1
print("---------1---------")
def my_enumerate(l, start=0):
    for i in range(start, len(l)):
        yield i, l[i]
        
for c, i in my_enumerate([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 3):
    print(c, i)
    
#2
print("---------2---------")
def fib():
    f1 = 0
    yield f1
    f2 = 1
    yield f2
    while True:
        f3 = f1 + f2
        yield f3
        f1 = f2
        f2 = f3
a = fib()
for _ in range(1, 10):
    print(next(a))
    
#3
print("---------3---------")
def sum_gen(l):
    s = 0
    for i in l:
        s += i
        yield s

x = sum_gen([10, 5, 2, 4, 6, 3])
print(next(x))
print(next(x))

#4
print("---------4---------")
def rev_str(s):
    for i in range(len(s) - 1, -1, -1):
        yield s[i]

rs = rev_str("alireza")
for i in rs:
    print(i)
    
#5
print("---------5---------")
def my_gen(odd_or_even="e"):
    c = 0
    if odd_or_even.lower() == "o":
        c = 1
    while True:
        yield c
        c += 2
eo = my_gen("o")
for _ in range(10):
    print(next(eo))
    
#6
print("---------6---------")
def star_gen():
    counter = 1
    while True:
        s = ""
        for _ in range(1, counter + 1):
            s += f"{counter}\t"
        yield s
        counter += 1
            
g = star_gen()
for _ in range(20):
    print(next(g))