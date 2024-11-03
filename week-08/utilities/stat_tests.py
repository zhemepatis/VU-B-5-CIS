def count_ones_and_zeroes(text):
    N = [0] * 2
    for char in text:
        num = int(char, 2)
        N[num] += 1

    return N


def frequency_test_stat(text):
    text_len = len(text)
    N = count_ones_and_zeroes(text)

    return ((N[1] - N[0])**2) / text_len


def bit_pairs_test_stat(text):
    text_len = len(text)
    N_pairs = [0] * 4 

    for i in range(text_len - 1):
        curr_pair = text[i:i + 2]
        num = int(curr_pair, 2)
        N_pairs[num] += 1

    N = count_ones_and_zeroes(text)
    return (4 / (text_len - 1)) * (N_pairs[0] ** 2 + N_pairs[1] ** 2 + N_pairs[2] ** 2 + N_pairs[3] ** 2) - (2 / text_len) * (N[0]**2 + N[1]** 2) + 1


def poker_test_stat(text, block_len):
    text_len = len(text)

    block_num = int(text_len / block_len)
    N = [0] * (2 ** block_len)
    for i in range(block_num):
        curr_block = text[i*block_len:(i + 1)*block_len]
        num = int(curr_block, 2)
        N[num] += 1

    return ((2 ** block_len) / block_num) * sum([n**2 for n in N]) - block_num


def test_hypothesis_by_probability(alfa, probability):
    if alfa > probability:
        print("Hypothesis H0 is rejected - the sequence is not typical.")
    else:
        print("Hypothesis H0 is accepted - the sequence is typical.")