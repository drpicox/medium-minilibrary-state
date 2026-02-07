#!/usr/bin/env python3
"""
MS-DOS Style Mini Library Manager
Emulator of ancient MS-DOS program with mini library management
Manage books: Title, Author, Lent To
"""

import json
import os
import platform
from datetime import datetime

BOOKS_FILE = "books.json"

"""
-----------------------------------------------------------
Main menu
-----------------------------------------------------------
"""

def main_menu():
    """Main program loop"""
    clear_screen()
    print("\n>>> Loading Mini Library Manager...\n")

    while True:
        books = load_books()
        clear_screen()
        print("\n" + "=" * 60)
        print("                 MINI LIBRARY MANAGER v1.0")
        print("=" * 60)
        print("\n1. List Books")
        print("2. Add New Book")
        print("3. Edit Book")
        print("4. Delete Book")
        print("0. Exit\n")
        print("=" * 60)

        choice = input(">>> Select an option: ").strip()

        if choice == "1":
            list_books(books)
        elif choice == "2":
            add_book(books)
        elif choice == "3":
            edit_book(books)
        elif choice == "4":
            delete_book(books)
        elif choice == "0":
            clear_screen()
            print("\n>>> Thank you for using Mini Library Manager. Goodbye!\n")
            break
        else:
            print(">>> ERROR: Invalid option. Please enter 0-4.\n")
            pause()

def display_main_menu():
    """Display main menu MS-DOS retro style"""

"""
-----------------------------------------------------------
1. List books
-----------------------------------------------------------
"""

def list_books(books):
    """Display all books in list format"""
    if not books:
        print("\n>>> No books in library.\n")
        return None

    clear_screen()
    print("-" * 62)
    print(f"{'ID':<2} | {'Title':<30} | {'Author':<20} | {'S':<1}")
    print("-" * 62)
    for idx, book in enumerate(books, 1):
        title = book['title'][:30].ljust(30)
        author = book['author'][:20].ljust(20)
        status = "L" if book.get("lent_to", "").strip() else " "
        print(f"{idx:<2} | {title} | {author} | {status}")
    print("-" * 62 + "\n")

    pause()

    return True


"""
-----------------------------------------------------------
2. Add new book
-----------------------------------------------------------
"""

def add_book(books):
    """Add a new book to the library"""
    clear_screen()
    print("\n" + "-" * 60)
    print("ADD NEW BOOK")
    print("-" * 60)

    title = input(">>> Title: ").strip()
    if not title:
        print(">>> ERROR: Title cannot be empty.\n")
        return

    author = input(">>> Author: ").strip()
    if not author:
        print(">>> ERROR: Author cannot be empty.\n")
        return

    lent_to = input(">>> Lent To (leave empty if not lent): ").strip()

    new_book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "lent_to": lent_to,
        "created_at": datetime.now().isoformat()
    }

    books.append(new_book)
    save_books(books)
    print(f"\n>>> Book '{title}' added successfully.\n")


"""
-----------------------------------------------------------
3. Edit book details
-----------------------------------------------------------
"""

def edit_book(books):
    """Edit menu for a selected book"""
    book_num = choose_book(books)

    if book_num is None:
        print(">>> Operation cancelled.\n")
        input(">>> Press ENTER to continue...")
        return

    idx = book_num - 1
    book = books[idx]

    while True:
        clear_screen()
        print("EDIT MENU:")
        print("-" * 60)
        print("1. View Book")
        print("2. Edit Title")
        print("3. Edit Author")
        print("4. Edit Lent To")
        print("0. Back to List\n")
        print("-" * 60)

        choice = input(">>> Choose an option: ").strip()

        if choice == "1":
            view_book(book, book_num)
        elif choice == "2":
            edit_title(book)
        elif choice == "3":
            edit_author(book)
        elif choice == "4":
            edit_lent_to(book)
        elif choice == "0":
            save_books(books)
            return
        else:
            print(">>> ERROR: Invalid option. Please enter 0-4.\n")

        input(">>> Press ENTER to continue...")

def view_book(book, book_num):
    """Display detailed information about a book"""
    print("\n" + "-" * 60)
    print(f"BOOK #{book_num}")
    print("-" * 60)
    print(f"Title:     {book['title']}")
    print(f"Author:    {book['author']}")
    lent_to = book.get("lent_to", "").strip()
    print(f"Lent To:   {lent_to if lent_to else '(Not lent)'}")
    print("-" * 60 + "\n")


def edit_title(book):
    """Edit a book's title"""
    new_title = input(">>> New Title: ").strip()
    if new_title:
        book["title"] = new_title
        print(">>> Title updated successfully.\n")
    else:
        print(">>> ERROR: Title cannot be empty.\n")


def edit_author(book):
    """Edit a book's author"""
    new_author = input(">>> New Author: ").strip()
    if new_author:
        book["author"] = new_author
        print(">>> Author updated successfully.\n")
    else:
        print(">>> ERROR: Author cannot be empty.\n")


def edit_lent_to(book):
    """Edit a book's lent status"""
    new_lent_to = input(">>> Lent To (leave empty if not lent): ").strip()
    book["lent_to"] = new_lent_to
    if new_lent_to:
        print(f">>> Book marked as lent to '{new_lent_to}'.\n")
    else:
        print(">>> Book marked as not lent.\n")



"""
-----------------------------------------------------------
4. Delete a book
-----------------------------------------------------------
"""

def delete_book(books):
    """Select and delete a book"""
    book_num = choose_book(books)
    
    if book_num is None:
        print(">>> Operation cancelled.\n")
        input(">>> Press ENTER to continue...")
        return
    
    idx = book_num - 1
    book_title = books[idx]["title"]
    
    confirm = input(f">>> Are you sure you want to delete '{book_title}'? (Y/N): ").strip().upper()
    if confirm == "Y":
        books.pop(idx)
        save_books(books)
        clear_screen()
        print(f"\n>>> Book '{book_title}' deleted successfully.\n")
        input(">>> Press ENTER to continue...")
    else:
        print(">>> Deletion cancelled.\n")
        input(">>> Press ENTER to continue...")

"""
-----------------------------------------------------------
Book selection utility function
-----------------------------------------------------------
"""

def choose_book(books):
    """Let user choose one book from the list, returns book number or None if 0 selected"""
    try:
        choice = input(">>> Enter book number (0 to select none): ").strip()

        if choice == "0":
            return None

        book_num = int(choice)
        idx = book_num - 1

        if 0 <= idx < len(books):
            return book_num
        else:
            print(">>> ERROR: Invalid book number.\n")
            return None
    except ValueError:
        print(">>> ERROR: Please enter a valid number.\n")
        return None


"""
-----------------------------------------------------------
Utility functions for MS-DOS style mini library manager
-----------------------------------------------------------
"""

def clear_screen():
    """Clear terminal screen MS-DOS style"""
    os.system("cls" if platform.system() == "Windows" else "clear")

def pause():
    """Pause execution until user presses ENTER"""
    input(">>> Press ENTER to continue...")

"""
-----------------------------------------------------------
Persistence functions to load and save books from JSON file
-----------------------------------------------------------
"""

def load_books():
    """Load books from JSON file, return empty list if file doesn't exist"""
    if os.path.exists(BOOKS_FILE):
        try:
            with open(BOOKS_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []


def save_books(books):
    """Save books to JSON file"""
    with open(BOOKS_FILE, "w") as f:
        json.dump(books, f, indent=2, ensure_ascii=False)

"""
-----------------------------------------------------------
Start of the program
-----------------------------------------------------------
"""

if __name__ == "__main__":
    main_menu()
