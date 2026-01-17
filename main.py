class Library:
    """
    Core Library class that manages books and borrowing operations.
    """

    def __init__(self):
        # Store all titles in lowercase
        self.books = {
    "crime and punishment": 2,
    "man's search for meaning": 5,
    "the courage to be disliked": 4,
    "surrounded by idiots": 3,
    "the old man and the sea": 5,

    "the brothers karamazov": 3,
    "white nights": 4,
    "the metamorphosis": 5,
    "atomic habits": 6,
    "the alchemist": 4,
    "thinking fast and slow": 3,
    "meditations": 5,
    "the subtle art of not giving a fck": 4,
    "the kite runner": 3,
    "1984": 4,
    "animal farm": 5,
    "to kill a mockingbird": 3,
    "the great gatsby": 4,
    "the catcher in the rye": 3,
    "notes from underground": 4,
    "beyond good and evil": 3,
    "thus spoke zarathustra": 2,
    "the idiot": 3,
    "the art of public speaking": 4,
    "how to read a person like a book": 4
}

        self.borrowed_books = {}

    # -------- Utility --------
    def _clean_title(self, title):
        return title.strip().lower()

    # -------- Book Management --------
    def add_books(self, title, copies):
        title = self._clean_title(title)

        if not title:
            print("Book title cannot be empty.")
            return

        if copies <= 0:
            print("Copies must be positive.")
            return

        if title in self.books:
            self.books[title] += copies
        else:
            self.books[title] = copies

        print(f"Added {copies} copies of '{title.title()}'.")

    def remove_books(self, title, copies):
        title = self._clean_title(title)

        if not title:
            print("Book title cannot be empty.")
            return

        if copies <= 0:
            print("Copies must be positive.")
            return

        if title not in self.books:
            print(f"'{title.title()}' not found in library.")
            return

        if self.books[title] > copies:
            self.books[title] -= copies
            print(f"Removed {copies} copies of '{title.title()}'.")
        elif self.books[title] == copies:
            del self.books[title]
            print(f"'{title.title()}' removed completely.")
        else:
            print(f"Cannot remove {copies}. Only {self.books[title]} copies available.")

    # -------- Borrow / Return --------
    def borrow_book(self, title, user_name):
        title = self._clean_title(title)

        if not title:
            print("Book title cannot be empty.")
            return

        if title not in self.books or self.books[title] == 0:
            print(f"'{title.title()}' is not available.")
            return

        if user_name in self.borrowed_books:
            print(f"{user_name}, return your current book first.")
            return

        self.books[title] -= 1
        self.borrowed_books[user_name] = title
        print(f"'{title.title()}' borrowed successfully by {user_name}.")
        print("You owe $1 per day for this book.")

    def return_book(self, title, user_name):
        title = self._clean_title(title)

        if user_name not in self.borrowed_books:
            print(f"{user_name}, you have not borrowed any book.")
            return

        if self.borrowed_books[user_name] != title:
            print(f"{user_name}, you can only return '{self.borrowed_books[user_name].title()}'.")
            return

        self.books[title] += 1
        del self.borrowed_books[user_name]
        print(f"'{title.title()}' returned successfully by {user_name}.")

    # -------- Search / View --------
    def search_book(self, title):
        title = self._clean_title(title)

        if not title:
            print("Book title cannot be empty.")
            return

        if title in self.books:
            print(f"'{title.title()}' is available with {self.books[title]} copies.")
        else:
            print(f"'{title.title()}' is not available.")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\nAvailable Books:")
        for title, copies in self.books.items():
            print(f"{title.title()} : {copies} copies")

    def view_borrowed_books(self):
        if not self.borrowed_books:
            print("No borrowed books.")
            return

        print("\nBorrowed Books:")
        for user, book in self.borrowed_books.items():
            print(f"{user} -> {book.title()}")


# ----------------------------------------------------


class LibraryManagementSystem:
    """
    Handles menus and user interaction.
    """

    ADMIN_PASSWORD = "admin123"

    def __init__(self):
        self.library = Library()

    # Safe integer input
    def _get_positive_int(self, message):
        try:
            value = int(input(message))
            if value <= 0:
                print("Enter a positive number.")
                return None
            return value
        except ValueError:
            print("Invalid number input.")
            return None

    # -------- Admin Menu --------
    def admin_menu(self):
        while True:
            choice = input(
                "\nAdmin Menu:\n"
                "1. Add Books\n"
                "2. Remove Books\n"
                "3. View Books\n"
                "4. Search Book\n"
                "5. View Borrowed Books\n"
                "6. Exit\n"
                "Choice: "
            )

            if choice == "1":
                title = input("Enter book title: ")
                copies = self._get_positive_int("Enter number of copies: ")
                if copies:
                    self.library.add_books(title, copies)

            elif choice == "2":
                title = input("Enter book title: ")
                copies = self._get_positive_int("Enter number of copies: ")
                if copies:
                    self.library.remove_books(title, copies)

            elif choice == "3":
                self.library.view_books()

            elif choice == "4":
                title = input("Enter book title to search: ")
                self.library.search_book(title)

            elif choice == "5":
                self.library.view_borrowed_books()

            elif choice == "6":
                break

            else:
                print("Invalid choice. Try again.")

    # -------- User Menu --------
    def user_menu(self, user_name):
        while True:
            choice = input(
                f"\nUser Menu ({user_name}):\n"
                "1. Borrow Book\n"
                "2. Return Book\n"
                "3. Search Book\n"
                "4. View Books\n"
                "5. Exit\n"
                "Choice: "
            )

            if choice == "1":
                title = input("Enter book title to borrow: ")
                self.library.borrow_book(title, user_name)

            elif choice == "2":
                title = input("Enter book title to return: ")
                self.library.return_book(title, user_name)

            elif choice == "3":
                title = input("Enter book title to search: ")
                self.library.search_book(title)

            elif choice == "4":
                self.library.view_books()

            elif choice == "5":
                break

            else:
                print("Invalid choice. Try again.")

    # -------- Login --------
    def login(self):
        while True:
            choice = input(
                "\nLibrary System:\n"
                "1. Admin Login\n"
                "2. User Login\n"
                "3. Exit\n"
                "Choice: "
            )

            if choice == "1":
                password = input("Enter admin password: ")
                if password == self.ADMIN_PASSWORD:
                    self.admin_menu()
                else:
                    print("Wrong password.")

            elif choice == "2":
                user_name = input("Enter your name: ").strip()
                if not user_name:
                    print("Name cannot be empty.")
                else:
                    self.user_menu(user_name)

            elif choice == "3":
                print("Exiting Library System...")
                break

            else:
                print("Invalid choice.")


# -------- Program Entry Point --------
if __name__ == "__main__":
    LibraryManagementSystem().login()
