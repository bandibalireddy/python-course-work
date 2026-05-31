# Assignment 13 — Personal Quiz App (Capstone)

## 🎯 What You Will Practice
Combine everything you've learned: lists of dictionaries, loops, conditionals, string comparison, and scoring logic.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Loop through `QUESTIONS` (a list of 5 question dicts)
2. For each question:
   - Get the student's answer from the `answers` list
   - Compare it to the correct answer (case-insensitive)
   - Track the question text, student's answer, correct answer, and whether it's correct
   - Add all this info to the `results` list as a dictionary
3. Count how many answers are correct (increment `score`)
4. Calculate percentage: `(score / 5) * 100`
5. Assign a performance label:
   - 5/5 correct → "Excellent"
   - 3-4 correct → "Good"
   - 0-2 correct → "Keep Practicing"

## 💡 Hints
- Use `enumerate()` or index to loop through questions and answers together
- Convert both answers to lowercase before comparing
- Build each result dict like: `{'question': ..., 'student_answer': ..., 'correct_answer': ..., 'is_correct': True/False}`
- Use `.append()` to add to results list
- Use if/elif/else for the performance label

## 🔍 Example
Input: answers = ["8", "blue", "7", "paris", "100"]
Expected Output:
- score = 5
- percentage = 100.0
- label = "Excellent"
- results shows all 5 questions with is_correct = True

Input: answers = ["8", "red", "7", "paris", "100"]
Expected Output:
- score = 4
- percentage = 80.0
- label = "Good"
- results shows 4 correct, 1 incorrect

## ✅ You Are Done When
- All 5 questions are graded
- Correct/incorrect status is accurate
- Score counts correctly
- Percentage calculates correctly
- Performance label matches the score range
- Results table shows all question details
- Case doesn't matter (e.g., "Blue" and "blue" both correct)
