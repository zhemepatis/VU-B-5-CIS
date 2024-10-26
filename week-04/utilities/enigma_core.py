import utilities.global_vars as gv

def get_reverse_rotor_lambda(rotor_lambda):
    num = len(rotor_lambda)
    return [rotor_lambda.index(idx) for idx in range(num)]

def get_shifts(letter_idx, key_1, key_2):
    alphabet_len = len(gv.alphabet)
    shift_1 = letter_idx % alphabet_len # m_1
    shift_2 = int((letter_idx - shift_1) / alphabet_len) # m_2

    shift_1 += key_1
    shift_2 += key_2

    return (shift_1, shift_2)

# passes rho^-1 . lambda . rho
def pass_iteration(letter, shift, rotor_lambda):
    alphabet_len = len(gv.alphabet)
    return (rotor_lambda[(letter + shift) % alphabet_len] - shift) % alphabet_len