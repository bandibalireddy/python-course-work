from django.shortcuts import render

# Student defines these functions above the view:
# def is_prime(n): ...
# def get_primes_up_to(limit): ...

# ── STUDENT CODE START ──────────────────────────
# TASK: Define prime number functions
# - is_prime(n): returns True if n is prime, False otherwise
# - get_primes_up_to(limit): returns list of all primes up to limit
# - Handle edge cases: negative numbers, 0, 1
pass  # ← Remove this line when you write your code
# ── STUDENT CODE END ────────────────────────────

def index(request):
    number = int(request.POST.get('number', 7))
    list_up_to = int(request.POST.get('list_up_to', 50))
    is_prime_result = None
    prime_list = []
    prime_count = 0

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Call both functions inside the view
        # - Call is_prime(number) and store result
        # - Call get_primes_up_to(list_up_to) and store result
        # - Count primes in the list
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'number': number,
        'list_up_to': list_up_to,
        'is_prime_result': is_prime_result,
        'prime_list': prime_list,
        'prime_count': prime_count,
    }
    return render(request, 'assignment31/index.html', context)
