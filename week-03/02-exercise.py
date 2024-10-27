# 2. Decipher Vigenere cipher when key starts with "BAL"
# UILFE ĄYNPV KLŠIĖ CTYZK HĮYYJ 
# TĘSUĘ GPSĮS SŽAVK ĘOYSH YŽDOI 
# LLSCŪ SLLTH ŠIGVT LTGLF OORŠS 
# ILCRD DĘTĮY NLYUY ŽYĘSV HSIĘF 
# ĄĘBRG IEĮBŠ GLOGY AĖŪEJ YMGFE 
# KVKHĮ ĮĖBIĄ ŠBLŽO CŽGCP ACSGC 
# PTVEĄ KŽIĘK IGBNG ĘAŪRK SSNST 
# NSKUĮ YNVVK HČEČŪ RSTUŲ DVDČE 
# ACSGĖ TŲCNV TĄĖIA ĮBAĘI RCĖŠN 
# COĖRG VGIYS ARSRS TOGCK KBIŲV 
# OĖRGV GĖARR CSCCL AGCKĮ YAHYI 
# SYNSI AIŠAĖ KATĖT GVGVČ AČKIY 
# ŲANCL CAUDK IYRLV SRCRO ĘTIKC 
# SYHRC RJTĄO YMAVK AĖYOA CMLYS V

import utils.global_vars as gv
import utils.vigenere_cipher as vc
import utils.str_funcs as sf
from utils.friedman_test import friedman_test

gv.alphabet = "AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ"

key_part = "BAL"
text = "UILFEĄYNPVKLŠIĖCTYZKHĮYYJTĘSUĘGPSĮSSŽAVKĘOYSHYŽDOILLSCŪSLLTHŠIGVTLTGLFOORŠSILCRDDĘTĮYNLYUYŽYĘSVHSIĘFĄĘBRGIEĮBŠGLOGYAĖŪEJYMGFEKVKHĮĮĖBIĄŠBLŽOCŽGCPACSGCPTVEĄKŽIĘKIGBNGĘAŪRKSSNSTNSKUĮYNVVKHČEČŪRSTUŲDVDČEACSGĖTŲCNVTĄĖIAĮBAĘIRCĖŠNCOĖRGVGIYSARSRSTOGCKKBIŲVOĖRGVGĖARRCSCCLAGCKĮYAHYISYNSIAIŠAĖKATĖTGVGVČAČKIYŲANCLCAUDKIYRLVSRCROĘTIKCSYHRCRJTĄOYMAVKAĖYOACMLYSV"
text_len = len(text)

# using Friedman test to find most probable length of key
for i in range(3, 32):
    test_result = friedman_test(text, i)
    print(f"len: {i}, probability: {test_result}")

# when key length is 6, we see a slight jump in numbers, therefore we assume that key length is 6
# getting most frequent letters to make key from them
text_splits = sf.get_splits(text, 6)
for split in text_splits:
    frequecies = sf.count_frequencies(split)
    print(f"most frequent letters: {frequecies}")

# assuming that key is "BALSAS"
key = "BALSAS"
result = vc.decrypt_text(text, key)
print(result)