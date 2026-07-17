# Assignment 2 — String Inspector

## 🎯 What You Will Practice
Learn how to work with strings, use string methods to change text, and count characters using loops.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────
text = "hello world"
print(len(text))
print(text.upper())
print(text.lower())
print(text.count('o'))
print(text[::-1])



# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Calculate the length of the string using `len()`
2. Convert the string to uppercase using `.upper()`
3. Convert the string to lowercase using `.lower()`
4. Reverse the string (hint: use slicing with `[::-1]`)
5. Count the vowels (a, e, i, o, u) — make it case-insensitive so it counts both uppercase and lowercase vowels
6. Store each result in its corresponding variable

## 💡 Hints
- `len(text)` gives you the number of characters
- `text.upper()` makes everything uppercase
- `text[::-1]` reverses a string
- Loop through each character and check if it's a vowel
- Convert each character to lowercase before checking if it's a vowel

## 🔍 Example
Input: user_text = "Hello World"
Expected Output:
- length = 11
- uppercase = "HELLO WORLD"
- lowercase = "hello world"
- reversed_text = "dlroW olleH"
- vowel_count = 3

## ✅ You Are Done When
- All five statistics show correctly on the page
- Vowel counting works for both uppercase and lowercase letters
- The string reversal shows the text backwards
