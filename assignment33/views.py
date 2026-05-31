from django.shortcuts import render

# Student defines these functions above the view:
# def slugify(text): ...
# def titlecase(text): ...
# def truncate(text, max_len): ...
# def word_wrap(text, width): ...
# def remove_extra_spaces(text): ...
# def count_sentences(text): ...

# ── STUDENT CODE START ──────────────────────────
# TASK: Define text formatter functions
# - slugify: lowercase, replace spaces with hyphens, remove special chars
# - titlecase: capitalize first letter of each word
# - truncate: cut at max_len and add "..." if longer
# - word_wrap: insert newline every `width` characters at word boundaries
# - remove_extra_spaces: collapse multiple spaces into one
# - count_sentences: count sentences by counting . ! ?
pass  # ← Remove this line when you write your code
# ── STUDENT CODE END ────────────────────────────

def index(request):
    text = request.POST.get('text', '')
    max_length = int(request.POST.get('max_length', 50))
    line_width = int(request.POST.get('line_width', 30))
    results = {}

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Build results dict with output of each function
        # - Call each function and store result in results dict
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'text': text,
        'max_length': max_length,
        'line_width': line_width,
        'results': results,
    }
    return render(request, 'assignment33/index.html', context)
