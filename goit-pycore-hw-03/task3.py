import re


def normalize_phone(phone_number: str) -> str:
    """Normalizes a phone number to a standard format."""

    pattern = r"[\D+]"
    modified_number = re.sub(pattern, "", phone_number)

    if not modified_number.startswith("+"):
        if modified_number.startswith("380"):
            modified_number = "+" + modified_number
        else:
            modified_number = "+38" + modified_number

    return modified_number


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

normalized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized numbers: ", normalized_numbers)
