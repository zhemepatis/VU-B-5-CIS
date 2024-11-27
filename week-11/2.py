'''
2. Privatusis Blumo-Goldwasserio  kriptosistemos raktas [p,q]=  [61543, 61547],h=8
Iššifruokite šifrą  
[131, 68, 117, 205, 34, 8, 110, 115, 140, 52, 145, 80, 178, 497514035]
'''

p, q = 78691, 78707
h = 8
C = [65, 76, 181, 188, 186, 254, 22, 58, 179, 247, 8, 22, 111, 1412592686]

# sudarom viesa rakta
n = p*q

# pasiimam paskutini skaiciu
t = len(C)
x = C[t-1] # x_{t+1}

d = power_mod((p+1)//4, t, p-1)
e = power_mod((q+1)//4, t, q-1)

u = power_mod(x, d, p) # gaunam x_0 mod p (berods)
v = power_mod(x, e, q) # gaunam x_0 mod q (berods)

# ieskom x_0, naudojant kinu liekanu teorema
a = 1 / q % p
b = 1 / p % q
x0 = (u*a*q + b*p*v) % n

# desifruojam
chr((power_mod(x0, 2, n)%256)^^C[0])  # paimam paskutinius 8 bitus
chr((power_mod(x0, 4, n)%256)^^C[1])

result = ''
for i in range(t-1):
    power = 2 ** (i + 1)
    result += chr((power_mod(x0, power, n)%256)^^C[i])

print(result)
    
    



