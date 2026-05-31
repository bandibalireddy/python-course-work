from django.shortcuts import render

class Student:
    def __init__(self, name, student_id):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

    def add_grade(self, subject, score):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

    def get_average(self):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

    def get_letter_grade(self):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

class Gradebook:
    def __init__(self):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

    def add_student(self, student):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

    def get_class_average(self):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

    def get_top_student(self):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

    def get_ranked_students(self):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

def index(request):
    student_name = request.POST.get('student_name', '')
    student_id = request.POST.get('student_id', '')
    subject = request.POST.get('subject', '')
    score = request.POST.get('score', '')
    action = request.POST.get('action', '')
    gradebook_data = request.POST.get('gradebook_data', '')
    
    gradebook = Gradebook()
    message = None
    gradebook_data_output = ''

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Implement student gradebook using Student and Gradebook classes
        # - Parse gradebook_data to restore state
        # - Add student, add grade, view rankings, or get class stats based on action
        # - Serialize gradebook back to string
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'student_name': student_name,
        'student_id': student_id,
        'subject': subject,
        'score': score,
        'action': action,
        'gradebook': gradebook,
        'message': message,
        'gradebook_data_output': gradebook_data_output,
    }
    return render(request, 'assignment38/index.html', context)
