# Assignment 41 — Safe Calculator with Exceptions

## 🎯 What You Will Practice
Learn how to use try/except, multiple exception types, raising exceptions, and finally blocks.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. try/except block wrapping ALL calculations
2. Catch ValueError: if inputs cannot be converted to numbers
3. Catch ZeroDivisionError: if dividing by zero
4. Catch TypeError: if operation receives wrong types
5. Custom check: raise ValueError if Square Root of negative number
6. Set error_type and error_message for any exception caught
7. Set was_successful = True only if no exception occurred
8. Add a finally block that logs the attempt (append to attempt_log)

## 💡 Hints
- try/except structure:
  ```python
  try:
      # calculation code
  except ValueError as e:
      error_type = "ValueError"
      error_message = str(e)
  except ZeroDivisionError as e:
      error_type = "ZeroDivisionError"
      error_message = "Cannot divide by zero"
  except TypeError as e:
      error_type = "TypeError"
      error_message = str(e)
  ```
- Square root check: `if operation == "Square Root" and num1 < 0: raise ValueError("Cannot calculate square root of negative number")`
- finally block: `finally: attempt_log.append(f"Attempt: {operation} - Success: {was_successful}")`

## 🔍 Example
Input: num1 = 10, num2 = 0, operation = "Divide"
Expected Output: error_type = "ZeroDivisionError", error_message = "Cannot divide by zero", was_successful = False

Input: num1 = -4, operation = "Square Root"
Expected Output: error_type = "ValueError", error_message = "Cannot calculate square root of negative number"

Input: num1 = 10, num2 = 2, operation = "Add"
Expected Output: result = 12, was_successful = True

## ✅ You Are Done When
- All exception types are caught correctly
- Custom ValueError is raised for negative square root
- error_type and error_message are set appropriately
- was_successful is True only on success
- attempt_log records all attempts in finally block
