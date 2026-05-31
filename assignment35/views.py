from django.shortcuts import render

class Book:
    def __init__(self, title, author, isbn):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

    def check_out(self):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

    def return_book(self):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

    def get_info(self):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

class Library:
    def __init__(self):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

    def add_book(self, book):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

    def find_book(self, title):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

    def get_available_books(self):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

def index(request):
    action = request.POST.get('action', '')
    title = request.POST.get('title', '')
    author = request.POST.get('author', '')
    isbn = request.POST.get('isbn', '')
    books_data = request.POST.get('books_data', '')
    
    library = Library()
    message = None
    books_data_output = ''

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Implement library book tracker using Book and Library classes
        # - Parse books_data to restore library state
        # - Add book, check out, return, or view all based on action
        # - Serialize library state back to string
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'action': action,
        'title': title,
        'author': author,
        'isbn': isbn,
        'library': library,
        'message': message,
        'books_data_output': books_data_output,
    }
    return render(request, 'assignment35/index.html', context)
