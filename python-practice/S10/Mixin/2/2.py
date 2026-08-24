class MathOperationsMixin:
    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def division(self):
        return self.x / self.y if self.y != 0 else "Error, division by zero."


class XAndY(MathOperationsMixin):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


xy = XAndY(6, 7)
print(xy.add())
print(xy.subtract())
print(xy.multiply())
print(xy.division())
