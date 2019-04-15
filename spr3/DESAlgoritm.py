import datetime
from tkinter import *
from tkinter import ttk

from bitarray import bitarray

import spr2.readBinFile as readBinFile
import spr3.DES as keygenerator
import spr3.des_key as des_key

width = 35
widthS = 10


# za parametr przyjmuje bitarray :)

def init_permutation(bit_array):
    array_after_permut = bitarray()
    for number in range(len(des_key.IP)):
        array_after_permut.append(bit_array[des_key.IP[number] - 1])
    return array_after_permut


def inverse_permutation(bit_array):
    array_after_permut = bitarray()
    for number in range(len(des_key.IPR)):
        array_after_permut.append(bit_array[des_key.IPR[number] - 1])
    return array_after_permut


def spliHalf(barray):
    return barray[:32], barray[32:]


def expand_with_E_permute(bit_array):
    array_after_expand = bitarray()
    for number in range(len(des_key.E)):
        array_after_expand.append(bit_array[des_key.E[number] - 1])
    return array_after_expand


def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i + n]


def f_function(bit_array, key):
    e_permute = expand_with_E_permute(bit_array)
    own_bit_array = bitarray(e_permute ^ key)
    bit_arrays = list(chunks(own_bit_array, 6))
    number = 0
    temp_to_add = ''
    for arr in bit_arrays:
        f_l_elements = arr[::5]
        mid_elements = arr[1:5]
        first = int(f_l_elements.to01(), 2)
        second = int(mid_elements.to01(), 2)
        s_box = des_key.S_BOX
        temp_to_add += str(bin(s_box[number][first][second]))[2:].zfill(4)
        number += 1
    result_of_s_box_operant = bitarray(temp_to_add)
    array_after_permut = bitarray()
    for number in range(len(des_key.P)):
        array_after_permut.append(result_of_s_box_operant[des_key.P[number] - 1])
    return array_after_permut


# przyjmuje bit array i tu i tu czyli przed klucz słowny zamienic na bitarray
def encrypt_block(message_in, key):
    permuted_message = init_permutation(message_in)
    left_message, right_massage = spliHalf(permuted_message)
    keys_list = keygenerator.generate_key(key)
    for i in range(16):
        temp_left = right_massage
        generate_key = keys_list[i]
        f_function_result = f_function(right_massage, generate_key)
        right_massage = left_message ^ f_function_result
        left_message = temp_left
    massage_after_iter = right_massage + left_message  # zamiana stron bo ostatni ma byc bez zamianay a petla
    # domyslnie ostatenie tez zamieni miejscami x:D :P
    result_encryption = inverse_permutation(massage_after_iter)
    return result_encryption


# przyjmuje bit array i tu i tu czyli przed klucz słowny zamienic na bitarray
def decrypt_block(encrypted_message_in, key):
    permuted_message = init_permutation(encrypted_message_in)
    left_message, right_massage = spliHalf(permuted_message)

    keys_list = keygenerator.generate_key(key)[::-1]  # Reverse generated keys. [ 0, 1, 2... 15 ] -> [ 15, 14, 13... 0 ]

    for i in range(16):
        temp_left = right_massage
        generate_key = keys_list[i]
        f_function_result = f_function(right_massage, generate_key)
        right_massage = left_message ^ f_function_result
        left_message = temp_left

    massage_after_iter = right_massage + left_message  # zamiana stron bo ostatni ma byc bez zamianay a petla
    # domyslnie ostatenie tez zamieni miejscami x:D :P
    result_decryption = inverse_permutation(massage_after_iter)
    return result_decryption


def encrypt_file_full_file(input_file, out, input_key):
    message_file = readBinFile.read_bin_file_to_bitarray(input_file)

    # add padding
    file_lenght = message_file.length() % 64
    if file_lenght != 0:
        to_add = 64 - file_lenght + 63
        message_file += bitarray("1")
        message_file += to_add * bitarray("0")
    else:
        message_file += bitarray("1")
        message_file += 63 * bitarray("0")

    encrypted_message = bitarray()
    for block in range(int(len(message_file) / 64)):
        block_message = message_file[(block * 64):((block + 1) * 64)]
        block_encrypted_message = encrypt_block(block_message, input_key)

        encrypted_message += block_encrypted_message

    readBinFile.write_bin_file(out, encrypted_message)


def decrypt_file_full_file(input_encrypted_file, out, input_key):
    message_encrypted_file = readBinFile.read_bin_file_to_bitarray(input_encrypted_file)

    decrypted_message = bitarray()
    for block in range(int(len(message_encrypted_file) / 64)):
        block_message = message_encrypted_file[(block * 64):((block + 1) * 64)]
        block_decrypted_message = decrypt_block(block_message, input_key)

        decrypted_message += block_decrypted_message

    # delete padding
    decrypted_message.reverse()
    message_copy = decrypted_message.copy()
    for num in range(len(decrypted_message)):
        if decrypted_message[num] == 1:
            message_copy.pop(0)
            break
        message_copy.pop(0)
    message_copy.reverse()
    readBinFile.write_bin_file(out, message_copy)


def makeform(root):
    tab = ttk.Frame(root)

    txt = Entry(tab, width=width)
    txt.grid(column=0, row=0)
    txt2 = Entry(tab, width=width)
    txt2.grid(column=1, row=0)

    def clicked():
        var = StringVar()
        if len(txt.get()) == 64 and len(txt2.get()) == 64:
            print("Start")
            res = encrypt_block(bitarray(txt.get()), bitarray(prep_input(txt2.get())))
            temp = bit_to_str(res)
            var.set(temp)
            print("Done")
        else:
            var.set("Inputs aren't 64 bits long")
        # bitarray('0111001101011001101100100001011000111110010011101101110001011000')
        lbl.configure(textvariable=var)

    btn = Button(tab, text="Encrypt", command=clicked)
    btn.grid(column=2, row=0)
    lbl = Entry(tab, width=width)
    lbl.grid(column=3, row=0)

    txt3 = Entry(tab, width=width)
    txt3.grid(column=0, row=1)
    txt4 = Entry(tab, width=width)
    txt4.grid(column=1, row=1)

    def clicked2():
        # res = decrypt_block(txt3.get(), txt4.get())
        # var = StringVar()
        # var.set(res)

        var = StringVar()
        if len(txt3.get()) == 64 and len(txt4.get()) == 64:
            print("Start")
            res = decrypt_block(bitarray(txt3.get()), bitarray(prep_input(txt4.get())))
            temp = bit_to_str(res)
            var.set(temp)
            print("Done")
        else:
            var.set("Inputs aren't 64 bits long")
        lbl2.configure(textvariable=var)

        var2 = StringVar()
        a = txt.get() == lbl2.get()
        b = txt.get() is lbl2.get()
        var2.set(txt.get() == lbl2.get())
        lbl3.configure(textvariable=var2)
        # if lbl.get() is lbl2.get():
        #     lbl3.configure(textvariable="True")
        # else:
        #     lbl3.configure(textvariable="False")

    btn2 = Button(tab, text="Decrypt", command=clicked2)
    btn2.grid(column=2, row=1)
    lbl2 = Entry(tab, width=width)
    lbl2.grid(column=3, row=1)
    lbl3 = Entry(tab, width=widthS)
    lbl3.grid(column=3, row=2)
    return tab


def makeform2(root):
    tab = ttk.Frame(root)

    txt = Entry(tab, width=width)
    txt.grid(column=0, row=0)
    txt2 = Entry(tab, width=width)
    txt2.grid(column=1, row=0)
    txt5 = Entry(tab, width=width)
    txt5.grid(column=2, row=0)

    def clicked():
        print("Start")
        time = datetime.datetime.now()
        encrypt_file_full_file(txt.get(), txt2.get(), bitarray(prep_input(txt5.get())))
        print("Done. Time:" + str(datetime.datetime.now() - time))

    btn = Button(tab, text="Encrypt", command=clicked)
    btn.grid(column=3, row=0)

    txt3 = Entry(tab, width=width)
    txt3.grid(column=0, row=1)
    txt4 = Entry(tab, width=width)
    txt4.grid(column=1, row=1)
    txt6 = Entry(tab, width=width)
    txt6.grid(column=2, row=1)

    def clicked2():
        print("Start")
        time = datetime.datetime.now()
        decrypt_file_full_file(txt3.get(), txt4.get(), bitarray(prep_input(txt6.get())))
        print("Done. Time:" + str(datetime.datetime.now() - time))

        # lbl2.configure(textvariable=var)

    btn2 = Button(tab, text="Decrypt", command=clicked2)
    btn2.grid(column=3, row=1)
    return tab

    # TODO Add  functiom that preps input. Change from hex to bin. Cut if longer than 64-bit. Fill with zeros if
    # shorter.


def prep_input(msg):
    temp = bin(int(msg, 16))[2:]
    if len(temp) > 64:
        temp = temp[len(temp) - 64:]
    else:
        while len(temp) < 64:
            temp = '0' + temp
    print("len(temp): " + str(len(temp)) + ", temp: " + str(temp))
    return temp


def bit_to_str(arr):
    out = ''
    for bit in arr:
        if bit:
            out += '1'
        elif not bit:
            out += '0'
    return out


if __name__ == '__main__':
    window = Tk()
    window.title("DES Algorithm")
    window.geometry('780x320')
    tab_control = ttk.Notebook(window)

    tab_control.add(makeform2(tab_control), text="DES File")
    tab_control.add(makeform(tab_control), text="DES Text")
    # a = bitarray("1111111110100011101000111010001110100011101000111010001110100011")
    # barrayP = init_permutation(a)
    # print(barrayP)
    # left, right = spliHalf(barrayP)
    # print(left)
    # print(right)
    # permut = expand_with_E_permute(right)
    # print(permut)
    # print(a[:48])
    # print("wynik F funkcji ")
    # print(f_function(right, a[:48]))
    input_key = bitarray('1110011111000011111100001000011110100101110000111001011001101001')

    # 'smth.png' file size is 2112 bits, so -> (2112 % 64) == 0
    # encrypt_file_full_file('smth.png', 'test1_encrypted.bin', input_key)  # encrypt file which (size % 64) == 0
    # decrypt_file_full_file('test1_encrypted.bin', 'test1_decrypted.png', input_key)
    # decrypt file which (size % 64) == 0

    message = bitarray("1111111110100011101000111010001110100011101000111010001110100011")

    print('Message - ' + str(message))
    print(
        "INTERNET Encrypt:" + '110100010010010100111101000011010000111000010010001001011101110')  # Tak, nie ma
    # początkowego zera

    # encrypted = encrypt_block(message, input_key)
    # print("Encrypted: " + str(encrypted))
    #
    # decrypted = decrypt_block(encrypted, input_key)
    # print("Decrypted: " + str(decrypted))

    tab_control.pack(expand=1, fill='both')
    window.mainloop()
