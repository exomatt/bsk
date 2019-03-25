import pathlib
import time

from spr2 import readBinFile

from tkinter import *
from tkinter import ttk

width = 40
widthS = 5


def check_params(arg1, arg2):
    while arg1.startswith("0"):
        arg1 = arg1[1:]

    if len(list(map(int, arg2))) == len(list(map(int, arg1))):
        return True
    else:
        return False


def correct_value(value):
    while value.startswith("0"):
        value = value[1:]
    value = list(map(int, value))  # convert string list to int list
    return value


def create_zeros_prefix(x):
    zeros = ''
    while x.startswith("0"):
        zeros = str(str(zeros) + str('0'))
        x = x[1:]
    return zeros


def create_shift_table(x_degree, polynomial_degree):
    table = [""] * (x_degree + 1)

    for row in range(x_degree + 1):
        table[row] = [""] * polynomial_degree

    return table


def encrypt(polynomial, seed):

    if check_params(polynomial, seed) is False or len(polynomial) == 0:
        print("Złe parametry")
        sys.exit(0)

    with open('zad3_input_X.bin', 'r') as content_file:
        x = content_file.read()

    x = correct_value(x)
    seed = list(map(int, seed))

    last_index_1_value = polynomial.rfind("1")

    first_index_1_value = polynomial.find("1")

    polynomial = correct_value(polynomial)  # (x^4 + x^2 + x^1)

    polynomial_degree = len(polynomial)
    x_degree = len(x)

    shift_table = create_shift_table(x_degree, polynomial_degree)

    polynomial_array = polynomial

    reversed_polynomial_array = polynomial_array[::-1]

    significent_value = polynomial_degree - (last_index_1_value - first_index_1_value)

    for row in range(x_degree + 1):
        xor_sum = 0
        for col in range(polynomial_degree):
            if row == 0:  # First row
                shift_table[row] = seed
                break
            else:  # Every row despite first one
                if polynomial_degree == 1:
                    shift_table[row][col] = (x[row - 1] + shift_table[row - 1][col]) % 2
                else:
                    if reversed_polynomial_array[col] == 1:
                        xor_sum += shift_table[row - 1][col]

                    if col > 0:
                        shift_table[row][col] = shift_table[row - 1][col - 1]
                        if col == (polynomial_degree - 1):  # Last column in every row
                            xor_sum += x[row - 1]
                            shift_table[row][0] = xor_sum % 2

    key = ""
    for row in range(x_degree):
        key = str(str(key) + str(shift_table[row + 1][0]))

    print(significent_value)

    current_dir = pathlib.Path(__file__).parent
    cur_time = time.strftime("%H:%M:%S")

    readBinFile.write_bin_file_string(str(current_dir) + '/encryption_result' + cur_time + '.bin', key)
    print('Y=' + str(key))

    return str(key)


def decrypt(polynomial, seed, y):

    with open('zad3_input_X.bin', 'r') as content_file:
        x = content_file.read()

    zeros = create_zeros_prefix(x)

    y = list(map(int, y))
    seed = list(map(int, seed))

    polynomial = correct_value(polynomial)  # (x^4 + x^2 + x^1)

    polynomial_degree = len(polynomial)
    y_degree = len(y)

    shift_table = create_shift_table(y_degree, polynomial_degree)

    polynomial_array = polynomial

    reversed_polynomial_array = polynomial_array[::-1]

    for row in range(y_degree + 1):
        for col in range(polynomial_degree):
            if row == 0:  # First row
                shift_table[row] = seed
                break
            else:  # For every row
                if col == 0:
                    shift_table[row][col] = y[row - 1]
                elif col > 0:
                    shift_table[row][col] = shift_table[row - 1][col - 1]
    x = ''

    for row in range(y_degree):
        value = 0
        for col in range(polynomial_degree):
            if reversed_polynomial_array[col] == 1:
                value += shift_table[row][col]
        value += y[row]

        value = value % 2

        x = str(str(x) + str(value))

    x = str(str(zeros) + str(x))

    current_dir = pathlib.Path(__file__).parent
    cur_time = time.strftime("%H:%M:%S")

    readBinFile.write_bin_file_string(str(current_dir) + '/decryption_result_' + cur_time + '.bin', x)

    # ------------------------------------------------------------------------------------------------------#
    # UWAGA! Żeby sprawdzić program porownujemy plik 'decryption_result_XX:XX:XX.bin' z 'zad3_input_X.bin' #
    # ------------------------------------------------------------------------------------------------------#


def main():

    polynomial = '101010'  # First param
    seed = '100010'        # Secound param

    Y = encrypt(polynomial, seed)
    decrypt(polynomial, seed, Y)


if __name__ == '__main__':
    main()


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

    # def clicked():
    #     obj.lfsr(txt.get(), txt2.get())
    #
    # def clicked2():
    #     var = StringVar()
    #     var.set(obj.next())
    #     lbl.configure(textvariable=var)
    #
    # def clicked3():
    #     obj.mode = 1
    #     with open("test.txt", "w") as f:
    #         f.write('')
    #     with open("test.txt", "a+") as f:
    #         for i in range(0, int(txt3.get())):
    #             print("Mode on")
    #             arr = obj.next()
    #             f.write(', '.join(str(x) for x in arr))
    #             f.write('\n')
    #     obj.mode = 0

    # btn = Button(tab, text="Prep LFSR", command=clicked)
    # btn.grid(column=3, row=0)
    # btn = Button(tab, text="Get Next", command=clicked2)
    # btn.grid(column=4, row=0)
    # btn = Button(tab, text="Do Many", command=clicked3)
    # btn.grid(column=5, row=0)
    return tab


def __str__():
    return "Ciphertext Autokey"
