import utilities.global_vars as gv

def letter_2_num(letter):
    return gv.alphabet.index(letter)

def num_2_letter(num):
    return gv.alphabet[num]