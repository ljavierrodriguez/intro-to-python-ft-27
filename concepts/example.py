class Libro:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def show_info(self):
        return f"Title: {self.title}, Author: {self.author}, Published:  {self.year}"


class Biblioteca:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    def show_books(self):
        print("Biblioteca: ", self.name)
        print("books:")
        for book in self.books:
            print(book.show_info())
    

libro1 = Libro("Cuando quiero llorar no lloro", "Gabriel Garcia Marquez", 1978)
libro2 = Libro("Doña Barbara", "Romulo Gallegos", 1958)

biblio = Biblioteca("Gran Biblioteca")
biblio.add_books(libro1)
biblio.add_books(libro2)

biblio.show_books()

biblio2 = Biblioteca("Gran Biblioteca 2")
biblio2.add_books(libro1)
biblio2.add_books(libro2)

biblio2.show_books()
