def encrypt(letter, k1, k2):
    return (k1 * letter + k2) % 32


text = "ĄFGĘZĘŲĖĄHJĖFĖADŪDĖGJĮŪHĖJNMJŲSJHFĖJOZJŲVHĖŲJMNHĖGJĮŪRŲHVZRKJĖEHĄHJUĖJĖLHTJŪĘJVMHBJVĄĘZĘŲUGĮJBVĘBUŲFVŲJĮŲGJĮŪHĖTĮVHĖJVTVHAFĖBHJŲZHĖHZĖJLFNŠĖKHLĮBJŪTBHGĘĘMJŲZHĖJVĄKHFVFĖĄFGĘLHZĘLHĖHJNŲJHJJVVĘBCĖJBHVĄKHFVĮĖŪJĖ"
k1 = 11
k2 = 11

abc = "AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ"
d_abc = "AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ"
e_abc = ""

for letter in abc:
    idx = abc.index(letter)
    e = encrypt(idx, k1, k2)
    e_abc = e_abc + abc[e]

result = ""
for letter in text:
    result = result + abc[e_abc.index(letter)]

print(result)