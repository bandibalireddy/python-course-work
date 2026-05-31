# Assignment 15 — Season Finder

## 🎯 What You Will Practice
Learn how to use nested if/else statements and string matching to make complex decisions.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Use nested if/else: first check hemisphere, then check month
2. Northern hemisphere seasons:
   - Winter: December, January, February
   - Spring: March, April, May
   - Summer: June, July, August
   - Autumn: September, October, November
3. Southern hemisphere: opposite seasons (Winter when it's Summer in Northern)
4. Set weather_tip based on season (e.g., "Wear warm clothes" for Winter)
5. Set months_in_season as a list of the 3 months in that season

## 💡 Hints
- Use if hemisphere == 'Northern': then check month
- Use elif hemisphere == 'Southern': then check month with opposite seasons
- Create lists for each season's months
- Set appropriate weather tips for each season

## 🔍 Example
Input: month = "January", hemisphere = "Northern"
Expected Output: season = "Winter", weather_tip = "Wear warm clothes", months_in_season = ["December", "January", "February"]

Input: month = "January", hemisphere = "Southern"
Expected Output: season = "Summer", weather_tip = "Stay cool and hydrated", months_in_season = ["December", "January", "February"]

## ✅ You Are Done When
- Both hemispheres are handled correctly
- All 12 months map to the correct season
- Weather tips are appropriate for each season
- months_in_season shows the correct 3 months
