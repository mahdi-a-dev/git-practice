class Matrix:
    def __init__(self, a: list, b:list) -> None:
        self.matrix: list = [a, b]

    def __add__(self, other: "Matrix") -> "Matrix":
        return Matrix([self.matrix[0][0] + other.matrix[0][0], self.matrix[0][1] + other.matrix[0][1]],
                      [self.matrix[1][0] + other.matrix[1][0], self.matrix[1][1] + other.matrix[1][1]])


    def __sub__(self, other: "Matrix") -> "Matrix":
            return Matrix([self.matrix[0][0] - other.matrix[0][0], self.matrix[0][1] - other.matrix[0][1]],
                          [self.matrix[1][0] - other.matrix[1][0], self.matrix[1][1] - other.matrix[1][1]])
    

    def __str__(self) -> str:
        return f"{self.matrix[0]}\n{self.matrix[1]}"


m1 = Matrix([3, 5], [4, 7])
m2 = Matrix([5, 1], [1, 9])

print(m1 + m2)
print(m1 - m2)