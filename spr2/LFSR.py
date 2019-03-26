import array

from tkinter import *
from tkinter import ttk

width = 40
widthS = 5


class LFSR:
    def __init__(self):
        with open("test.txt", "w") as f:
            f.write('')
        self.seed = 0
        self.output = 0
        self.polynomial = None
        self.arr = None
        self.poly = None
        self.mode = 0

    def lfsr(self, seed, polynomial):
        if polynomial.endswith('0'):
            print("Polynomial ends with 0")
            return None
        if len(seed) != len(polynomial):
            print("Params arent the same length")
            return None
        self.arr = array.array('i', (0 for i in range(0, len(seed))))
        self.poly = array.array('i', (0 for i in range(0, len(seed))))
        # out = array.array('i', (0 for i in range(0, int(n))))
        for i in range(0, len(seed)):
            self.arr[i] = int(seed[i])
            self.poly[i] = int(polynomial[i])
        print(self.arr)
        print(self.poly)

    def next(self):
        if self.poly is None or self.arr is None:
            return None
        # temp = self.arr[:]
        self.output = self.arr[len(self.poly) - 1]
        for j in range(len(self.poly) - 1, 0, -1):
            if self.poly[j - 1] == 1:
                x = self.poly[j - 1]
                y = self.arr[j - 1]
                self.output = (self.output + self.arr[j - 1]) % 2
        for j in range(len(self.arr) - 1, 0, -1):
            self.arr[j] = self.arr[j - 1]
        self.arr[0] = self.output
        if self.mode == 1:
            return self.arr
            # with open("test.txt", "a+") as f:
            #     # print("Mode on")
            #     f.write(', '.join(str(x) for x in self.arr))
            #     f.write('\n')
        else:
            return self.arr[0]


def main():
    print("Main")
    obj = LFSR()
    obj.lfsr("111010", "101011")
    odp="1110100101"
    # obj.mode = 1
    for i in range(0, 10):
        print(obj.next())

    # loc = os.getcwd() + "\\test2.bin"
    # my_array = readBinFile.read_bin_file_to_bitarray(os.getcwd() + "/test.bin")
    # array2 = my_array[:]
    # array3 = my_array[:]
    # counter = 0
    #
    # for i in range(len(my_array)):
    #     counter += 1
    #     x = obj.next()
    #     if x is None:
    #         return
    #     array2[i] = (my_array[i] + x) % 2
    #     if counter % 50000 == 0:
    #         print(counter)
    # readBinFile.write_bin_file(os.getcwd() + "/test_enc.bin", array2)
    #
    # obj2 = LFSR()
    # obj2.lfsr("10110", "10011", "24")
    #
    # counter = 0
    # array2 = readBinFile.read_bin_file_to_bitarray(os.getcwd() + "/test_enc.bin")
    # for i in range(len(array2)):
    #     counter += 1
    #     x = obj2.next()
    #     if x is None:
    #         return
    #     array3[i] = (array2[i] + x) % 2
    #     if counter % 50000 == 0:
    #         print(counter)
    # readBinFile.write_bin_file(os.getcwd() + "/test_dec.bin", array3)
    #
    # print(readBinFile.compare_two_bin_files(my_array, array2))


def makeform(root):
    tab = ttk.Frame(root)
    txt = Entry(tab, width=width)
    txt.grid(column=0, row=0)
    txt2 = Entry(tab, width=width)
    txt2.grid(column=1, row=0)
    txt3 = Entry(tab, width=widthS)
    txt3.grid(column=2, row=0)
    lbl = Entry(tab, width=width)
    lbl.grid(column=6, row=0)
    obj = LFSR()

    def clicked():
        obj.lfsr(txt.get(), txt2.get())

    def clicked2():
        var = StringVar()
        var.set(obj.next())
        lbl.configure(textvariable=var)

    def clicked3():
        obj.mode = 1
        with open("test.txt", "w") as f:
            f.write('')
        with open("test.txt", "a+") as f:
            for i in range(0, int(txt3.get())):
                print("Mode on")
                arr = obj.next()
                f.write(', '.join(str(x) for x in arr))
                f.write('\n')
        obj.mode = 0

    btn = Button(tab, text="Prep LFSR", command=clicked)
    btn.grid(column=3, row=0)
    btn = Button(tab, text="Get Next", command=clicked2)
    btn.grid(column=4, row=0)
    btn = Button(tab, text="Do Many", command=clicked3)
    btn.grid(column=5, row=0)
    return tab


def __str__():
    return "LFSR"


if __name__ == '__main__':
    main()
