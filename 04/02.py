'''
3. Enigma  šifro (su atspindžiu) raktas =[2, 10]

Rotoriai:
 L_1=[10, 2, 11, 18, 8, 20, 19, 25, 23, 1, 15, 9, 14, 6, 24, 0, 17, 7, 22, 21, 4, 12, 5, 3, 16, 13]
 L_2=[14, 2, 7, 20, 18, 9, 19, 25, 23, 1, 13, 17, 22, 5, 3, 0, 24, 8, 21, 10, 11, 12, 15, 4, 6, 16]

Atspindžio keitinys s=[2, 4, 0, 6, 1, 11, 3, 8, 7, 13, 16, 5, 15, 9, 18, 12, 10, 19, 14, 17, 25, 22, 21, 24, 23, 20]
Iššifruokite šifrą 
BAZSF OJPTG ODIBG RHYVI VCWJR 
OEKPH QGQVM WOETJ WBGZC BKMQG 
GFWSF LCBRQ LMESG OFNUE MSBWU 
VPWLB OZNXS UUGQJ CDLBR MCXKL 
JNSAT KVUSF OWBTK ZGVIJ YUZAW 
DUZKF JIHLM PIRQV ONKWE 

'''

sf = "TSBZYOKWKWCEARFDBMFWJOILEFHQURDTYCGLEWHJPLYYNIQKMJTLGLIHLVTNMDSOYZVEPMEQPPFRHMJQBVXEYXRPXNSUIUEFYOTQKCOEJEDCFXJAPVJTZQQEGGSHPCYMRLUVNWFJFGSALNYHXAUNPAPHIGVBQXHRHAFZKZCDLEVBFZGCKAKYJLEXAIJSTNYVUZNQWYEENTGXRCIVGPDYALUG"
abc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = len(abc)
k1 = 12
L_1=[8, 13, 24, 18, 9, 0, 7, 14, 10, 11, 19, 25, 4, 17, 12, 21, 15, 3, 22, 2, 20, 16, 23, 1, 6, 5]
L_2=[10, 2, 21, 18, 23, 6, 16, 14, 8, 11, 1, 25, 15, 20, 0, 24, 17, 19, 22, 5, 4, 3, 9, 12, 13, 7]
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

#a - raide, k - numeris tekste (raides)
def enc(a, k, k1, k2):
    m1 = k%n
    m2 = (k-m1)//n
    m1 = m1+k1
    m2 = m2+k2
    
    c = rotor(a, m1, L_1) # perejom kiauriai pirma rotoriu
    return rotor(c, m2, L_2) # perejom kiauriai pirma rotoriu

# cia turi but pakeista
def denc(a, k, k1, k2):
    m1 = k%n
    m2 = (k-m1)//n
    m1 = m1+k1
    m2 = m2+k2
    
    c = rotor(a, m2, L_2a) # perejom kiauriai pirma rotoriu
    return rotor(c, m1, L_1a) # perejom kiauriai pirma rotoriu

sfn = pas(sf)
sfn_num = len(sfn)

for k2 in range(0, 26):
    result = ""
    for i in range(0, sfn_num):
        curr = sfn[i]
        ats = denc(curr, i, k1, k2)
        result = result + abc[ats]
        
    if result[0] == "J":
        print(f"k2:{k2} {result}")   