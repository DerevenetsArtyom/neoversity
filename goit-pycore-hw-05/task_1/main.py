def caching_fibonacci() -> callable:
    """Return a function that calculates Fibonacci numbers using caching."""
    cache = {}  # a dictionary to keep already calculated values

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            # return the number from cache if present
            return cache[n]
        else:
            # get the result and add it to cache
            result = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = result
            return result

    return fibonacci


# Get the `fibonacci` function
fib = caching_fibonacci()

# Print 55 cache {2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55}
print(fib(10))
# Print 610 cache {....11: 89, 12: 144, 13: 233, 14: 377, 15: 610}
print(fib(15))
