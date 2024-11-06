'''
2. Viešasis Grahamo-Shamiro kuprinės kriptosistemos raktas   [v_1,...,v_8,p]=  [33706718645, 32531954669, 92811174971, 45116856847, 87387905022, 63633664654, 2318277336, 1241233345, 109003931257].
Pirmoji privataus rakto komponentė w_1=21820735546.
Pranešimas slypi  11-18 bituose (skaičiuojant nuo galo). 
Iššifruokite G-SH kuprinės šifrą 
[83532373718, 41081262340, 18404065963, 17580431728, 65015565911, 92811174971, 83532373718, 17580431728, 63774332566, 65015565911, 17580431728, 65015565911]
'''
V = [33706718645, 32531954669, 92811174971, 45116856847, 87387905022, 63633664654, 2318277336, 1241233345, 109003931257]
p = 109003931257
w_1=21820735546 # - pirmas gero svorio elementas, gautas sugadinus svori v_1
# ieskom t * v_1 = w_1
C = [83532373718, 41081262340, 18404065963, 17580431728, 65015565911, 92811174971, 83532373718, 17580431728, 63774332566, 65015565911, 17580431728, 65015565911]
# zinute slypes 18 - 11 bituose
v_1 = V[0]
gcd(v_1, p)
t = w_1 / v_1 % p # perskaiciuojam kuprine
Cn = [c*t%p for c in C]

# isreiskiam pirma kuprine dvejetainiu
chr(int(bin(Cn[0])[-18:-10], 2))
chr(int(bin(Cn[1])[-18:-10], 2))