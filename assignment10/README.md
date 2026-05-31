# Assignment 10 — FizzBuzz with Custom Rules

## 🎯 What You Will Practice
Learn how to use for loops, check multiple conditions, and build lists programmatically.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Convert `limit` from string to integer
2. Create a for loop that goes from 1 to `limit` (inclusive)
3. For each number:
   - If divisible by 3 AND 5: append `fizz_word + buzz_word` to `results`
   - If divisible by 3 only: append `fizz_word` to `results`
   - If divisible by 5 only: append `buzz_word` to `results`
   - Otherwise: append the number itself to `results`

## 💡 Hints
- Use `range(1, limit + 1)` to loop from 1 to limit (inclusive)
- Use `%` to check divisibility
- Check "divisible by both" first, then check individual conditions
- Use `and` to check if both conditions are true
- Use `.append()` to add items to the results list
- The default fizz_word is "Fizz" and buzz_word is "Buzz"

## 🔍 Example
Input: limit = "15", fizz_word = "Fizz", buzz_word = "Buzz"
Expected Output: results = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]

Input: limit = "5", fizz_word = "Foo", buzz_word = "Bar"
Expected Output: results = [1, 2, "Foo", 4, "Bar"]

## ✅ You Are Done When
- Numbers divisible by 3 show the fizz word
- Numbers divisible by 5 show the buzz word
- Numbers divisible by both show both words combined
- Other numbers show as regular numbers
- Custom words work when you change them
