def binary_search_with_upper_bound(arr, x):
    """Performs binary search for element 'x' in a sorted list arr."""

    # Initial index of the left and the right boundaries of the list
    low, high = 0, len(arr) - 1

    # Variable to count iterations
    iterations = 0

    # Variable to store the upper bound
    upper_bound = None

    while low <= high:
        iterations += 1  # Increment iteration counter

        mid = (high + low) // 2  # Calculate the middle index

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1

        else:
            upper_bound = arr[mid]
            return iterations, upper_bound

    # If the element is not found, return the number of iterations and the upper bound
    return iterations, upper_bound


# Testing the function
arr = [1.1, 1.3, 2.5, 3.8, 4.6]
print(binary_search_with_upper_bound(arr, 3.5))  # (2, 3.8)
print(binary_search_with_upper_bound(arr, 4))    # (3, 4.6)
print(binary_search_with_upper_bound(arr, 6.0))  # (3, None)
print(binary_search_with_upper_bound(arr, 2.5))  # (1, 2.5)
print(binary_search_with_upper_bound(arr, 0))    # (2, 1.1)
