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
        # TASK: Generate a multiplication table using a for loop
        # - Use a for loop from 1 to limit (inclusive)
        # - Each iteration: calculate number x multiplier
        # - Append dict {'multiplier': i, 'result': product} to table list
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'result': result,
        'number': number,
        'limit': limit,
        'table': table,
    }
    return render(request, 'assignment16/index.html', context)
