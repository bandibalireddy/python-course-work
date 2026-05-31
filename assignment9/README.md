# Assignment 9 — Word Counter & Analyzer

## 🎯 What You Will Practice
Learn how to split text into words, use loops to process text, and find unique items in a list.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Split the text into words using `.split()`
2. Count total words using `len()`
3. Find the longest word by comparing lengths in a loop
4. Find unique words:
   - Convert to a set to remove duplicates
   - Convert back to a list
   - Sort the list alphabetically
5. Count total characters (excluding spaces) — use `.replace()` to remove spaces first

## 💡 Hints
- `text.split()` splits on whitespace by default
- `len(list)` gives you the count
- Use a loop to find the longest word: keep track of the longest you've seen
- `set(list)` removes duplicates
- `sorted(list)` sorts alphabetically
- `text.replace(" ", "")` removes all spaces

## 🔍 Example
Input: text = "Hello world hello Python"
Expected Output:
- word_count = 4
- longest_word = "Python" (or "Hello" — both are 5 letters)
- unique_words = ["Hello", "Python", "world"] (sorted alphabetically)
- char_count = 17 (excluding spaces)

## ✅ You Are Done When
- Word count matches the actual number of words
- Longest word is correctly identified
- Unique words show no duplicates and are sorted
- Character count excludes spaces
- All statistics appear on the page
