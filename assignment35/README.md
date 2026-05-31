# Assignment 35 — Library Book Tracker

## 🎯 What You Will Practice
Learn how to use multiple classes, object composition, and lists of objects.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find the class methods:
```python
# ── STUDENT CODE START ──

# ── STUDENT CODE END ──
```

## 📝 Your Tasks
1. Book.__init__: set title, author, isbn, is_available=True
2. Book.check_out: set is_available=False if available, else return error message
3. Book.return_book: set is_available=True
4. Book.get_info: return dict of book details
5. Library.__init__: set self.books = []
6. Library.add_book: append Book to self.books
7. Library.find_book: search by title, return Book or None
8. Library.get_available_books: return list of available books

## 💡 Hints
- Book.__init__: `self.title = title`, `self.author = author`, `self.isbn = isbn`, `self.is_available = True`
- Book.check_out: `if self.is_available: self.is_available = False else: return "Book is already checked out"`
- Book.return_book: `self.is_available = True`
- Book.get_info: `return {'title': self.title, 'author': self.author, 'isbn': self.isbn, 'is_available': self.is_available}`
- Library.__init__: `self.books = []`
- Library.add_book: `self.books.append(book)`
- Library.find_book: `for book in self.books: if book.title == title: return book`
- Library.get_available_books: `[book for book in self.books if book.is_available]`

## 🔍 Example
Add Book: title = "Python Programming", author = "John Smith", isbn = "1234567890"
Expected Output: book added to library, is_available = True

Check Out: title = "Python Programming"
Expected Output: book.is_available = False

Return Book: title = "Python Programming"
Expected Output: book.is_available = True

## ✅ You Are Done When
- Books can be added to the library
- Books can be checked out when available
- Check out fails when book is already checked out
- Books can be returned
- get_available_books returns only available books
- Library state persists across form submissions
