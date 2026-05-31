from django.shortcuts import render

def index(request):
    result = None
    start = None
    step = None
    stop_at = None
    countdown_steps = []
    total_steps = 0

    if request.method == 'POST':
        start = int(request.POST.get('start_number', 10))
        step = int(request.POST.get('step', 1))
        stop_at = int(request.POST.get('stop_at', 0))
        countdown_steps = []
        total_steps = 0

        # ── STUDENT CODE START ──────────────────────────
        # TASK: Create a countdown timer using a while loop
        # - While loop starting from start, decrementing by step, stopping at stop_at
        # - Append each value to countdown_steps
        # - Count total_steps taken
        # - Add "Blast Off!" or "Done!" as final element
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'result': result,
        'start': start,
        'step': step,
        'stop_at': stop_at,
        'countdown_steps': countdown_steps,
        'total_steps': total_steps,
    }
    return render(request, 'assignment24/index.html', context)
