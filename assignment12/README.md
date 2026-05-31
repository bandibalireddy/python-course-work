# Assignment 12 — Student Grade Book

## 🎯 What You Will Practice
Learn how to work with lists of dictionaries, sort data, calculate averages, and assign letter grades programmatically.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Parse `gradebook_str` into a list of dictionaries:
   - Format: "name:score,name:score,..."
   - Create dicts like `{'name': 'John', 'score': 85}`
2. Handle actions:
   - "Add Student": Add new student dict to the list
   - "Clear All": Empty the students list
   - "Show Results": Just display (no changes)
3. Calculate class average:
   - Sum all scores and divide by number of students
4. Find highest scoring student (name and score)
5. Find lowest scoring student (name and score)
6. Sort students by score in descending order (highest first)
7. Assign letter grades to each student:
   - 90-100 → A, 80-89 → B, 70-79 → C, 60-69 → D, below 60 → F
   - Add 'grade' key to each student dict

## 💡 Hints
- Parse similar to assignment 11 (split by comma, then by colon)
- Convert score to float or int
- Use `sum()` and `len()` for average
- Use a loop to find highest/lowest (track max/min as you go)
- Use `sorted(students, key=lambda x: x['score'], reverse=True)` to sort
- Add grade to each dict: `student['grade'] = 'A'`

## 🔍 Example
Input: gradebook_str = "John:85,Jane:92,Bob:78", action = "Show Results"
Expected Output:
- class_average ≈ 85.0
- highest = "Jane: 92"
- lowest = "Bob: 78"
- ranked_students = [{'name': 'Jane', 'score': 92, 'grade': 'B'}, {'name': 'John', 'score': 85, 'grade': 'B'}, {'name': 'Bob', 'score': 78, 'grade': 'C'}]

## ✅ You Are Done When
- Students parse correctly from the string
- Class average calculates correctly
- Highest and lowest students are identified
- Students are ranked from highest to lowest score
- Each student has the correct letter grade
- Add and clear actions work properly
