from django.shortcuts import render

def index(request):
    cart_str = request.POST.get('cart_items', '')
    item_name = request.POST.get('item_name', '')
    item_price = request.POST.get('item_price', '')
    action = request.POST.get('action', '')
    cart = []
    total = None
    discount = None
    final_price = None

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Manage shopping cart
        # - Parse cart_str into list of dicts: [{'name': ..., 'price': ...}]
        # - Handle Add / Remove Last / Clear actions
        # - Calculate total price
        # - Apply 10% discount if total > 50
        # - Calculate final_price after discount
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'cart': cart,
        'cart_items': cart_str,
        'item_name': item_name,
        'item_price': item_price,
        'action': action,
        'total': total,
        'discount': discount,
        'final_price': final_price,
    }
    return render(request, 'assignment11/index.html', context)
