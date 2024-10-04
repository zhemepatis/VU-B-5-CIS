sf = "TSBZYOKWKWCEARFDBMFWJOILEFHQURDTYCGLEWHJPLYYNIQKMJTLGLIHLVTNMDSOYZVEPMEQPPFRHMJQBVXEYXRPXNSUIUEFYOTQKCOEJEDCFXJAPVJTZQQEGGSHPCYMRLUVNWFJFGSALNYHXAUNPAPHIGVBQXHRHAFZKZCDLEVBFZGCKAKYJLEXAIJSTNYVUZNQWYEENTGXRCIVGPDYALUG"
abc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = len(abc)
[k1, k2] = [21, 19]
L_1=[14, 2, 7, 20, 18, 9, 19, 25, 23, 1, 13, 17, 22, 5, 3, 0, 24, 8, 21, 10, 11, 12, 15, 4, 6, 16]
L_2=[5, 3, 2, 0, 17, 10, 8, 24, 20, 11, 1, 12, 9, 22, 16, 6, 25, 4, 18, 21, 7, 13, 15, 23, 19, 14]
s=[2, 4, 0, 6, 1, 11, 3, 8, 7, 13, 16, 5, 15, 9, 18, 12, 10, 19, 14, 17, 25, 22, 21, 24, 23, 20]
L_1a = [L_1.index(i) for i in range(0, n)]
L_2a = [L_2.index(i) for i in range(0, n)]

def pas(t):
    c = []
    for r in t:
        if r in abc: c.append(r)
        
    return [abc.index(e) for e in c] 

# pereinam i rotoriu ir iseinam i plokstele
def rotor(a, m, l):
    # l - ieinam i rotoriu
    # - m % n - iseina is rotoriaus ??  
    return (l[int((a+m)%n)] - m) % n

def atsp(a, s):
    return s.index(a)


#a - raide, k - numeris tekste (raides)
def enc(a, k, k1, k2):
    m1 = k%n
    m2 = (k-m1)//n
    m1 = m1+k1
    m2 = m2+k2
    
    c = rotor(a, m1, L_1) # perejom kiauriai pirma rotoriu
    return rotor(c, m2, L_2) # perejom kiauriai antra rotoriu??

# cia turi but pakeista
def denc(a, k, k1, k2):
    m1 = k%n
    m2 = (k-m1)//n
    m1 = m1+k1
    m2 = m2+k2

    c = rotor(a, m2, L_2a) # sugristam per antra rotoriu
    return rotor(c, m1, L_1a) # sugristam per pirma rotoriu

sfn = pas(sf)
sfn_num = len(sfn)

result = ""
for i in range(0, sfn_num):
    curr = sfn[i]

    temp = enc(curr, i, k1, k2)
    ats = atsp(temp, s)
    ats = denc(ats, i, k1, k2)
    result = result + abc[ats]

print(f"{result}")   