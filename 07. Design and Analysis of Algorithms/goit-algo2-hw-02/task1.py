def find_min_max(arr):
    if not arr:
        raise ValueError("Масив не може бути порожнім")

    def helper(low, high):
        # Якщо в масиві лише один елемент
        if low == high:
            return arr[low], arr[low]
        # Якщо є два елементи, порівнюємо їх безпосередньо
        if high == low + 1:
            if arr[low] < arr[high]:
                return arr[low], arr[high]
            else:
                return arr[high], arr[low]

        # Розділяємо масив на дві частини
        mid = (low + high) // 2
        left_min, left_max = helper(low, mid)
        right_min, right_max = helper(mid + 1, high)

        # Об'єднуємо результати з обох частин
        return min(left_min, right_min), max(left_max, right_max)

    return helper(0, len(arr) - 1)


# Приклад використання:
if __name__ == "__main__":
    data = [3, 5, 1, 2, 4, 8, -2, 7]
    min_val, max_val = find_min_max(data)
    print("Мінімум:", min_val)
    print("Максимум:", max_val)
