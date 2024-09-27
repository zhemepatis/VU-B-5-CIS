import utils.global_vars as gv

def encode_letter(letter, text_idx, key):
    alphabet_len = len(gv.alphabet)
    key_len = len(key)

    alphabet_idx = gv.alphabet.index(letter)

    shift = gv.alphabet.index(key[text_idx % key_len])
    return (alphabet_idx + shift) % alphabet_len

def decode_letter(letter, text_idx, key):
    alphabet_len = len(gv.alphabet)
    key_len = len(key)

    alphabet_idx = gv.alphabet.index(letter)

    shift = gv.alphabet.index(key[text_idx % key_len])
    return (alphabet_idx - shift) % alphabet_len

def decode_text(text, key):
    text_len = len(text)

    result = ""
    for i in range(0, text_len - 1):
        e_letter = text[i]
        d_letter = decode_letter(e_letter, i, key)

        result = result + gv.alphabet[d_letter]
    
    return result