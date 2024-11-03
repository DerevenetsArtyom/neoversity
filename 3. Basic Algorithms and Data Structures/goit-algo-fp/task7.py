import random
from fractions import Fraction

import matplotlib.pyplot as plt
import pandas as pd


def monte_carlo_simulation(num_simulations: int) -> dict:
    """Симуляція кидків двох кубиків з підрахунком ймовірностей для кожної суми."""
    sum_counts = {i: 0 for i in range(2, 13)}

    # Симуляція кидків кубиків
    for _ in range(num_simulations):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        sum_counts[total] += 1  # Збільшення лічильника для відповідної суми

    # Обчислення ймовірностей у відсотках
    probabilities = {s: (count / num_simulations) * 100 for s, count in sum_counts.items()}
    return probabilities


def analytical_probabilities() -> dict:
    """Розрахунок аналітичних ймовірностей для кожної суми при кидку двох кубиків."""
    return {
        2: (1, 36),
        3: (2, 36),
        4: (3, 36),
        5: (4, 36),
        6: (5, 36),
        7: (6, 36),
        8: (5, 36),
        9: (4, 36),
        10: (3, 36),
        11: (2, 36),
        12: (1, 36),
    }


def display_results(monte_carlo_probs: dict, analytical_probs: dict) -> pd.DataFrame:
    """Функція для виведення результатів у вигляді таблиці."""
    table_data = []

    for s in range(2, 13):
        monte_carlo_prob = monte_carlo_probs[s]
        # Обчислення аналітичної ймовірності
        analytical_prob = analytical_probs[s][0] / analytical_probs[s][1] * 100
        # Перетворення в дробовий вигляд
        fraction = Fraction(analytical_probs[s][0], analytical_probs[s][1])

        table_data.append([s, f"{monte_carlo_prob:.2f}%", f"{analytical_prob:.2f}% ({fraction})"])

    # Створення DataFrame для зручності виведення
    df = pd.DataFrame(
        table_data,
        columns=["Сума", "Монте-Карло", "Аналітично"],
    )
    print(df.to_string(index=False))
    return df


def plot_probabilities(df: pd.DataFrame):
    """Побудова графіка для порівняння аналітичних і симуляційних ймовірностей."""

    df_plot = df.copy()
    # Перетворення значень на float
    df_plot["Монте-Карло"] = df_plot["Монте-Карло"].str.rstrip("%").astype(float)
    # Витягування числових значень
    df_plot["Аналітично"] = df_plot["Аналітично"].str.extract(r"(\d+\.\d+)%").astype(float)

    # Побудова графіка
    df_plot.plot(
        x="Сума",
        y=["Монте-Карло", "Аналітично"],
        kind="bar",
        color=["blue", "orange"],
        alpha=0.7,
    )
    plt.title("Ймовірності сум чисел на двох кубиках")
    plt.ylabel("Ймовірність (%)")
    plt.xlabel("Сума чисел на кубиках")
    plt.xticks(rotation=0)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


num_simulations = 100_000  # Кількість симуляцій
monte_carlo_probs = monte_carlo_simulation(num_simulations)
analytical_probs = analytical_probabilities()

df = display_results(monte_carlo_probs, analytical_probs)

plot_probabilities(df)
