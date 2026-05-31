# Assignment 29 — Unit Converter

## 🎯 What You Will Practice
Learn how to define functions, use parameters, return values, and call functions.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Define 6 conversion functions above the index() function:
   - km_to_miles(km): km × 0.621371
   - miles_to_km(miles): miles ÷ 0.621371
   - kg_to_lbs(kg): kg × 2.20462
   - lbs_to_kg(lbs): lbs ÷ 2.20462
   - celsius_to_fahrenheit(c): (c × 9/5) + 32
   - fahrenheit_to_celsius(f): (f - 32) × 5/9
2. Each function takes one parameter and returns the converted value rounded to 2 decimal places
3. Inside the view: if/elif to call the correct function based on conversion_type
4. Set formula_used to a string showing the formula

## 💡 Hints
- Function definition: `def km_to_miles(km): return round(km * 0.621371, 2)`
- Round to 2 decimal places: `round(value, 2)`
- Call function: `result = km_to_miles(value)`
- Set formula: `formula_used = "km × 0.621371"`

## 🔍 Example
Input: value = 100, conversion_type = "km to miles"
Expected Output: result = 62.14, formula_used = "km × 0.621371"

Input: value = 0, conversion_type = "Celsius to Fahrenheit"
Expected Output: result = 32.0, formula_used = "(C × 9/5) + 32"

## ✅ You Are Done When
- All 6 functions are defined correctly
- Functions return values rounded to 2 decimal places
- Correct function is called based on conversion_type
- Formula string is displayed
