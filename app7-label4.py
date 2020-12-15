from tkinter import *

menu_inicial = Tk()

menu_inicial.title('Titulo')
menu_inicial.geometry('500x300')


label_1 = Label(menu_inicial,
                text='este é label 1',
                font='arial 20',
                bg='red',
                width=20,
                )
label_1.pack()

label_2 = Label(menu_inicial,
                text='este é label 2',
                font='arial 40',
                bg='red',
                width=20,
                )
label_2.pack()


menu_inicial.mainloop()
