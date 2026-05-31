# Assignment 40 — CSV Data Analyzer

## 🎯 What You Will Practice
Learn how to parse files, handle string parsing, and use exception handling for data processing.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find:
```python
# ── STUDENT CODE START ──────────────────────────

# ── STUDENT CODE END ────────────────────────────
```

## 📝 Your Tasks
1. Split csv_data into lines
2. Parse header row using delimiter
3. Loop through remaining lines, split each by delimiter
4. Try to convert each cell to float for numeric columns
5. Catch ValueError for non-numeric cells, add to errors list
6. Build rows as list of dicts {header: value}
7. Calculate numeric_stats for all numeric columns (min, max, avg, sum)
8. Count valid rows

## 💡 Hints
- Split lines: `lines = csv_data.strip().split('\n')`
- Parse header: `headers = lines[0].split(delimiter)`
- Loop rows: `for line in lines[1:]: cells = line.split(delimiter)`
- Try convert: `try: value = float(cell) except ValueError: keep as string`
- Build dict: `row_dict = {headers[i]: cells[i] for i in range(len(headers))}`
- Numeric stats: track min, max, sum, count for each numeric column
- Calculate avg: `sum / count` when count > 0

## 🔍 Example
CSV: "Name,Age,Score\nAlice,25,95\nBob,30,88"
Expected Output: headers = ["Name", "Age", "Score"], rows = [{"Name": "Alice", "Age": 25, "Score": 95}, ...], numeric_stats = {"Age": {"min": 25, "max": 30, "avg": 27.5, "sum": 55}, "Score": {...}}

## ✅ You Are Done When
- CSV is parsed correctly with different delimiters
- Header row is identified
- Data rows are converted to dicts
- Numeric columns are identified and statistics calculated
- Non-numeric values are caught and errors are logged
