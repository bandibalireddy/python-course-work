from django.shortcuts import render

def index(request):
    current_list_str = request.POST.get('current_list', '')
    grocery_list = current_list_str.split(',') if current_list_str else []
    action = request.POST.get('action', '')
    item_name = request.POST.get('item_name', '').strip()
    message = None

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Manage the grocery list
        # - If action is "Add Item": add item_name to grocery_list (avoid duplicates)
        # - If action is "Remove Item": remove item_name if it exists, else set message = "Item not found"
        # - If action is "View List": just display the list
        # - If action is "Clear List": empty the list
        # Always set message to summarize what happened
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'grocery_list': grocery_list,
        'current_list_str': ','.join(grocery_list),
        'message': message,
        'item_name': item_name,
        'action': action,
    }
    return render(request, 'assignment4/index.html', context)
