import utilities.frequency_test as ft

def get_substring_count(text, substring):
    text_len = len(text)

    count = 0
    for i in range(text_len - len(substring) + 1):
        if text[i::].startswith(substring):
            count += 1

    return count

def get_pattern_frequencies(text):
    N_00 = get_substring_count(text, "00")
    N_01 = get_substring_count(text, "01")
    N_10 = get_substring_count(text, "10")
    N_11 = get_substring_count(text, "11")

    return [N_00, N_01, N_10, N_11]

def get_bit_pair_test_statistic(text):
    N_00, N_01, N_10, N_11 = get_pattern_frequencies(text)
    N_0, N_1, n = ft.get_ones_zeroes_freq(text)
    return (4 / (n - 1)) * (N_00 ** 2 + N_01 ** 2 + N_10 ** 2 + N_11 ** 2) - (2 / n) * (N_0**2 + N_1 ** 2) + 1
