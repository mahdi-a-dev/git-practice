import math_operations as math

x = float(input("Enter number1: "))
y = float(input("Enter number2: "))

print(f"{x} + {y}: {math.add(x, y)}")
print(f"{x} - {y}: {(math.subtract(x ,y)):.2}")
print(f"{x} * {y}: {(math.multiply(x, y))}")
print(f"{x} / {y}: {(math.division(x, y)):.2}")