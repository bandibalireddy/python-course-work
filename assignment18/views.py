from django.shortcuts import render

def index(request):
    result = None
    rows = None
    pattern_type = None
    character = None
    pattern_lines = []

    if request.method == 'POST':
        rows = int(request.POST.get('rows', 5))
        pattern_type = request.POST.get('pattern_type', 'Right Triangle')
        character = request.POST.get('character', '*')
        pattern_lines = []

        # ── STUDENT CODE START ──────────────────────────
        # TASK: Generate patterns using nested for loops
        # - Use if/elif for each pattern type
        # - Use nested for loops and string building to create each line
        # - Append each line as a string to pattern_lines
        # - Right Triangle: 1 char on row 1, 2 on row 2, etc.
        # - Pyramid: centered, row 1 has 1, row 2 has 3, etc.
        # - Diamond: pyramid + inverted pyramid
        # - Inverted Triangle: reverse of right triangle
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'result': result,
        'rows': rows,
        'pattern_type': pattern_type,
        'character': character,
        'pattern_lines': pattern_lines,
    }
    return render(request, 'assignment18/index.html', context)
