from django.shortcuts import render

def index(request):
    result = None
    start = None
    end = None
    step = None
    filter_type = None
    included_numbers = []
    total = 0
    count = 0

    if request.method == 'POST':
        start = int(request.POST.get('start', 1))
        end = int(request.POST.get('end', 10))
        step = int(request.POST.get('step', 1))
        filter_type = request.POST.get('filter_type', 'All Numbers')
        included_numbers = []
        total = 0
        count = 0

        # ── STUDENT CODE START ──────────────────────────
        # TASK: Sum numbers in a range with filtering
        # - Use a for loop from start to end using step
        # - Apply filter based on filter_type using if/elif
        # - Filter types: All Numbers, Even Only, Odd Only, Multiples of 3
        # - Append qualifying numbers to included_numbers
        # - Accumulate total and count
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'result': result,
        'start': start,
        'end': end,
        'step': step,
        'filter_type': filter_type,
        'included_numbers': included_numbers,
        'total': total,
        'count': count,
    }
    return render(request, 'assignment17/index.html', context)
