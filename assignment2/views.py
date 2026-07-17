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
        text = user_text
        length = len(text)
        uppercase = text.upper()
        lowercase = text.lower()
        reversed_text = text[::-1]
        vowel_count = text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u')

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
