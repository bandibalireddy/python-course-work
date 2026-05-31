# Assignment 30 — Password Strength Checker

## 🎯 What You Will Practice
Learn how to define functions, use boolean return values, string methods, and loops.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Define 6 functions above the view:
   - has_min_length(pwd, min_len=8): returns True if len(pwd) >= min_len
   - has_uppercase(pwd): returns True if pwd has at least one uppercase letter
   - has_lowercase(pwd): returns True if pwd has at least one lowercase letter
   - has_digit(pwd): returns True if pwd has at least one digit
   - has_special_char(pwd): returns True if pwd has at least one special character
   - calculate_strength(score): returns "Weak"(0-2), "Medium"(3), "Strong"(4), "Very Strong"(5)
2. Inside view: call each function, build checks dict, total score, determine strength

## 💡 Hints
- Check uppercase: `any(c.isupper() for c in pwd)`
- Check lowercase: `any(c.islower() for c in pwd)`
- Check digit: `any(c.isdigit() for c in pwd)`
- Check special: `any(not c.isalnum() for c in pwd)`
- Build checks: `checks = {'min_length': has_min_length(password), ...}`
- Score: `score = sum(checks.values())`

## 🔍 Example
Input: password = "Pass123!"
Expected Output: score = 5, strength = "Very Strong", all checks = True

Input: password = "pass"
Expected Output: score = 1, strength = "Weak", only lowercase = True

## ✅ You Are Done When
- All 6 functions are defined correctly
- Each check returns True/False
- Score is calculated from passed checks
- Strength is determined based on score
- Checks dict shows all results
