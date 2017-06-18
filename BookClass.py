class Book:

    def book_info(self):
        print(self.name_book, self.name_autor, self.relise_date, self.genre_book)

sita = Book()
sita.name_book = "Sita"
sita.name_autor = "Shekhar Kapur"
sita.relise_date = "29 May 2017"
sita.genre_book = "Adventure"


sita.book_info()
