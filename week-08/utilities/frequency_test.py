def freq_test_statistic(ones_num, zeroes_num, char_num):
    return ((ones_num - zeroes_num)**2) / char_num

def get_ones_zeroes_freq(bin_text):
    txt_len = len(bin_text)

    zeroes_count = 0
    for char in bin_text:
        if char == "0":
            zeroes_count += 1

    return [zeroes_count, txt_len - zeroes_count, txt_len]