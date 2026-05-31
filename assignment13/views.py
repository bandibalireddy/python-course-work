from django.shortcuts import render

QUESTIONS = [
    {'question': 'What is 5 + 3?', 'answer': '8'},
    {'question': 'What color is the sky?', 'answer': 'blue'},
    {'question': 'How many days in a week?', 'answer': '7'},
    {'question': 'What is the capital of France?', 'answer': 'paris'},
    {'question': 'What is 10 x 10?', 'answer': '100'},
]

def index(request):
    score = 0
    results = []
    percentage = None
    label = None

    if request.method == 'POST':
        answers = [request.POST.get(f'q{i}', '').strip().lower() for i in range(5)]

        # ── STUDENT CODE START ──────────────────────────
        # TASK: Grade the quiz
        # - Loop through QUESTIONS and compare each to submitted answers
        # - For each question, track: question text, student's answer, correct answer, is_correct (True/False)
        # - Add to results list as dicts
        # - Count total score
        # - Calculate percentage
        # - Assign a performance label: "Excellent" (5/5), "Good" (3-4), "Keep Practicing" (0-2)
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'questions': QUESTIONS,
        'score': score,
        'results': results,
        'percentage': percentage,
        'label': label,
    }
    return render(request, 'assignment13/index.html', context)
