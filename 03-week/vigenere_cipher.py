global alphabet

def encode_letter(letter, text_idx, key):
    alphabet_len = len(alphabet)
    key_len = len(key)

    alphabet_idx = alphabet.index(letter)

    shift = alphabet.index(key[text_idx % key_len])
    return (alphabet_idx + shift) % alphabet_len

def decode_letter(letter, text_idx, key):
    alphabet_len = len(alphabet)
    key_len = len(key)

    alphabet_idx = alphabet.index(letter)

    shift = alphabet.index(key[text_idx % key_len])
    return (alphabet_idx - shift) % alphabet_len