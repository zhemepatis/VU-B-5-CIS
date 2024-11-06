'''
2. Algio viešas RSA raktas [n,e]=  [148023531651267802845633489092899460941, 119].
Iššifruokite Algiui skirtą šifrą 
101052745856747284302775110811213599506
'''

A='abcdefghijklmnopqrstuvwxyz'
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
    
    
[n,em,dm] = [103358995545025928935004138017670200331300243739031907, 41, 37814266662814364244513708642205234557338923937525561]
[n, ea] = [103358995545025928935004138017670200331300243739031907, 77]
c = 66996264610252193384215071113050989046042092186748942


t = em*dm-1 # kadangi lygine, tai dalinsim tol kol gausim nelygine
t = t // 2 // 2 // 2 // 2 // 2

a = 19199123
a0 = power_mod(a, t, n)
a1 = power_mod(a0, 2, n)
a2 = power_mod(a1, 2, n)
a3 = power_mod(a2, 2, n)
a4 = power_mod(a3, 2, n)


p = gcd(a0 - 1, n)

q = n // p
fi = (p - 1)*(q-1) 
da = 1/ea%fi # algio privatus raktas

m = power_mod(c, da, n)
print(i_teksta(m))

# ats:
# iskelta veliava

