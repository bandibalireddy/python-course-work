from django.shortcuts import render

def index(request):
    text = None
    word_count = None
    longest_word = None
    unique_words = None
    char_count = None

    if request.method == 'POST':
        text = request.POST.get('paragraph', '')

        # ── STUDENT CODE START ──────────────────────────
        # TASK: Analyze the paragraph
        # - Split text into words
        # - Count total words
        # - Find the longest word
        # - Find unique words (no duplicates), return as a sorted list
        # - Count total characters (excluding spaces)
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'text': text,
        'word_count': word_count,
        'longest_word': longest_word,
        'unique_words': unique_words,
        'char_count': char_count,
    }
    return render(request, 'assignment9/index.html', context)
