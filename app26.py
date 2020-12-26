from tkinter import *

root = Tk()

def apresentar():
    print(valor_check.get())
root.title('CHECKBOX')
root.geometry('300x20')

valor_check = IntVar()

check = Checkbutton(
    root,
    text='esta é uma checkbox.',
    variable=valor_check,
    command=apresentar).pack()

root.mainloop()