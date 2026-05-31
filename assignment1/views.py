from django.shortcuts import render

def index(request):
    result = None
    number1 = None
    number2 = None
    operation = None

    if request.method == 'POST':
        number1 = request.POST.get('number1', '')
        number2 = request.POST.get('number2', '')
        operation = request.POST.get('operation', '')

        # ── STUDENT CODE START ──────────────────────────
        # TASK: Convert inputs to floats and perform the operation
        # - If operation is 'Add': number1 + number2
        # - If operation is 'Subtract': number1 - number2
        # - If operation is 'Multiply': number1 * number2
        # - If operation is 'Divide': number1 / number2 (handle division by zero)
        # Store the final answer in `result`
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'result': result,
        'number1': number1,
        'number2': number2,
        'operation': operation,
    }
    return render(request, 'assignment1/index.html', context)
