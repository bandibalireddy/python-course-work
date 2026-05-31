from django.shortcuts import render

def index(request):
    weeks = [
        {
            'name': 'Week 1-2',
            'topic': 'Variables, Strings, Lists & Loops',
            'assignments': [
                {'number': 1, 'title': 'Simple Calculator', 'description': 'Perform basic arithmetic operations with two numbers.', 'url': '/assignment1/'},
                {'number': 2, 'title': 'String Inspector', 'description': 'Analyze strings: length, case conversion, reversal, and vowel counting.', 'url': '/assignment2/'},
                {'number': 3, 'title': 'Even/Odd & Divisibility Checker', 'description': 'Check if a number is even/odd and divisible by 3, 5, or both.', 'url': '/assignment3/'},
                {'number': 4, 'title': 'Grocery List Manager', 'description': 'Add, remove, view, and clear items from a grocery list.', 'url': '/assignment4/'},
                {'number': 5, 'title': 'Number List Stats', 'description': 'Calculate min, max, sum, average, and sort a list of numbers.', 'url': '/assignment5/'},
                {'number': 6, 'title': 'Mini Profile Card', 'description': 'Create a profile card with name, age, hobbies, and city.', 'url': '/assignment6/'},
                {'number': 7, 'title': 'Grade Classifier', 'description': 'Convert numerical scores to letter grades with messages.', 'url': '/assignment7/'},
                {'number': 8, 'title': 'Number Guessing Game', 'description': 'Guess a secret number with hints and attempt tracking.', 'url': '/assignment8/'},
                {'number': 9, 'title': 'Word Counter & Analyzer', 'description': 'Count words, find longest word, unique words, and characters.', 'url': '/assignment9/'},
                {'number': 10, 'title': 'FizzBuzz with Custom Rules', 'description': 'Custom FizzBuzz game with customizable words.', 'url': '/assignment10/'},
                {'number': 11, 'title': 'Shopping Cart', 'description': 'Manage a shopping cart with items, prices, and discounts.', 'url': '/assignment11/'},
                {'number': 12, 'title': 'Student Grade Book', 'description': 'Track student grades and calculate class statistics.', 'url': '/assignment12/'},
                {'number': 13, 'title': 'Personal Quiz App', 'description': 'Answer 5 questions and get scored with performance feedback.', 'url': '/assignment13/'},
            ]
        },
        {
            'name': 'Week 3',
            'topic': 'If/Else & For Loops',
            'assignments': [
                {'number': 14, 'title': 'Age Group Classifier', 'description': 'Classify age into groups using if/elif/else.', 'url': '/assignment14/'},
                {'number': 15, 'title': 'Number Range Validator', 'description': 'Check if a number falls within specified ranges.', 'url': '/assignment15/'},
                {'number': 16, 'title': 'List Builder', 'description': 'Build a list using for loops and range().', 'url': '/assignment16/'},
                {'number': 17, 'title': 'Nested Condition Builder', 'description': 'Use nested if/elif/else for complex logic.', 'url': '/assignment17/'},
                {'number': 18, 'title': 'String Pattern Matcher', 'description': 'Match string patterns using loops and conditionals.', 'url': '/assignment18/'},
            ]
        },
        {
            'name': 'Week 4',
            'topic': 'Dictionaries',
            'assignments': [
                {'number': 19, 'title': 'Student Grades Lookup', 'description': 'Look up student grades using dictionaries.', 'url': '/assignment19/'},
                {'number': 20, 'title': 'Word Frequency Counter', 'description': 'Count word occurrences in text.', 'url': '/assignment20/'},
                {'number': 21, 'title': 'Country Capital Finder', 'description': 'Find capitals using a hardcoded dictionary.', 'url': '/assignment21/'},
                {'number': 22, 'title': 'Student Report Card', 'description': 'Create report cards with dict operations.', 'url': '/assignment22/'},
                {'number': 23, 'title': 'Inventory Manager', 'description': 'Manage inventory with nested dictionaries.', 'url': '/assignment23/'},
            ]
        },
        {
            'name': 'Week 5',
            'topic': 'While Loops & Match/Case',
            'assignments': [
                {'number': 24, 'title': 'Countdown Timer', 'description': 'Create a countdown using while loop.', 'url': '/assignment24/'},
                {'number': 25, 'title': 'Collatz Conjecture', 'description': 'Explore the Collatz sequence with while loops.', 'url': '/assignment25/'},
                {'number': 26, 'title': 'ATM Simulator', 'description': 'Simulate ATM operations with while loop.', 'url': '/assignment26/'},
                {'number': 27, 'title': 'Day Type Classifier', 'description': 'Classify days using match/case.', 'url': '/assignment27/'},
                {'number': 28, 'title': 'HTTP Status Decoder', 'description': 'Decode HTTP codes using match/case.', 'url': '/assignment28/'},
            ]
        },
        {
            'name': 'Week 6',
            'topic': 'Functions',
            'assignments': [
                {'number': 29, 'title': 'Unit Converter', 'description': 'Convert units using custom functions.', 'url': '/assignment29/'},
                {'number': 30, 'title': 'Password Strength Checker', 'description': 'Check password strength with functions.', 'url': '/assignment30/'},
                {'number': 31, 'title': 'Prime Number Checker', 'description': 'Check primes and list them using functions.', 'url': '/assignment31/'},
                {'number': 32, 'title': 'BMI Calculator', 'description': 'Calculate BMI with multiple functions.', 'url': '/assignment32/'},
                {'number': 33, 'title': 'Text Formatter Library', 'description': 'Transform text using function library.', 'url': '/assignment33/'},
            ]
        },
        {
            'name': 'Week 7',
            'topic': 'Classes & OOP',
            'assignments': [
                {'number': 34, 'title': 'Bank Account Class', 'description': 'Implement a BankAccount class.', 'url': '/assignment34/'},
                {'number': 35, 'title': 'Library Book Tracker', 'description': 'Track books using Book and Library classes.', 'url': '/assignment35/'},
                {'number': 36, 'title': 'Simple RPG Character', 'description': 'Create RPG characters with Character class.', 'url': '/assignment36/'},
                {'number': 37, 'title': 'Vehicle Fleet Manager', 'description': 'Manage vehicles using inheritance.', 'url': '/assignment37/'},
                {'number': 38, 'title': 'Student Gradebook OOP', 'description': 'Manage grades using OOP.', 'url': '/assignment38/'},
            ]
        },
        {
            'name': 'Week 8',
            'topic': 'Files & Exceptions',
            'assignments': [
                {'number': 39, 'title': 'File Word Counter', 'description': 'Write, read, and analyze text files.', 'url': '/assignment39/'},
                {'number': 40, 'title': 'CSV Data Analyzer', 'description': 'Parse CSV data with exception handling.', 'url': '/assignment40/'},
                {'number': 41, 'title': 'Safe Calculator with Exceptions', 'description': 'Calculator with comprehensive exception handling.', 'url': '/assignment41/'},
                {'number': 42, 'title': 'Personal Diary', 'description': 'Write and read diary entries with dates.', 'url': '/assignment42/'},
                {'number': 43, 'title': 'Exception Hierarchy Explorer', 'description': 'Explore custom exceptions and hierarchy.', 'url': '/assignment43/'},
            ]
        },
    ]
    return render(request, 'home/index.html', {'weeks': weeks})
