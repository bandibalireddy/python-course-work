# 🐍 Python Learning Assignments — Django Edition

## 📋 Overview
This project contains 13 beginner Python assignments built with Django.
Each assignment teaches a core Python concept. You write the logic,
Django handles the rest.

## 🗂️ Assignment List

| # | Assignment | Concepts Covered |
|---|-----------|-----------------|
| 1 | Simple Calculator | Variables, floats, if/elif/else |
| 2 | String Inspector | Strings, string methods |
| 3 | Even/Odd & Divisibility | Integers, modulo operator |
| 4 | Grocery List Manager | Lists, add/remove items |
| 5 | Number List Stats | Lists, min/max/sum/average |
| 6 | Mini Profile Card | Variables, lists, type conversion |
| 7 | Grade Classifier | Conditionals, ranges |
| 8 | Number Guessing Game | Integers, comparisons, state |
| 9 | Word Counter & Analyzer | Strings, lists, loops |
| 10 | FizzBuzz Custom Rules | Loops, conditionals, lists |
| 11 | Shopping Cart | Lists of dicts, math, logic |
| 12 | Student Grade Book | Lists, sorting, averages |
| 13 | Personal Quiz App | Lists of dicts, loops, scoring |

---

## 💻 Requirements

- Python 3.10 or higher
- pip (comes with Python)
- A code editor (VS Code recommended)

---

## 🚀 First Time Setup (Do this once)

### Step 1 — Check Python is installed
Open your terminal (Mac/Linux) or Command Prompt (Windows) and run:
```
python --version
```
You should see something like `Python 3.11.x` 
If not, download Python from https://www.python.org/downloads/

### Step 2 — Download or Clone this project
If you have Git:
```
git clone <your-repo-url>
cd python_learning
```
Or download the ZIP from GitHub and unzip it, then open that folder in your terminal.

### Step 3 — Create a Virtual Environment (Recommended)

**Mac/Linux:**
```
python -m venv venv
source venv/bin/activate
```

**Windows:**
```
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` appear at the start of your terminal line.

### Step 4 — Install Django
```
pip install -r requirements.txt
```

### Step 5 — Run the Server
```
python manage.py runserver
```

### Step 6 — Open in Browser
Open your browser and go to:
```
http://127.0.0.1:8000
```
You will see the Assignment Dashboard. Click any assignment to start.

---

## ✏️ How to Complete an Assignment

1. Open the assignment folder, e.g. `assignment1/views.py` 
2. Find the clearly marked section:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```
3. Write your Python logic between those two lines
4. Save the file — Django auto-reloads, no need to restart the server
5. Go back to the browser and test your solution

---

## ❌ Common Errors & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `python: command not found` | Python not installed or not in PATH | Install from python.org or use `python3` instead |
| `pip: command not found` | pip not in PATH | Use `python -m pip install -r requirements.txt` |
| `No module named django` | Django not installed | Run `pip install -r requirements.txt` |
| `(venv)` not showing | Virtual env not activated | Run `source venv/bin/activate` (Mac) or `venv\Scripts\activate` (Windows) |
| Port 8000 already in use | Another server is running | Run `python manage.py runserver 8080` and go to `http://127.0.0.1:8080` |
| Page not updating | File not saved | Press Ctrl+S to save, then refresh browser |

---

## 📁 Project Structure
```
python_learning/
├── manage.py                  ← Django management tool (don't edit)
├── requirements.txt           ← Python packages needed
├── README.md                  ← You are here
├── python_learning/           ← Project settings (don't edit)
│   ├── settings.py
│   └── urls.py
├── home/                      ← Dashboard page (don't edit)
└── assignment1/               ← Your assignment folders
    ├── views.py               ← ✏️  YOU WRITE CODE HERE
    ├── urls.py                ← (don't edit)
    └── templates/
        └── assignment1/
            └── index.html     ← (don't edit)
```

---

## 💡 Tips for Beginners

- **Save your file** before refreshing the browser (Ctrl+S)
- **Read the instructions** shown on each assignment page carefully
- **Use print()** to debug — output appears in the terminal where you ran `runserver` 
- **Don't edit** any file outside of the `STUDENT CODE START/END` section
- If something breaks, check the terminal — Django shows error details there
- Google is your friend — searching Python error messages is a real developer skill!

---

## 🆘 Getting Help

- Read the error message in the terminal carefully
- Check the Common Errors table above
- Ask your instructor and share:
  - A screenshot of the error in the terminal
  - Your code from views.py
