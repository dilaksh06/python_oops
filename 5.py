class Book:
    def __init__(self):
        self.books = {}  # Dictionary to store book details

    def show_details(self):
        print("\n--- Books Details ---")
        if not self.books:
            print("No books available in the library.")
        else:
            count = 1
            for title, (copies, author) in self.books.items():
                print(f"{count}. Title: {title}, Copies: {copies}, Author: {author}")
                count += 1


class Library(Book):
    def add_book(self, book_details):
        self.books.update(book_details)
        print("\nBooks added successfully!\n")
        self.show_details()

    def borrow_book(self, title):
        if title in self.books:
            if self.books[title][0] > 0:
                self.books[title] = [self.books[title][0] - 1, self.books[title][1]]
                print(f"\nSuccessfully borrowed '{title}'.\n")
            else:
                print(f"Sorry, '{title}' is currently out of stock.")
        else:
            print(f"Book '{title}' not found in the library.")
        self.show_details()

    def return_book(self, title):
        if title in self.books:
            self.books[title] = [self.books[title][0] + 1, self.books[title][1]]
            print(f"\nSuccessfully returned '{title}'.\n")
        else:
            print(f"Book '{title}' not found in the library.")
        self.show_details()


# Main Program
if __name__ == "__main__":
    print("\n", format("*", "*<10"), "Welcome to Library Management System", format("*", "*>10"))

    library = Library()

    # Adding initial books
    initial_books = {"a": [5, "Dilaksha"], "b": [15, "Abi"]}
    library.add_book(initial_books)

    # Menu loop
    while True:
        print("\nOptions:")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Display Books")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            title = input("Enter the title of the book: ")
            copies = int(input("Enter the number of copies: "))
            author = input("Enter the author's name: ")
            library.add_book({title: [copies, author]})

        elif choice == 2:
            title = input("Enter the title of the book: ")
            library.borrow_book(title)

        elif choice == 3:
            title = input("Enter the title of the book: ")
            library.return_book(title)

        elif choice == 4:
            library.show_details()

        elif choice == 5:
            print("Exiting the Library Management System... Goodbye!")
            break

        else:
            print("Invalid choice! Please select from the options above.")
