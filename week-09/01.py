# [v_1,...,v_8,p]=  
V = [43514209, 25505652, 36088150, 30223379, 38469826, 4698585, 43416650, 60724099, 63890710]
p = 63890710
v_1 = V[0]
# pirmoji rakto komponente
w_1=441117 # v_1 = v[0] - buvo gautas sugadinus gera svori. bandom rasti toki t, kad t * v_1 = w_1 mod p => t = w_1 / v_1 % p - legalu, kai p ir v_1 - pirminiai
C = [4285800, 37704892, 58427191, 42651716, 29458445, 4285800, 36088150, 40871503, 58427191, 33006307, 12532247, 58427191, 4285800]

gcd(v_1, p) # == 1
t = w_1 / v_1 % p
t = 907523

# bandom atkurti gerus svorius
W = [v * t % p for v in V]
W

# perskaiciuojam kuprines
Cn = W = [v * t % p for v in C]

# turim gauti bitukus, kurie reprezentuoja raide ir t.t. ir pan.
