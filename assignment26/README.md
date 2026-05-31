# Assignment 26 — ATM Simulator

## 🎯 What You Will Practice
Learn how to use while loop simulation, conditionals, and running state management.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Parse transaction_log from log_str (format: "action|amount|balance;action|amount|balance")
2. If Deposit: add amount to balance, append to log
3. If Withdraw:
   - Check if amount > balance → set message = "Insufficient funds"
   - Else subtract and log
4. If Check Balance: just display
5. Serialize log back to string

## 💡 Hints
- Parse: split by ';' then by '|' to get action, amount, balance
- Build list: `transaction_log.append({'action': action, 'amount': amount, 'balance': balance})`
- Deposit: `balance += amount`, append log entry
- Withdraw: `if amount > balance: message = "Insufficient funds"` else `balance -= amount`
- Serialize: join with '|' for each entry, then ';' between entries

## 🔍 Example
Input: action = "Deposit", amount = 100, balance = 1000
Expected Output: balance = 1100, transaction_log = [{"action": "Deposit", "amount": 100, "balance": 1100}]

Input: action = "Withdraw", amount = 2000, balance = 1000
Expected Output: message = "Insufficient funds", balance = 1000

## ✅ You Are Done When
- Deposit adds to balance correctly
- Withdraw subtracts when sufficient funds
- Withdraw shows error when insufficient funds
- Transaction log persists across submissions
