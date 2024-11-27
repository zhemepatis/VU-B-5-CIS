# 1. Decrypt Merkle-Hellman knapsack cipher when public key is [v_1, ..., v_8, p] = [33296009, 53900889, 91823633, 83338012, 81973128, 60025814, 63224980, 44488765, 94085941] 
# First private key component is w_1 = 667872
# Cipher: [40890652, 10029691, 2041405, 54518456, 49954406, 84014533, 68690621, 31206258, 2041405, 91823633, 70055505, 62067219, 84014533, 53153572, 5465641, 2041405]

import math

def decipher_letter(ciphered_letter, key_private):
    key_private.sort(reverse = True)

    result = ''
    for weight in key_private:
        if ciphered_letter >= weight:
            result += '1'
            ciphered_letter -= weight
        else:
            result += '0'
    
    result = result[::-1]
    return int(result, 2)


cipher = [40890652, 10029691, 2041405, 54518456, 49954406, 84014533, 68690621, 31206258, 2041405, 91823633, 70055505, 62067219, 84014533, 53153572, 5465641, 2041405]
key_public = [33296009, 53900889, 91823633, 83338012, 81973128, 60025814, 63224980, 44488765]
p = 94085941
w_1 = 667872

# checking if Greatest Common Divisor of p and v_1 is 1.
v_1 = key_public[0]
print(f"Greatest common divisor of v_1 and p: {math.gcd(v_1, p)}")

# since it is equal to 1, we can proceed by searching s part of private key.
s = pow(v_1, -1, p) * w_1 % p

# now that we know s, we calculate private key.
key_private = [v * s % p for v in key_public]

# deciphering text
cipher_altered = [letter * s % p for letter in cipher]

result = ''
for e_letter in cipher_altered:
    d_letter = chr(decipher_letter(e_letter, key_private))
    result += d_letter

print(f"answer: {result}")