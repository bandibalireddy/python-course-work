from django.shortcuts import render

def index(request):
    current_list_str = request.POST.get('current_list', '')
    grocery_list = current_list_str.split(',') if current_list_str else []
    action = request.POST.get('action', '')
    item_name = request.POST.get('item_name', '').strip()
    message = None

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        if action == "Add Item":
            if item_name in grocery_list:
                message = "item_name is already present"
            else:
                grocery_list.append(item_name)
                message = "Added item_name to list"
        elif action == "Remove Item":
            if item_name in grocery_list:
                grocery_list.remove(item_name)
                message = "item_name removed "
            else:
                message = "Item not found"
        elif action == "View List":
            print(grocery_list)
        elif action == "Clear List":
            grocery_list.clear()
            message = "List cleared"
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'grocery_list': grocery_list,
        'current_list_str': ','.join(grocery_list),
        'message': message,
        'item_name': item_name,
        'action': action,
    }
    return render(request, 'assignment4/index.html', context)
