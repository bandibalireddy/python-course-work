from django.shortcuts import render

SECRET_NUMBER = 66

def index(request):
    guess = None
    attempts = 0
    hint = None
    won = False

    if request.method == 'POST':
        guess = int(request.POST.get('guess', ''))
        attempts = int(request.POST.get('attempts', 0)) + 1

        # ── STUDENT CODE START ──────────────────────────
        guess = int(guess)
        if guess < SECRET_NUMBER:
            hint = "Too low! go higher"
        elif guess > SECRET_NUMBER:
            hint = "Too high! Go lower."
        elif guess == SECRET_NUMBER:
            hint = "correct!"
            won = "true"
    
            
        
        
    
    
    
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'guess': guess,
        'attempts': attempts,
        'hint': hint,
        'won': won,
    }
    return render(request, 'assignment8/index.html', context)
