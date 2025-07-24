# 📚 Book Collection Manager

A simple, interactive **command-line application** for tracking the books you own, what you’ve read, and your overall reading progress. Data is saved locally in a JSON file (`books_data.json`), so your collection persists between runs.

---

## ✨ Features

- **Add books** with title, author, publication year, genre, and read/unread status.
- **Delete books** by title.
- **Search** by partial match on title _or_ author.
- **Update** any field of an existing book (leave blank to keep current value).
- **List all books** in a clean, numbered view.
- **Reading progress stats** – see % of books you’ve completed.
- **Persistent storage** using a JSON file.

---

## 🗂 Data Model

Each book is stored as a JSON object:

```json
{
  "title": "Atomic Habits",
  "author": "James Clear",
  "year": "2018",
  "genre": "Self-Help",
  "read": true
}
```

All books are kept in a list and written to `books_data.json` in the application directory.

---

## 🚀 Getting Started

### 1. Clone or copy the script

Save the Python code to a file, e.g. `main.py`.

### 2. Run the app

```bash
python main.py
```

The app will auto-create `books_data.json` if it doesn’t exist.

---

## 📋 Menu Walkthrough

When you start the program you’ll see this menu:

```
📚 Welcome to Your Book Collection Manager! 📚
1. Add a new book
2. Remove a book
3. Search for books
4. Update book details
5. View all books
6. View reading progress
7. Exit
```

Enter the number of the action you want to perform. Inputs are text-based and prompted step‑by‑step.

---

## 🔍 Searching Tips

- Search is **case-insensitive**.
- You can enter any partial word: searching for `har` will match _"Harry Potter"_ and _"Harper Lee"_.
- The numeric menu prompt in the search function is currently informational; the code always searches both title and author.

---

## 🛠 Updating a Book

When updating, press **Enter** without typing anything to keep the current value for that field. You will be asked again for read status (`yes` or `no`).

---

## 📈 Reading Progress

The progress percentage = `(books_marked_read / total_books) * 100`. Useful for reading challenges!

---

## 🤖 Example Session

```text
Please choose an option (1-7): 1
Enter book title: Deep Work
Enter author: Cal Newport
Enter publication year: 2016
Enter genre: Productivity
Have you read this book? (yes/no): yes
Book added successfully!
```

---

## 🧼 Clearing / Resetting Your Collection

Just delete the `books_data.json` file (or empty the list in code) and restart the app. A fresh file will be created automatically.

---

## 🧪 Testing Ideas

If you want to test quickly, you can seed some sample data by editing the JSON file directly:

```json
[
  {
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "year": "2008",
    "genre": "Programming",
    "read": true
  },
  {
    "title": "1984",
    "author": "George Orwell",
    "year": "1949",
    "genre": "Dystopian",
    "read": false
  }
]
```

---

## 🧭 Possible Improvements (Pull Requests Welcome!)

- Validate year input (numeric, 4 digits).
- Enforce unique titles or use IDs.
- Allow marking read/unread without full update.
- Export stats (CSV, Markdown).
- Sort / filter by genre, year, or status.
- Add colored CLI output.
- Build a Streamlit or Tkinter GUI version.

---

## ❓ FAQ

**Q: Where is my data saved?**
In a local file named `books_data.json` created in the same folder as the script.

**Q: Can I move my data?**
Yes. Copy the JSON file along with the script to another machine.

**Q: The program crashed and my JSON is corrupted. What now?**
Delete or fix the JSON file. The app will start with an empty list if the file can’t be read.

---

## 🙌 Credits

Created by **Hafiz Siddiqui**. Enjoy building your personal reading tracker!

---
