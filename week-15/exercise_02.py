# 2. Find the discrete logarithm log_gy and publish the non-interactive proof, that you know the solution.
# [g,y,p] = [2, 37421, 100003]

import random
import hashlib

[g,y,p] = [2, 37421, 100003]

# searching for solution using brute-force
solution = -1
for x in range(p - 2):
    if pow(g, x, p) == y:
        solution = x
        break

random.seed(1000)
v = random.randint(1, p - 1)

t = g**v % p

hash_inp = str(g) + str(y) + str(t)
hash_inp = hash_inp.encode(encoding = "utf-8")

hash_func = hashlib.md5()
hash_func.update(hash_inp)
hash_result = hash_func.hexdigest()

c = int(hash_result, 16) % (p - 1)
r = (v - c * x) % (p - 1)

# checking if solution was found
t_sh = (g**r * y**c) % p

hash_inp = str(g) + str(y) + str(t_sh)
hash_inp = hash_inp.encode(encoding="utf-8")

h = hashlib.md5()
h.update(hash_inp)
hash_result = hash_func.hexdigest()

if int(hash_result, 16) % (p - 1) == c:
    print("Correct solution was found:")
    # printing answers
    print(f"c = {c}")
    print(f"r = {r}")
else:
    print("No correct solution was found.")