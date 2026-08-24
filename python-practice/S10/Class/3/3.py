class Student:
    def __init__(self, name: str, age: int, marks: list) -> None:
        self.name = name
        self.age = age
        self.marks = marks

    def add_mark(self, mark: float) -> None:
        self.marks.append(mark)

    def avg(self) -> float:
        return sum(self.marks) / len(self.marks)

    def info(self) -> None:
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")
    

def main():
    st = Student("mohammadreza", 20, [14, 20, 15, 18])
    st.add_mark(17.5)
    print(st.avg())
    st.info()
    st.add_mark(12.5)
    print(st.avg())
    st.info()



if __name__ == "__main__":
    main()