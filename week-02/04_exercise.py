abc = "AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ"
text = "UŲGŪĘHBĘEPŪBGDUŲGRPIORHEŠDABAŲYIRRRHYNEYŲČTGIŠYIĖKEPTGMCORZPVŠŽOŲLČPGCĖZBDRĖERŠČJOĮANBIŠĘŠOŽBDCČYŠŠČTGČOŠHRAŲLMEČJNĄOŠAČVŽŠĮĄKĄŪBŠBŲNŲČYAĖSRŲĖŠČ"
inverse = [9, -4, -10, 19]

length = len(text)
num = (int) (length / 2)
print(num)


result = ""
for i in range(0, int(num)):
    c1 = abc.index(text[i*2])
    c2 = abc.index(text[i*2+1])

    m1, m2 =  (19*c1 -10*c2)%32, (-4*c1+19*c2)%32
    result = result + abc[m1] + abc[m2]

print(result)
