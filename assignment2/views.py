from django.shortcuts import render

def index(request):
    user_text = None
    length = None
    uppercase = None
    lowercase = None
    reversed_text = None
    vowel_count = None

    if request.method == 'POST':
        user_text = request.POST.get('user_text', '')

        # ── STUDENT CODE START ──────────────────────────
        # TASK: Analyze the string
        # - Calculate the length of the string
        # - Convert to uppercase
        # - Convert to lowercase
        # - Reverse the string
        # - Count vowels (a, e, i, o, u — case insensitive)
        # Store each in the corresponding variable
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'user_text': user_text,
        'length': length,
        'uppercase': uppercase,
        'lowercase': lowercase,
        'reversed_text': reversed_text,
        'vowel_count': vowel_count,
    }
    return render(request, 'assignment2/index.html', context)
