# Assignment 24 — Countdown Timer

## 🎯 What You Will Practice
Learn how to use while loops, decrement operations, and list building.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. While loop starting from start, decrementing by step, stopping at stop_at
2. Append each value to countdown_steps
3. Count total_steps taken
4. Add "Blast Off!" or "Done!" as final element

## 💡 Hints
- Initialize: `current = start`
- While condition: `while current >= stop_at:`
- Append: `countdown_steps.append(current)`
- Decrement: `current -= step`
- Count: `total_steps += 1`
- Final message: `countdown_steps.append("Blast Off!")` or `"Done!"`

## 🔍 Example
Input: start = 10, step = 1, stop_at = 0
Expected Output: countdown_steps = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, "Blast Off!"], total_steps = 11

Input: start = 10, step = 2, stop_at = 0
Expected Output: countdown_steps = [10, 8, 6, 4, 2, 0, "Blast Off!"], total_steps = 6

## ✅ You Are Done When
- Countdown works with different start values
- Step value is respected
- Loop stops at stop_at correctly
- Total steps are counted accurately
- Final message is added
