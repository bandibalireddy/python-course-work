# Assignment 20 — Word Frequency Counter

## 🎯 What You Will Practice
Learn how to use dictionaries, loops, string methods, and sorting to analyze text.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Split text into words, strip punctuation from each word
2. Loop through words, build word_freq dict with counts
3. Count total_words and unique_count
4. Sort based on sort_by selection (Most Frequent, Least Frequent, Alphabetical)
5. Store sorted result as list of (word, count) tuples

## 💡 Hints
- Split: `words = text.split()`
- Strip punctuation: `word.strip('.,!?;:"')`
- Build dict: `if word in word_freq: word_freq[word] += 1 else: word_freq[word] = 1`
- Sort by frequency: `sorted(word_freq.items(), key=lambda x: x[1], reverse=True)`
- Sort alphabetically: `sorted(word_freq.items(), key=lambda x: x[0])`

## 🔍 Example
Input: text = "hello world hello python world", sort_by = "Most Frequent"
Expected Output: sorted_words = [("hello", 2), ("world", 2), ("python", 1)], total_words = 4, unique_count = 3

## ✅ You Are Done When
- Words are counted correctly
- Punctuation is stripped from words
- All three sort options work
- Total and unique counts are accurate
