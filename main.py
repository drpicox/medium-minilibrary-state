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


def clear_screen():
    """Clear terminal screen MS-DOS style"""
    os.system("cls" if platform.system() == "Windows" else "clear")


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


def display_main_menu():
    """Display main menu MS-DOS retro style"""
    print("\n" + "=" * 60)
    print("                 MINI LIBRARY MANAGER v1.0")
    print("=" * 60)
    print("\n1. List Books")
    print("2. Add New Book")
    print("3. Edit Book")
    print("0. Exit\n")
    print("=" * 60)


def list_books(books):
    """Display all books in list format"""
    if not books:
        print("\n>>> No books in library.\n")
        return None

    print("\n" + "-" * 60)
    print("LIBRARY CONTENTS:")
    print("-" * 60)
    for idx, book in enumerate(books, 1):
        lent_status = f" (Lent to: {book['lent_to']})" if book.get("lent_to", "").strip() else ""
        print(f"  [{idx}] {book['title']:<30} - {book['author']}{lent_status}")
    print("-" * 60 + "\n")

    return True


def display_book_details(book, book_num):
    """Display detailed information about a book"""
    print("\n" + "-" * 60)
    print(f"BOOK #{book_num}")
    print("-" * 60)
    print(f"Title:     {book['title']}")
    print(f"Author:    {book['author']}")
    lent_to = book.get("lent_to", "").strip()
    print(f"Lent To:   {lent_to if lent_to else '(Not lent)'}")
    print("-" * 60 + "\n")


def add_book(books):
    """Add a new book to the library"""
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


def edit_book_menu(book, book_num):
    """Display edit menu for a specific book"""
    while True:
        display_book_details(book, book_num)

        print("EDIT MENU:")
        print("-" * 60)
        print("1. View Book")
        print("2. Edit Title")
        print("3. Edit Author")
        print("4. Edit Lent To")
        print("5. Delete Book")
        print("0. Back to List\n")
        print("-" * 60)

        choice = input(">>> Choose an option: ").strip()

        if choice == "1":
            print("\n(Book details shown above)\n")
        elif choice == "2":
            new_title = input(">>> New Title: ").strip()
            if new_title:
                book["title"] = new_title
                print(">>> Title updated successfully.\n")
            else:
                print(">>> ERROR: Title cannot be empty.\n")
        elif choice == "3":
            new_author = input(">>> New Author: ").strip()
            if new_author:
                book["author"] = new_author
                print(">>> Author updated successfully.\n")
            else:
                print(">>> ERROR: Author cannot be empty.\n")
        elif choice == "4":
            new_lent_to = input(">>> Lent To (leave empty if not lent): ").strip()
            book["lent_to"] = new_lent_to
            if new_lent_to:
                print(f">>> Book marked as lent to '{new_lent_to}'.\n")
            else:
                print(">>> Book marked as not lent.\n")
        elif choice == "5":
            confirm = input(">>> Are you sure you want to delete this book? (Y/N): ").strip().upper()
            if confirm == "Y":
                title = book["title"]
                return "DELETE", title
            else:
                print(">>> Deletion cancelled.\n")
        elif choice == "0":
            return "BACK", None
        else:
            print(">>> ERROR: Invalid option. Please enter 0-5.\n")

        input(">>> Press ENTER to continue...")
        clear_screen()


def edit_book(books):
    """Select and edit a book"""
    if not list_books(books):
        return

    try:
        choice = input(">>> Enter book number to edit (0 to cancel): ").strip()

        if choice == "0":
            print(">>> Operation cancelled.\n")
            return

        book_num = int(choice)
        idx = book_num - 1

        if 0 <= idx < len(books):
            clear_screen()
            while True:
                action, data = edit_book_menu(books[idx], book_num)

                if action == "DELETE":
                    books.pop(idx)
                    save_books(books)
                    clear_screen()
                    print(f"\n>>> Book '{data}' deleted successfully.\n")
                    break
                elif action == "BACK":
                    save_books(books)
                    clear_screen()
                    break
        else:
            print(">>> ERROR: Invalid book number.\n")
    except ValueError:
        print(">>> ERROR: Please enter a valid number.\n")


def main():
    """Main program loop"""
    clear_screen()
    print("\n>>> Loading Mini Library Manager...\n")

    while True:
        books = load_books()
        display_main_menu()

        choice = input(">>> Select an option: ").strip()

        clear_screen()

        if choice == "1":
            list_books(books)
        elif choice == "2":
            add_book(books)
        elif choice == "3":
            edit_book(books)
        elif choice == "0":
            clear_screen()
            print("\n>>> Thank you for using Mini Library Manager. Goodbye!\n")
            break
        else:
            print(">>> ERROR: Invalid option. Please enter 0-3.\n")
            input(">>> Press ENTER to continue...")
            clear_screen()


if __name__ == "__main__":
    main()
