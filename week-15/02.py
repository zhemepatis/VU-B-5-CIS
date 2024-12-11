'''
1. Solve the congruence x^2=c mod p and publish the non-interactive proof, that you know the solution.
[c,p]=[18312, 100003]

2. Find the discrete logarithm log_gy and publish the non-interactive proof, that you know the solution.
[g,y,p]=[2, 36465, 100003]

import hashlib
h = hashlib.md5()
t=b'11110'
h.update(t)
h_value=h.hexdigest()
print(h_value)
print(bin(int(h_value[-2::],16))[-5::]) # 5 least significant bits 
N=464646466 # just for example 
int(h_value,16)%N # conversion to number
'''

# antras uzdavinys 
[g,y,p]=[2, 36465, 100003] 

# kadangi skaiciaimazi naudojam brute force
for x in range(0, p-2):
    if power_mod(g, x, p) == y:
        print("LOG = ", x)
        break

x = 59029
v = 65444 # paimta random
t = g**v % p
t = 13287
huh = b"23646513287"

import hashlib
h = hashlib.md5()
h.update(huh)
h_value=h.hexdigest()

c = int(h_value, 16) % (p-1)
r = (v - c*x) % (p-1)

# tikrinimas
t_sh = ((g**r) * (y**c)) % p

h = hashlib.md5()
huh = b"23646513287"
h.update(huh)
h_value=h.hexdigest()

print(t_sh)

print(int(h_value, 16) % (p - 1) == c)

