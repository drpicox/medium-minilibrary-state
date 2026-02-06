# Mini Library Manager - Web Edition

A modern Flask-based web interface for managing your personal book library.

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

## Features

✨ **Intuitive Web Interface** - Clean, retro-modern design  
📚 **Full CRUD Operations** - Manage your library completely  
💾 **Persistent Storage** - Saves to JSON automatically  
🎨 **Responsive Design** - Works on desktop and mobile  
🔄 **Shared Data** - Syncs with CLI edition's books.json  

## Navigation

- **📖 Library** - View all your books in a card layout
- **➕ Add Book** - Add new books to your collection
- **ℹ️ About** - Learn more about the project

## Workflow

### Adding a Book

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
├── app.py                    # Flask application
├── books.json               # Library data (auto-created)
├── requirements.txt         # Python dependencies
├── README.md               # This file
├── templates/
│   ├── base.html           # Base template
│   ├── index.html          # Library listing
│   ├── add_book.html       # Add book form
│   ├── book_details.html   # Book details view
│   ├── edit_book.html      # Edit book form
│   └── about.html          # About/info page
└── static/
    └── style.css           # Styling
```

## API Routes

- `GET /` - Display all books
- `GET /add`, `POST /add` - Add new book form & submission
- `GET /book/<id>` - View book details
- `GET /edit/<id>`, `POST /edit/<id>` - Edit book form & submission
- `POST /delete/<id>` - Delete book
- `GET /about` - About page

## Data Sharing

Both CLI and web editions share the same `books.json` format:

```json
{
  "id": 1,
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "lent_to": "John",
  "created_at": "2026-02-06T22:34:34"
}
```

You can:
- Add books in the web version, view them in CLI
- Modify data in CLI, see changes reflected in web
- Edit `books.json` directly if needed
- Back up your library by copying the JSON file

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
