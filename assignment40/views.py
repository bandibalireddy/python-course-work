from django.shortcuts import render

def index(request):
    csv_data = request.POST.get('csv_data', '')
    delimiter_choice = request.POST.get('delimiter', 'Comma')
    delimiter_map = {'Comma': ',', 'Semicolon': ';', 'Tab': '\t'}
    delimiter = delimiter_map.get(delimiter_choice, ',')
    headers = []
    rows = []
    numeric_stats = {}
    errors = []
    row_count = 0

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Parse CSV data and calculate statistics
        # - Split csv_data into lines
        # - Parse header row using delimiter
        # - Loop through remaining lines, split each by delimiter
        # - Try to convert each cell to float for numeric columns
        # - Catch ValueError for non-numeric cells, add to errors list
        # - Build rows as list of dicts {header: value}
        # - Calculate numeric_stats for all numeric columns
        # - Count valid rows
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'csv_data': csv_data,
        'delimiter_choice': delimiter_choice,
        'headers': headers,
        'rows': rows,
        'numeric_stats': numeric_stats,
        'errors': errors,
        'row_count': row_count,
    }
    return render(request, 'assignment40/index.html', context)
