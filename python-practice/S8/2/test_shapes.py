from shapes import rectangle, circle

x = float(input("x:"))
y = float(input("y: "))

print(f"masahat: {rectangle.masahat(x, y)}")
print(f"mohit: {rectangle.mohit(x, y)}")

r = float(input("r: "))
print(f"masahat: {circle.masahat(r)}")
print(f"mohit: {circle.mohit(r)}")