from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary():
        """ Calculate employee's salary """

class HourlyEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary
        self.bounos_percent = 10

    def calculate_salary(self):
        return self.salary + (self.salary * self.bounos_percent / 100)


class SalariedEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary
        self.bounos_percent = 15

    def calculate_salary(self):
        return self.salary + (self.salary * self.bounos_percent / 100)


h = HourlyEmployee(1000)
print(h.calculate_salary())

s = SalariedEmployee(1000)
print(s.calculate_salary())