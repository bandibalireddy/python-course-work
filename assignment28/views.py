from django.shortcuts import render

def index(request):
    result = None
    code = int(request.POST.get('status_code', 200))
    category = None
    meaning = None
    description = None
    is_error = False

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Decode HTTP status codes using match/case
        # - match/case on code:
        #     200 → "OK", 201 → "Created", 301 → "Moved Permanently",
        #     400 → "Bad Request", 401 → "Unauthorized", 403 → "Forbidden",
        #     404 → "Not Found", 500 → "Internal Server Error",
        #     502 → "Bad Gateway", 503 → "Service Unavailable"
        #     case _: → "Unknown Status Code"
        # - Determine category based on first digit (1xx, 2xx, 3xx, 4xx, 5xx)
        # - Set is_error = True for 4xx and 5xx codes
        # - Set a helpful description for each code
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'result': result,
        'code': code,
        'category': category,
        'meaning': meaning,
        'description': description,
        'is_error': is_error,
    }
    return render(request, 'assignment28/index.html', context)
