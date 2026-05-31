# Assignment 4 — Grocery List Manager

## 🎯 What You Will Practice
Learn how to work with lists, add and remove items, and manage state across multiple form submissions.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. If action is "Add Item":
   - Add `item_name` to the `grocery_list` (only if it's not already there)
   - Set `message` to something like "Added [item] to list"
2. If action is "Remove Item":
   - Check if `item_name` exists in the list
   - If it exists, remove it and set a success message
   - If it doesn't exist, set `message = "Item not found"`
3. If action is "View List":
   - Just display the list (no changes needed)
4. If action is "Clear List":
   - Empty the `grocery_list` completely
   - Set a message like "List cleared"

## 💡 Hints
- Use `.append()` to add an item to a list
- Use `.remove()` to remove an item from a list
- Use `if item in list` to check if something exists
- Use `list = []` to clear a list
- The `grocery_list` is already created for you from the hidden input

## 🔍 Example
Input: action = "Add Item", item_name = "Apples"
Expected Output: grocery_list = ["Apples"], message = "Added Apples to list"

Input: action = "Remove Item", item_name = "Bananas" (when Bananas is not in list)
Expected Output: message = "Item not found"

## ✅ You Are Done When
- You can add items to the list
- You can remove items that exist
- Trying to remove a non-existent item shows "Item not found"
- Clear list empties the entire list
- The message always tells the user what happened
