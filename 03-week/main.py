import vigenere_cipher

vigenere_cipher.alphabet = "AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ"

# 1st exercise
key = "DANGTIS"
text = "ŪUĖGKŠKHNCRIŠFŽPNŪTKCDUCGZVSLKĘCNBCŽDNČCŠSŽNTRYEYBAČGILČPĄVRMAĘLABGNZSŠOĖADRCSTŽĄKŪĮŽPĮŲDŽĄDIKŠFLDZIKRKEYZITUKFSŲBŽČKDCHKDKIŪLŪĮGRYIĮHIVZĖŠFŽSŠĘDLVVIDCFMKŽRKGGIGGIERĮVSLKFZZHCTCŽNŽBTRAIZJAŪNKČMKBHGĖGKYDCŠTOĘTVSŠDOĄTEĖĮLTRZAYLSTŽMŠGZAKGGIGGAKRŽDHŪLNRFEODDŽVTCCGVŽJŽČCSTNŽJAFHTŲTĮVSLKĮ"
text_len = len(text)

result = ""
for i in range(0, text_len - 1):
    e_letter = text[i]
    d_letter = vigenere_cipher.decode_letter(e_letter, i, key)

    result = result + vigenere_cipher.alphabet[d_letter]

print(result)