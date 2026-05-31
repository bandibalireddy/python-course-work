# Assignment 8 — Number Guessing Game

## 🎯 What You Will Practice
Learn how to compare numbers, track state across submissions, and provide feedback based on comparisons.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Convert `guess` from string to integer
2. Compare `guess` to `SECRET_NUMBER` (which is 42)
3. If guess is too low:
   - Set `hint = "Too low! Go higher."`
4. If guess is too high:
   - Set `hint = "Too high! Go lower."`
5. If guess is correct:
   - Set `hint = "Correct!"`
   - Set `won = True`

## 💡 Hints
- The `SECRET_NUMBER` is already defined at the top of the file
- Use `<` for less than, `>` for greater than, `==` for equal
- The `attempts` variable is already being tracked for you
- Convert the guess to integer before comparing
- Check for correct answer first, then too high/low

## 🔍 Example
Input: guess = "30"
Expected Output: hint = "Too low! Go higher.", won = False

Input: guess = "50"
Expected Output: hint = "Too high! Go lower.", won = False

Input: guess = "42"
Expected Output: hint = "Correct!", won = True

## ✅ You Are Done When
- Low guesses show "Too low! Go higher."
- High guesses show "Too high! Go lower."
- Correct guess shows "Correct!" and won = True
- The attempts counter increases with each guess
- The win message appears when you guess correctly
