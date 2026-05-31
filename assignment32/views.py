from django.shortcuts import render

# Student defines these functions above the view:
# def calculate_bmi_metric(weight_kg, height_m): ...
# def calculate_bmi_imperial(weight_lbs, height_ft, height_in): ...
# def get_bmi_category(bmi): ...
# def get_health_advice(category): ...

# ── STUDENT CODE START ──────────────────────────
# TASK: Define BMI calculator functions
# - calculate_bmi_metric: returns BMI rounded to 1 decimal
# - calculate_bmi_imperial: converts to metric first, then calculates
# - get_bmi_category: returns Underweight/Normal/Overweight/Obese
# - get_health_advice: returns advice string per category
pass  # ← Remove this line when you write your code
# ── STUDENT CODE END ────────────────────────────

def index(request):
    weight = float(request.POST.get('weight', 0))
    height = float(request.POST.get('height', 0))
    unit_system = request.POST.get('unit_system', 'Metric')
    height_inches = float(request.POST.get('height_inches', 0))
    bmi = None
    category = None
    health_advice = None

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Call correct function based on unit_system
        # - Call correct function based on unit_system
        # - Get BMI category and health advice
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'weight': weight,
        'height': height,
        'unit_system': unit_system,
        'height_inches': height_inches,
        'bmi': bmi,
        'category': category,
        'health_advice': health_advice,
    }
    return render(request, 'assignment32/index.html', context)
