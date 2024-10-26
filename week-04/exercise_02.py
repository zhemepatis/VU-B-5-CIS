import utilities.global_vars as gv
from utilities.letter_conversion_by_alphabet import letter_2_num, num_2_letter
from utilities.simplified_enigma_cipher import decrypt_letter

# defining global variable
gv.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_len = len(gv.alphabet)

# defining ENIGMA setup
rotor_lambda_1 = [8, 13, 24, 18, 9, 0, 7, 14, 10, 11, 19, 25, 4, 17, 12, 21, 15, 3, 22, 2, 20, 16, 23, 1, 6, 5]
rotor_lambda_2 = [10, 2, 21, 18, 23, 6, 16, 14, 8, 11, 1, 25, 15, 20, 0, 24, 17, 19, 22, 5, 4, 3, 9, 12, 13, 7]

# defining keys
key_1 = 12
text = "TSBZYOKWKWCEARFDBMFWJOILEFHQURDTYCGLEWHJPLYYNIQKMJTLGLIHLVTNMDSOYZVEPMEQPPFRHMJQBVXEYXRPXNSUIUEFYOTQKCOEJEDCFXJAPVJTZQQEGGSHPCYMRLUVNWFJFGSALNYHXAUNPAPHIGVBQXHRHAFZKZCDLEVBFZGCKAKYJLEXAIJSTNYVUZNQWYEENTGXRCIVGPDYALUG"
text_len = len(text);

for key_2 in range(alphabet_len):
    result = ''
    for letter_idx in range(text_len):
        curr_letter = text[letter_idx]
        letter_num = letter_2_num(curr_letter)
        decrypted_letter = decrypt_letter(letter_num, letter_idx, key_1, key_2, rotor_lambda_1, rotor_lambda_2)
        result += num_2_letter(decrypted_letter)
    
    if result.startswith('J'):
        print(result)