# Assignment 18 — Pattern Printer

## 🎯 What You Will Practice
Learn how to use nested for loops and string building to create visual patterns.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Use if/elif for each pattern type
2. Use nested for loops and string building to create each line
3. Append each line as a string to pattern_lines
4. Right Triangle: 1 char on row 1, 2 on row 2, etc.
5. Pyramid: centered, row 1 has 1, row 2 has 3, etc. (odd numbers: 1, 3, 5, 7...)
6. Diamond: pyramid + inverted pyramid (share the middle row)
7. Inverted Triangle: reverse of right triangle

## 💡 Hints
- Right Triangle: outer loop for rows, inner loop for chars per row
- Pyramid: use spaces for centering: `(' ' * (rows - i - 1)) + (character * (2*i + 1))`
- Diamond: combine pyramid and inverted pyramid logic
- Inverted Triangle: start from rows and go down to 1
- Build each line as a string and append to pattern_lines

## 🔍 Example
Input: rows = 3, pattern_type = "Right Triangle", character = "*"
Expected Output:
```
*
**
***
```

Input: rows = 3, pattern_type = "Pyramid", character = "*"
Expected Output:
```
  *
 ***
*****
```

## ✅ You Are Done When
- All four pattern types work correctly
- Patterns are properly centered (pyramid, diamond)
- Diamond shows both pyramid and inverted pyramid
- Character is used correctly in all patterns
