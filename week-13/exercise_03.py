# 3. Use secret from 2nd exercise and share it for 5 people using Shamir's secret sharing schema.
# t is 3

import sympy
import random

def a(secret, A, x):
    return secret + A[0]*x + A[1]*(x**2)

random.seed(1000) # to be able reproduce later

people_num = 5
p = sympy.nextprime(13**13) 
A = [651135, 985685]

secret = 10863200

X = [random.randint(1, p) for _ in range(people_num)]
S = []
for x in X:
    S.append(a(secret, A, x))

print(f"secret: {secret}")
print(f"p: {p}")
print(f"X: {X}")
print(f"S: {S}")

