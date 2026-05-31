from django.shortcuts import render

# Student defines these functions above the view:
# def has_min_length(pwd, min_len=8): ...
# def has_uppercase(pwd): ...
# def has_lowercase(pwd): ...
# def has_digit(pwd): ...
# def has_special_char(pwd): ...
# def calculate_strength(score): ...

# ── STUDENT CODE START ──────────────────────────
# TASK: Define password strength checker functions
# - has_min_length(pwd, min_len=8): returns True if len(pwd) >= min_len
# - has_uppercase(pwd): returns True if pwd has at least one uppercase letter
# - has_lowercase(pwd): returns True if pwd has at least one lowercase letter
# - has_digit(pwd): returns True if pwd has at least one digit
# - has_special_char(pwd): returns True if pwd has at least one special character
# - calculate_strength(score): returns "Weak"(0-2), "Medium"(3), "Strong"(4), "Very Strong"(5)
pass  # ← Remove this line when you write your code
# ── STUDENT CODE END ────────────────────────────

def index(request):
    password = request.POST.get('password', '')
    strength = None
    score = 0
    checks = {}
    masked_password = '*' * len(password)
    strength_class = strength.lower().replace(' ', '-') if strength else ''

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Check password strength using the functions
        # - Call each function, build checks dict with True/False
        # - Total score based on passed checks
        # - Determine strength based on score
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'password': password,
        'strength': strength,
        'score': score,
        'checks': checks,
        'masked_password': masked_password,
        'strength_class': strength_class,
    }
    return render(request, 'assignment30/index.html', context)
