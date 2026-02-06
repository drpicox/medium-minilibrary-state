```
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║                    MINI LIBRARY MANAGER v1.0                               ║
║                  An MS-DOS Style Database Application                      ║
║                                                                            ║
║         "RETRO Computing Meets Modern Python for Book Management"          ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
```

## About This Project

**Mini Library Manager** is a nostalgic emulator of classic MS-DOS-era database programs (think dBASE, circa 1980s). It lets you manage your personal book collection with a simple, text-based interface reminiscent of the golden age of computing.

The application demonstrates fundamental **CRUD operations** (Create, Read, Update, Delete) in an authenically retro style, with menu-driven navigation and persistent JSON storage.

---

## Features

✨ **Menu-Driven Interface** - Navigate through options just like vintage MS-DOS programs  
📚 **Book Management** - Add, view, edit, and delete books from your library  
📝 **Three Essential Fields** - Track book Title, Author, and whom you lent it to  
💾 **Persistent Storage** - Your library is saved in JSON format  
🎨 **Retro Aesthetics** - All the charm of 1980s computing without the floppy disks

---

## Installation

### Requirements

- Python 3.6 or higher
- Unix-like system (macOS, Linux) or Windows with command-line access

### Setup

1. **Clone or download the repository:**

   ```bash
   git clone <repository-url>
   cd msdos
   ```

2. **Run the program:**
   ```bash
   python3 main.py
   ```

That's it! No dependencies to install. Simple and clean.

---

## Usage Guide

### Main Menu

When you launch the program, you'll see:

```
============================================================
                 MINI LIBRARY MANAGER v1.0
============================================================

1. List Books
2. Add New Book
3. Edit Book
0. Exit

============================================================
>>> Select an option:
```

### Operation 1: List Books

View all your books at a glance:

```
============================================================
LIBRARY CONTENTS:
============================================================
  [1] The Hobbit                     - J.R.R. Tolkien (Lent to: John)
  [2] 1984                           - George Orwell (Not lent)
  [3] The Fellowship of the Ring     - J.R.R. Tolkien (Lent to: Bookshelf 1)
============================================================
```

### Operation 2: Add New Book

Add a new book to your collection:

```
============================================================
ADD NEW BOOK
============================================================
>>> Title: The Name of the Wind
>>> Author: Patrick Rothfuss
>>> Lent To (leave empty if not lent): [LEAVE BLANK]

>>> Book 'The Name of the Wind' added successfully.
```

**Interactive prompts:**

- **Title** - The book's title (required)
- **Author** - The author's name (required)
- **Lent To** - Who has borrowed it, or leave blank if it's in your collection

### Operation 3: Edit Book

Select a book and modify its details:

```
============================================================
LIBRARY CONTENTS:
>>> Enter book number to edit (0 to cancel): 1

BOOK #1
============================================================
Title:     The Hobbit
Author:    J.R.R. Tolkien
Lent To:   John
============================================================

EDIT MENU:
============================================================
1. View Book
2. Edit Title
3. Edit Author
4. Edit Lent To
5. Delete Book
0. Back to List

============================================================
>>> Choose an option: 4
>>> Lent To (leave empty if not lent): [LEAVE BLANK]
>>> Book marked as not lent.
```

**Edit Options:**

1. **View Book** - Display current book details
2. **Edit Title** - Change the book's title
3. **Edit Author** - Change the author's name
4. **Edit Lent To** - Update lending status (or mark as not lent)
5. **Delete Book** - Permanently remove the book (with confirmation)
6. **Back to List** - Return to main menu

---

## Data Storage

Your library is automatically saved in `books.json`. Here's an example:

```json
[
  {
    "id": 1,
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "lent_to": "John",
    "created_at": "2026-02-06T22:34:34.857548"
  },
  {
    "id": 2,
    "title": "1984",
    "author": "George Orwell",
    "lent_to": "",
    "created_at": "2026-02-06T22:35:12.123456"
  }
]
```

**No automatic saves needed!** Changes are persisted immediately when you modify data.

---

## Technical Details

### Project Structure

```
msdos/
├── main.py          # Main application (single file, easy to run)
├── books.json       # Your library data (auto-created on first run)
├── README.md        # This file
└── .git/            # Git repository data
```

### Architecture

The application is built with simplicity in mind:

- **Single-file Python app** - No complex class hierarchies or frameworks
- **Functional design** - Clear, readable functions for each operation
- **JSON storage** - Human-readable data format you can inspect anytime
- **MS-DOS UX** - Text-based menus with minimal graphics

### Key Functions

| Function              | Purpose                         |
| --------------------- | ------------------------------- |
| `load_books()`        | Load library from JSON          |
| `save_books()`        | Persist changes to disk         |
| `display_main_menu()` | Show main menu interface        |
| `list_books()`        | Display all books               |
| `add_book()`          | Create new book entry           |
| `edit_book()`         | Modify book details             |
| `edit_book_menu()`    | Edit menu for single book       |
| `clear_screen()`      | Clear terminal (cross-platform) |

---

## Tips & Tricks

💡 **Organizing Your Library**  
Use the "Lent To" field creatively:

- `Bookshelf 1`, `Bookshelf 2` - Physical locations
- `John`, `Maria` - People who borrowed them
- `Being read` - Currently reading
- `Office` - Books you keep at work

💡 **Backing Up Your Library**  
Just copy `books.json` to another location. It's plain text!

💡 **Exporting Your Library**  
The JSON file can be opened in any text editor or imported into other programs.

---

## Development Notes

### Why Python?

- **Cross-platform** - Runs on Windows, macOS, Linux
- **Simple syntax** - Easy to understand and modify
- **Built-in JSON** - No dependency hell
- **Batteries included** - Everything you need in the standard library

### Retro Design Philosophy

This project intentionally mimics 1980s database programs to:

- Demonstrate fundamental CRUD operations
- Show that simplicity can be elegant
- Remind us that you don't need frameworks for small, focused applications
- Have fun with computing history!

---

## Future Enhancements (If You Wanted More)

These features could be added without losing the retro charm:

- 📅 **Date borrowed/returned tracking**
- ⭐ **Personal ratings for books**
- 🔍 **Search functionality**
- 📊 **Statistics** (total books, borrowed, etc.)
- 🎯 **Status flags** (wishlist, read, unread, etc.)

But for now, we keep it simple and authentic.

---

## License

This project is free to use and modify. Do with it as you please!

---

## Author's Note

> "Sometimes the best software is the simplest software. This project proves that you can build something useful and charming using only fundamental programming concepts and a healthy respect for retro aesthetics."

---

**Enjoy your retro library experience! 📚**

```
════════════════════════════════════════════════════════════════════════════════
                         MINI LIBRARY MANAGER v1.0
                    Made with ❤️  and a love for computing history
════════════════════════════════════════════════════════════════════════════════
```
