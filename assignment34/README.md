# Assignment 34 — Bank Account Class

## 🎯 What You Will Practice
Learn how to define classes, use __init__, instance methods, and self.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find the BankAccount class methods:
```python
# ── STUDENT CODE START ──

# ── STUDENT CODE END ──
```

## 📝 Your Tasks
1. __init__: set self.owner, self.balance, self.transaction_count
2. deposit: add amount, increment transaction_count, return new balance
3. withdraw: check funds, subtract if sufficient, return balance or error
4. get_balance: return current balance
5. In the view: parse account_data, create/use account, serialize state

## 💡 Hints
- __init__: `self.owner = owner`, `self.balance = initial_balance`, `self.transaction_count = 0`
- deposit: `self.balance += amount`, `self.transaction_count += 1`, return `self.balance`
- withdraw: `if amount > self.balance: return "Insufficient funds"` else `self.balance -= amount`
- get_balance: `return self.balance`
- Serialize: `f"{account.owner}|{account.balance}|{account.transaction_count}"`

## 🔍 Example
Create Account: owner = "John", initial_balance = 1000
Expected Output: account.owner = "John", account.balance = 1000, account.transaction_count = 0

Deposit: amount = 500
Expected Output: account.balance = 1500, account.transaction_count = 1

Withdraw: amount = 200
Expected Output: account.balance = 1300, account.transaction_count = 2

## ✅ You Are Done When
- Account is created with owner and initial balance
- Deposit adds to balance and increments transaction count
- Withdraw subtracts when sufficient, shows error when not
- get_balance returns current balance
- Account state persists across form submissions
