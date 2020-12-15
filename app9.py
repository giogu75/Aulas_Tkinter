from tkinter import *

menu_inicial = Tk()

menu_inicial.title('Titulo')
menu_inicial.geometry('500x300+1000+300')


label_1 = Label(menu_inicial,
                text='0123456789',
                font='arial 20',
                bd=2,
                relief='solid',
                width=20,
                height=4,
                anchor=NE)  # N-> norte S-> sul E-> dir; W-> esq e CENTER
                            # NE; NW; SE e SW
label_1.pack()

menu_inicial.mainloop()
