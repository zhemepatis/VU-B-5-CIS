# 1. Rabin kriptosistemos privatusis raktas [p,q]=  [79496847203390844133441739, 79496847203390844133441987].
# Iššifruokite  šifrą 
# 369412936784193964016448726382270848904560824373225. Tekstas keičiamas skaičiumi kaip RSA užduotyje.

A = 'abcdefghijklmnopqrstuvwxyz '

def i_teksta(M):
    n = M
    text = ''
    while n > 0:
        ind = n % 100
        ind = ind - 1
        if 0 <= ind < len(A):
            text += A[ind]
            n = (n - ind - 1) // 100
        else:
            text += '?'
            n = (n - ind - 1) // 100
    return text[::-1]

p, q = 79496847203390844133441739, 79496847203390844133441987
C = 369412936784193964016448726382270848904560824373225

# calculating public key
n = p * q

# getting parts of message
m1 = pow(C, (p + 1) // 4, p)
m2 = pow(C, (q + 1) // 4, q)

# calculating message using chineese reminders theorem
p_inv = pow(p, -1, q)
q_inv = pow(q, -1, p)
m = (m1 * q * q_inv - m2 * p * p_inv) % n

# printing message
print(i_teksta(m))
