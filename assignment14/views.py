from django.shortcuts import render

def index(request):
    result = None
    speed = None
    zone_type = None
    status = None
    advice = None

    if request.method == 'POST':
        speed = int(request.POST.get('speed', 0))
        zone_type = request.POST.get('zone_type', '')
        advice = None
        status = None

        # ── STUDENT CODE START ──────────────────────────
        # TASK: Check speed against zone limits and determine status
        # - Zone limits: School Zone (15 mph), Residential (25 mph), City Center (35 mph), Highway (70 mph)
        # - Set status to "Safe" (at or below limit), "Warning" (within 10mph over), or "Danger" (more than 10mph over)
        # - Set advice with a descriptive message based on status and zone
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'result': result,
        'speed': speed,
        'zone_type': zone_type,
        'status': status,
        'advice': advice,
    }
    return render(request, 'assignment14/index.html', context)
