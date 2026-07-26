from django.shortcuts import render

def index(request):
    limit = None
    fizz_word = None
    buzz_word = None
    results = []

    if request.method == 'POST':
        limit = request.POST.get('limit', '20')
        fizz_word = request.POST.get('fizz_word', 'Fizz')
        buzz_word = request.POST.get('buzz_word', 'Buzz')

        # ── STUDENT CODE START ──────────────────────────
        limit = int(limit)
        results = []
        for number in range(1, limit + 1):
            if number % 15 == 0:
                results.append(fizz_word + buzz_word)
            elif number % 3 == 0:
                results.append(fizz_word)
            elif number % 5 == 0:
                results.append(buzz_word)
            else:
                results.append(number)
            
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'limit': limit,
        'fizz_word': fizz_word,
        'buzz_word': buzz_word,
        'results': results,
    }
    return render(request, 'assignment10/index.html', context)
