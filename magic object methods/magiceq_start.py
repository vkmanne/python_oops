# 
# Using the __str__ and __repr__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: the __eq__ method checks for equality between two objects

    # TODO: the __ge__ establishes >= relationship with another obj

    # TODO: the __lt__ establishes < relationship with another obj


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

# TODO: Check for equality
print(b1==b3)

# TODO: Check for greater and lesser value

# books = [b1, b3, b2, b4]
# books.sort()
# TODO: Now we can sort them too
