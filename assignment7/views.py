from django.shortcuts import render

def index(request):
    score = None
    grade = None
    message = None
    error = None

    if request.method == 'POST':
        score = request.POST.get('score', '')

        # ── STUDENT CODE START ──────────────────────────
        # TASK: Classify the score into a letter grade
        # - 90–100 → A, 80–89 → B, 70–79 → C, 60–69 → D, below 60 → F
        # - Assign an encouraging message per grade
        # - Handle out-of-range scores (below 0 or above 100) with an error message
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'score': score,
        'grade': grade,
        'message': message,
        'error': error,
    }
    return render(request, 'assignment7/index.html', context)
