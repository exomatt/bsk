from tkinter import *
from tkinter import ttk
import RailFence as first
import Task2a as second
import Task2b as secondB
import Task2c as secondC
import Task3a as third
import Task3b as thirdB
import Task4 as fourth
from spr2 import LFSR, zad2, zad3

labels = (first, second, secondB, secondC, third, thirdB, fourth)
width = 40
widthS = 5


def makeform(root, field):
    tab = ttk.Frame(root)
    # tab.id

    txt = Entry(tab, width=width)
    txt.grid(column=0, row=0)
    txt2 = Entry(tab, width=width)
    txt2.grid(column=1, row=0)

    def clicked():
        res = field.encrypt(txt.get(), txt2.get())
        var = StringVar()
        var.set(res)
        lbl.configure(textvariable=var)

    btn = Button(tab, text="Click Me", command=clicked)
    btn.grid(column=2, row=0)
    lbl = Entry(tab, width=width)
    lbl.grid(column=3, row=0)

    txt3 = Entry(tab, width=width)
    txt3.grid(column=0, row=1)
    txt4 = Entry(tab, width=width)
    txt4.grid(column=1, row=1)

    def clicked2():
        res = field.decrypt(txt3.get(), txt4.get())
        var = StringVar()
        var.set(res)
        lbl2.configure(textvariable=var)

    btn2 = Button(tab, text="Click Me", command=clicked2)
    btn2.grid(column=2, row=1)
    lbl2 = Entry(tab, width=width)
    lbl2.grid(column=3, row=1)
    return tab


def fix_tab(root, index):
    root.forget(index)
    tab = ttk.Frame(root)
    txt = Entry(tab, width=width)
    txt.grid(column=00, row=0)
    txt2 = Entry(tab, width=width)
    txt2.grid(column=10, row=0)
    txt5 = Entry(tab, width=widthS)
    txt5.grid(column=12, row=0)
    txt6 = Entry(tab, width=widthS)
    txt6.grid(column=14, row=0)

    def clicked():
        res = labels[index].encrypt(txt.get(), txt2.get(), txt5.get(), txt6.get())
        var = StringVar()
        var.set(res)
        lbl.configure(textvariable=var)

    btn = Button(tab, text="Click Me", command=clicked)
    btn.grid(column=20, row=0)
    lbl = Entry(tab, width=width)
    lbl.grid(column=30, row=0)

    txt3 = Entry(tab, width=width)
    txt3.grid(column=00, row=1)
    txt4 = Entry(tab, width=width)
    txt4.grid(column=10, row=1)
    txt7 = Entry(tab, width=widthS)
    txt7.grid(column=12, row=1)
    txt8 = Entry(tab, width=widthS)
    txt8.grid(column=14, row=1)

    def clicked2():
        res = labels[index].decrypt(txt3.get(), txt4.get(), txt7.get(), txt8.get())
        var = StringVar()
        var.set(res)
        lbl2.configure(textvariable=var)

    btn2 = Button(tab, text="Click Me", command=clicked2)
    btn2.grid(column=20, row=1)
    lbl2 = Entry(tab, width=width)
    lbl2.grid(column=30, row=1)

    root.insert(index, tab, text=labels[5].__str__())


def main():
    # for field in labels:
    #     print('\n' + field.__str__())
    #     field.main()
    window = Tk()
    window.title("Some fancy title")
    window.geometry('780x320')
    tab_control = ttk.Notebook(window)

    for field in labels:
        tab_control.add(makeform(tab_control, field), text=field.__str__())

    fix_tab(tab_control, 5)
    tab_control.add(LFSR.makeform(tab_control), text=LFSR.__str__())
    tab_control.add(zad2.makeform(tab_control), text=zad2.__str__())
    tab_control.add(zad3.makeform(tab_control), text=zad3.__str__())

    tab_control.pack(expand=1, fill='both')

    window.mainloop()


if __name__ == '__main__':
    main()

'''
Testing bench
1. ALA_MA_KOTA, 4
2. HERE_IS_A_SECRET_MESSAGE_ENCIPHERED_BY_TRANSPOSITION, 5-2-1-3-4
3. HERE_IS_A_SECRET_MESSAGE_ENCIPHERED_BY_TRANSPOSITION, CONVENIENCE
4. CRYPTOGRAPHY, 26, 5, 7
5. CRYPTOGRAPHY, BREAKBREAKBR
'''
