from django.shortcuts import render

def index(request):
    result = None
    inventory_data_str = request.POST.get('inventory_data', '')
    inventory = {}
    action = request.POST.get('action', '')
    item_name = request.POST.get('item_name', '')
    quantity = request.POST.get('quantity', '')
    price = request.POST.get('price', '')
    total_value = 0
    low_stock = []
    message = None
    inventory_data_output = ''

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Manage inventory with nested dictionaries
        # - Parse inventory_data_str into nested inventory dict: {item_name: {'quantity': int, 'price': float}}
        # - Handle each action using dict operations
        # - Calculate total_value = sum of (qty * price) for all items
        # - Find low_stock items (quantity < 5)
        # - Serialize inventory back to string for hidden field
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'result': result,
        'inventory': inventory,
        'action': action,
        'item_name': item_name,
        'quantity': quantity,
        'price': price,
        'total_value': total_value,
        'low_stock': low_stock,
        'message': message,
        'inventory_data_output': inventory_data_output,
    }
    return render(request, 'assignment23/index.html', context)
