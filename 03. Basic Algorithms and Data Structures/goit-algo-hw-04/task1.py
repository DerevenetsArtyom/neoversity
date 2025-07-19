import random
import timeit


def insertion_sort(array: list[int]) -> list[int]:
    # Assume that the first element is already sorted, so the loop starts from the second element.
    for i in range(1, len(array)):
        # The element "key" will be inserted into the correct place in the already sorted part of the list.
        key = array[i]

        # To compare key with elements, initialize j as the index of the previous element relative to key.
        j = i - 1

        # To insert key into the sorted part of the list, we compare it with each element before it, starting from
        # the last element of the sorted part (index j) and continuing until the beginning of the list (j >= 0).
        while j >= 0 and key < array[j]:
            # Shift array[j] (the previous element) one position to the right to make room for key.
            array[j + 1] = array[j]
            # Decrease j to continue comparing with previous elements.
            j -= 1

        # After exiting the while loop, j will be one less than the index where key should be inserted.
        array[j + 1] = key
        # Insert key into the correct place in the sorted part of the list.

    return array


def merge_sort(array: list[int]) -> list[int]:
    # A list with one element does not need sorting, so continue the sorting only if the list length is greater than 1.
    if len(array) > 1:

        # Find the middle of the list to divide it into two halves.
        mid = len(array) // 2

        # Create the left half of the list, containing elements from the beginning to the middle.
        left_half = array[:mid]  # list from the beginning to the middle (excluding the middle).

        # The right half of the list, containing elements from the middle to the end.
        right_half = array[mid:]  # list from the middle to the end (including the middle).

        # Recursively sort the left half of the list.
        merge_sort(left_half)

        # Recursively sort the right half of the list.
        merge_sort(right_half)

        # Initialize indices i, j, k for iterating through the left, right halves, and merged list, respectively.
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            # While there are elements in both halves, compare them.
            if left_half[i] < right_half[j]:
                # If the element from the left half is smaller, add it to the merged list.
                array[k] = left_half[i]

                # The element from the left half was added to the merged list (there is one less element in left half),
                # so we move the index i to the next element in the left half.
                i += 1

            else:
                # If the element from the right half is smaller or equal, add it to the merged list.
                array[k] = right_half[j]

                # Accordingly, there is one less element in the right half,
                # so we move the index j to the next element in the right half.
                j += 1

            # Regardless of which element was added to the merged list,
            # increase the index k to insert the next element in the next position.
            k += 1

        # In case the list length is odd and as a result of integer division, there are elements left in
        # one of the halves, add the last element from that half to the end of the merged list.
        while i < len(left_half):  # If present, add the remaining elements from the left half.
            array[k] = left_half[i]
            i += 1
            k += 1

        # If there are elements in the right half, add them.
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

    return array


def test_sort_algorithms() -> None:
    sizes = [100, 1000, 10000]  # Array sizes for testing
    repetitions = 5  # Number of repetitions for each test

    for size in sizes:
        # Generate a random array of integers
        array = [random.randint(0, size) for _ in range(size)]
        print(f"\nArray size: {size}")

        # Measure the time for insertion sort
        insertion_time = timeit.timeit(lambda: insertion_sort(array.copy()), number=repetitions)
        print(f"Insertion Sort: {insertion_time / repetitions:.6f} seconds")

        # Measure the time for merge sort
        merge_time = timeit.timeit(lambda: merge_sort(array.copy()), number=repetitions)
        print(f"Merge Sort: {merge_time / repetitions:.6f} seconds")

        # Measure the time for Timsort (built-in sorted function)
        timsort_time = timeit.timeit(lambda: sorted(array.copy()), number=repetitions)
        print(f"Timsort: {timsort_time / repetitions:.6f} seconds")


if __name__ == "__main__":
    test_sort_algorithms()


"""
Test Results (number of repetitions = 100):

Array size: 100
    Insertion Sort: 0.000442 seconds
    Merge Sort: 0.000355 seconds
    Timsort: 0.000008 seconds

Array size: 1000
    Insertion Sort: 0.026151 seconds
    Merge Sort: 0.001959 seconds
    Timsort: 0.000077 seconds

Array size: 10000
    Insertion Sort: 2.552459 seconds
    Merge Sort: 0.026298 seconds
    Timsort: 0.001108 seconds

Висновок:
"Merge sort" є більш ефективним, ніж "insertion sort", особливо для великих масивів. 
Вбудована функція sorted (Timsort) є швидшою за інші наявні тут алгоритми. Для практичного використання в реальних
проектах варто використовувати вбудовані функції сортування Python (sort() або sorted()), оскільки вони реалізовані
на основі Timsort і забезпечують найкращу продуктивність та ефективність для більшості випадків.
"""
