def char_to_binary(letter):
    return bin(ord(letter))[2::]

def text_to_binary(text):
    txt_bin = ''
    for letter in text:
        txt_bin += bin(ord(letter))[2::]

    return txt_bin

def num_to_binary(num):
    return bin(num)[2::]

def num_list_to_binary(num_list):
    txt_bin = ''
    for num in num_list:
        txt_bin += num_to_binary(num)

    return txt_bin