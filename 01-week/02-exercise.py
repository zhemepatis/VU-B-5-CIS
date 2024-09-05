# reading data
with open("02-data.txt") as data:
    key = data.readline()
    txt = data.read()

txt = txt.replace(" ", "").replace("\n", "")
key = key.replace(" ", "").replace("\n", "")

# finding row order
ordered_key = [letter for letter in key]
ordered_key.sort()
ordered_key = "".join(ordered_key)

row_order = []
for letter in key:
    row_order.append(ordered_key.index(letter) + 1)
    ordered_key = ordered_key.replace(letter, "-", 1)

# re-organizing text
txt_len = len(txt)
row_num = len(key)
col_num = txt_len / row_num

result = []
for i in range(0, txt_len):
    result.append(txt[(int) ((row_order[i%row_num] - 1)*col_num + i / row_num)])

print("".join(result))
