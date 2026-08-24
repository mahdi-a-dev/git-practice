class Animal:
    def __init__(self, name: str, species: str) -> None:
        self.name = name
        self.species = species

    def make_sound(self):
        print("Generic animal sound")


class Mammal(Animal):
    def __init__(self, name: str, species: str, legs: int) -> None:
        super().__init__(name, species)
        self.legs = legs


    def make_sound(self):
            print("Generic mammal sound")


class Dog(Mammal):
    def __init__(self, name: str, species: str, legs: int, race: str) -> None:
        super().__init__(name, species, legs)
        self.race = race


    def make_sound(self):
            print("woof!")


mammal = Mammal("lusy", "cow", 4)
dog = Dog("james", "dog", 4, "golden")

for i in mammal, dog:
     i.make_sound()


