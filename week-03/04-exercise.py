# 4. Decipher Vigenere autokey cipher when key is "LIETUS"
#
# Cipher:
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

text = "KŠBJBEKMJĄYSJZBĮEĘFPYDHĘĖCĘŽBODCNPYOLUKĄBDSNŪOYDCGĖGĮNĖAĖRČNĄSVRPKĮSFĮGGČĮCEČŲKĘUDGĮŠŠUUŠŪZĮUNČMCĮINŲĄCĘŽTVĘBNMTSSĖČZIKŠŠČODUEPGĘLIIĖČZGMYORŽCEZĄHŽŪVŠLĄDAFŠČUMKFČTNNĘSOYŽFTŠČYPBFŠKKLĘFGKĘNĮŽVŪĄCĮRORAJAGCRUĄOULEHPCAAUPŲĮZILYPĄĮIĖBEĮĮBOT"
key = "LIETUS" + text
result = vc.decrypt_text(text, key)
print(result)