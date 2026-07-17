# Assignment 1 — Simple Calculator

## 🎯 What You Will Practice
Learn how to work with variables, convert strings to numbers, and use if/elif/else statements to make decisions in your code.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────
num_1 = float(num_1)
num_2 = float(num_2)
if "addition" :
   print(num_1 + num_2 )
elif "subtraction" :
   print(num_1 - num_2 )
elif "multiply" :
   print(num_1 * num_2 )
elif division :
   if num_2 == 0
   print(cannot divide by zero)
   else :
   print(num_1 / num_2 )

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Convert the input strings `number1` and `number2` to floats
2. Use if/elif/else to check which operation was selected
3. Perform the correct math operation:
   - Add: `number1 + number2`
   - Subtract: `number1 - number2`
   - Multiply: `number1 * number2`
   - Divide: `number1 / number2`
4. Handle division by zero — if someone tries to divide by zero, set `result` to an error message like "Cannot divide by zero"
5. Store the final answer in the `result` variable

## 💡 Hints
- Use `float()` to convert a string to a number
- The `operation` variable tells you which math to do
- For division, check if `number2` equals 0 before dividing
- Use `==` to compare values, not `=` (that's for assigning)

## 🔍 Example
Input: number1 = "10", number2 = "5", operation = "Add"
Expected Output: result = 15.0

Input: number1 = "10", number2 = "0", operation = "Divide"
Expected Output: result = "Cannot divide by zero"

## ✅ You Are Done When
- You can add, subtract, multiply, and divide two numbers
- Division by zero shows a helpful error message
- The result appears on the page after clicking "Calculate"