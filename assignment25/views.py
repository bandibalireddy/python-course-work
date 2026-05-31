from django.shortcuts import render

def index(request):
    result = None
    number = int(request.POST.get('number', 6))
    sequence = [number]
    steps = 0
    is_even_steps = 0
    is_odd_steps = 0

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Implement the Collatz Conjecture
        # - While loop: continue until number reaches 1
        # - If number is even: divide by 2
        # - If number is odd: multiply by 3 and add 1
        # - Append each new value to sequence
        # - Track total steps, even steps, and odd steps
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'result': result,
        'number': number,
        'sequence': sequence,
        'steps': steps,
        'is_even_steps': is_even_steps,
        'is_odd_steps': is_odd_steps,
    }
    return render(request, 'assignment25/index.html', context)
