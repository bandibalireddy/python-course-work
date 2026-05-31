# Assignment 27 — Day Type Classifier

## 🎯 What You Will Practice
Learn how to use match/case statements for pattern matching and string classification.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. match/case on day to determine day_type
2. Weekday: set typical work_hours (9am-5pm)
3. Weekend: set work_hours to "Day Off"
4. Use nested match/case or if/else for country-specific notes
5. Set fun_suggestion based on day type

## 💡 Hints
- Weekdays: Monday, Tuesday, Wednesday, Thursday, Friday
- Weekends: Saturday, Sunday
- match/case syntax:
  ```python
  match day:
      case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
          day_type = "Weekday"
          work_hours = "9am-5pm"
      case "Saturday" | "Sunday":
          day_type = "Weekend"
          work_hours = "Day Off"
  ```
- Fun suggestions: "Time to be productive!" for weekdays, "Relax and enjoy!" for weekends
- Country-specific notes: e.g., "Sunday is a holiday in India"

## 🔍 Example
Input: day = "Monday", country = "USA"
Expected Output: day_type = "Weekday", work_hours = "9am-5pm", fun_suggestion = "Time to be productive!"

Input: day = "Saturday", country = "India"
Expected Output: day_type = "Weekend", work_hours = "Day Off", fun_suggestion = "Relax and enjoy!", public_holiday_note = "Sunday is a holiday in India"

## ✅ You Are Done When
- All 7 days are classified correctly
- Weekdays and weekends are distinguished
- Work hours are set appropriately
- Fun suggestions are provided
- Country-specific notes are included
