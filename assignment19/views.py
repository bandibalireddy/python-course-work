from django.shortcuts import render

def index(request):
    result = None
    contacts_data_str = request.POST.get('contacts_data', '')
    contacts = {}
    action = request.POST.get('action', '')
    contact_name = request.POST.get('contact_name', '')
    contact_phone = request.POST.get('contact_phone', '')
    contact_email = request.POST.get('contact_email', '')
    result = None
    message = None
    contacts_data_output = ''

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Implement contact book CRUD operations
        # - Parse contacts_data_str into contacts dict: {name: {'phone': ..., 'email': ...}}
        # - If Add: add new contact to dict
        # - If Search: look up by name, set result to contact dict or "Not Found"
        # - If Delete: remove from dict if exists
        # - If View All: result = entire contacts dict
        # - Serialize contacts dict back to string for hidden field
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'result': result,
        'contacts': contacts,
        'action': action,
        'contact_name': contact_name,
        'contact_phone': contact_phone,
        'contact_email': contact_email,
        'message': message,
        'contacts_data_output': contacts_data_output,
    }
    return render(request, 'assignment19/index.html', context)
