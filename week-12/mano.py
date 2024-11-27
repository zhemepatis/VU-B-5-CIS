'''
 4 užduotis 
Viešasis Algio ElGamalio schemos raktas parašų tikrinimui ir šifravimui: 
[p,g,bt]=[4640650289117164100520051333566036654627, 2, 3341239999495377769078067240488125379603]
g yra vietoj alfa?

Algis pasirašė žinutę = iskelta veliava. Parašas:
[gamma, delta_1]=[3757359024922607955461127104540918427850, 2657744583164683453615599287262487940731]

Algis pasirašė žinutę = smagus darbas. Parašas:
[gamma, delta_2]=[3757359024922607955461127104540918427850, 1824601941863231577635399491545820671789]

1. Patikrinkite parašus.
2. Raskite Algio privatųjį raktą.
3. Iššifruokite Algiui skirtą šifrą 
[C_1,C_2]=[4009037285178334239434974126886762855590, 3667710087034209265854651236964947768616]
'''

A='abcdefghijklmnopqrstuvwxyz '
def i_skaiciu(text):
    t=''
    for r in text:
        if r in A:
            ind=A.index(r)+1
            if ind<10: t=t+'0'+str(ind)
            else: t=t+str(ind)
    return int(t,10)  

def i_teksta(M):
    n=M
    text=''
    while n>0:
        ind=n%100
        ind=ind-1
        if (ind>=0) & (ind<len(A)):
            text+=A[ind]
            n=(n-ind+1)//100
        else:
            text+='?'
            n=(n-ind+1)//100            
    return text[::-1]     
    
# viesas raktas
[p,g,bt]=[4640650289117164100520051333566036654627, 2, 3278559382442092433039423892493516119965]

m1 = 'didelis akmuo' # pirma zinute
[gamma, delta_1]=[4627689834969117253446515994336739172661, 3612425379785901298764257971722483086306] # pirmas parasas

m2 = 'svarbus asmuo' # antra zinute
[gamma, delta_2]=[4627689834969117253446515994336739172661, 2937787076078797335846005195484921310966] # antras parasas

[C_1,C_2]=[1772558991422069315333706757978920808392, 2270896162773124323933214773953959812386]

# paverciam zinutes i skaiciu
x1 = i_skaiciu(m1) # ieskom delta 1: delta_1 * k = x1 - a * gamma => (delta_1 - delta_2) * k = x1 - x2 mod (p-1)
x2 = i_skaiciu(m2) # ieskom delta 2: delta_2 * k = x2 - a * gamma
#[x1,x2] = [919110512200122051209012201, 191301072119040118020119]

gcd((delta_1 - delta_2), (p-1)) # nelygus vienetui, tai reikia susiprastinti:

# ieskom sumazinto p
pm = (p-1)//2
k = (x1-x2)/(delta_1 - delta_2) % pm # kazkas negerai
k = 3233
print(power_mod(g, k, p) == gamma, k)

# a * gamma = x2- delta_2*k mod (p - 1)
a = (x2 - delta_2*k) / gamma % pm
print(power_mod(g, a, p) == beta, a)

res = i_teksta(C_2 * power_mod(C_1, -a, p) % p)
print(res)

# pereinam prie DSS
factor(p - 1)
q = 16049949467441720218442582204919577
al = power_mod(g, (p-1)//q, p)
al