import os
import datetime
from django.conf import settings
from django.shortcuts import render

def index(request):
    DIARY_FILE = os.path.join(settings.BASE_DIR, 'student_files', 'diary.txt')
    action = request.POST.get('action', '')
    entry_text = request.POST.get('entry_text', '')
    mood = request.POST.get('mood', '')
    entries = []
    message = None
    today = datetime.date.today().strftime('%Y-%m-%d')

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Implement personal diary with file operations
        # - If Write Entry: open diary file in 'a' (append) mode, write formatted entry
        # - If Read Today: open file in 'r' mode, parse entries, filter to today's date
        # - If Read All: open file, parse ALL entries into entries list
        # - If Delete All: open file in 'w' mode, write empty string
        # - Wrap in try/except: FileNotFoundError → create file first
        # - Mood emojis: Happy=😊 Sad=😢 Excited=🎉 Calm=😌 Anxious=😰 Grateful=🙏
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'action': action,
        'entry_text': entry_text,
        'mood': mood,
        'entries': entries,
        'message': message,
        'today': today,
    }
    return render(request, 'assignment42/index.html', context)
