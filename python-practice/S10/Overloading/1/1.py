class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


p1 = Point(5, 7)
p2 = Point(2, 1)

p3 = p1 + p2

print(f"x: {p3.x}, y: {p3.y}")