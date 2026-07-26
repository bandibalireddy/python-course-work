# Assignment 7 — Grade Classifier

## 🎯 What You Will Practice
Learn how to use if/elif/else chains to handle multiple conditions and provide different outputs based on ranges.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Convert `score` from string to float
2. Use if/elif/else to assign letter grades:
   - 90–100 → grade = "A"
   - 80–89 → grade = "B"
   - 70–79 → grade = "C"
   - 60–69 → grade = "D"
   - below 60 → grade = "F"
3. Assign an encouraging message for each grade (e.g., "Excellent work!" for A)
4. Handle out-of-range scores:
   - If score < 0 or score > 100, set `error` to "Score must be between 0 and 100"

## 💡 Hints
- Convert the score to float first
- Use `>=` and `<=` to check ranges
- Order matters in if/elif/else — check from highest to lowest
- You can combine conditions with `or`
- Set the error message before the grade checks

## 🔍 Example
Input: score = "85"
Expected Output: grade = "B", message = "Good job! Keep it up!"

Input: score = "105"
Expected Output: error = "Score must be between 0 and 100"

Input: score = "92"
Expected Output: grade = "A", message = "Excellent work!"

## ✅ You Are Done When
- All letter grades assign correctly
- Each grade has an encouraging message
- Scores below 0 show an error
- Scores above 100 show an error
- Valid scores show both grade and message
