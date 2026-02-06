# Mini Library Manager - Web Edition

A modern Flask-based web interface for managing your personal book library with **multi-user support**.

## Quick Start

### Installation

1. **Navigate to the web directory:**
   ```bash
   cd web
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python3 app.py
   ```

4. **Open your browser:**
   ```
   http://localhost:5000
   ```

### Demo Account

Quick access - no need to register:
- **Username:** `demo`
- **Password:** `1234`

## Features

✨ **Intuitive Web Interface** - Clean, retro-modern design  
📚 **Full CRUD Operations** - Manage your library completely  
💾 **Persistent Storage** - Saves to JSON automatically  
🎨 **Responsive Design** - Works on desktop and mobile  
� **Multi-User Support** - Each user has their own library  
👤 **User Accounts** - Register and login securely  
🔄 **Data Isolation** - Users only see their own books  

## Navigation

- **� Login** - Enter your account
- **✍️ Register** - Create a new account
- **📖 Library** - View all your books
- **➕ Add Book** - Add new books to your collection
- **ℹ️ About** - Learn more about the project
- **🚪 Logout** - Exit your account

## Workflow

### 1. Getting Started

**Option A: Try Demo Account**
```
Username: demo
Password: 1234
```

**Option B: Create Your Account**
1. Click "✍️ Create Account"
2. Choose username (min 3 characters)
3. Create password (min 4 characters)
4. Click "✅ Create Account"
5. Start adding books!

### 2. Managing Books

The workflow is identical to other editions - Add, View, Edit, Delete.

1. Click **"➕ Add Book"**
2. Fill in:
   - **Title** (required)
   - **Author** (required)
   - **Lent To** (optional - who borrowed it or where it is)
3. Click **"✅ Add Book"**

### Viewing Books

1. On the **"📖 Library"** page, see all books
2. Badge shows if book is **Available** or **Lent**
3. Click **"👁️ View"** to see full details

### Editing a Book

1. Click **"✏️ Edit"** on any book card or details page
2. Update the information
3. Click **"✅ Update Book"**

### Deleting a Book

1. Click **"🗑️ Delete"** on any book card or details page
2. Confirm deletion
3. Book is permanently removed

## Design Philosophy

This web edition maintains the **retro-modern aesthetic** of the CLI version while providing:
- Visual feedback through colors and badges
- Click-based navigation instead of menu text
- Card-based layout for better organization
- Responsive design for all devices

## Technical Stack

- **Backend:** Flask (Python web framework)
- **Frontend:** HTML/Jinja2 templates + CSS
- **Storage:** JSON files
- **Styling:** Custom CSS with retro green terminal theme

## File Structure

```
web/
├── app.py                    # Flask application with auth
├── users.json               # User accounts database
├── requirements.txt         # Python dependencies
├── README.md               # This file
├── users/                  # User data directory
│   └── demo/
│       └── books.json      # Demo user's books
├── templates/
│   ├── base.html           # Base template with navbar
│   ├── login.html          # Login page
│   ├── register.html       # Register page
│   ├── index.html          # Library listing
│   ├── add_book.html       # Add book form
│   ├── book_details.html   # Book details view
│   ├── edit_book.html      # Edit book form
│   └── about.html          # About/info page
└── static/
    └── style.css           # Styling
```

## API Routes

### Authentication
- `GET /login` - Login form
- `POST /login` - Submit login credentials
- `GET /register` - Registration form
- `POST /register` - Create new user account
- `GET /logout` - End session and logout

### Library Management
- `GET /` - Display all books (requires login)
- `GET /add`, `POST /add` - Add new book form & submission
- `GET /book/<id>` - View book details
- `GET /edit/<id>`, `POST /edit/<id>` - Edit book form & submission
- `POST /delete/<id>` - Delete book
- `GET /about` - About page

## Data Storage & Security

### Multi-User Architecture

Each user's data is **completely isolated** using this directory structure:

```
web/
├── users.json              ← All user accounts with password hashes
└── users/
    ├── demo/
    │   └── books.json      ← Demo user's books
    ├── alice/
    │   └── books.json      ← Alice's books
    └── bob/
        └── books.json      ← Bob's books
```

### User Privacy

- **Passwords:** Hashed using SHA256, never stored plaintext
- **Books:** Each user sees ONLY their own library
- **Sessions:** Flask session management with timeout
- **No Mixing:** Users cannot access other users' books

### Book Data Format

Each user's `users/username/books.json` contains:

```json
[
  {
    "id": 1,
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "lent_to": "John",
    "created_at": "2026-02-06T22:34:34"
  }
]
```

### Backup & Migration

To backup a specific user's library:
```bash
cp web/users/demo/books.json backup/demo-books.json
```

To export all user accounts:
```bash
cp web/users.json backup/users.json
```

⚠️ **Important:** Keep `users.json` and `web/users/` safe - they contain all library data and user credentials.

## Browser Compatibility

- ✅ Chrome/Chromium
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Opera

## Tips

💡 **Organizing Your Library**
- Use "Lent To" field creatively:
  - `Bookshelf 1`, `Bookshelf 2` for locations
  - Person's name for borrowers
  - `Being read` for current reads
  - `Office` for work books

💡 **Backup Your Library**
```bash
cp books.json books.json.backup
```

💡 **Debug Mode**
The app runs in debug mode by default, which enables:
- Auto-reload on file changes
- Detailed error messages
- Interactive debugger

To disable debug mode, edit `app.py`:
```python
app.run(debug=False, port=5000)
```

## Troubleshooting

**"ModuleNotFoundError: No module named 'flask'"**
```bash
pip install -r requirements.txt
```

**Port 5000 already in use?**
Change the port in `app.py`:
```python
app.run(debug=True, port=5001)  # Use 5001 instead
```

**CSS not loading?**
Clear your browser cache (Ctrl+Shift+Delete or Cmd+Shift+Delete)

## Future Enhancements

- 📅 Date tracking for loans/returns
- ⭐ Book ratings and reviews
- 🔍 Search and filter functionality
- 📊 Library statistics dashboard
- 🎯 Book status flags (wishlist, read, unread)
- 📤 Export library to PDF/CSV

---

**Enjoy managing your library with style!** 📚✨
