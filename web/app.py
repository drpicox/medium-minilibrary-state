#!/usr/bin/env python3
"""
Mini Library Manager - Web Edition
Flask-based web interface for the Mini Library application
"""

import json
import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "mini-library-secret-2026"

BOOKS_FILE = "books.json"


def load_books():
    """Load books from JSON file"""
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


@app.route("/")
def index():
    """Home page - list all books"""
    books = load_books()
    return render_template("index.html", books=books, count=len(books))


@app.route("/add", methods=["GET", "POST"])
def add_book():
    """Add a new book"""
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        author = request.form.get("author", "").strip()
        lent_to = request.form.get("lent_to", "").strip()

        if not title or not author:
            flash("❌ Title and Author are required!", "error")
            return redirect(url_for("add_book"))

        books = load_books()
        new_book = {
            "id": len(books) + 1,
            "title": title,
            "author": author,
            "lent_to": lent_to,
            "created_at": datetime.now().isoformat()
        }

        books.append(new_book)
        save_books(books)
        flash(f"✅ Book '{title}' added successfully!", "success")
        return redirect(url_for("index"))

    return render_template("add_book.html")


@app.route("/book/<int:book_id>")
def view_book(book_id):
    """View book details"""
    books = load_books()
    book = next((b for b in books if b["id"] == book_id), None)

    if not book:
        flash("❌ Book not found!", "error")
        return redirect(url_for("index"))

    return render_template("book_details.html", book=book)


@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    """Edit a book"""
    books = load_books()
    book_idx = next((i for i, b in enumerate(books) if b["id"] == book_id), None)

    if book_idx is None:
        flash("❌ Book not found!", "error")
        return redirect(url_for("index"))

    book = books[book_idx]

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        author = request.form.get("author", "").strip()
        lent_to = request.form.get("lent_to", "").strip()

        if not title or not author:
            flash("❌ Title and Author are required!", "error")
            return redirect(url_for("edit_book", book_id=book_id))

        book["title"] = title
        book["author"] = author
        book["lent_to"] = lent_to
        save_books(books)

        flash(f"✅ Book '{title}' updated successfully!", "success")
        return redirect(url_for("view_book", book_id=book_id))

    return render_template("edit_book.html", book=book)


@app.route("/delete/<int:book_id>", methods=["POST"])
def delete_book(book_id):
    """Delete a book"""
    books = load_books()
    book_idx = next((i for i, b in enumerate(books) if b["id"] == book_id), None)

    if book_idx is None:
        flash("❌ Book not found!", "error")
        return redirect(url_for("index"))

    deleted_title = books.pop(book_idx)["title"]
    save_books(books)

    flash(f"✅ Book '{deleted_title}' deleted successfully!", "success")
    return redirect(url_for("index"))


@app.route("/about")
def about():
    """About page"""
    return render_template("about.html")


if __name__ == "__main__":
    # Copy books.json from cli/ if it exists
    cli_books = "../cli/books.json"
    if os.path.exists(cli_books) and not os.path.exists(BOOKS_FILE):
        with open(cli_books, "r") as src:
            books_data = json.load(src)
        save_books(books_data)

    app.run(debug=True, port=5000)
