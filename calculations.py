"""calculations.py - Pure business logic: totals, averages and grading rule.

No input() or print() calls live here, so the logic can be tested and
reused with any user interface (console, GUI, web).
"""


def calculate_total(marks):
    """Return the sum of all marks."""
    return sum(marks)


def calculate_average(marks):
    """Return the average of the marks."""
    return calculate_total(marks) / len(marks)


def calculate_grade(average):
    """Return the letter grade for an average mark."""
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"
