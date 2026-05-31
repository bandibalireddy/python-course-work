# Assignment 14 — Traffic Light Advisor

## 🎯 What You Will Practice
Learn how to use if/elif/else statements with comparison operators to make decisions based on multiple conditions.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Check the speed against the zone limits:
   - School Zone limit: 15 mph
   - Residential limit: 25 mph
   - City Center limit: 35 mph
   - Highway limit: 70 mph
2. Set status based on how much over the limit:
   - "Safe" if at or below the limit
   - "Warning" if within 10 mph over the limit
   - "Danger" if more than 10 mph over the limit
3. Set advice with a descriptive message based on the status and zone type

## 💡 Hints
- Use if/elif/else to check each zone type
- Calculate how much over the limit: `speed - limit`
- Use comparison operators: <=, >, etc.
- Set meaningful advice messages for each status

## 🔍 Example
Input: speed = 20, zone_type = "School Zone"
Expected Output: status = "Danger", advice = "You're going 5 mph over the limit in a school zone! Slow down immediately!"

Input: speed = 30, zone_type = "Highway"
Expected Output: status = "Safe", advice = "You're driving safely on the highway."

## ✅ You Are Done When
- All four zone types are checked correctly
- Status is set to Safe/Warning/Danger based on speed
- Advice messages are helpful and specific to the zone
