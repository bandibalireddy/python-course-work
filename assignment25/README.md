# Assignment 25 — Collatz Conjecture

## 🎯 What You Will Practice
Learn how to use while loops, modulo operations, and conditionals inside loops.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. While loop: continue until number reaches 1
2. If number is even: divide by 2
3. If number is odd: multiply by 3 and add 1
4. Append each new value to sequence
5. Track total steps, even steps, and odd steps

## 💡 Hints
- While condition: `while number != 1:`
- Check even: `if number % 2 == 0:`
- Even operation: `number = number // 2`, increment `is_even_steps`
- Odd operation: `number = number * 3 + 1`, increment `is_odd_steps`
- Append: `sequence.append(number)`
- Increment total: `steps += 1`

## 🔍 Example
Input: number = 6
Expected Output: sequence = [6, 3, 10, 5, 16, 8, 4, 2, 1], steps = 8, is_even_steps = 4, is_odd_steps = 4

Input: number = 7
Expected Output: sequence = [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], steps = 16

## ✅ You Are Done When
- Sequence ends at 1
- Even/odd operations are tracked correctly
- Total steps are accurate
- All values are appended to sequence
