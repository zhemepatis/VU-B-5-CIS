import math

with open("01-data.txt") as data:
    txt = data.read()

txt = txt.replace(" ", "").replace("\n", "")
txt_len = len(txt)


i = 1
divisors = []
while (i <= math.sqrt(txt_len)):
    if txt_len % i == 0:
        divisors.append(i)

        if i != txt_len/i:
            divisors.append((int) (txt_len/i))

    i += 1


divisors.sort()
for num in divisors:
    step = (int) (txt_len / num)

    result = []
    for i in range(0, txt_len):    
        result.append(txt[num*(i%step) + (int) (i/step)])

    print(f'Result when key is {num}')
    print("".join(result))

    if divisors[len(divisors) - 1] == num:
        break

    print("Proceed? [Y/n]")
    key = input()

    if key == "n" or key == "N":
        break