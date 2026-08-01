from django.shortcuts import render

def index(request):
    raw_input = None
    number_list = []
    minimum = None
    maximum = None
    total = None
    average = None
    sorted_list = None
    error_message = None

    if request.method == 'POST':
        raw_input = request.POST.get('numbers', '')
        number_list = [x.strip() for x in raw_input.split(',') if x.strip()]

        # ── STUDENT CODE START ───────────────────────
        if number_list == []  :
          result = "please enter a number"
        else : 
           number_list = int(input("enter the numbers:"))
           minimum = min(number_list)
           maximum = max(number_list)
           total   = sum(number_list)
           average = total / len(number_list)
           sorted_list = sorted(number_list)
 
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'raw_input': raw_input,
        'number_list': number_list,
        'minimum': minimum,
        'maximum': maximum,
        'total': total,
        'average': average,
        'sorted_list': sorted_list,
        'error_message': error_message,
    }
    return render(request, 'assignment5/index.html', context)
