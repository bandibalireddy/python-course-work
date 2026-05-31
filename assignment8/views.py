from django.shortcuts import render

SECRET_NUMBER = 42

def index(request):
    guess = None
    attempts = 0
    hint = None
    won = False

    if request.method == 'POST':
        guess = request.POST.get('guess', '')
        attempts = int(request.POST.get('attempts', 0)) + 1

        # ── STUDENT CODE START ──────────────────────────
        # TASK: Compare guess to SECRET_NUMBER
        # - If too low → hint = "Too low! Go higher."
        # - If too high → hint = "Too high! Go lower."
        # - If correct → hint = "Correct!", won = True
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'guess': guess,
        'attempts': attempts,
        'hint': hint,
        'won': won,
    }
    return render(request, 'assignment8/index.html', context)
