import utils.global_vars as gv
from collections import defaultdict

def get_splits(text, num):
    text_len = len(text)

    result = num*[""]
    for i in range(0, text_len):
        result[i % num] = result[i % num] + text[i]

    return result

def count_frequencies(text):   
    letter_dict = defaultdict(int)

    for letter in text:
        letter_dict[letter] = letter_dict[letter] + 1

    result = ""
    for letter in sorted(letter_dict, key=letter_dict.get, reverse=True):
        result = result + letter

    return result