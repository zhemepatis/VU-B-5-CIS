from itertools import permutations 

# reading data
with open("03-data.txt") as data:
    key = data.readline()
    txt = data.read()

txt = txt.replace(" ", "").replace("\n", "")
key = int(key.replace(" ", "").replace("\n", ""))

# re-organizing text
txt_len = len(txt)
row_num = key
col_num = txt_len / row_num

potential_row_orders = list(permutations([x for x in range(1, row_num + 1)]))

for curr_row_order in potential_row_orders:
    result = []

    for i in range(0, txt_len):
        result.append(txt[(int) ((curr_row_order[i%row_num] - 1)*col_num + i / row_num)])

    print(f'Result when key is {curr_row_order}')
    print("".join(result))

    if potential_row_orders[len(potential_row_orders) - 1] == curr_row_order:
        break

    print("Proceed? [Y/n]")
    inp = input()

    if inp == "n" or inp == "N":
        break
