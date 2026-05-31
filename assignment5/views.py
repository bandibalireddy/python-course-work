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

        # ── STUDENT CODE START ──────────────────────────
        # TASK: Calculate statistics for the number list
        # - Convert number_list items to floats/ints
        # - Find minimum value
        # - Find maximum value
        # - Calculate the sum (total)
        # - Calculate the average
        # - Sort the list in ascending order
        # - Handle empty input with a message
        pass  # ← Remove this line when you write your code
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
