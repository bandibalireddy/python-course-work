from django.shortcuts import render

COUNTRIES = {
    'France': 'Paris',
    'Japan': 'Tokyo',
    'Brazil': 'Brasilia',
    'Australia': 'Canberra',
    'Egypt': 'Cairo',
    'Canada': 'Ottawa',
    'India': 'New Delhi',
    'Germany': 'Berlin',
    'Mexico': 'Mexico City',
    'South Africa': 'Pretoria'
}

def index(request):
    result = None
    results = []
    score = 0
    total = len(COUNTRIES)
    percentage = 0

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Grade the country capital quiz
        # - Loop through COUNTRIES dict
        # - Get student answer from POST for each country (use country name as key)
        # - Compare answer (case insensitive) to correct capital
        # - Append to results: {'country': ..., 'correct': ..., 'given': ..., 'is_correct': ...}
        # - Calculate score and percentage
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'result': result,
        'results': results,
        'score': score,
        'total': total,
        'percentage': percentage,
        'countries': COUNTRIES,
    }
    return render(request, 'assignment21/index.html', context)
