# 1. Solve the congruence x^2 = c mod p and publish the non-interactive proof, that you know the solution.
# Here [c,p] = [69060, 100003]

import random
import hashlib

c = 69060
p = 100003

random.seed(1000) # to be able reproduce later
R =[random.randint(1, p - 1) for _ in range(5)]

C = [c * pow(r, -2, p) % p for r in R]

solution = pow(c, (p + 1) // 4, p)
U = [pow(r, -1, p) * solution % p for r in R]

hash_inp = "".join([str(c) for c in C])
hash_inp = hash_inp.encode(encoding="utf-8")

hash_func = hashlib.md5()
hash_func.update(hash_inp)
hash_result = hash_func.hexdigest()

bits = str(bin(int(hash_result[-2::], 16))[-5::])
bits = [int(bit) for bit in bits]

P = []
for i in range(5):
    if bits[i] == 0:
        P.append(R[i])
    else:
        P.append(U[i])


# checking if solution was found
is_correct = True
for i in range(5):
    if bits[i] == 0:
        is_correct = pow(P[i], 2, p) == pow(C[i], -1, p) * c % p
    else:
        is_correct = pow(P[i], 2, p) == C[i]

    if not is_correct:
        break

if is_correct:
    print("Correct solution was found:")
    # printing answers
    print(f"c = {c}")
    print(f"C = {C}")
    print(f"P = {P}")
else:
    print("No correct solution was found.")
        