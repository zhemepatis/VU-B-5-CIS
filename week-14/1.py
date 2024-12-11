'''
1. Given the elliptic curve G = EllipticCurve(GF(3001),[-7,2]) and the point P[21 : 2819] of prime order p=509.

The private key of Menezes-Vanstone cryptosystem is r=122.
Decrypt the cipher 

[[[2160, 2703], 251, 70], [[2962, 2136], 217, 227], [[1798, 2129], 261, 348], [[521, 2166], 252, 70], [[428, 1276], 7, 244], [[681, 2922], 79, 156]]


 2. Sign the message m=100 using El Gamal signature with the elliptic curve and the private key given.
'''

p=97
E=EllipticCurve(GF(p),[-2,2])
T = E.points()
T # pirmas elementas - ??, kiti taskai x - primas elementas, y - antras elementas??
#E.cardinality()

T[45].order() # elemento eile, jeigu sudedu sita elementa sudedu pati su savim tai gaunu 0 elementa
# T[45] = x * T[56] x=? - surasti sita sarysi sunku

# ================================

T=E.points()
P=T[10]
Q=T[11]
# Coordinates
print('Coordinates of Q=',[Q[0],Q[1]])
print('Order of Q =',Q.order())
P+Q # - gauname tasko koordinates??

# ================================
# Menez - Vanstone cryptosystem

G = EllipticCurve(GF(3001),[-7,2])
P=G([21 , 2819])
p=P.order()
K_pr=352
K_v=K_pr*P
K_pr, K_v

# ===============================

p=97
E=EllipticCurve(GF(p),[-2,2])
T = E.points()
T[45].order()

E.plot(pointsize=40)

T=E.points()
P=T[10]
Q=T[11]
# Coordinates
print('Coordinates of Q=',[Q[0],Q[1]])
print('Order of Q =',Q.order())
P+Q

p=107
Cr=EllipticCurve(GF(p),[-5,2])
Cr.cardinality()
Pt=Cr.points()
mx=max([t.order() for t in Pt])
mx
P=Pt[55]
K_pr=17
K_v=K_pr*P
K_pr, K_v

M=Pt[10]
k=13
C=[k*P,k*K_v+M]
C

Md=C[1]-K_pr*C[0]
M==Md

P=Pt[55]
K_pr=17
K_v=K_pr*P
K_pr, K_v
#N=P.order()
N=106
def f(t):
    return int(t[0])

M=101
k=23
R=k*P
Sig=[R,int(M-K_pr*f(R))/k%N]
Sig

R=Sig[0]
s=Sig[1]
V1=f(R)*K_v+s*R
V2=M*P
V1==V2, V1

G = EllipticCurve(GF(3001),[-7,2])
P=G([21 , 2819])
p=P.order()
K_pr=122 # cia yra r
K_v=K_pr*P
K_pr, K_v

M=[100,200]
k=321
C0=k*P
R=k*K_v
C1=M[0]*int(R[0])%p
C2=M[1]*int(R[1])%p
[C0,C1,C2]

S = [[2160, 2703], 251, 70]
C0 = G([2160, 2703])
C1 = S[1]
C2 = S[2]
Q=K_pr*C0
[x,y]=[int(Q[0]),int(Q[1])]
Md=[C1/x%p,C2/y%p]
chr(Md[0]) + chr(Md[1])