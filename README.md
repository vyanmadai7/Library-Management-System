# Library Management System

A Python based command line program for managing library operations including book inventory, borrowing, and returns.

----------FEATURES----------

### For Administrators
- Add new books or increase existing book copies
- Remove books from the inventory
- View all available books
- Search for specific books
- Track borrowed books and their borrowers

### For Users
- Borrow books from the library
- Return borrowed books
- Search for book availability
- View the complete book catalog

## Installation

```bash
git clone https://github.com/vyanmadai7/Library-Management-System.git
cd Library-Management-System
```

**Requirements:** Python 3.8 or higher

## Usage

### Admin Login
- Select option 1 from the main menu
- Enter password: `admin123`
- Access admin features

### User Login
- Select option 2 from the main menu
- Enter your name
- Start borrowing or returning books

### Example

```
Library System:
1. Admin Login
2. User Login
3. Exit
Choice: 2

Enter your name: Sarah

User Menu (Sarah):
1. Borrow Book
2. Return Book
3. Search Book
4. View Books
5. Exit
Choice: 1

Enter book title to borrow: The Old Man and the Sea
'The Old Man And The Sea' borrowed successfully by Sarah.
You owe $1 per day for this book.
```

## How It Works

### Borrowing Rules
- Each user can borrow only one book at a time
- Books must be returned before borrowing another
- A daily fee of $1 applies to borrowed books

### Book Management
- Book titles are matched regardless of uppercase or lowercase
- The system prevents invalid operations like removing more books than available
- Admins can track who has borrowed which books

## Default Books

The library starts with these books:

- Crime and Punishment - 2 copies
- Man's Search for Meaning - 5 copies
- The Courage to be Disliked - 4 copies
- Surrounded by Idiots - 3 copies
- The Old Man and the Sea - 5 copies


## Future Improvements

- Add database support for data persistence
- Implement user accounts with secure passwords
- Add due dates and automatic fine calculation
- Create a web interface
- Add book categories and authors
- Generate reports and statistics

## Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

## License

This project is open source and available under the MIT License.

## Notes

This is an educational project demonstrating basic Python programming concepts including object-oriented programming, user input handling, and data management. The default admin password should be changed for any real-world use.

---

Made with Python 🐍
