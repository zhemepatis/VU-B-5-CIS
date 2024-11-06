'''
3. Antano viešas RSA raktas [n,e]=  [2579162015491690188116396966327053695822671, 37].
Birutės  viešas RSA raktas [n,e]=  [2579162015491690188116396966327053695822671, 67].
Jiems abiems pasiųsta ta pati žinutė. 
 Šifrai: 
 346897295536692492310491500389714872068993
200776512679510959441135187916297036360331
 
Pasinaudokite bendro modulio ataka ir iššifruokite žinutę.
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
    
[n, ea] = [1800927138376531785763511974731548192529993897418304343019, 41]
[n, eb] = [1800927138376531785763511974731548192529993897418304343019, 73]
c1 = 1508490432418896473167430378567471558661594178136773044921
c2 = 417233865624933231270891279732241478501883699520393538777

# zinute ta pati, tai  c1 = m^ea (mod), c2 = m^eb, gcd(ea, eb) = 1 - negalima isspresti - parasyti destytojui, x*ea+y*eb=1
# c1^x*c2^y=m^(x*ea)*m^(g*eb) = m^(1) = m
# xgcd(ea, eb) - isplestinis euklido algoritmas (?, x, y)
[_, x, y] = xgcd(ea, eb)

m = power_mod(c1, x, n) * power_mod(c2, y, n) % n
print(i_teksta(m))

# ats:
# iskelta veliava