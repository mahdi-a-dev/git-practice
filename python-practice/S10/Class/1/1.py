class Rectangle:

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.heigth = height

    def masahat(self) -> float:
        return self.width * self.heigth
    

    def mohit(self) -> float:
        return (self.width + self.heigth) * 2


def main():
    r1 = Rectangle(5, 8)
    print(r1.masahat())
    print(r1.mohit())


if __name__ == "__main__":
    main()