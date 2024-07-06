import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """Function to generate a set of unique random numbers for the lotteries."""

    # Check if the input parameters are valid and return an empty list if they are not
    for num in [min, max, quantity]:
        if not isinstance(num, int):
            return []

    if (min < 1) or (max > 1000) or not (min <= quantity <= max):
        return []  
    
    # Generate 'quantity' unique random numbers within the range
    random_numbers = random.sample(range(min, max + 1), quantity)

    # Sort the generated numbers
    random_numbers.sort()

    # Return the list of random numbers
    return random_numbers


print("Your numbers are: ", get_numbers_ticket(1, 49, 6))
print("Your numbers are: ", get_numbers_ticket(10, 10, 5))
print("Your numbers are: ", get_numbers_ticket(0, 10, 5))
print("Your numbers are: ", get_numbers_ticket(0, 1005, 2))
print("Your numbers are: ", get_numbers_ticket(1, 10, 20))
print("Your numbers are: ", get_numbers_ticket("3", 10, 2))
