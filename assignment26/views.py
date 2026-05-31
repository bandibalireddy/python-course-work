from django.shortcuts import render

def index(request):
    result = None
    balance = float(request.POST.get('balance', 1000.00))
    action = request.POST.get('action', '')
    amount = float(request.POST.get('amount', 0))
    log_str = request.POST.get('transaction_log', '')
    transaction_log = []
    message = None
    log_output = ''

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Simulate an ATM with while loop logic
        # - Parse transaction_log from log_str
        # - if action is Deposit: add amount to balance, append to log
        # - if action is Withdraw:
        #     check if amount > balance → set message = "Insufficient funds"
        #     else subtract and log
        # - if action is Check Balance: just display
        # - Serialize log back to string
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'result': result,
        'balance': balance,
        'action': action,
        'amount': amount,
        'transaction_log': transaction_log,
        'message': message,
        'log_output': log_output,
    }
    return render(request, 'assignment26/index.html', context)
