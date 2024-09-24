def encrypt(letter, k1, k2):
    return (k1 * letter + k2) % 32


text = "ITŠĘJRCRĘGYMŠLIDJČŠBMAĘČCYTŽBIĖŠČĘPLRKIPIIZĄĘĖZŠČDADŠBMRGAĘTHKBĖYLČHPŠĖLŠBĘRĖČUĖŠĘŠTĘČTČĖI"
k1 = 9
k2 = 25

abc = "AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ"
d_abc = "AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ"
e_abc = ""

for letter in abc:
    idx = abc.index(letter)
    e = encrypt(idx, 9, 24)
    e_abc = e_abc + abc[e]

result = ""
for letter in text:
    result = result + abc[e_abc.index(letter)]

print(result)

