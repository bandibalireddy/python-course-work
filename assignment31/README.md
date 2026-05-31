# Assignment 31 — Prime Number Checker

## 🎯 What You Will Practice
Learn how to define functions, use loops inside functions, and boolean logic.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Define is_prime(n): returns True if n is prime, False otherwise
2. Define get_primes_up_to(limit): returns list of all primes up to limit
3. Handle edge cases: negative numbers, 0, 1
4. Call both functions inside the view

## 💡 Hints
- is_prime: if n < 2 return False, then check divisibility from 2 to sqrt(n)
- Use `for i in range(2, int(n**0.5) + 1):`
- If n % i == 0, return False
- get_primes_up_to: loop from 2 to limit, call is_prime on each
- Build list: `primes = [i for i in range(2, limit + 1) if is_prime(i)]`

## 🔍 Example
Input: number = 7
Expected Output: is_prime_result = True

Input: number = 12
Expected Output: is_prime_result = False

Input: list_up_to = 20
Expected Output: prime_list = [2, 3, 5, 7, 11, 13, 17, 19], prime_count = 8

## ✅ You Are Done When
- is_prime correctly identifies primes
- Edge cases (negative, 0, 1) are handled
- get_primes_up_to returns correct list
- Prime count is accurate
