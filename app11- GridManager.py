'''
grid manager
____________________________________________________
|                |                |                |
| row=0 column=0 | row=0 column=1 | row=0 column=2 |
_________________|________________|________________|
|                |                |                |
| row=1 column=0 | row=1 column=1 | row=1 column=2 |
_________________|________________|________________|
|                |                |                |
| row=2 column=0 | row=2 column=1 | row=2 column=2 |
|________________|________________|________________|
'''
from tkinter import *

menu_inicial=Tk()
menu_inicial.title('Titulo')
#menu_inicial.geometry('500x500+100+300')

label1=Label(menu_inicial, text='label1', font='arial 20', bg='blue')
label2=Label(menu_inicial, text='label2', font='arial 20', bg='red')
label3=Label(menu_inicial, text='label3', font='arial 20', bg='green')

bt1=Button(menu_inicial, text='OK1')
bt2=Button(menu_inicial, text='OK2')
bt3=Button(menu_inicial, text='OK3')

label1.grid(row=0, column=0) #substitui o --> label1.pack()
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)

bt1.grid(row=1, column=0)
bt2.grid(row=1, column=1)
bt3.grid(row=1, column=2)


menu_inicial.mainloop()

