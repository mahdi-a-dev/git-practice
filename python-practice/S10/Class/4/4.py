class Book:
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title = title
        self.author = author
        self.year = year

    def info(self) -> None:
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")

def main():
    book = Book("one hundred years of solitude", "gabriel garcia marquez", "1982")
    book.info()


if __name__ == "__main__":
    main()