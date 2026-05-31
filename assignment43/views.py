from django.shortcuts import render

class AppError(Exception):
    # ── STUDENT CODE START ──
    pass
    # ── STUDENT CODE END ──

class ValidationError(AppError):
    # ── STUDENT CODE START ──
    pass
    # ── STUDENT CODE END ──

class NetworkError(AppError):
    # ── STUDENT CODE START ──
    pass
    # ── STUDENT CODE END ──

class DatabaseError(AppError):
    # ── STUDENT CODE START ──
    pass
    # ── STUDENT CODE END ──

def trigger_scenario(scenario, value):
    # ── STUDENT CODE START ──────────────────────────
    # TASK: Trigger different exceptions based on scenario
    # - Email validation: raise ValidationError if '@' not in value
    # - Age validation: raise ValidationError if age < 0 or > 150
    # - Network: always raise NetworkError(timeout_seconds=30)
    # - Database: always raise DatabaseError(db_name='main_db')
    # - Divide by Zero: attempt 1/0
    # - Catch All: raise AppError directly
    # - No Error: return "All systems OK"
    pass  # ← Remove this line when you write your code
    # ── STUDENT CODE END ────────────────────────────

def index(request):
    scenario = request.POST.get('scenario', '')
    input_value = request.POST.get('input_value', '')
    
    caught_exception = None
    exception_type = None
    exception_message = None
    error_code = None
    extra_attributes = {}
    result = None

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Catch and display exception information
        # - Wrap call in try/except catching each type separately, most specific first
        # - Store exception type, message, error_code, and extra attributes
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'scenario': scenario,
        'input_value': input_value,
        'caught_exception': caught_exception,
        'exception_type': exception_type,
        'exception_message': exception_message,
        'error_code': error_code,
        'extra_attributes': extra_attributes,
        'result': result,
    }
    return render(request, 'assignment43/index.html', context)
