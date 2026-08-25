from abc import ABC, abstractmethod

class Person(ABC):

    @abstractmethod
    def greet():
        """ greeting """

    @abstractmethod
    def introduce():
        """ introducing """

class Student(Person):
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role


    def greet(self):
        print(f"Hello how are you?")


    def introduce(self):
        print(f"I am a {self.role}, my name is {self.name}, i'm {self.age} years old.")


class Teacher(Person):
    def __init__(self, name, age, role):
            self.name = name
            self.age = age
            self.role = role


    def greet(self):
        print(f"Hello how are you?")


    def introduce(self):
        print(f"I am a {self.role}, my name is {self.name}, i'm {self.age} years old.")


s = Student("ali", 20, "student")
s.greet()
s.introduce()
print(40 * "*")
t = Teacher("reza", 36, "teacher")
t.greet()
t.introduce()
