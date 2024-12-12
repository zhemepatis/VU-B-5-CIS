# 1. Solve the congruence x^2 = c mod p and publish the non-interactive proof, that you know the solution.
# Here [c,p] = [69060, 100003]

import random
import hashlib

c = 69060
p = 100003

random.seed(1000) # to be able reproduce later
R =[random.randint(1, p - 1) for _ in range(5)]

C = [c * pow(r, -2, p) % p for r in R]

u = pow(c, (p + 1)//4, p)
U = [u//r%p for r in R]

hash_inp = "".join([str(c) for c in C])
hash_inp = hash_inp.encode(encoding="utf-8")

hash_func = hashlib.md5()
hash_func.update(hash_inp)
hash_result = hash_func.hexdigest()

bits = str(bin(int(hash_result[-2::], 16))[-5::])

P = []
for idx in range(5):
    bit = bits[idx]
    if bit == 0:
        P.append(U[idx])
    else:
        P.append(R[idx])

print(f"c: {c}")
print(f"C: {C}")
print(f"P: {P}")