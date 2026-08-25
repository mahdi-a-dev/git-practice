from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def start():
        """ start the car """

    @abstractmethod
    def stop():
        """ stop the car """

class SportCar(Car):
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"Sport Car: {self.brand} is starting")

    def stop(self):
        print(f"Sport Car: {self.brand} is stoping")


class Sedan(Car):
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"Sedan: {self.brand} is starting")

    def stop(self):
        print(f"Sedan: {self.brand} is stoping")


s = SportCar("lamborghini")
s.start()
s.stop()

c = Sedan("toyota camry")
c.start()
c.stop()