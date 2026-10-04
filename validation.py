"""validation.py - Rules for deciding whether a mark is acceptable."""

MIN_MARK = 0
MAX_MARK = 100
INVALID_MESSAGE = "Invalid marks. Enter 0-100."


def validate_mark(mark):
    """Return True if mark is within the allowed range (0-100), else False."""
    return MIN_MARK <= mark <= MAX_MARK
