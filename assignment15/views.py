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
        if hemisphere == 'Northern':
            if month == 'June' or month == 'July' or month == 'August':
                season = 'summer'
                weather_tip = 'wear cotton clothes'
                months_in_season = ['june', 'july', 'august']
            elif month == 'December' or month == 'January' or month == 'February':
                season = 'winter'
                weather_tip = 'wear woollen clothes'
                months_in_season = ['december', 'january', 'february']
            elif month == 'September' or month == 'October' or month == 'November':
                season = 'autumn'
                weather_tip = "don't worry about your plant's leaves. They will grow again."
                months_in_season = ['September', 'October', 'November']
            elif month == 'March' or month == 'April' or month == 'May':
                season = 'spring'
                weather_tip = 'enjoy the beauty of nature while it is with you'
                months_in_season = ['march', 'april', 'may']
        elif hemisphere == 'Southern':
                    if month == 'June' or month == 'July' or month == 'August':
                        season = 'winter'
                        weather_tip = 'wear woollen clothes'
                        months_in_season = ['june', 'july', 'august']
                    elif month == 'December' or month == 'January' or month == 'February':
                        season = 'summer'
                        weather_tip = 'wear cotton clothes'
                        months_in_season = ['december', 'january', 'february']
                    elif month == 'September' or month == 'October' or month == 'November':
                        season = 'spring'
                        weather_tip = "enjoy the beauty of nature while it is with you"
                        months_in_season = ['September', 'October', 'November']
                    elif month == 'March' or month == 'April' or month == 'May':
                        season = 'autumn'
                        weather_tip = "don't worry about your plant's leaves. They will grow again."
                        months_in_season = ['march', 'april', 'may']
            
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
