import utilities.enigma_core as ec

def encrypt_letter(letter, letter_idx, key_1, key_2, rotor_lambda_1, rotor_lambda_2):
    shift_1, shift_2 = ec.get_shifts(letter_idx, key_1, key_2)
    letter = ec.pass_iteration(letter, shift_1, rotor_lambda_1)
    return ec.pass_iteration(letter, shift_2, rotor_lambda_2)

def decrypt_letter(letter, letter_idx, key_1, key_2, rotor_lambda_1, rotor_lambda_2):
    rotor_lambda_1 = ec.get_reverse_rotor_lambda(rotor_lambda_1)
    rotor_lambda_2 = ec.get_reverse_rotor_lambda(rotor_lambda_2)

    shift_1, shift_2 = ec.get_shifts(letter_idx, key_1, key_2)

    letter = ec.pass_iteration(letter, shift_2, rotor_lambda_2)
    return ec.pass_iteration(letter, shift_1, rotor_lambda_1)