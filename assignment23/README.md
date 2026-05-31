# Assignment 23 — Inventory Manager

## 🎯 What You Will Practice
Learn how to use nested dictionaries, dict methods, and arithmetic operations.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Parse inventory_data_str into nested inventory dict: {item_name: {'quantity': int, 'price': float}}
   - Format: "name|qty|price;name|qty|price"
2. Handle each action using dict operations:
   - Add Item: add new item to dict
   - Update Quantity: update existing item's quantity
   - Remove Item: delete item from dict
   - View Inventory: show all items
3. Calculate total_value = sum of (qty * price) for all items
4. Find low_stock items (quantity < 5)
5. Serialize inventory back to string for hidden field

## 💡 Hints
- Parse: split by ';' then by '|'
- Add: `inventory[item_name] = {'quantity': int(quantity), 'price': float(price)}`
- Update: `if item_name in inventory: inventory[item_name]['quantity'] = int(quantity)`
- Remove: `if item_name in inventory: del inventory[item_name]`
- Total value: loop through inventory and sum `info['quantity'] * info['price']`
- Low stock: `[item for item, info in inventory.items() if info['quantity'] < 5]`

## 🔍 Example
Input: action = "Add Item", item_name = "Widget", quantity = "10", price = "5.99"
Expected Output: inventory = {"Widget": {"quantity": 10, "price": 5.99}}, total_value = 59.90

## ✅ You Are Done When
- All four actions work correctly
- Inventory persists across form submissions
- Total value is calculated correctly
- Low stock items are identified
