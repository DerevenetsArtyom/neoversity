import time
import re
import mmh3

class HyperLogLog:
    def __init__(self, precision=14):
        self.precision = precision
        self.buckets = [0] * (2 ** precision)

    def add(self, item):
        hash_value = mmh3.hash(item, signed=False)
        index = hash_value >> (32 - self.precision)
        rank = (hash_value & ((1 << (32 - self.precision)) - 1)).bit_length()
        self.buckets[index] = max(self.buckets[index], rank)

    def count(self):
        alpha = 0.7213 / (1 + 1.079 / len(self.buckets))
        estimate = alpha * len(self.buckets) ** 2 / sum(2 ** -b for b in self.buckets)
        return round(estimate)


def load_ip_addresses(file_path):
    """Завантаження IP-адрес з лог-файлу, ігноруючи некоректні рядки."""
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    ip_addresses = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = ip_pattern.search(line)
            if match:
                ip_addresses.append(match.group())
    return ip_addresses


def exact_count(ip_addresses):
    """Точний підрахунок унікальних IP-адрес."""
    return len(set(ip_addresses))


def hyperloglog_count(ip_addresses):
    """Підрахунок унікальних IP-адрес за допомогою HyperLogLog."""
    hll = HyperLogLog()
    for ip in ip_addresses:
        hll.add(ip)
    return hll.count()


if __name__ == "__main__":
    file_path = "C:/Users/38098/PyCharmProjects/Algorithm_tacks/HW_Algorithms/lms-stage-access.log"

    # Завантаження даних
    ip_addresses = load_ip_addresses(file_path)

    # Точний підрахунок
    start_time = time.time()
    exact_result = exact_count(ip_addresses)
    exact_time = time.time() - start_time

    # Підрахунок HyperLogLog
    start_time = time.time()
    hll_result = hyperloglog_count(ip_addresses)
    hll_time = time.time() - start_time

    # Виведення результатів у вигляді таблиці
    print("Результати порівняння:")
    print(f"{'':<25}{'Точний підрахунок':<20}{'HyperLogLog':<15}")
    print(f"{'Унікальні елементи':<25}{exact_result:<20}{hll_result:<15}")
    print(f"{'Час виконання (сек.)':<25}{exact_time:<20.5f}{hll_time:<15.5f}")
