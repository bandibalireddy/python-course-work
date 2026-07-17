from django.shortcuts import render

def index(request):
    number = None
    is_even = None
    div_by_3 = None
    div_by_5 = None
    div_by_both = None

    if request.method == 'POST':
        number = request.POST.get('number', '')
        print(number)
        # ── STUDENT CODE START ──────────────────────────
        number = int(number)
        if number % 2 == 0 :
            is_even = 'even'
        else :
            is_even = 'odd'
            
        if number % 15 == 0 :  
            div_by_both = 'true'
        else :
            div_by_both = 'false'
        if number % 3 == 0 :  
            div_by_3 = 'true'
        else :
            div_by_3 = 'false'
        if number % 5 == 0 :  
            div_by_5 = 'true'
        else :
            div_by_5 = 'false'
        
        # ── STUDENT CODE END ────────────────────────────
        
    context = {
        'number': number,
        'is_even': is_even,
        'div_by_3': div_by_3,
        'div_by_5': div_by_5,
        'div_by_both': div_by_both,
    }
    return render(request, 'assignment3/index.html', context)
