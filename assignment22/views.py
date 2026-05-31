from django.shortcuts import render

def index(request):
    result = None
    subjects_raw = [(request.POST.get(f'subject_{i}'), request.POST.get(f'score_{i}')) for i in range(1,6)]
    report = {}
    gpa = None
    best_subject = None
    worst_subject = None
    grade_report = {}

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Create a student report card
        # - Build report dict from subjects_raw (skip empty entries)
        # - Calculate GPA (average of all scores)
        # - Find best and worst subject using dict operations
        # - Assign letter grade to each subject (same scale as assignment 7)
        # - Build grade_report dict
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'result': result,
        'report': report,
        'gpa': gpa,
        'best_subject': best_subject,
        'worst_subject': worst_subject,
        'grade_report': grade_report,
    }
    return render(request, 'assignment22/index.html', context)
