class Library:
    def __init__(self, name, books=None):
        if books == None:
            books = [[]]
        self.books = books
        self.name = name
    
    def __add__(self, book):
        if len(self.books[0]) == 0:
            self.books.pop(0)    
        self.books = self.books + book.info
        return self.books 
    
    def __str__(self):
        return (f'{self.books}')

class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
        self.info = [[book.name, book.author, str(book.year)]]
biblio = Library(name="Библиотека МФТИ")
book = Book(
    name="Теоретическая физика. Том 1. Механика",
    author="Ландау Л.Д., Лифшиц Е.М.",
    year=2004
)
book1 = Book(
    name="Теоретическая физика. Том 2. Теория поля",
    author="Ландау Л.Д., Лифшиц Е.М.",
    year=2006
)

biblio = biblio + book1
biblio = biblio + book
print(biblio)

