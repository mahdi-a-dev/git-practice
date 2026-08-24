class PrintInfoMixin:
    def print_info(self):
        print(f"{self.__class__.__name__}\n{dir(self)}")


class Book(PrintInfoMixin):
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title = title
        self.author = author
        self.year = year


c = Book("one ", "marcez", 1455)
c.print_info()