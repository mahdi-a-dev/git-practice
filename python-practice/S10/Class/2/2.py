class Car:
    def __init__(self, brand: str, model: str, make_year: str) -> None:
        self.brand = brand
        self.model = model
        self.make_year = make_year

    def info(self) -> None:
        print(f"Brand: {self.brand}, Model: {self.model}, Make_year: {self.make_year}")

def main():
    c1 = Car("Toyota", "aurion", "2008")
    c1.info()


if __name__ == "__main__":
    main()