# Assignment 42 — Personal Diary

## 🎯 What You Will Practice
Learn how to use file append mode, read specific sections, date handling, and exceptions.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. If Write Entry: open diary file in 'a' (append) mode, write formatted entry
2. If Read Today: open file in 'r' mode, parse entries, filter to today's date
3. If Read All: open file, parse ALL entries into entries list
4. If Delete All: open file in 'w' mode, write empty string
5. Wrap in try/except: FileNotFoundError → create file first
6. Mood emojis: Happy=😊 Sad=😢 Excited=🎉 Calm=😌 Anxious=😰 Grateful=🙏

## 💡 Hints
- Write entry: `with open(DIARY_FILE, 'a') as f: f.write(f"DATE: {today} | MOOD: {mood}\n{entry_text}\n---\n")`
- Read file: `with open(DIARY_FILE, 'r') as f: content = f.read()`
- Parse entries: split by '---', then parse each entry for date, mood, text
- Mood emoji map: `{'Happy': '😊', 'Sad': '😢', 'Excited': '🎉', 'Calm': '😌', 'Anxious': '😰', 'Grateful': '🙏'}`
- Filter today: check if entry.date == today
- Delete all: `with open(DIARY_FILE, 'w') as f: f.write('')`
- Exception: `except FileNotFoundError: with open(DIARY_FILE, 'w') as f: pass`

## 🔍 Example
Write Entry: entry_text = "Had a great day!", mood = "Happy"
Expected Output: entry written to file with date and mood emoji

Read Today: today = "2026-05-18"
Expected Output: entries list with only today's entries

Read All:
Expected Output: entries list with all diary entries

## ✅ You Are Done When
- Entries are written to file with correct format
- Today's entries are filtered correctly
- All entries are read and displayed
- Delete all clears the file
- FileNotFoundError is handled by creating file
- Mood emojis are displayed correctly
