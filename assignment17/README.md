# Assignment 17 — Sum of Range

## 🎯 What You Will Practice
Learn how to use for loops with range(), the accumulator pattern, and conditional filtering.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Use a for loop from start to end using step
2. Apply filter based on filter_type using if/elif
3. Filter types: All Numbers, Even Only, Odd Only, Multiples of 3
4. Append qualifying numbers to included_numbers
5. Accumulate total and count

## 💡 Hints
- Use `for i in range(start, end + 1, step):` to loop with step
- For even: `if i % 2 == 0:`
- For odd: `if i % 2 != 0:`
- For multiples of 3: `if i % 3 == 0:`
- Accumulate: `total += i` and `count += 1`

## 🔍 Example
Input: start = 1, end = 10, step = 1, filter_type = "Even Only"
Expected Output: included_numbers = [2, 4, 6, 8, 10], total = 30, count = 5

Input: start = 1, end = 10, step = 1, filter_type = "Multiples of 3"
Expected Output: included_numbers = [3, 6, 9], total = 18, count = 3

## ✅ You Are Done When
- All four filter types work correctly
- The loop uses the correct step value
- Total and count are calculated accurately
- Average is displayed when count > 0
