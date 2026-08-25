class Temperature:
    def __init__(self, C):
        self._C = C

    @property
    def CToF(self):
        return self._C * 1.8 * 32

c = Temperature(5)
print(c.CToF)