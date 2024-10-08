# 1. Feistel cipher with three iterations, where the keys are [45, 108, 192]
# Iteration function is (m|k)^((m//16)&k)
# Decipher cipher made using EBC mode:
# [[197, 60], [205, 55], [193, 60], [199, 37], [200, 56], [210, 41], [219, 46], [203, 53], [217, 40], [201, 36], [213, 41], [199, 33], [209, 58], [193, 36], [204, 34], [202, 32], [207, 35], [208, 59], [199, 37], [221, 41], [201, 52], [220, 47], [203, 50], [201, 44], [207, 42], [211, 60], [209, 58], [207, 48], [197, 39], [205, 37], [215, 62], [201, 52], [192, 34], [205, 37], [202, 50], [208, 45], [208, 41], [207, 43], [194, 60], [214, 57], [210, 39], [217, 40], [193, 58], [201, 52], [223, 44], [210, 41], [202, 46], [207, 45], [217, 40], [193, 36], [211, 60]]

import utils.feistel_scheme as fs

keys = [45, 108, 192]
byte_pairs = [[197, 60], [205, 55], [193, 60], [199, 37], [200, 56], [210, 41], [219, 46], [203, 53], [217, 40], [201, 36], [213, 41], [199, 33], [209, 58], [193, 36], [204, 34], [202, 32], [207, 35], [208, 59], [199, 37], [221, 41], [201, 52], [220, 47], [203, 50], [201, 44], [207, 42], [211, 60], [209, 58], [207, 48], [197, 39], [205, 37], [215, 62], [201, 52], [192, 34], [205, 37], [202, 50], [208, 45], [208, 41], [207, 43], [194, 60], [214, 57], [210, 39], [217, 40], [193, 58], [201, 52], [223, 44], [210, 41], [202, 46], [207, 45], [217, 40], [193, 36], [211, 60]]
func = "(r | key) ^ ((r // 16) & key)"

result_str = ""
for pair in byte_pairs:
    l_result, r_result = fs.decrypt_ebc(pair, func, keys)
    result_str += chr(l_result) + chr(r_result)

print(result_str)