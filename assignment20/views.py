from django.shortcuts import render

def index(request):
    result = None
    text = request.POST.get('text', '').lower()
    sort_by = request.POST.get('sort_by', 'Most Frequent')
    word_freq = {}
    sorted_words = []
    unique_count = 0
    total_words = 0

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Count word frequencies and sort them
        # - Split text into words, strip punctuation from each word
        # - Loop through words, build word_freq dict with counts
        # - Count total_words and unique_count
        # - Sort based on sort_by selection (Most Frequent, Least Frequent, Alphabetical)
        # - Store sorted result as list of (word, count) tuples
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'result': result,
        'text': text,
        'sort_by': sort_by,
        'word_freq': word_freq,
        'sorted_words': sorted_words,
        'unique_count': unique_count,
        'total_words': total_words,
    }
    return render(request, 'assignment20/index.html', context)
