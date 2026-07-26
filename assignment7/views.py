from django.shortcuts import render

def index(request):
    score = None
    grade = None
    message = None
    error = None

    if request.method == 'POST':
        score = request.POST.get('score', '')

        # ── STUDENT CODE START ──────────────────────────
        score = float(score)
        if  score < 0 or score > 100 :
            error = " score must be between 0 and 100 " 

        elif score >= 90 :
            grade = "A"
            message = "excellent work"
        elif score >= 80 :
            grade = "B"
            message = "good job"
        elif score >= 70 :
            grade = "C"
            message = "can do better"
        elif score >= 60 :
            grade = "D"
            message = "work hard"
        else :
            grade = "F"
            message = "need to do a lot of hardwork"

        # ── STUDENT CODE END ────────────────────────────

    context = {
        'score': score,
        'grade': grade,
        'message': message,
        'error': error,
    }
    return render(request, 'assignment7/index.html', context)
