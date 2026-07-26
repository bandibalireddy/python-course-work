from django.shortcuts import render

def index(request):
    name = None
    age = None
    hobbies_raw = None
    city = None
    hobbies_list = None
    age_next_year = None
    hobby_count = None

    if request.method == 'POST':
        name = request.POST.get('name', '')
        age = request.POST.get('age', '')
        hobbies_raw = request.POST.get('hobbies', '')
        city = request.POST.get('city', '')

        # ── STUDENT CODE START ──────────────────────────
        hobbies_list = hobbies_raw.split()
        age = int(age)
        age_next_year = age + 1
        hobby_count = len(hobbies_list)
        name = name.title()
        city = city.title()
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'name': name,
        'age': age,
        'hobbies_raw': hobbies_raw,
        'city': city,
        'hobbies_list': hobbies_list,
        'age_next_year': age_next_year,
        'hobby_count': hobby_count,
    }
    return render(request, 'assignment6/index.html', context)
