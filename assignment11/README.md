# Assignment 11 — Shopping Cart

## 🎯 What You Will Practice
Learn how to work with lists of dictionaries, parse complex string data, and apply conditional logic for discounts.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Parse `cart_str` into a list of dictionaries:
   - The string format is "name:price,name:price,..."
   - Split by comma to get items
   - Split each item by colon to get name and price
   - Create dicts like `{'name': 'apple', 'price': 2.5}`
2. Handle actions:
   - "Add Item": Add new item dict to cart list
   - "Remove Last Item": Remove the last item from the list
   - "Clear Cart": Empty the cart list
3. Calculate total by summing all prices
4. If total > 50:
   - Apply 10% discount (total * 0.1)
   - Set `discount` to the discount amount
   - Set `final_price` to total - discount
5. If total <= 50:
   - Set `discount = None`
   - Set `final_price = total`

## 💡 Hints
- Use `.split(',')` to separate items
- Use `.split(':')` to separate name from price
- Convert price to float when creating the dict
- Use `.append()` to add items
- Use `.pop()` or slicing to remove the last item
- Use `list = []` to clear the list
- Calculate discount as `total * 0.1`

## 🔍 Example
Input: cart_str = "apple:2.5,banana:1.5", action = "Show Results"
Expected Output:
- cart = [{'name': 'apple', 'price': 2.5}, {'name': 'banana', 'price': 1.5}]
- total = 4.0
- discount = None
- final_price = 4.0

Input: cart with total = 60.0
Expected Output:
- total = 60.0
- discount = 6.0
- final_price = 54.0

## ✅ You Are Done When
- Items parse correctly from the string format
- Add, remove, and clear actions work
- Total calculates correctly
- 10% discount applies when total > 50
- Final price shows correctly with or without discount
