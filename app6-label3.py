
from tkinter import *

menu_inicial=Tk()

menu_inicial.title('titulo')
menu_inicial.geometry('500x300')

label_1 = Label(menu_inicial,
                text = 'este é o label 1',
                bg='yellow',
                fg='#FF0000',
                font='arial',                                       
                )
label_1.pack()

label_2 = Label(menu_inicial,
                text = 'este é o label 2',
                bg='yellow',
                fg='black',
                font='arial 20 bold italic'                                     
                )
label_2.pack()

label_3 = Label(menu_inicial,
                text = 'este é o label 2',
                bg='blue',
                fg='#aaaaaa', #cinza
                font='verdana 42 bold italic'                                     
                )
label_3.pack()


'''
RGB #FF0000
RED
GREEN
BLUE
www.w3schools.com/colors/colors_picker.asp

FONTES:
arial 20 bold italic --) tamanho, negrito, italico
times
verdana
etc
'''

menu_inicial.mainloop()

