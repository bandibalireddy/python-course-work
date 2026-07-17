from django.shortcuts import render

def index(request):
    current_list_str = request.POST.get('current_list', '')
    grocery_list = current_list_str.split(',') if current_list_str else []
    action = request.POST.get('action', '')
    item_name = request.POST.get('item_name', '').strip()
    message = None

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        if action == "add item" :
            if item_name not in grocery_list :
                grocery_list.append(item_name)
                message = "your item has been added"
        elif action == "remove item" :
            if item_name in grocery_list :
                grocery_list.remove(item_name)
                message = "your item has been removed"
            else :
                message = "your item is not in the list"
        elif action == "clear list" :
            grocery_list.clear()
            message = "your list has been cleared"
        elif action == "view list" :
            pass
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'grocery_list': grocery_list,
        'current_list_str': ','.join(grocery_list),
        'message': message,
        'item_name': item_name,
        'action': action,
    }
    return render(request, 'assignment4/index.html', context)
