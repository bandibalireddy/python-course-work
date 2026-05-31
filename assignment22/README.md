# Assignment 22 — Student Report Card

## 🎯 What You Will Practice
Learn how to use dictionaries, values(), min/max with dicts, and averaging.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Build report dict from subjects_raw (skip empty entries)
2. Calculate GPA (average of all scores)
3. Find best and worst subject using dict operations
4. Assign letter grade to each subject (same scale as assignment 7):
   - A: 90-100
   - B: 80-89
   - C: 70-79
   - D: 60-69
   - F: 0-59
5. Build grade_report dict

## 💡 Hints
- Skip empty: `if subject and score:`
- Build dict: `report[subject] = int(score)`
- GPA: `sum(report.values()) / len(report.values())`
- Best: `max(report.items(), key=lambda x: x[1])`
- Worst: `min(report.items(), key=lambda x: x[1])`
- Letter grade: use if/elif/else based on score

## 🔍 Example
Input: Math=95, Science=88, English=92
Expected Output: gpa=91.67, best_subject="Math", worst_subject="Science", grade_report={"Math": "A", "Science": "B", "English": "A"}

## ✅ You Are Done When
- Report dict is built correctly
- GPA is calculated accurately
- Best and worst subjects are identified
- Letter grades are assigned correctly
