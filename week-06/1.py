'''
1. AES-V parametrai: p=317, [a,b]=[13, 15], T=[1, 11, 31, 4]. Raktas K=[111, 289, 102, 251]
Iššifruokite šifrą C=[[28, 115, 243, 168], [91, 93, 210, 15], [13, 146, 279, 289], [141, 122, 114, 103], [275, 158, 152, 113], [146, 36, 46, 62], [84, 245, 121, 191], [193, 188, 62, 138], [0, 233, 61, 270], [8, 221, 308, 271], [236, 75, 279, 50], [124, 160, 300, 215], [227, 178, 194, 200], [208, 215, 86, 299], [3, 266, 76, 149], [89, 292, 84, 126], [138, 203, 48, 261], [87, 157, 225, 302], [49, 239, 138, 221], [90, 207, 26, 199], [218, 144, 35, 55], [1, 100, 304, 61], [74, 299, 41, 264], [152, 116, 216, 225], [166, 85, 192, 312], [15, 180, 254, 13], [275, 55, 52, 241], [138, 293, 223, 106], [71, 277, 56, 85], [266, 33, 224, 24], [42, 211, 162, 173], [28, 115, 243, 168], [288, 291, 12, 260], [113, 25, 183, 69], [257, 109, 287, 35], [174, 137, 267, 30], [257, 109, 287, 35]]
'''

p = 317
[a,b]=[13, 15]
T=[1, 11, 31, 4]
Ta=[190, 270, 271, 206]
K=[168, 184, 178, 139]
C=[[282, 2, 96, 225], [59, 301, 16, 294], [152, 169, 23, 21], [162, 245, 264, 230], [59, 301, 16, 294], [119, 212, 311, 285], [152, 105, 168, 172], [315, 241, 22, 25], [128, 82, 178, 29], [297, 0, 25, 244], [40, 124, 294, 162], [308, 152, 33, 219], [131, 241, 122, 311], [146, 73, 254, 192], [87, 195, 162, 12], [146, 228, 151, 278], [298, 272, 17, 164], [212, 303, 109, 94], [152, 202, 71, 279], [91, 303, 185, 244], [255, 196, 165, 309], [200, 164, 113, 123], [295, 103, 150, 203], [285, 190, 16, 299], [219, 132, 284, 294], [176, 145, 219, 36], [136, 75, 96, 111], [38, 215, 259, 145], [59, 148, 135, 61], [261, 27, 4, 60], [8, 32, 46, 81]]
# c=[28, 115, 243, 168]



def Key_p(K,a,b):
    if K[3]==0: k0=b
    else: k0=(K[0]+(a/K[3]%p+b)%p)%p
    k1=(k0+K[1])%p
    k2=(k1+K[2])%p
    k3=(k2+K[3])%p
    return [k0,k1,k2,k3]

def Key(K,a,b): # outputs the subkeys for iterations 
    K1=Key_p(K,a,b)
    K2=Key_p(K1,a,b)
    return [K,K1,K2]

# desifravimui viska reikia atvirksciai daryti (atgrezti)
def sbe(m):
    if m  == 0:
        mi = b
    else:
        mi = (a/m + b)%p
    
    return mi

def sbd(mi):
    if mi == b:
        m = 0
    else:
        # m = a/mi + b - reikia isprest sita lygti
        m = (mi - b)/a%p
        m = 1/m%p
    return m

def en_1(M):
    return [sbe(m) for m in M]

def de_1(M):
    return [sbd(m) for m in M]

def en_2(M):
    return [M[i] for i in [0,1,3,2]]

def de_2(M):
    return [M[i] for i in [0,1,3,2]]

# 3 layeris (matircas dauginam)
def en_3(M):
    m11 = (T[0]*M[0]+T[1]*M[2])%p
    m12 = (T[0]*M[1]+T[1]*M[3])%p
    m21 = (T[2]*M[0]+T[3]*M[2])%p
    m22 = (T[2]*M[1]+T[3]*M[3])%p
    
    return [m11, m12, m21, m22]

def de_3(M):
    m11 = (Ta[0]*M[0]+Ta[1]*M[2])%p
    m12 = (Ta[0]*M[1]+Ta[1]*M[3])%p
    m21 = (Ta[2]*M[0]+Ta[3]*M[2])%p
    m22 = (Ta[2]*M[1]+Ta[3]*M[3])%p
    
    return [m11, m12, m21, m22]

def en_4(M, k):
    return [(M[i]+k[i])%p for i in range(0, 4)]

def de_4(M, k):
    return [(M[i]-k[i])%p for i in range(0, 4)]

def iter_en(M, k):
    C = en_1(M)
    C = en_2(C)
    C = en_3(C)
    return en_4(C, k)

def iter_de(C, k):
    M = de_4(C, k)
    M = de_3(M)
    M = de_2(M)
    return de_1(M)

def aes_en(M, key):
    C = iter_en(M, key[0])
    C = iter_en(C, key[1])
    return iter_en(C, key[2])

def aes_de(C, key):
    M = iter_de(C, key[2])
    M = iter_de(M, key[1])
    return iter_de(M, key[0])

#key = Key(K,a,b)
#key
key = [[168, 184, 178, 139], [288, 155, 16, 155], [254, 92, 108, 263]]
# sbd(sbe(0))

#T=[1, 11, 31, 4]
#Tdet = 1/(1*4-11*31)%p
#Ta = [Tdet*4%p, Tdet*(-11)%p, Tdet*(-31)%p, Tdet*1%p] - atvirkstine matrica
# de_3(en_3([1,1,1,1])) - tikrinam

# aes_de(aes_en([1,1,1,1], key), key) #- tikrinam

#m = aes_de(c, key)
#chr(m[0])+chr(m[1])+chr(m[2])+chr(m[3])

res = ""
for c in C:
    temp = aes_de(c, key)
    res += chr(temp[0])+chr(temp[1])+chr(temp[2])+chr(temp[3])
    
print(res)