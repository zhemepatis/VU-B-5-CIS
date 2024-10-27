import utils.global_vars as gv

def encrypt_letter(letter, letter_idx, key):
    alphabet_len = len(gv.alphabet)
    key_len = len(key)

    alphabet_idx = gv.alphabet.index(letter)

    shift = gv.alphabet.index(key[letter_idx % key_len])
    return gv.alphabet[(alphabet_idx + shift) % alphabet_len]

def decrypt_letter(letter, letter_idx, key):
    alphabet_len = len(gv.alphabet)
    key_len = len(key)

    alphabet_idx = gv.alphabet.index(letter)
    
    shift = gv.alphabet.index(key[letter_idx % key_len])
    return gv.alphabet[(alphabet_idx - shift) % alphabet_len]

def decrypt_text(text, key):
    text_len = len(text)

    result = ""
    for i in range(0, text_len - 1):
        e_letter = text[i]
        d_letter = decrypt_letter(e_letter, i, key)

        result = result + d_letter
    
    return result