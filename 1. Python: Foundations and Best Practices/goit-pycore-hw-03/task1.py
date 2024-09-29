from datetime import datetime


def get_days_from_today(date: str) -> int:
    """Calculate the number of days between the given date and today's date."""

    if not isinstance(date, str):
        raise ValueError("Input date should be a string in 'YYYY-MM-DD' format.")

    try:
        # Convert the input date string into a datetime object
        date_object = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        # Handle the case when the input date format is not correct
        raise ValueError("Invalid input date format. Enter date in 'YYYY-MM-DD' format.")

    # Get the current timestamp
    current_date = datetime.today()

    # Calculate the difference between the current date and the input date
    delta = current_date - date_object

    # Return the difference in days
    return delta.days


# Test the function
print(get_days_from_today("2021-10-09"))
print(get_days_from_today("2025-10-09"))
print(get_days_from_today("2024-07-06"))
print(get_days_from_today(333))
print(get_days_from_today("foo bar"))
