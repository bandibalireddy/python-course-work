# Assignment 32 — BMI Calculator

## 🎯 What You Will Practice
Learn how to define functions with multiple parameters and chained function calls.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Define calculate_bmi_metric(weight_kg, height_m): returns BMI rounded to 1 decimal
2. Define calculate_bmi_imperial(weight_lbs, height_ft, height_in): converts to metric first, then calculates
3. Define get_bmi_category(bmi): returns Underweight/Normal/Overweight/Obese
4. Define get_health_advice(category): returns advice string per category
5. Call correct function based on unit_system

## 💡 Hints
- BMI formula: weight / (height * height)
- Imperial conversion: weight_kg = weight_lbs / 2.20462, height_m = (height_ft * 12 + height_in) * 0.0254
- Categories: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), Obese (>=30)
- Round: `round(bmi, 1)`

## 🔍 Example
Input: weight = 70, height = 1.75, unit_system = "Metric"
Expected Output: bmi = 22.9, category = "Normal", health_advice = "Maintain a healthy lifestyle"

Input: weight = 180, height = 5, height_inches = 10, unit_system = "Imperial"
Expected Output: bmi = 25.8, category = "Overweight", health_advice = "Consider increasing physical activity"

## ✅ You Are Done When
- Metric BMI is calculated correctly
- Imperial conversion and BMI are correct
- Category is determined based on BMI ranges
- Health advice is appropriate for each category
