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
        # TASK: Implement FizzBuzz with custom words
        # - Loop from 1 to limit (inclusive)
        # - If divisible by 3 and 5 → append fizz_word + buzz_word
        # - If divisible by 3 only → append fizz_word
        # - If divisible by 5 only → append buzz_word
        # - Otherwise → append the number
        # - Store all values in results list
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'limit': limit,
        'fizz_word': fizz_word,
        'buzz_word': buzz_word,
        'results': results,
    }
    return render(request, 'assignment10/index.html', context)
