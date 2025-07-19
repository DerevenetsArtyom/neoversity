import heapq


def connect_cables_min_cost(cable_lengths):
    # Ініціалізуємо мін-купу
    heapq.heapify(cable_lengths)

    # Визначаємо загальні витрати
    total_cost = 0

    # Поки в купі більше ніж один кабель
    while len(cable_lengths) > 1:
        # Вибираємо два найменших елементи
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)

        # Об'єднуємо, вартість об'єднання додається до загальних витрат
        cost = first + second
        total_cost += cost

        # Додаємо новий об'єднаний кабель назад до купи
        heapq.heappush(cable_lengths, cost)

        print(f"Об'єднання кабелів {first} та {second} з витратами {cost}. Загальні витрати: {total_cost}")
        print(f"Поточний стан купи: {cable_lengths}")

    return total_cost


if __name__ == "__main__":
    cable_lengths = [7, 1, 6, 4]
    min_cost = connect_cables_min_cost(cable_lengths)
    print("Мінімальні витрати на об'єднання кабелів:", min_cost)  # Вихід: 34

    print()
    cable_lengths = [4, 3, 2, 6]
    min_cost = connect_cables_min_cost(cable_lengths)
    print("Мінімальні витрати на об'єднання кабелів:", min_cost)  # Вихід: 29
