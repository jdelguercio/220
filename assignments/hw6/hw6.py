"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

from math import pi

def cash_converter():
    cash_int = float(input("enter an integer:"))
    cash_float = "{:.2f}".format(cash_int)
    print("That is ${}".format(cash_float))


def encode():
    message, key = input('enter a message:'), eval(input('enter a key:'))
    uni = []
    uniconv = []
    convback = []
    for i in message:
        conv1 = ord(i)
        uni.append(conv1)
    for j in uni:
        conv2 = j + key
        uniconv.append(conv2)
    for q in uniconv:
        conv3 = chr(q)
        convback.append(conv3)
    print(''.join(convback))

def sphere_area(radius):
    surf_area = 4.0 * pi * radius**2.0
    return surf_area

def sphere_volume(radius):
    vol = (4.0/3.0) * pi * radius**3.0
    return vol


def sum_n(number):
    sum = 0
    for i in range(1,number+1):
        sum += i
    return sum


def sum_n_cubes(number):
    sum = 0
    for i in range(1, number + 1):
        sum += (i**3)
    return sum


def encode_better():
    message, key = input('enter a message:'), input('enter a key:')
    key_lengthened = (key * (len(message)//len(key)+1))[:len(message)]
    key_list, message_list = list(key_lengthened), list(message)
    key_list_uni = []
    message_list_uni = []
    output_ord = []
    output_char = []

    for i in key_list:
        uni_keyk = ord(i)
        key_list_uni.append(uni_keyk)
    print(key_list_uni)
    for j in message_list:
        uni_keym = ord(j)
        message_list_uni.append(uni_keym)
    print(message_list_uni)
    for q in range(0, len(message)):
        key_combine = (((key_list_uni[q] - 65) + (message_list_uni[q] - 65)) % 57) + 64
        output_ord.append(key_combine)
    print(output_ord)
    for z in output_ord:
        out_char = chr(z)
        output_char.append(out_char)
    print(output_char)
    out_string = ''.join(output_char)
    print(out_string)






    uni_message = []
    conv_message = []




if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
