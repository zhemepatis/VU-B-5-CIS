# 2. Decrypt Graham-Shamir knapsack cipher when public key is [v_1, ..., v_8, p] = [131676723585, 126193584671, 121776689089, 12005769919, 48330596845, 6864144972, 96139001343, 34712894969, 138956504769]
# First private key component is w_1 = 25099108461
# Message is in 11-18 bits.
# Cipher: [59964901008, 17147397582, 10283252610, 65106525955, 10283252610, 25252006039, 53100756036, 121391007382, 11634304163, 121776689089, 59964901008, 23640074082, 107773305506, 11634304163]

import math

cipher = [59964901008, 17147397582, 10283252610, 65106525955, 10283252610, 25252006039, 53100756036, 121391007382, 11634304163, 121776689089, 59964901008, 23640074082, 107773305506, 11634304163]
key_public = [131676723585, 126193584671, 121776689089, 12005769919, 48330596845, 6864144972, 96139001343, 34712894969]
p = 25099108461
w_1 = 21820735546

# checking if Greatest Common Divisor (GCD) of p and v_1 is 1.
v_1 = key_public[0]
print(f"Greatest common divisor of v_1 and p: {math.gcd(v_1, p)}")

# since v_1_reduced and p_reducded GCD is 9 not 1, we proceed calculating s with reduced values
s = pow(v_1//9, -1, p//9) * w_1 % p

# deciphering text
cipher_altered = [letter * s % p for letter in cipher]

result = ''
for e_letter in cipher_altered:
    result += chr(int(bin(e_letter)[-18:-10], 2))

print(f"answer: {result}")