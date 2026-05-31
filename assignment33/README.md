# Assignment 33 — Text Formatter Library

## 🎯 What You Will Practice
Learn how to define functions, string manipulation, and multiple return values.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Define 6 text formatting functions:
   - slugify: lowercase, replace spaces with hyphens, remove special chars
   - titlecase: capitalize first letter of each word
   - truncate: cut at max_len and add "..." if longer
   - word_wrap: insert newline every `width` characters at word boundaries
   - remove_extra_spaces: collapse multiple spaces into one
   - count_sentences: count sentences by counting . ! ?
2. Build results dict with output of each function

## 💡 Hints
- slugify: `text.lower().replace(' ', '-').strip('.,!?;:')`
- titlecase: `text.title()` or `' '.join(word.capitalize() for word in text.split())`
- truncate: `text[:max_len] + '...' if len(text) > max_len else text`
- word_wrap: split into words, rebuild with newlines at width
- remove_extra_spaces: `' '.join(text.split())`
- count_sentences: `text.count('.') + text.count('!') + text.count('?')`

## 🔍 Example
Input: text = "Hello World! This is a test."
Expected Output:
- slugify: "hello-world-this-is-a-test"
- titlecase: "Hello World! This Is A Test."
- truncate (max_len=20): "Hello World! This..."
- word_wrap (width=10): "Hello\nWorld!\nThis is\na test."
- remove_extra_spaces: "Hello World! This is a test."
- count_sentences: 2

## ✅ You Are Done When
- All 6 functions work correctly
- Results dict contains all transformations
- Original text is displayed for comparison
