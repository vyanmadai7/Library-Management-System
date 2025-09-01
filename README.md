# Library Management System
# --------------------------
# A simple Python program to manage a library.
# Features:
#   - Add and remove books
#   - Borrow and return books
#   - Search for books
#   - View all books
#   - Separate admin and user menus
#
# Admin password (default): admin123

class Library:
    def __init__(self):
        # Dictionary to store books -> available copies
        self.books = {
            "crime and punishment": 2,
            "man's search for meaning": 5,
            "the courage to be disliked": 4,
            "surrounded by idiots": 3,
            "the old man and the sea": 6,
            "the alchemist": 7,
            "the kite runner": 4,
            "thinking, fast and slow": 5,
            "the metamorphosis": 3,
            "atomic habits": 8,
            "the subtle art of not giving a f*ck": 6,
            "meditations": 5,
            "the art of seduction": 2,
            "white nights": 4,
            "dark psychology secrets": 3
        }
        self.borrowed_books = {}

    def add_books(self, title, copies):
        # Add new books
        title = title.lower()
        if title in self.books:
            self.books[title] += copies
        else:
            self.books[title] = copies
        print(f"✅ Added {copies} copies of '{title.title()}'.")

    def remove_books(self, title, copies):
        # Remove books 
        title = title.lower()
        if title in self.books:
            if self.books[title] > copies:
                self.books[title] -= copies
                print(f"🗑 Removed {copies} copies of '{title.title()}'.")
            elif self.books[title] == copies:
                del self.books[title]
                print(f"🗑 '{title.title()}' removed completely.")
            else:
                print(f"⚠ Cannot remove {copies} copies. Only {self.books[title]} copies available.")
        else:
            print(f"❌ '{title.title()}' not found in the library.")

    def borrow_book(self, title, user_name):
        # Borrow a book if it's available
        title = title.lower()
        if title in self.books and self.books[title] > 0:
            if user_name in self.borrowed_books:
                print(f"⚠ Sorry {user_name}, you already borrowed '{self.borrowed_books[user_name].title()}'. Return it before borrowing another.")
            else:
                self.books[title] -= 1
                self.borrowed_books[user_name] = title
                print(f"📖 '{title.title()}' borrowed successfully by {user_name}. You owe $0.50/day for this book.")
        else:
            print(f"❌ '{title.title()}' is not available.")

    def return_book(self, title, user_name):
        # Return a borrowed book
        title = title.lower()
        if user_name not in self.borrowed_books:
            print(f"⚠ {user_name}, you haven't borrowed any book yet.")
        elif self.borrowed_books[user_name] != title:
            print(f"⚠ Sorry {user_name}, you borrowed '{self.borrowed_books[user_name].title()}'. You must return that specific book.")
        else:
            self.books[title] += 1
            del self.borrowed_books[user_name]
            print(f"✅ '{title.title()}' returned successfully by {user_name}.")

    def search_book(self, title):
        # Search for a book and display available copies
        title = title.lower()
        if title in self.books:
            print(f"🔎 '{title.title()}' is available with {self.books[title]} copies.")
        else:
            print(f"❌ '{title.title()}' is not available.")

    def view_books(self):
        # Display all available books with copies
        if self.books:
            print("\n📚 Available books:")
            for title, copies in self.books.items():
                print(f"   • {title.title()} : {copies} copies")
        else:
            print("⚠ No books available.")


class LibraryManagementSystem:
    def __init__(self):
        # Initialize the library system
        self.library = Library()

    def admin_menu(self):
        # Menu options for admin
        while (choice := input("\n--- Admin Menu ---\n1. Add books\n2. Remove books\n3. View books\n4. Search books\n5. Logout\nChoice: ")) != "5":
            if choice == '1':
                title = input("Enter book title to add: ")
                copies = int(input("Enter number of copies: "))
                self.library.add_books(title, copies)
            elif choice == '2':
                title = input("Enter book title to remove: ")
                copies = int(input("Enter number of copies to remove: "))
                self.library.remove_books(title, copies)
            elif choice == '3':
                self.library.view_books()
            elif choice == '4':
                title = input("Enter book title to search: ")
                self.library.search_book(title)
            else:
                print("⚠ Invalid input, try again.")

    def user_menu(self, user_name):
        # Menu options for users
        while (choice := input(f"\n--- User Menu ({user_name}) ---\n1. Borrow book\n2. Return book\n3. View books\n4. Search books\n5. Logout\nChoice: ")) != "5":
            if choice == '1':
                title = input("Enter book title to borrow: ")
                self.library.borrow_book(title, user_name)
            elif choice == '2':
                title = input("Enter book title to return: ")
                self.library.return_book(title, user_name)
            elif choice == '3':
                self.library.view_books()
            elif choice == '4':
                title = input("Enter book title to search: ")
                self.library.search_book(title)
            else:
                print("⚠ Invalid input, try again.")

    def login(self):
        # Login system for both admin and users
        while (choice := input("\n=== Library Management System ===\n1. Admin Login\n2. User Login\n3. Exit\nChoice: ")) != '3':
            if choice == '1' and input("Enter admin password: ") == "admin123":
                self.admin_menu()
            elif choice == '2':
                user_name = input("Enter your name: ")
                self.user_menu(user_name)
            else:
                print("⚠ Invalid choice or incorrect password.")


if __name__ == "__main__":
    # Start the system
    LibraryManagementSystem().login()
