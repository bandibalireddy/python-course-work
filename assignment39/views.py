import os
from django.conf import settings
from django.shortcuts import render

def index(request):
    FILE_DIR = os.path.join(settings.BASE_DIR, 'student_files')
    os.makedirs(FILE_DIR, exist_ok=True)
    
    text_content = request.POST.get('text_content', '')
    filename = request.POST.get('filename', 'my_text.txt')
    action = request.POST.get('action', '')
    file_content = None
    word_count = 0
    line_count = 0
    char_count = 0
    message = None

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Implement file operations with exception handling
        # - Build full file path safely using os.path.join(FILE_DIR, filename)
        # - If Save: open file with 'w' mode, write text_content, set message
        # - If Read: open file with 'r' mode, read content into file_content
        # - If Count: open file, count words (split), lines (splitlines), chars (len)
        # - Wrap all file operations in try/except for FileNotFoundError, IOError
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'text_content': text_content,
        'filename': filename,
        'action': action,
        'file_content': file_content,
        'word_count': word_count,
        'line_count': line_count,
        'char_count': char_count,
        'message': message,
    }
    return render(request, 'assignment39/index.html', context)
