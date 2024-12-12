# pirma uzduotis
[c,p]=[18312, 100003]

#reikia ispresti kvadratini lygini
u = power_mod(c, (p+1)//4, p)
u = 40974

# i hash funkcija reikia talpinti visus c_i, ne r
# tikrintojas gali i maisos funkcija susideti ...?
#renkames 5 atsitiktinius skaiciukus
R = [randint(1, p) for i in range(5)]
R = [34990, 95453, 74497, 24689, 41088]

# skaicuojam c_i
C = [c*power_mod(r, -2, p) % p for r in R]
C = [49571, 26514, 40258, 70308, 661]

#daromes 5 bitukus
Ct = [str(c) for c in C]
Ct = ['49571', '26514', '40258', '70308', '661']

# sujungiam
t = "".join(Ct)
t = '49571265144025870308661'

# paverciam t i baitu srauta
t = b'49571265144025870308661'

#h.update(t)
#h_value=h.hexdigest()
#print(h_value)
#print(bin(int(h_value[-2::],16))[-5::]) # 5 least significant bits 

bt = [0,1,0,1,1] # gavom is antros print funkcijos

U = [u/r%p for r in R]
U = [7152, 63905, 50341, 71242, 93710]

# jeigu bt yra 1, tai dedam is U, jeigu 0, tai dedam is R
P = [R[0], U[1], R[2], U[3], U[4]]
C, P

# kaip tikrinti 
for i in range(5):
    if bt[i]  == 1:
        print(power_mod(P[i], 2, p) == C[i])
    else:
        print(power_mod(P[i], 2, p) == c/C[i]%p)

# atsakymas C, P ir c



