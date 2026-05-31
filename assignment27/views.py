from django.shortcuts import render

def index(request):
    result = None
    day = request.POST.get('day', '')
    country = request.POST.get('country', '')
    day_type = None
    work_hours = None
    fun_suggestion = None
    public_holiday_note = None

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Classify days using match/case
        # - match/case on day to determine day_type
        # - Weekday: set typical work_hours (9am-5pm)
        # - Weekend: set work_hours to "Day Off"
        # - Use nested match/case or if/else for country-specific notes
        # - Set fun_suggestion based on day type
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'result': result,
        'day': day,
        'country': country,
        'day_type': day_type,
        'work_hours': work_hours,
        'fun_suggestion': fun_suggestion,
        'public_holiday_note': public_holiday_note,
    }
    return render(request, 'assignment27/index.html', context)
