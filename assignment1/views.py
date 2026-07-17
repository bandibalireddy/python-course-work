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
        print(number1 , number2 , operation )

        # ── STUDENT CODE START ──────────────────────────
        number1 = float(number1)
        number2 = float(number2)
        if operation == "Add" :
           result = number1 + number2
        elif operation == "Subtract" :
           result = number1 - number2
        elif operation ==  "Multiply" :
           result = number1 * number2  
        elif operation == "Divide" :
           if number2 == 0 :
              result = "not Division by zero"
           else :
              result = number1 / number2
         
         


        # ── STUDENT CODE END ──────
        # ──────────────────────
        print(result)
    context = {
        'result': result,
        'number1': number1,
        'number2': number2,
        'operation': operation,
    }
    return render(request, 'assignment1/index.html', context)
