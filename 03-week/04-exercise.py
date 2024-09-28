# 4. Vigenere-auto šifro raktas =LIETUS. Iššifruokite šifrą 
# KŠBJB EKMJĄ YSJZB ĮEĘFP YDHĘĖ 
# CĘŽBO DCNPY OLUKĄ BDSNŪ OYDCG 
# ĖGĮNĖ AĖRČN ĄSVRP KĮSFĮ GGČĮC 
# EČŲKĘ UDGĮŠ ŠUUŠŪ ZĮUNČ MCĮIN 
# ŲĄCĘŽ TVĘBN MTSSĖ ČZIKŠ ŠČODU 
# EPGĘL IIĖČZ GMYOR ŽCEZĄ HŽŪVŠ 
# LĄDAF ŠČUMK FČTNN ĘSOYŽ FTŠČY 
# PBFŠK KLĘFG KĘNĮŽ VŪĄCĮ RORAJ 
# AGCRU ĄOULE HPCAA UPŲĮZ ILYPĄ 
# ĮIĖBE ĮĮBOT

import utils.global_vars as gv
import utils.vigenere_cipher as vc
import utils.str_funcs as sf

gv.alphabet = "AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ"

key = "LIETUS"
text = "KŠBJBEKMJĄYSJZBĮEĘFPYDHĘĖCĘŽBODCNPYOLUKĄBDSNŪOYDCGĖGĮNĖAĖRČNĄSVRPKĮSFĮGGČĮCEČŲKĘUDGĮŠŠUUŠŪZĮUNČMCĮINŲĄCĘŽTVĘBNMTSSĖČZIKŠŠČODUEPGĘLIIĖČZGMYORŽCEZĄHŽŪVŠLĄDAFŠČUMKFČTNNĘSOYŽFTŠČYPBFŠKKLĘFGKĘNĮŽVŪĄCĮRORAJAGCRUĄOULEHPCAAUPŲĮZILYPĄĮIĖBEĮĮBOT"
text_len = len(text)

for idx in range(0, text_len):
    e_letter = text[idx]
    d_letter = vc.decode_letter(e_letter, idx, key)

    key = key + d_letter
    print(key)

result = vc.decode_text(text, key)
print(result)