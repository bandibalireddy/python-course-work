# Assignment 21 — Country Capital Quiz

## 🎯 What You Will Practice
Learn how to use dictionaries for key lookup, comparison, and scoring.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Loop through COUNTRIES dict
2. Get student answer from POST for each country (use country name as key)
3. Compare answer (case insensitive) to correct capital
4. Append to results: {'country': ..., 'correct': ..., 'given': ..., 'is_correct': ...}
5. Calculate score and percentage

## 💡 Hints
- Loop: `for country, correct_capital in COUNTRIES.items():`
- Get answer: `student_answer = request.POST.get(country, '')`
- Compare: `is_correct = student_answer.lower() == correct_capital.lower()`
- Append: `results.append({'country': country, 'correct': correct_capital, 'given': student_answer, 'is_correct': is_correct})`
- Calculate: `percentage = int((score / total) * 100)`

## 🔍 Example
Input: France = "Paris", Japan = "Tokyo", Brazil = "Rio"
Expected Output: score = 2, percentage = 20, results shows correct for France and Japan, incorrect for Brazil

## ✅ You Are Done When
- All 10 countries are checked
- Comparison is case insensitive
- Score and percentage are calculated correctly
- Results table shows all answers
