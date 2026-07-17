# Assignment 3 — Even/Odd & Divisibility Checker

## 🎯 What You Will Practice
Learn how to use the modulo operator (%) to check divisibility and use boolean values (True/False) in Python.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────
num = int(num)
if num % 2 == 0 :
   print("even")
else :
   print("odd") and 
   if num % 3 == 0 :
      print("div_by_3")
   else num % 5 == 0 :
      print("div_by_5")
   else num % both 3 & 5 == 0 :
      print("div_by_both_3_and_5")




# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Convert the input to an integer
2. Check if the number is even or odd using `% 2`
   - If even, set `is_even` to "Even"
   - If odd, set `is_even` to "Odd"
3. Check if divisible by 3 using `% 3` — store True or False in `div_by_3`
4. Check if divisible by 5 using `% 5` — store True or False in `div_by_5`
5. Check if divisible by BOTH 3 and 5 — store True or False in `div_by_both`

## 💡 Hints
- `%` is the modulo operator — it gives you the remainder
- `number % 2 == 0` means the number is even
- `number % 3 == 0` means the number is divisible by 3
- Use `and` to check if both conditions are true
- Remember to convert the string input to an integer first

## 🔍 Example
Input: number = "15"
Expected Output:
- is_even = "Odd"
- div_by_3 = True
- div_by_5 = True
- div_by_both = True

Input: number = "7"
Expected Output:
- is_even = "Odd"
- div_by_3 = False
- div_by_5 = False
- div_by_both = False

## ✅ You Are Done When
- Even/odd detection works correctly
- All divisibility checks show True or False
- The "divisible by both" check only shows True when both conditions are met
