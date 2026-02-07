#!/usr/bin/env python3
"""
Mini Library Manager - Web Edition
Flask-based web interface for the Mini Library application
Multi-user support with JSON-based user data
"""

import json
import os
import hashlib
from functools import wraps
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = "mini-library-secret-2026"

USERS_DIR = "users"
USERS_FILE = "users.json"

# Ensure users directory exists
os.makedirs(USERS_DIR, exist_ok=True)


def hash_password(password):
    """Simple password hashing"""
    return hashlib.sha256(password.encode()).hexdigest()


def load_users():
    """Load users database"""
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}


def save_users(users):
    """Save users database"""
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2, ensure_ascii=False)


def get_user_books_file(username):
    """Get path to user's books file"""
    user_dir = os.path.join(USERS_DIR, username)
    return os.path.join(user_dir, "books.json")


def load_user_books(username):
    """Load books for specific user"""
    books_file = get_user_books_file(username)
    if os.path.exists(books_file):
        try:
            with open(books_file, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []


def save_user_books(username, books):
    """Save books for specific user"""
    user_dir = os.path.join(USERS_DIR, username)
    os.makedirs(user_dir, exist_ok=True)
    books_file = os.path.join(user_dir, "books.json")
    with open(books_file, "w") as f:
        json.dump(books, f, indent=2, ensure_ascii=False)


def login_required(f):
    """Decorator to require login"""
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated


@app.route("/")
def index():
    """Home - redirect to login if not logged in"""
    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session['username']
    books = load_user_books(username)
    return render_template("index.html", books=books, username=username, count=len(books))


@app.route("/login", methods=["GET", "POST"])
def login():
    """Login page"""
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        if not username or not password:
            flash("❌ Username and password are required!", "error")
            return redirect(url_for('login'))

        users = load_users()
        
        if username in users and users[username]['password_hash'] == hash_password(password):
            session['username'] = username
            flash(f"✅ Welcome back, {username}!", "success")
            return redirect(url_for('index'))
        else:
            flash("❌ Invalid username or password!", "error")
            return redirect(url_for('login'))

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register new user"""
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        password_confirm = request.form.get("password_confirm", "").strip()

        if not username or not password:
            flash("❌ Username and password are required!", "error")
            return redirect(url_for('register'))

        if len(username) < 3:
            flash("❌ Username must be at least 3 characters!", "error")
            return redirect(url_for('register'))

        if len(password) < 4:
            flash("❌ Password must be at least 4 characters!", "error")
            return redirect(url_for('register'))

        if password != password_confirm:
            flash("❌ Passwords don't match!", "error")
            return redirect(url_for('register'))

        users = load_users()
        
        if username in users:
            flash("❌ Username already exists!", "error")
            return redirect(url_for('register'))

        # Create new user
        users[username] = {
            "password_hash": hash_password(password),
            "created_at": datetime.now().isoformat()
        }
        save_users(users)

        # Create user directory and empty books file
        user_dir = os.path.join(USERS_DIR, username)
        os.makedirs(user_dir, exist_ok=True)
        save_user_books(username, [])

        flash(f"✅ Account created! Welcome, {username}!", "success")
        session['username'] = username
        return redirect(url_for('index'))

    return render_template("register.html")


@app.route("/logout")
def logout():
    """Logout user"""
    username = session.get('username', 'User')
    session.clear()
    flash(f"👋 Goodbye, {username}!", "success")
    return redirect(url_for('login'))


@app.route("/add", methods=["GET", "POST"])
@login_required
def add_book():
    """Add a new book"""
    username = session['username']
    
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        author = request.form.get("author", "").strip()
        lent_to = request.form.get("lent_to", "").strip()

        if not title or not author:
            flash("❌ Title and Author are required!", "error")
            return redirect(url_for("add_book"))

        books = load_user_books(username)
        new_book = {
            "id": len(books) + 1,
            "title": title,
            "author": author,
            "lent_to": lent_to,
            "created_at": datetime.now().isoformat()
        }

        books.append(new_book)
        save_user_books(username, books)
        flash(f"✅ Book '{title}' added successfully!", "success")
        return redirect(url_for("index"))

    return render_template("add_book.html")


@app.route("/book/<int:book_id>")
@login_required
def view_book(book_id):
    """View book details"""
    username = session['username']
    books = load_user_books(username)
    book = next((b for b in books if b["id"] == book_id), None)

    if not book:
        flash("❌ Book not found!", "error")
        return redirect(url_for("index"))

    return render_template("book_details.html", book=book)


@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
@login_required
def edit_book(book_id):
    """Edit a book"""
    username = session['username']
    books = load_user_books(username)
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
        save_user_books(username, books)

        flash(f"✅ Book '{title}' updated successfully!", "success")
        return redirect(url_for("view_book", book_id=book_id))

    return render_template("edit_book.html", book=book)


@app.route("/delete/<int:book_id>", methods=["POST"])
@login_required
def delete_book(book_id):
    """Delete a book"""
    username = session['username']
    books = load_user_books(username)
    book_idx = next((i for i, b in enumerate(books) if b["id"] == book_id), None)

    if book_idx is None:
        flash("❌ Book not found!", "error")
        return redirect(url_for("index"))

    deleted_title = books.pop(book_idx)["title"]
    save_user_books(username, books)

    flash(f"✅ Book '{deleted_title}' deleted successfully!", "success")
    return redirect(url_for("index"))


@app.route("/about")
def about():
    """About page"""
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=False, port=5001)
