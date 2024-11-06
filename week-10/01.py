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
    
[n, e, d] = [103358995545025928935004138017670200331300243739031907, 41, 37814266662814364244513708642205234557338923937525561]
c1 = 63326144740166123960884492849835654619469382130828824

m = power_mod(c1, d, n)
print(i_teksta(m))

# ats:
# smagusdarbas