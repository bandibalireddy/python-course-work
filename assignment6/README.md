# Assignment 6 — Mini Profile Card

## 🎯 What You Will Practice
Learn how to convert data types, work with lists from comma-separated strings, and format text for display.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Convert `hobbies_raw` (a comma-separated string) into a Python list
2. Convert `age` from string to integer
3. Calculate `age_next_year` (age + 1)
4. Count the number of hobbies using `len()`
5. Capitalize `name` properly using `.capitalize()` or `.title()`
6. Capitalize `city` properly using `.capitalize()` or `.title()`

## 💡 Hints
- Use `.split(',')` to turn a comma-separated string into a list
- Use `.strip()` on each item to remove extra spaces
- `int()` converts a string to an integer
- `len(list)` tells you how many items are in a list
- `.capitalize()` makes only the first letter uppercase
- `.title()` makes the first letter of each word uppercase

## 🔍 Example
Input: name = "john", age = "25", hobbies_raw = "reading, swimming, coding", city = "new york"
Expected Output:
- hobbies_list = ["reading", "swimming", "coding"]
- age_next_year = 26
- hobby_count = 3
- name = "John" (or "John")
- city = "New York" (or "New york")

## ✅ You Are Done When
- The hobbies appear as a list (not one long string)
- Age shows as a number, not a string
- Age next year is calculated correctly
- Hobby count matches the number of hobbies entered
- Name and city are properly capitalized
