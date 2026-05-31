# Assignment 16 — Multiplication Table

## 🎯 What You Will Practice
Learn how to use for loops and range() to generate sequences of data.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Use a for loop from 1 to limit (inclusive)
2. Each iteration: calculate number x multiplier
3. Append dict {'multiplier': i, 'result': product} to table list

## 💡 Hints
- Use `for i in range(1, limit + 1):` to loop from 1 to limit inclusive
- Calculate product: `number * i`
- Append to list: `table.append({'multiplier': i, 'result': product})`

## 🔍 Example
Input: number = 5, limit = 3
Expected Output: table = [{'multiplier': 1, 'result': 5}, {'multiplier': 2, 'result': 10}, {'multiplier': 3, 'result': 15}]

## ✅ You Are Done When
- The table shows the correct multiplication results
- The loop goes from 1 to the limit (inclusive)
- Each row has the multiplier and result
