class Bookshelf:
    def __init__(self,*books):
        self.books=books
    def __str__(self):
        return f"Bookshel with {len(self.books)} books "
class Book:
    def __init__(self,name):
        self.nane=name

    def __str__(self):
        return  f"Book {self.name}"


book1=Book("Harry Potter")
book2=Book("Bob The winner")
shelf=Bookshelf(book1,book2)
print(shelf)

