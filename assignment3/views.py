from django.shortcuts import render

def index(request):
    number = None
    is_even = None
    div_by_3 = None
    div_by_5 = None
    div_by_both = None

    if request.method == 'POST':
        number = request.POST.get('number', '')

        # ── STUDENT CODE START ──────────────────────────
        # TASK: Check divisibility properties
        # - Check if even or odd → store "Even" or "Odd" in is_even
        # - Check divisibility by 3 → store True/False in div_by_3
        # - Check divisibility by 5 → store True/False in div_by_5
        # - Check divisibility by both 3 and 5 → store True/False in div_by_both
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'number': number,
        'is_even': is_even,
        'div_by_3': div_by_3,
        'div_by_5': div_by_5,
        'div_by_both': div_by_both,
    }
    return render(request, 'assignment3/index.html', context)
