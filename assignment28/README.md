# Assignment 28 — HTTP Status Decoder

## 🎯 What You Will Practice
Learn how to use match/case with ranges/guards and structured data lookup.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. match/case on code:
   - 200 → "OK", 201 → "Created", 301 → "Moved Permanently"
   - 400 → "Bad Request", 401 → "Unauthorized", 403 → "Forbidden"
   - 404 → "Not Found", 500 → "Internal Server Error"
   - 502 → "Bad Gateway", 503 → "Service Unavailable"
   - case _: → "Unknown Status Code"
2. Determine category based on first digit (1xx, 2xx, 3xx, 4xx, 5xx)
3. Set is_error = True for 4xx and 5xx codes
4. Set a helpful description for each code

## 💡 Hints
- match/case syntax:
  ```python
  match code:
      case 200:
          meaning = "OK"
          description = "Request succeeded"
      case 404:
          meaning = "Not Found"
          description = "Resource not found"
      case _:
          meaning = "Unknown Status Code"
          description = "Status code not recognized"
  ```
- Category: `category = f"{str(code)[0]}xx"`
- is_error: `is_error = code >= 400`

## 🔍 Example
Input: code = 200
Expected Output: category = "2xx", meaning = "OK", description = "Request succeeded", is_error = False

Input: code = 404
Expected Output: category = "4xx", meaning = "Not Found", description = "Resource not found", is_error = True

## ✅ You Are Done When
- All specified status codes are decoded correctly
- Category is determined from first digit
- is_error is set correctly for 4xx and 5xx
- Descriptions are helpful and accurate
