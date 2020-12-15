from tkinter import *

menu_inicial = Tk()

menu_inicial.title('Titulo')
menu_inicial.geometry('500x300+1000+300')


label_1 = Label(menu_inicial,
                text='Giovani Gualdi\nGiovani\nGi',
                font='arial 15',
                bd=2,
                relief='solid',
                padx=50,
                pady=50,
                justify=RIGHT
    )
label_1.pack()

label_1 = Label(menu_inicial,
                text='Giovani Gualdi\nGiovani\nGi',
                font='arial 15',
                bd=2,
                relief='solid',
                width=30,
                height=5,
                justify=LEFT,
                anchor=E
    )
label_1.pack()

menu_inicial.mainloop()