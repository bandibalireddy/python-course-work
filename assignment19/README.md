# Assignment 19 — Contact Book

## 🎯 What You Will Practice
Learn how to use dictionaries for CRUD operations (Create, Read, Update, Delete).

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Parse contacts_data_str into contacts dict: {name: {'phone': ..., 'email': ...}}
   - Format: "name|phone|email;name|phone|email"
2. If Add Contact: add new contact to dict
3. If Search Contact: look up by name, set result to contact dict or "Not Found"
4. If Delete Contact: remove from dict if exists
5. If View All: result = entire contacts dict
6. Serialize contacts dict back to string for hidden field

## 💡 Hints
- Parse: split by ';' to get contacts, then split each by '|' to get name, phone, email
- Add: `contacts[name] = {'phone': phone, 'email': email}`
- Search: `result = contacts.get(name, "Not Found")`
- Delete: `if name in contacts: del contacts[name]`
- Serialize: join with '|' for each contact, then ';' between contacts

## 🔍 Example
Input: action = "Add Contact", contact_name = "John", contact_phone = "555-1234", contact_email = "john@example.com"
Expected Output: contacts = {"John": {"phone": "555-1234", "email": "john@example.com"}}

Input: action = "Search Contact", contact_name = "John"
Expected Output: result = {"phone": "555-1234", "email": "john@example.com"}

## ✅ You Are Done When
- All four actions work correctly
- Contacts persist across form submissions via hidden field
- Search returns "Not Found" for missing contacts
- Delete removes contacts from the dict
