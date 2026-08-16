#1
print("---------1--------")
l = [4, 5, 8, 4, 6, 9, 12, 1, 13, 15, 17, 19, 20]
even = len(list(filter(lambda x: x % 2 == 0, l)))
odd = len(list(filter(lambda x: x % 2 != 0, l)))
print(f"even: {even}\nodd: {odd}")

#2
print("---------2--------")
t = [("ali", 35), ("reza", 41), ("mohammadreza", 20)]
t.sort(key=lambda x: x[1])
print(t)

#3
print("---------3--------")
l = [{"name": "apple", "weight": 60, "color": "red"},
     {"name": "banana", "weight": 70, "color": "yellow"},
     {"name": "orange", "weight": 65, "color": "orenge"},
     {"name": "coconut", "weight": 100, "color": "brown"}]

l.sort(key=lambda x: x["color"])
print(l)

#4
print("---------4--------")
l = [4, 5, 8, 4, 6, 9, 12, 1, 13, 15, 17, 19, 20]
even = list(filter(lambda x: x % 2 == 0, l))
odd = list(filter(lambda x: x % 2 != 0, l))
print(f"even: {even}\nodd: {odd}")

#5
print("---------5--------")
l = [4, 5, 8, 7, 6, 9, 3, 10]
square = list(map(lambda x: x ** 2, l))
cube = list(map(lambda x: x ** 3, l))
print(f"square: {square}\ncube: {cube}")

#6
print("---------6--------")
s = "hello world"
start_with = lambda s: True if s.startswith("h") else False
print(start_with(s))

#7
print("---------7--------")
s = "5.5"
is_number = lambda s: s.replace(".", "", 1).isdigit() 
print(is_number(s))