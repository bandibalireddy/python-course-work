from django.shortcuts import render

def index(request):
    expression = request.POST.get('expression', '')
    num1_str = request.POST.get('num1', '')
    num2_str = request.POST.get('num2', '')
    operation = request.POST.get('operation', '')
    result = None
    error_type = None
    error_message = None
    was_successful = False
    attempt_log = []

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Implement safe calculator with exception handling
        # - try/except block wrapping ALL calculations
        # - Catch ValueError: if inputs cannot be converted to numbers
        # - Catch ZeroDivisionError: if dividing by zero
        # - Catch TypeError: if operation receives wrong types
        # - Custom check: raise ValueError if Square Root of negative number
        # - Set error_type and error_message for any exception caught
        # - Set was_successful = True only if no exception occurred
        # - Add a finally block that logs the attempt (append to attempt_log)
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'expression': expression,
        'num1_str': num1_str,
        'num2_str': num2_str,
        'operation': operation,
        'result': result,
        'error_type': error_type,
        'error_message': error_message,
        'was_successful': was_successful,
        'attempt_log': attempt_log,
    }
    return render(request, 'assignment41/index.html', context)
