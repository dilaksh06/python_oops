# Class: Book
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def show_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Copies: {self.copies}")


# Class: Library
class Library:
    def __init__(self):
        self.books = []  # List to store book objects

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title} by {book.author} with {book.copies} copies.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.copies > 0:
                    book.copies -= 1
                    print(f"Successfully borrowed '{book.title}'.")
                else:
                    print(f"Sorry, '{book.title}' is out of stock.")
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.copies += 1
                print(f"Successfully returned '{book.title}'.")
                return
        print(f"Book '{title}' not found in the library.")

    def list_books(self):
        print("\n--- Available Books ---")
        if not self.books:
            print("No books available in the library.")
        for book in self.books:
            book.show_details()


# Main Program
if __name__ == "__main__":
    # Create a Library instance
    library = Library()

    # Create some Book objects
    book1 = Book("Python Basics", "John Doe", 5)
    book2 = Book("Advanced Python", "Jane Smith", 2)
    book3 = Book("Data Science 101", "Alice Brown", 3)

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # List all books
    library.list_books()

    # Borrow a book
    library.borrow_book("Python Basics")

    # List books after borrowing
    library.list_books()

    # Return a book
    library.return_book("Python Basics")

    # List books after returning
    library.list_books()

    # Attempt to borrow a book not in the library
    library.borrow_book("Nonexistent Book")

    # Attempt to return a book not in the library
    library.return_book("Nonexistent Book")
