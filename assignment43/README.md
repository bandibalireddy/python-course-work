# Assignment 43 — Exception Hierarchy Explorer

## 🎯 What You Will Practice
Learn how to create custom exceptions, understand exception hierarchy, and use raise/except with as.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find the class methods and trigger_scenario function:
```python
# ── STUDENT CODE START ──

# ── STUDENT CODE END ──
```

## 📝 Your Tasks
1. AppError.__init__(self, message, error_code): store both, call super().__init__(message)
2. ValidationError: adds field_name attribute
3. NetworkError: adds timeout_seconds attribute
4. DatabaseError: adds db_name attribute
5. trigger_scenario(): use if/elif to raise the correct exception per scenario
6. Wrap call in try/except catching each type separately, most specific first

## 💡 Hints
- AppError.__init__: `self.message = message`, `self.error_code = error_code`, `super().__init__(message)`
- ValidationError.__init__: `super().__init__(message, error_code)`, `self.field_name = field_name`
- trigger_scenario scenarios:
  - Email: `if '@' not in value: raise ValidationError("Invalid email", "VAL001", field_name="email")`
  - Age: `if age < 0 or age > 150: raise ValidationError("Invalid age", "VAL002", field_name="age")`
  - Network: `raise NetworkError("Network timeout", "NET001", timeout_seconds=30)`
  - Database: `raise DatabaseError("Connection failed", "DB001", db_name="main_db")`
  - Divide by Zero: `result = 1/0`
  - Catch All: `raise AppError("General error", "GEN001")`
  - No Error: `return "All systems OK"`
- try/except order: most specific first (ValidationError, NetworkError, DatabaseError), then AppError, then Exception

## 🔍 Example
Scenario: "Validate Email", input_value = "invalid"
Expected Output: caught_exception = ValidationError, exception_type = "ValidationError", error_code = "VAL001", extra_attributes = {"field_name": "email"}

Scenario: "Simulate Network Timeout"
Expected Output: caught_exception = NetworkError, exception_type = "NetworkError", error_code = "NET001", extra_attributes = {"timeout_seconds": 30}

## ✅ You Are Done When
- All custom exceptions are defined with proper attributes
- trigger_scenario raises correct exception per scenario
- try/except catches exceptions in proper order (most specific first)
- Exception type, message, error_code, and extra attributes are displayed
- Exception hierarchy is shown
