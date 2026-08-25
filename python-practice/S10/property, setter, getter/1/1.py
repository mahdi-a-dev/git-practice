class Circle:
    def __init__(self, radius: float) -> None:
        self._radius = radius

    @property
    def area(self) -> float:
        """
            Calculate circle area.
        """
        return self._radius ** 2 * 3.14

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius > 0:
            self._radius = radius
        else:
            print("Radius must be greater than 0.")


c = Circle(7)
print(c.area)
c.radius = -5
help(c)