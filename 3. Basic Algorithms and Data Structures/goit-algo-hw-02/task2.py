from collections import deque


def is_palindrome(string) -> bool:
    # Remove spaces and convert to lowercase
    string = string.replace(' ', '').lower()

    # Create a deque (double-ended queue)
    char_deque = deque(string)

    # Compare characters from both ends of the deque
    while len(char_deque) > 1:
        if char_deque.pop() != char_deque.popleft():
            return False

    return True


# Tests
print("A man a plan a canal Panama --> ", is_palindrome("A man a plan a canal Panama"))
print("hell --> ", is_palindrome("hell"))
print("racecar --> ", is_palindrome("racecar"))
print("noon --> ", is_palindrome("noon"))
print("Was it a car or a cat I saw --> ", is_palindrome("Was it a car or a cat I saw"))
print("Never odd or even --> ", is_palindrome("Never odd or even"))

