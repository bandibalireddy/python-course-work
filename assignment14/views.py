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
        if zone_type == 'School Zone':
            if speed <= 15:
                status = 'safe'
                advice = 'you are driving safely'
            elif 15 < speed <= 25:
                status = 'warning'
                advice = 'you are going fast than the speed limit'
            else:
                status = 'danger'
                advice = 'u immediately need to slow down'
        elif zone_type == ' Residential':
                    if speed <= 25:
                        status = 'safe'
                        advice = 'you are driving safely'
                    elif 25 < speed <= 35:
                        status = 'warning'
                        advice = 'you are going fast than the speed limit'
                    else:
                        status = 'danger'
                        advice = 'u immediately need to slow down'
        if zone_type == 'City Center':
                    if speed <= 35:
                        status = 'safe'
                        advice = 'you are driving safely'
                    elif 35 < speed <= 45:
                        status = 'warning'
                        advice = 'you are going fast than the speed limit'
                    else:
                        status = 'danger'
                        advice = 'u immediately need to slow down'  
        if zone_type == 'Highway':
                    if speed <= 70:
                        status = 'safe'
                        advice = 'you are driving safely'
                    elif 70 < speed <= 80:
                        status = 'warning'
                        advice = 'you are going fast than the speed limit'
                    else:
                        status = 'danger'
                        advice = 'u immediately need to slow down'   




    
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'result': result,
        'speed': speed,
        'zone_type': zone_type,
        'status': status,
        'advice': advice,
    }
    return render(request, 'assignment14/index.html', context)
