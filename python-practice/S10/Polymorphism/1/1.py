class Vehicle:
    def __init__(self, color: str, weight: float, speed: str) -> None:
        self.color = color
        self.weight = weight
        self.speed = speed


    def move(self):
        print("Vehicle is moving...")



class Car(Vehicle):
    def move(self):
        print("Car is moving...")



class Bicycle(Vehicle):
    def move(self):
        print("Bicycle is moving...")



class Airplane(Vehicle):
    def move(self):
        print("Airplane is moving...")



class Lamborghini(Car):
    def __init__(self, color: str, weight: float, speed: str, model: str):
        super().__init__(color, weight, speed)
        self.model = model


    def move(self):
        print("Lamborghini is moving...")



class Benz(Car):
    def __init__(self, color: str, weight: float, speed: str, model: str):
        super().__init__(color, weight, speed)
        self.model = model


    def move(self):
        print("Benz is moving...")


car = Car("red", 1500, "200")
bicycle = Bicycle("black", 30, "80")
airplane = Airplane("white", 60000, "1000")
lamborghini = Lamborghini("blue", 1450, "350", "Terzo Millennio")
benz = Benz("orange", 1800, "320", "SUVs")

for i in car, bicycle, airplane, lamborghini, benz:
     i.move()


