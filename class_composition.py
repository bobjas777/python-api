class Bookshelf:
    def __init__(self,*books):
        self.books=books
    def __str__(self):
        return f"Bookshel with {len(self.books)} books "
class Book:
    def __init__(self,namequantity):


shelf=Bookshelf(300)
print(shelf)


