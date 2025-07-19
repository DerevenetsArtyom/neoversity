def check_brackets(expression: str) -> str:
    stack = []
    matching_bracket = {")": "(", "}": "{", "]": "["}

    # Iterate over each character in the string
    for char in expression:
        # If the character is in the values of the brackets dictionary, add it to the stack
        if char in "({[":
            stack.append(char)

        elif char in ")}]":
            if not stack or stack.pop() != matching_bracket[char]:
                return "Asymmetric"

    return "Symmetric" if not stack else "Asymmetric"


# Function check
print(check_brackets("( ){[ 1 ]( 1 + 3 )( ){ }}"))
print(check_brackets("( 23 ( 2 - 3);"))
print(check_brackets("( 11 }"))
print(check_brackets("( () }"))
