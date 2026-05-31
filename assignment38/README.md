# Assignment 38 — Student Gradebook OOP

## 🎯 What You Will Practice
Learn how to use classes, lists of objects, and methods that operate on collections.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find the class methods:
```python
# ── STUDENT CODE START ──

# ── STUDENT CODE END ──
```

## 📝 Your Tasks
1. Student.__init__: name, student_id, grades = {}
2. Student.add_grade: grades[subject] = score
3. Student.get_average: mean of grades.values()
4. Student.get_letter_grade: based on average (same scale as assignment 7)
5. Gradebook.__init__: self.students = []
6. Gradebook.add_student: append to list
7. Gradebook.get_class_average: average of all student averages
8. Gradebook.get_top_student: student with highest average
9. Gradebook.get_ranked_students: sorted list by average descending

## 💡 Hints
- Student.__init__: `self.name = name`, `self.student_id = student_id`, `self.grades = {}`
- Student.add_grade: `self.grades[subject] = score`
- Student.get_average: `sum(self.grades.values()) / len(self.grades.values())` if grades exist
- Student.get_letter_grade: use if/elif with average (A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60)
- Gradebook.__init__: `self.students = []`
- Gradebook.add_student: `self.students.append(student)`
- Gradebook.get_class_average: average of all `student.get_average()`
- Gradebook.get_top_student: `max(self.students, key=lambda s: s.get_average())`
- Gradebook.get_ranked_students: `sorted(self.students, key=lambda s: s.get_average(), reverse=True)`

## 🔍 Example
Add Student: name = "Alice", student_id = "001"
Expected Output: Student added with empty grades dict

Add Grade: student_id = "001", subject = "Math", score = 95
Expected Output: student.grades = {"Math": 95}

Get Average: student.grades = {"Math": 95, "Science": 88}
Expected Output: average = 91.5

## ✅ You Are Done When
- Students can be added to gradebook
- Grades can be added to students
- Student average is calculated correctly
- Letter grade is assigned based on average
- Class average is calculated from all students
- Top student is identified correctly
- Students are ranked by average descending
- Gradebook state persists across form submissions
