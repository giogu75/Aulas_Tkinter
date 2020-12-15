from tkinter import *

menu_inicial = Tk()

menu_inicial.title('Titulo')
menu_inicial.geometry('500x900')

border = 20     #define a largura da borda/quadro

label_1 = Label(menu_inicial,
                text='este é label 1\nesteé label2\n''',
                font='arial 20',
                bg='red',

                bd=border, # faz quadro em volta texto
                relief='solid' #pode ainda ser de outros tipos --> groove, flat, raised, sunken, ridge
                )
label_1.pack()

label_1 = Label(menu_inicial,
                text='este é label 1\nesteé label2\n''',
                font='arial 20',
                bg='red',

                bd=border, # faz quadro em volta texto
                relief='groove' #pode ainda ser de outros tipos --> groove, flat, raised, sunken, ridge
                )
label_1.pack()

label_1 = Label(menu_inicial,
                text='este é label 1\nesteé label2\n''',
                font='arial 20',
                bg='green',

                bd=border, # faz quadro em volta texto
                relief='flat' #pode ainda ser de outros tipos --> groove, flat, raised, sunken, ridge
                )
label_1.pack()

label_1 = Label(menu_inicial,
                text='este é label 1\nesteé label2\n''',
                font='arial 20',
                bg='white',

                bd=border, # faz quadro em volta texto
                relief='raised' #pode ainda ser de outros tipos --> groove, flat, raised, sunken, ridge
                )
label_1.pack()

label_1 = Label(menu_inicial,
                text='este é label 1\nesteé label2\n''',
                font='arial 20',
                bg='yellow',

                bd=border, # faz quadro em volta texto
                relief='sunken' #pode ainda ser de outros tipos --> groove, flat, raised, sunken, ridge
                )
label_1.pack()

label_1 = Label(menu_inicial,
                text='este é label 1\nesteé label2\n''',
                font='arial 20',
                bg='blue',

                bd=border, # faz quadro em volta texto
                relief='ridge' #pode ainda ser de outros tipos --> groove, flat, raised, sunken, ridge
                )
label_1.pack()




# label_2 = Label(menu_inicial,
#                 text='este é label 1\n\neste é label2',
#                 font='arial 20',
#                 bg='red',
#                 width=20,
#                 )
# label_2.pack()




menu_inicial.mainloop()