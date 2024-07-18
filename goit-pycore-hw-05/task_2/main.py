import re
from typing import Callable


def generator_numbers(text: str):
    """The function to generate a sequence of float numbers that are found in the input text."""
    pattern = r"\b\d+\.\d+\b"  # Regexp to match float numbers

    for match in re.finditer(pattern, text):
        yield float(match.group())  # Yield each float number


def sum_profit(text: str, func: Callable) -> float:
    """The function to calculate the total profit based on the input text."""
    return sum(func(text))


# Example usage
text = """Загальний дохід працівника складається з декількох частин: 
1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."""
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
