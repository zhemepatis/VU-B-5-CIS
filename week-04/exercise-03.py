import utilities.global_vars as gv

# defining global variables












# def pas(t):
#     c = []
#     for r in t:
#         if r in abc: c.append(r)
        
#     return [abc.index(e) for e in c] 

# # pereinam i rotoriu ir iseinam i plokstele
# def rotor(a, m, l):
#     # l - ieinam i rotoriu
#     # - m % n - iseina is rotoriaus ??  
#     return (l[int((a+m)%n)] - m) % n

# def atsp(a, s):
#     return s.index(a)


# #a - raide, k - numeris tekste (raides)
# def enc(a, k, k1, k2):
#     m1 = k%n
#     m2 = (k-m1)//n
#     m1 = m1+k1
#     m2 = m2+k2
    
#     c = rotor(a, m1, L_1) # perejom kiauriai pirma rotoriu
#     return rotor(c, m2, L_2) # perejom kiauriai antra rotoriu??

# # cia turi but pakeista
# def denc(a, k, k1, k2):
#     m1 = k%n
#     m2 = (k-m1)//n
#     m1 = m1+k1
#     m2 = m2+k2

#     c = rotor(a, m2, L_2a) # sugristam per antra rotoriu
#     return rotor(c, m1, L_1a) # sugristam per pirma rotoriu

# sfn = pas(sf)
# sfn_num = len(sfn)

# result = ""
# for i in range(0, sfn_num):
#     curr = sfn[i]

#     temp = enc(curr, i, k1, k2)
#     ats = atsp(temp, s)
#     ats = denc(ats, i, k1, k2)
#     result = result + abc[ats]

# print(f"{result}")   