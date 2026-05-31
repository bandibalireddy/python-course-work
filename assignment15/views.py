from django.shortcuts import render

def index(request):
    result = None
    month = None
    hemisphere = None
    season = None
    weather_tip = None
    months_in_season = None

    if request.method == 'POST':
        month = request.POST.get('month', '')
        hemisphere = request.POST.get('hemisphere', '')
        season = None
        weather_tip = None
        months_in_season = None

        # ── STUDENT CODE START ──────────────────────────
        # TASK: Determine the season based on month and hemisphere
        # - Northern hemisphere seasons: Winter (Dec, Jan, Feb), Spring (Mar, Apr, May), Summer (Jun, Jul, Aug), Autumn (Sep, Oct, Nov)
        # - Southern hemisphere: opposite seasons
        # - Set weather_tip based on season (e.g. "Wear warm clothes" for Winter)
        # - Set months_in_season as a list of the 3 months in that season
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'result': result,
        'month': month,
        'hemisphere': hemisphere,
        'season': season,
        'weather_tip': weather_tip,
        'months_in_season': months_in_season,
    }
    return render(request, 'assignment15/index.html', context)
