import utilities.global_vars as gv
from utilities.letter_conversion_by_alphabet import letter_2_num, num_2_letter
from utilities.simplified_enigma_cipher import decrypt_letter

# defining global variable
gv.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# defining ENIGMA setup
rotor_lambda_1 = [14, 2, 7, 20, 18, 9, 19, 25, 23, 1, 13, 17, 22, 5, 3, 0, 24, 8, 21, 10, 11, 12, 15, 4, 6, 16]
rotor_lambda_2 = [5, 3, 2, 0, 17, 10, 8, 24, 20, 11, 1, 12, 9, 22, 16, 6, 25, 4, 18, 21, 7, 13, 15, 23, 19, 14]

# defining keys
[key_1, key_2] = [3, 4]
text = "SWTZLWYFHZRDKYXUVCHVHUKGFSYAFHORDTIHMABVKYONWKYRLXKWHKCVIEIFXUWYYMNZYHONLXAXBRZVFIHPGLLXNXIKXJSCBLLRTGYLGTIOWUXTAEQWRTFJQNQOOSQKNJZTSVSKLXLVWDFQHBPWMIQCCHVVYDRRSFDRKOFAIOPOONZYUXLOAYWPVJQSFFJPUOKSYJFICKHLHZYXTIKZNTAZGQFDREDMUOALJDOZZDAVNXVPSVRRBIHCKWEPIOIACKDLWXXPXLIBSFIOXUXNVLIQZXLQJPPJLAFYPDKYYFCATPEPJFJTBLRIYCQGFUQGXZMXULIELY"
text_len = len(text);

result = ''
for letter_idx in range(text_len):
    curr_letter = text[letter_idx]
    letter_num = letter_2_num(curr_letter)
    decrypted_letter = decrypt_letter(letter_num, letter_idx, key_1, key_2, rotor_lambda_1, rotor_lambda_2)
    result += num_2_letter(decrypted_letter)

print(result)