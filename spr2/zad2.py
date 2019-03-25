import os

from tkinter import *
from tkinter import ttk

from spr2 import LFSR, readBinFile

width = 25
widthS = 5


def encrypt(seed, poly, file, file2):
    obj = LFSR.LFSR()
    obj.lfsr(seed, poly)
    my_array = readBinFile.read_bin_file_to_bitarray(os.getcwd() + "/spr2/" + file)
    array2 = my_array[:]
    # array3 = my_array[:]
    counter = 0

    for i in range(len(my_array)):
        counter += 1
        x = obj.next()
        if x is None:
            return
        array2[i] = (my_array[i] + x) % 2
        if counter % 50000 == 0:
            print(counter)
    readBinFile.write_bin_file(os.getcwd() + "/spr2/" + file2, array2)


def decrypt(seed, poly, file, file2):
    obj = LFSR.LFSR()
    obj.lfsr(seed, poly)
    counter = 0
    array2 = readBinFile.read_bin_file_to_bitarray(os.getcwd() + "/spr2/" + file)
    array3 = array2[:]
    for i in range(len(array2)):
        counter += 1
        x = obj.next()
        if x is None:
            return
        array3[i] = (array2[i] + x) % 2
        if counter % 50000 == 0:
            print(counter)
    readBinFile.write_bin_file(os.getcwd() + "/spr2/" + file2, array3)

    # print(readBinFile.compare_two_bin_files(my_array, array2))


def main():
    print("Main")
    # obj = LFSR.LFSR()
    # obj.lfsr("111010", "101011")
    encrypt("010111", "110101", "smth.png", "smth.bin")
    decrypt("010111", "110101", "smth.bin", "smth2.png")


def makeform(root):
    tab = ttk.Frame(root)
    txt = Entry(tab, width=width)
    txt.grid(column=0, row=0)
    txt2 = Entry(tab, width=width)
    txt2.grid(column=1, row=0)
    txt3 = Entry(tab, width=width)
    txt3.grid(column=2, row=0)
    txt4 = Entry(tab, width=width)
    txt4.grid(column=3, row=0)
    lbl = Entry(tab, width=width)
    # lbl.grid(column=6, row=0)
    obj = LFSR.LFSR()

    # def clicked():
    #     obj.lfsr(txt.get(), txt2.get())

    def clicked2():
        encrypt(txt.get(), txt2.get(), txt3.get(), txt4.get())

    def clicked3():
        decrypt(txt.get(), txt2.get(), txt3.get(), txt4.get())

    # btn = Button(tab, text="Prep LFSR", command=clicked)
    # btn.grid(column=4, row=0)
    btn = Button(tab, text="Encrypt", command=clicked2)
    btn.grid(column=5, row=0)
    btn = Button(tab, text="Decrypt", command=clicked3)
    btn.grid(column=6, row=0)
    return tab


def __str__():
    return "Synchronous Stream Cipher"


if __name__ == '__main__':
    main()
