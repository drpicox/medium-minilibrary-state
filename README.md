# Mini Library Manager - Monorepo Edition

```
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║                    MINI LIBRARY MANAGER MONOREPO                          ║
║                                                                            ║
║    Two Approaches to the Same Problem:                                    ║
║    Retro CLI vs Modern Web Interface                                      ║
║                                                                            ║
║         "Demonstrating design philosophy through interface choice"        ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
```

## 📚 What is This?

**Mini Library Manager** is a demonstration project that shows how the same application can be built two different ways:

1. **CLI Edition** - A retro text-based interface inspired by 1980s MS-DOS database programs
2. **Web Edition** - A modern web interface built with Flask

Both manage the same data (your personal book library) but provide dramatically different user experiences.

---

## 🎯 Project Goals

✅ Demonstrate **identical business logic** across different interfaces  
✅ Show the importance of **architecture** in software design  
✅ Celebrate **computing history** while applying modern principles  
✅ Provide a **learning resource** for understanding design patterns  
✅ Create a **practical tool** for managing books  

---

## 📁 Repository Structure

```
msdos-library/
│
├── README.md                 ← You are here
├── COMPARATIVA.md           ← Deep comparison analysis
│
├── cli/                      ← Command-line version
│   ├── main.py             ← Single Python file (232 lines)
│   ├── books.json          ← Data storage
│   └── README.md           ← CLI-specific documentation
│
└── web/                      ← Web version
    ├── app.py              ← Flask application
    ├── requirements.txt    ← Python dependencies
    ├── books.json          ← Shared data storage
    ├── README.md           ← Web-specific documentation
    ├── templates/          ← HTML templates
    │   ├── base.html       ← Base template
    │   ├── index.html      ← Library listing
    │   ├── add_book.html   ← Add book form
    │   ├── book_details.html
    │   ├── edit_book.html
    │   └── about.html
    └── static/             ← CSS and assets
        └── style.css       ← Retro styling
```

---

## 🚀 Quick Start

### CLI Edition (2 seconds)

```bash
cd cli
python3 main.py
```

✅ No setup, no dependencies, runs immediately!

### Web Edition (2 minutes)

```bash
cd web
pip install -r requirements.txt
python3 app.py
# Open http://localhost:5000 in your browser
```

---

## 📖 Documentation

### For CLI Edition
See [cli/README.md](cli/README.md) for:
- Installation instructions
- Usage guide with examples
- Technical details
- Data format explanation

### For Web Edition
See [web/README.md](web/README.md) for:
- Getting started guide
- Feature documentation
- Troubleshooting
- Future enhancements

### Architecture & Design Analysis
See [COMPARATIVA.md](COMPARATIVA.md) for:
- Side-by-side comparison
- Architecture diagrams
- Performance analysis
- Use case recommendations
- Design philosophy discussion

---

## ✨ Features (Both Editions)

### Create
- ✅ Add new books with Title, Author, and Lent To status
- ✅ Automatic timestamps on creation

### Read
- ✅ View all books in your library
- ✅ Individual book detail views
- ✅ Status indicators (Available/Lent)

### Update
- ✅ Edit book information
- ✅ Change lending status
- ✅ Modify any field

### Delete
- ✅ Remove books from library
- ✅ With confirmation to prevent accidents

### Additional
- ✅ Persistent JSON storage
- ✅ Data sharing between editions
- ✅ Cross-platform compatibility

---

## 🔄 Data Interoperability

Both editions use the same JSON format:

```json
{
  "id": 1,
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "lent_to": "Bookshelf 1",
  "created_at": "2026-02-06T22:34:34.857548"
}
```

**This means:**
- Add a book in the **Web** edition → appears in **CLI** edition
- Edit a book in the **CLI** edition → appears in **Web** edition
- Delete a book in either edition → gone from both
- Manual JSON editing instantly reflects in both

**Note:** Each edition has its own `books.json` file. To truly sync them, you can:
```bash
# Copy from CLI to Web
cp cli/books.json web/books.json

# Or the other way
cp web/books.json cli/books.json
```

---

## 📊 Comparison at a Glance

| Aspect | CLI | Web |
|--------|-----|-----|
| **Setup Time** | ~5 seconds | ~2 minutes |
| **Dependencies** | None | Flask |
| **Platforms** | All | All (with browser) |
| **Interface** | Text menus | Visual cards |
| **User Type** | Terminal users | Everyone |
| **Best For** | Scripting, SSH | Browsing, sharing |
| **Performance** | Excellent | Good |
| **Extensibility** | Limited | Good |

For a **detailed comparison**, see [COMPARATIVA.md](COMPARATIVA.md).

---

## 🛠️ Technology Stack

### CLI Edition
- **Language:** Python 3.6+
- **Dependencies:** Standard library only
- **Storage:** JSON
- **Interface:** Terminal/Console

### Web Edition
- **Language:** Python 3.6+
- **Framework:** Flask 2.3.3
- **Templating:** Jinja2
- **Styling:** Custom CSS
- **Storage:** JSON
- **Interface:** Web Browser

### Both
- **Version Control:** Git
- **Data Format:** JSON

---

## 🎓 Learning Resources

This monorepo teaches several concepts:

1. **Design Patterns**
   - MVC architecture (Web edition)
   - Functional programming (CLI edition)
   - Separation of concerns

2. **Architecture**
   - Same business logic, different interfaces
   - Data-driven design
   - Cross-platform compatibility

3. **Python Programming**
   - CLI: Simple, readable Python code
   - Web: Flask framework basics
   - Both: File I/O and JSON handling

4. **Software Design**
   - Trade-offs between simplicity and features
   - User experience design
   - Historical context (MS-DOS era)

5. **Web Development**
   - HTTP request/response cycle
   - Template rendering
   - CSS styling and responsive design
   - Form validation

---

## 🎨 Retro Aesthetics

Both editions celebrate **computing history**:

### CLI Edition
- 🖥️ MS-DOS command prompt aesthetic
- ⌨️ Text-based menu navigation
- 💾 Reminiscent of dBASE, early database programs
- 📟 Monospace fonts and simple formatting

### Web Edition
- 🟩 Classic green-on-black terminal colors
- 🎨 Modern CSS with retro theme
- 📱 Responsive design (works on all devices)
- ✨ Hover effects and visual feedback

The combination proves you can be **both retro and modern** in different contexts!

---

## 📝 File Descriptions

### Root Files

| File | Purpose |
|------|---------|
| `README.md` | This file - project overview |
| `COMPARATIVA.md` | Detailed comparison of both editions |
| `.gitignore` | Git configuration |
| `.git/` | Version control history |

### CLI Directory (`cli/`)

| File | Purpose |
|------|---------|
| `main.py` | Main application (232 lines) |
| `books.json` | Library data |
| `README.md` | CLI documentation |

### Web Directory (`web/`)

| File | Purpose |
|------|---------|
| `app.py` | Flask application |
| `requirements.txt` | Python dependencies |
| `books.json` | Library data (shared format) |
| `README.md` | Web documentation |
| `templates/base.html` | Base HTML template |
| `templates/index.html` | Library listing |
| `templates/add_book.html` | Add book form |
| `templates/book_details.html` | Book details page |
| `templates/edit_book.html` | Edit book form |
| `templates/about.html` | About/info page |
| `static/style.css` | Styling (600+ lines) |

---

## 🔍 Quick Examples

### Example 1: Adding a Book

**CLI:**
```
>>> Select an option: 2
>>> Title: The Name of the Wind
>>> Author: Patrick Rothfuss
>>> Lent To: [leave blank]
>>> Book 'The Name of the Wind' added successfully.
```

**Web:**
```
Click "➕ Add Book" → Fill form → Click "✅ Add Book"
```

### Example 2: Finding Your Book

**CLI:**
```
>>> Select an option: 1
[1] The Hobbit - J.R.R. Tolkien
[2] 1984 - George Orwell
[3] The Name of the Wind - Patrick Rothfuss
```

**Web:**
```
See card grid with all books at once
```

### Example 3: Marking as Lent

**CLI:**
```
>>> Select an option: 3
>>> Enter book number: 1
>>> Choose option: 4 (Edit Lent To)
>>> Lent To: John
```

**Web:**
```
Click "✏️ Edit" → Change "Lent To" field → Save
```

---

## 🐛 Troubleshooting

### CLI Issues

**"No such file or directory: books.json"**
- Normal! It's created automatically on first run

**"Permission denied when running main.py"**
```bash
chmod +x cli/main.py
```

### Web Issues

**"ModuleNotFoundError: No module named 'flask'"**
```bash
cd web
pip install -r requirements.txt
```

**"Port 5000 already in use"**
Change the port in `app.py` (line ~300) and access `http://localhost:5001`

---

## 📈 Future Enhancements

The architecture supports adding:

- 🔐 User authentication
- 👥 Multi-user sharing
- ⭐ Ratings and reviews
- 🔍 Advanced search
- 📊 Statistics dashboard
- 📱 Mobile app
- ☁️ Cloud sync
- 📖 Reading list generation

---

## 🎓 Educational Value

This project is perfect for:

- 👨‍💻 Learning Python fundamentals
- 🌐 Understanding Flask basics
- 🏗️ Studying software architecture
- 📚 Exploring design patterns
- 🎨 Learning CSS and web design
- 🕰️ Appreciating computing history

---

## 🤝 Contributing

Want to improve this project? Ideas:

- Add features to either edition
- Improve documentation
- Optimize performance
- Add more sophisticated styling
- Create mobile app versions
- Write additional tests
- Improve error handling

---

## 📄 License

Free to use, modify, and distribute.

---

## 🙏 Acknowledgments

- Inspired by classic MS-DOS era database programs
- Built with Python and Flask
- Designed with learning in mind
- Created to celebrate both retro and modern computing

---

## 📞 Getting Started Now

**Choose your path:**

### 🖥️ Want the retro experience?
```bash
cd cli
python3 main.py
```

### 🌐 Want the modern interface?
```bash
cd web
pip install -r requirements.txt
python3 app.py
```

### 📖 Want to understand the differences?
Read [COMPARATIVA.md](COMPARATIVA.md)

---

```
════════════════════════════════════════════════════════════════════════════════
                  CLI and Web | Retro and Modern | Simple and Complex
                        All Working Together Beautifully
════════════════════════════════════════════════════════════════════════════════
```

**Happy library managing!** 📚✨
