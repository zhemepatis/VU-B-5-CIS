# 2. Find a secret that was shared using Asmuth - Blum schema with t = 3
# [p, p1, p2, p3] = [21726401, 43452811, 86905607, 173811257]
# [s1, s2, s3] = [32588314, 32588284, 32588327]

t = 3
p, p1, p2, p3 = [21726401, 43452811, 86905607, 173811257]
s1, s2, s3 = [32588314, 32588284, 32588327]

# applying chineese remainder theorem
n = p1*p2*p3
m1 = n // p1
m2 = n // p2
m3 = n // p3

d1 = pow(m1, -1, p1)
d2 = pow(m2, -1, p2)
d3 = pow(m3, -1, p3)

x = (s1*d1*m1 + s2*d2*m2 + s3*d3*m3) % n

# finding S*
x_inv = pow(x, -1, n)
S_ast_inv = x_inv % n

# finding S
S = pow(S_ast_inv, -1, n) % p
print(f"answer: {S}")