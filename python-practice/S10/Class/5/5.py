class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def raise_salary(self, amount: float) -> None:
        if amount > 0:
            self.salary += amount
        else:
            print("The amount must be greater than zero!")

    def info(self) -> None:
        print(f"Name: {self.name}, Salary: {self.salary}")

def main():
    employee = Employee("ali", 150000)
    employee.info()
    employee.raise_salary(1200.500)
    employee.info()


if __name__ == "__main__":
    main()