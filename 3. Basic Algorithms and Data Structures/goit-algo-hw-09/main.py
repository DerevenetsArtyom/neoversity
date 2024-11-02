import timeit
from tabulate import tabulate

coins = [50, 25, 10, 5, 2, 1]  # Set of available coins


# Greedy algorithm function for dispensing change
def find_coins_greedy(amount):
    result = {}  # Dictionary to store the results

    for coin in coins:  # Iterate through each coin
        if amount >= coin:  # Check if this coin can be used
            result[coin] = amount // coin  # Add the number of coins of this denomination
            amount = amount % coin  # Update the remaining amount

    return result


# Dynamic programming function for dispensing change
def find_min_coins(amount):
    min_coins = [0] + [float("inf")] * amount  # Initialize list of minimum number of coins for each amount
    coin_count = [{} for _ in range(amount + 1)]  # List to store dictionaries with coin counts for each amount

    for coin in coins:  # Iterate through each coin
        for x in range(coin, amount + 1):  # Iterate through each amount from the coin denomination to the target amount
            if min_coins[x - coin] + 1 < min_coins[x]:  # Check if we can reduce the number of coins
                min_coins[x] = min_coins[x - coin] + 1  # Update the minimum number of coins for amount x
                coin_count[x] = coin_count[x - coin].copy()  # Copy the dictionary with coin counts for amount x - coin
                if coin in coin_count[x]:  # Check if the coin is already used
                    coin_count[x][coin] += 1  # Increase the count of this denomination
                else:
                    coin_count[x][coin] = 1  # Add the new coin to the dictionary

    return coin_count[amount]


# Define different amounts for dispensing change
amounts = [10, 55, 113, 207, 505, 1001]

# Collecting execution time results
results = []

for amount in amounts:
    # Measure execution time of greedy algorithm
    time_greedy = timeit.timeit(lambda: find_coins_greedy(amount), number=1000)
    # Measure execution time of dynamic programming algorithm
    time_dp = timeit.timeit(lambda: find_min_coins(amount), number=1000)
    results.append([amount, time_greedy, time_dp])

# Display results in table format
headers = ["Amount", "Greedy Algorithm (s)", "Dynamic Programming (s)"]  # Table headers
table = tabulate(results, headers, tablefmt="pipe")  # Create table with results
print(table)
