# -- coding: utf-8 --

from tkinter import *
from tkinter import messagebox


def d2():
    arg = txt1.get()
    i = 2
    N = int(txt1.get())
    if N >= 2:
     while N % i != 0:
        i += 1
     messagebox.showinfo('Результат', i)
    else:
     messagebox.showinfo('Результат', 'No')



l1 = 0


l2 = 0
S = 0
def d6():
    global l2
    global Z
    arg = int(txt5.get())
    if arg != 0:
        l2 +=1
        Z += arg
    else:
        messagebox.showinfo('Результат', Z / l2)
        l2 = 0
        Z = 0
    txt5.delete(0, END)

m = 0
Z = 0


m1 = 0
Z1 = 1
M = 0


window = Tk()
window.title("N6")
window.geometry('700x300')

lbl1 = Label(window, text = "Введите число")
lbl1.grid(column=0, row = 1)
txt1 = Entry(window, width = 10)
txt1.grid(column=1, row = 1)
btn1 = Button(window, text = "N5_2",command = d2)
btn1.grid(column=2, row = 1)




lbl5 = Label(window, text = "Введите число")
lbl5.grid(column=0, row = 5)
txt5 = Entry(window, width = 10)
txt5.grid(column=1, row = 5)
btn5 = Button(window, text = "N5_6", command = d6)
btn5.grid(column=2, row = 5)



window.mainloop()