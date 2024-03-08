import json
import datetime

# Base class representing an item in the library
class Item:
    def __init__(self, title):
        self.title = title

    # Method to display details of the item
    def display_details(self):
        print("Title:", self.title)

# Class representing a book, inheriting from Item
class Book(Item):
    def __init__(self, title, author, isbn, quantity):
        super().__init__(title)
        self.author = author
        self.isbn = isbn
        self.quantity = quantity

    # Method to display details of the book
    def display_details(self):
        super().display_details()
        print("Author:", self.author)
        print("ISBN:", self.isbn)
        print("Quantity:", self.quantity)

# Class representing a patron, inheriting from Item
class Patron(Item):
    def __init__(self, title, patron_id, contact_info):
        super().__init__(title)
        self.patron_id = patron_id
        self.contact_info = contact_info

    # Method to display details of the patron
    def display_details(self):
        super().display_details()
        print("Patron ID:", self.patron_id)
        print("Contact Information:", self.contact_info)

# Base class representing an action in the library (e.g., checkout, checkin)
class Action:
    def __init__(self, item, patron):
        self.item = item
        self.patron = patron
        self.date = datetime.date.today()

# Class representing a transaction (e.g., checkout), inheriting from Action
class Transaction(Action):
    def __init__(self, item, patron, checkout=False):
        super().__init__(item, patron)
        self.checkout = checkout
        if self.checkout:
            self.due_date = self.date + datetime.timedelta(days=14)  # Default 14 days checkout period

    # Method to check in a book
    def check_in(self):
        self.return_date = datetime.date.today()

# Class representing the library
class Library:
    def __init__(self):
        self.books = []         # List to store books
        self.patrons = []       # List to store patrons
        self.transactions = []  # List to store transactions

    # Method to add an item (book or patron) to the library
    def add_item(self, item):
        if isinstance(item, Book):
            self.books.append(item)
        elif isinstance(item, Patron):
            self.patrons.append(item)

    # Method to remove an item from the library
    def remove_item(self, item):
        if isinstance(item, Book):
            self.books.remove(item)
        elif isinstance(item, Patron):
            self.patrons.remove(item)

    # Method to checkout a book to a patron
    def checkout_item(self, item, patron):
        if isinstance(item, Book) and item.quantity > 0:
            transaction = Transaction(item, patron, checkout=True)
            self.transactions.append(transaction)
            item.quantity -= 1
            return transaction
        else:
            return None

    # Method to check in a book
    def checkin_item(self, transaction):
        transaction.check_in()
        transaction.item.quantity += 1

    # Method to search items (books or patrons) by title
    def search_items(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        found_patrons = [patron for patron in self.patrons if title.lower() in patron.title.lower()]
        return found_books + found_patrons

    # Method to generate a report of books and patrons in the library
    def generate_report(self):
        print("Books in Library:")
        for book in self.books:
            book.display_details()
            print()

        print("\nPatrons in Library:")
        for patron in self.patrons:
            patron.display_details()
            print()

# Function to load data from a file by using Json
def load_data():
    try:
        with open("library_data.json", "r") as file:
            data = json.load(file)
        return data["books"], data["patrons"], data["transactions"]
    except FileNotFoundError:
        return [], [], []

# Function to save data to a file
def save_data(books, patrons, transactions):
    data = {"books": books, "patrons": patrons, "transactions": transactions}
    with open("library_data.json", "w") as file:
        json.dump(data, file)

# Main function to run the library management system
def main():
    # Load data from file
    books, patrons, transactions = load_data()
    library = Library()
    library.books = [Book(**book) for book in books]
    library.patrons = [Patron(**patron) for patron in patrons]
    # Rest of the code is for the CLI, which display the main functionality of the program
    # Perform actions based on user choice
    while True:
        print("\n1. Add Book")
        print("2. Remove Book")
        print("3. Add Patron")
        print("4. Remove Patron")
        print("5. Checkout Book")
        print("6. Checkin Book")
        print("7. Search Items")
        print("8. Generate Report")
        print("9. Exit")
        # Get user input for choice
        choice = input("Enter your choice: ")

        if choice == "1":
            # Implementation of adding a book
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            quantity = int(input("Enter quantity: "))
            book = Book(title, author, isbn, quantity)
            library.add_item(book)
        elif choice == "2":
            # Implementation of removing a book
            title = input("Enter title of book to remove: ")
            items = library.search_items(title)
            if items:
                for i, item in enumerate(items):
                    print(f"{i+1}. {item.title}")
                index = int(input("Enter index of item to remove: ")) - 1
                library.remove_item(items[index])
            else:
                print("Item not found.")
        elif choice == "3":
            # Implementation of add a patron
            title = input("Enter patron name: ")
            patron_id = input("Enter patron ID: ")
            contact_info = input("Enter contact information: ")
            patron = Patron(title, patron_id, contact_info)
            library.add_item(patron)
        elif choice == "4":
            # Implementation of remove a patron

            patron_id = input("Enter patron ID to remove: ")
            items = [patron for patron in library.patrons if patron.patron_id == patron_id]
            if items:
                library.remove_item(items[0])
                print("The patron has being removed")
            else:
                print("Patron not found.")
        elif choice == "5":
            # Implementation of checking out books
            title = input("Enter title of book to checkout: ")
            items = library.search_items(title)
            if items:
                for i, item in enumerate(items):
                    print(f"{i+1}. {item.title}")
                index = int(input("Enter index of item to checkout: ")) - 1
                title = input("Enter patron ID: ")
                patrons = [patron for patron in library.patrons if patron.patron_id == title]
                if patrons:
                    transaction = library.checkout_item(items[index], patrons[0])
                    if transaction:
                        print("Book checked out successfully.")
                    else:
                        print("Book out of stock.")
                else:
                    print("Patron not found.")
            else:
                print("Book not found.")
        elif choice == "6":
            # Implementation of checking in books
            print("Checked-out Books:")
            for i, transaction in enumerate(library.transactions):
                if not hasattr(transaction, 'return_date'):
                    print(f"{i+1}. {transaction.item.title} by {transaction.item.author} (Due Date: {transaction.due_date})")
            if library.transactions:
                index = int(input("Enter index of book to check in: ")) - 1
                if 0 <= index < len(library.transactions):
                    transaction = library.transactions[index]
                    library.checkin_item(transaction)
                    print("Book checked in successfully.")
                else:
                    print("Invalid index.")
            else:
                print("No books checked out.")
        elif choice == "7":
            # Implementation of search a book
            title = input("Enter title to search: ")
            found_items = library.search_items(title)
            if found_items:
                for i, item in enumerate(found_items):
                    print(f"{i+1}. {item.title}")
            else:
                print("No book found.")
        elif choice == "8":
            # Implementation of display the details of itle,
            # author (for books), ISBN (for books), quantity (for books), patron name, patron ID,
            # and contact information (for patrons).
            library.generate_report()
        elif choice == "9":
            save_data([vars(book) for book in library.books], [vars(patron) for patron in library.patrons], [])
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
