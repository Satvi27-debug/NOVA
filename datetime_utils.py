"""
datetime_utils.py
=================
Module responsible for retrieving and formatting system date and time.

PRD Compliance:
- FR-03: Display current date on request.
- FR-04: Display current time on request.
"""

from datetime import datetime


def get_current_time() -> str:
    """
    Retrieves and formats the current system time.

    Returns:
        str: Human-readable 12-hour time representation (e.g., '07:45 PM').
    """
    now = datetime.now()
    formatted_time = now.strftime("%I:%M %p")
    return f"Assistant: It's currently {formatted_time}."


def get_current_date() -> str:
    """
    Retrieves and formats the current system date.

    Returns:
        str: Human-readable date representation (e.g., 'Thursday, October 22, 2026').
    """
    now = datetime.now()
    formatted_date = now.strftime("%A, %B %d, %Y")
    return f"Assistant: Today's date is {formatted_date}."
