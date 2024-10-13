import timeit


def build_shift_table(pattern):
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table


def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    return -1


def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)
    lps = compute_lps(pattern)
    i = j = 0
    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1
        if j == M:
            return i - j
    return -1


def polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def rabin_karp_search(main_string, substring):
    substring_length = len(substring)
    main_string_length = len(main_string)
    base = 256
    modulus = 101
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    h_multiplier = pow(base, substring_length - 1) % modulus
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i : i + substring_length] == substring:
                return i
        if i < main_string_length - substring_length:
            current_slice_hash = (
                current_slice_hash - ord(main_string[i]) * h_multiplier
            ) % modulus
            current_slice_hash = (
                current_slice_hash * base + ord(main_string[i + substring_length])
            ) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus
    return -1


pattern_existing = "відомі алгоритми пошуку"
pattern_non_existing = "випадковий підрядок"

with open("articles/article1.txt", "r", encoding="utf-8") as file:
    text_1 = file.read()
with open("articles/article2.txt", "r", encoding="utf-8") as file:
    text_2 = file.read()


def measure_time(func, text, pattern):
    return timeit.timeit(lambda: func(text, pattern), number=1000)

time_bm_1_existing = measure_time(boyer_moore_search, text_1, pattern_existing)
time_bm_1_non_existing = measure_time(boyer_moore_search, text_1, pattern_non_existing)

time_kmp_1_existing = measure_time(kmp_search, text_1, pattern_existing)
time_kmp_1_non_existing = measure_time(kmp_search, text_1, pattern_non_existing)

time_rk_1_existing = measure_time(rabin_karp_search, text_1, pattern_existing)
time_rk_1_non_existing = measure_time(rabin_karp_search, text_1, pattern_non_existing)

time_bm_2_existing = measure_time(boyer_moore_search, text_2, pattern_existing)
time_bm_2_non_existing = measure_time(boyer_moore_search, text_2, pattern_non_existing)

time_kmp_2_existing = measure_time(kmp_search, text_2, pattern_existing)
time_kmp_2_non_existing = measure_time(kmp_search, text_2, pattern_non_existing)

time_rk_2_existing = measure_time(rabin_karp_search, text_2, pattern_existing)
time_rk_2_non_existing = measure_time(rabin_karp_search, text_2, pattern_non_existing)

results = {
    "Article 1": {
        "Existing": {
            "Boyer-Moore": time_bm_1_existing,
            "Knuth-Morris-Pratt": time_kmp_1_existing,
            "Rabin-Karp": time_rk_1_existing,
        },
        "Non-Existing": {
            "Boyer-Moore": time_bm_1_non_existing,
            "Knuth-Morris-Pratt": time_kmp_1_non_existing,
            "Rabin-Karp": time_rk_1_non_existing,
        },
    },
    "Article 2": {
        "Existing": {
            "Boyer-Moore": time_bm_2_existing,
            "Knuth-Morris-Pratt": time_kmp_2_existing,
            "Rabin-Karp": time_rk_2_existing,
        },
        "Non-Existing": {
            "Boyer-Moore": time_bm_2_non_existing,
            "Knuth-Morris-Pratt": time_kmp_2_non_existing,
            "Rabin-Karp": time_rk_2_non_existing,
        },
    },
}


def print_results(results):
    for article, types in results.items():
        print(f"{article}:")
        for result_type, algorithms in types.items():
            print(f"  {result_type}:")
            for algo, time in algorithms.items():
                print(f"    {algo}: {time:.6f} seconds")
        print()


print_results(results)
