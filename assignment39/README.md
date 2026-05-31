# Assignment 39 — File Word Counter

## 🎯 What You Will Practice
Learn how to write files, read files, use file modes, and the with statement.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Build full file path safely using os.path.join(FILE_DIR, filename)
2. If Save: open file with 'w' mode, write text_content, set message
3. If Read: open file with 'r' mode, read content into file_content
4. If Count: open file, count words (split), lines (splitlines), chars (len)
5. Wrap all file operations in try/except for FileNotFoundError, IOError

## 💡 Hints
- File path: `file_path = os.path.join(FILE_DIR, filename)`
- Write: `with open(file_path, 'w') as f: f.write(text_content)`
- Read: `with open(file_path, 'r') as f: file_content = f.read()`
- Count words: `words = content.split()`, `word_count = len(words)`
- Count lines: `lines = content.splitlines()`, `line_count = len(lines)`
- Count chars: `char_count = len(content)`
- Exception handling: `try: ... except FileNotFoundError: message = "File not found" except IOError: message = "Error reading file"`

## 🔍 Example
Save to File: text_content = "Hello World", filename = "test.txt"
Expected Output: file saved, message = "File saved successfully"

Read from File: filename = "test.txt"
Expected Output: file_content = "Hello World"

Count Words in File: filename = "test.txt"
Expected Output: word_count = 2, line_count = 1, char_count = 11

## ✅ You Are Done When
- Files are saved correctly to student_files directory
- Files are read and content is displayed
- Word, line, and character counts are accurate
- Exceptions are caught and handled gracefully
