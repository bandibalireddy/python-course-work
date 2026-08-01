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
        for i in range(start, end + 1, step):
            if filter_type == 'Even only':
                included_numbers = 'i % 2 == 0'

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
