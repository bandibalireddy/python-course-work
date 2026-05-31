# Assignment 5 — Number List Stats

## 🎯 What You Will Practice
Learn how to work with lists of numbers, convert string data, and use built-in functions to calculate statistics.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Convert each item in `number_list` from string to float (or int)
2. Find the minimum value using `min()`
3. Find the maximum value using `max()`
4. Calculate the sum using `sum()`
5. Calculate the average (sum divided by the number of items)
6. Sort the list in ascending order using `sorted()`
7. If the list is empty, set `error_message` to "Please enter some numbers"

## 💡 Hints
- Use a loop or list comprehension to convert strings to numbers
- `min(list)` finds the smallest number
- `max(list)` finds the largest number
- `sum(list)` adds all numbers together
- `len(list)` tells you how many items are in the list
- `sorted(list)` returns a new sorted list (doesn't change the original)
- Check if the list is empty before doing calculations

## 🔍 Example
Input: numbers = "4, 7, 2, 9"
Expected Output:
- minimum = 2
- maximum = 9
- total = 22
- average = 5.5
- sorted_list = [2, 4, 7, 9]

## ✅ You Are Done When
- All five statistics calculate correctly
- The sorted list shows numbers in order
- Empty input shows an error message
- The calculations work with both integers and decimals
