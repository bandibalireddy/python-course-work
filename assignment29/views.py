from django.shortcuts import render

# Student defines these functions above the view:
# def km_to_miles(km): ...
# def miles_to_km(miles): ...
# def kg_to_lbs(kg): ...
# def lbs_to_kg(lbs): ...
# def celsius_to_fahrenheit(c): ...
# def fahrenheit_to_celsius(f): ...

# ── STUDENT CODE START ──────────────────────────
# TASK: Define conversion functions
# - Each function takes one parameter and returns the converted value rounded to 2 decimal places
# - km_to_miles: km × 0.621371
# - miles_to_km: miles ÷ 0.621371
# - kg_to_lbs: kg × 2.20462
# - lbs_to_kg: lbs ÷ 2.20462
# - celsius_to_fahrenheit: (c × 9/5) + 32
# - fahrenheit_to_celsius: (f - 32) × 5/9
pass  # ← Remove this line when you write your code
# ── STUDENT CODE END ────────────────────────────

def index(request):
    result = None
    value = float(request.POST.get('value', 0))
    conversion_type = request.POST.get('conversion_type', '')
    result = None
    formula_used = None

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Call the correct function based on conversion_type
        # - Inside the view: if/elif to call the correct function based on conversion_type
        # - Set formula_used to a string showing the formula e.g. "km × 0.621371"
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'result': result,
        'value': value,
        'conversion_type': conversion_type,
        'formula_used': formula_used,
    }
    return render(request, 'assignment29/index.html', context)
