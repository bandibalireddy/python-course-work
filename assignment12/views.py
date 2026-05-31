from django.shortcuts import render

def index(request):
    gradebook_str = request.POST.get('gradebook', '')
    student_name = request.POST.get('student_name', '')
    student_score = request.POST.get('student_score', '')
    action = request.POST.get('action', '')
    students = []
    class_average = None
    highest = None
    lowest = None
    ranked_students = None

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Manage student grade book
        # - Parse gradebook_str into list of dicts with name and score
        # - Add or clear students based on action
        # - Calculate class average
        # - Find highest and lowest scoring student
        # - Sort students by score descending (ranked list)
        # - Assign letter grades to each student (90-100=A, 80-89=B, 70-79=C, 60-69=D, below 60=F)
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'students': students,
        'gradebook': gradebook_str,
        'student_name': student_name,
        'student_score': student_score,
        'action': action,
        'class_average': class_average,
        'highest': highest,
        'lowest': lowest,
        'ranked_students': ranked_students,
    }
    return render(request, 'assignment12/index.html', context)
