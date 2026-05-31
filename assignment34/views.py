from django.shortcuts import render

class BankAccount:
    def __init__(self, owner, initial_balance=0):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

    def deposit(self, amount):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

    def withdraw(self, amount):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

    def get_balance(self):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

def index(request):
    action = request.POST.get('action', '')
    account_name = request.POST.get('account_name', '')
    amount = request.POST.get('amount', '')
    account_data = request.POST.get('account_data', '')
    
    account = None
    message = None
    account_data_output = ''

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Implement bank account operations using the BankAccount class
        # - Parse account_data to restore state
        # - Create account, deposit, withdraw, or check balance based on action
        # - Serialize account state back to string
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'action': action,
        'account_name': account_name,
        'amount': amount,
        'account': account,
        'message': message,
        'account_data_output': account_data_output,
    }
    return render(request, 'assignment34/index.html', context)
