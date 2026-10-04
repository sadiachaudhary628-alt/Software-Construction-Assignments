"""display.py - Presentation of the result. Knows nothing about how values are computed."""


def display_result(name, total, average, grade):
    """Print the formatted student result."""
    print("\nStudent Result")
    print("----------------")
    print("Name:", name)
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)
