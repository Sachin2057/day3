class Book:
    def __init__(self,title,author,isbn,genere,availability):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.gener=genere
        self.availability=availability
    def __str__(self):
        return f"Name:{self.title}\nAuthor:{self.author}\nIsbn:{self.isbn}\ngenere:{self.gener}"
class LibrayCatatlog:
    def __init__(self):
        self.books=[]
    def get_book_detail(self,isbn_number):
        for i in self.books:
            if(i.isbn==isbn_number):
                return i
        print("Book not found")
        return None
    def add_books(self,book:Book):
        self.books.append(book)    
class BorrowingSystem:
    def __init__(self, catalog):
        self.catalog = catalog
        self.borrowed_books = {}

    def borrow_book(self, isbn, borrower):
        book = self.catalog.get_book_detail(isbn)
        if book is None:
            print("Book not found.")
            return False
        if book.availability:
            book.availability = False
            self.borrowed_books[isbn] = borrower
            print(f"Book '{book.title}' borrowed by {borrower}.")
            return True
        else:
            print(f"Book '{book.title}' is not available for borrowing.")
            return False

    def return_book(self, isbn):
        if isbn in self.borrowed_books:
            book = self.catalog.get_book_by_isbn(isbn)
            book.availability = True
            borrower = self.borrowed_books.pop(isbn)
            print(f"Book '{book.title}' returned by {borrower}.")
            return True
        else:
            print("Book not borrowed.")
            return False
book1=Book("Dance of dragons","George R R Martin",123456,"fantasy",True)
librayCatatlog=LibrayCatatlog()
librayCatatlog.add_books(book1)
borrowingSystem=BorrowingSystem(librayCatatlog)
borrowingSystem.borrow_book(123456,"Sachin")
# print(librayCatatlog.get_book_detail(123456))
                    