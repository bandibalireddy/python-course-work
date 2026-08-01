from django.shortcuts import render

def index(request):
    result = None
    number = None
    limit = None
    table = []

    if request.method == 'POST':
        number = int(request.POST.get('number', 1))
        limit = int(request.POST.get('limit', 12))
        table = []

        # ── STUDENT CODE START ──────────────────────────
        for i in range(1, limit + 1):
            product = number * i
            table.append({'multiplier': i, 'result': product})
         
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'result': result,
        'number': number,
        'limit': limit,
        'table': table,
    }
    return render(request, 'assignment16/index.html', context)
