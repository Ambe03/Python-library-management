import mysql
import mysql.connector

# Database connection details (replace with your own)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ambe",
    database="library"
)
mycursor = mydb.cursor()

# Library data structure (consider using a dictionary for efficiency)
library = []

def main_menu():
    """Displays the main menu and handles user input."""
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Books")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice not in ('1', '2', '3', '4', '5', '6'):
        print("Invalid choice. Please try again.")
        return

    if choice == '1':
        add_book()
    elif choice == '2':
        view_books()
    elif choice == '3':
        search_books()
    elif choice == '4':
        borrow_book()
    elif choice == '5':
        return_book()
    else:
        print("Exiting the library management system.")

def add_book():
    """book details and adds book to library."""
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    is_available = True  # Track availability (optional, can be a separate field)

    # Data validation (consider using regular expressions for robust validation)
    if not title or not author:
        print("Please enter both book title and author.")
        return

    print(f"Book '{title}' by {author} added successfully!")

def view_books():
    """Displays all books in the library."""
    if not library:
        print("There are no books in the library yet.")
        return

    print("\nList of Books:")
    for i, book in enumerate(library):
        title, author, is_available = book
        availability = "Available" if is_available else "Borrowed"
        print(f"{i+1}. {title} by {author} ({availability})")

def search_books():
    """Searches for books by title or author."""
    search_term = input("Enter book title or author to search: ")

    found_books = []
    for book in library:
        title, author, _ = book
        if search_term.lower() in title.lower() or search_term.lower() in author.lower():
            found_books.append(book)

    if not found_books:
        print(f"No books found matching '{search_term}'.")
        return

    print("\nSearch results:")
    for i, book in enumerate(found_books):
        title, author, _ = book
        print(f"{i+1}. {title} by {author}")

def borrow_book():
    """Allows borrowing a book if available."""
    if not library:
        print("There are no books available to borrow.")
        return

    view_books()  # Display available books

    choice = input("Enter the number of the book you want to borrow: ")
    try:
        index = int(choice) - 1
        if index < 0 or index >= len(library):
            print("Invalid book number. Please try again.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    book = library[index]
    title, author, is_available = book

    if not is_available:
        print(f"Sorry, '{title}' is not available for borrowing at this time.")
        return

    # Update availability (optional)
    library[index] = (title, author, False)

    print(f"Book '{title}' by {author} borrowed successfully!")

def return_book():
    """Allows returning a borrowed book."""
    if not library:
        print("There are no books borrowed currently.")
        return

    view_books()  # Display all books (including borrowed ones)

    choice = input("Enter the number of the book you want to return: ")


    try:
        index = int(choice) - 1
        if index < 0 or index >= len(library):
            print("Invalid book number. Please try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")
        return

main_menu()
