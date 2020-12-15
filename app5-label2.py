from tkinter import *

menu_inicial = Tk()
menu_inicial.title ('Titulo')

label_1 = Label(menu_inicial, text = 'Este é o label 1.')
label_2 = Label(menu_inicial, text = 'Este é o label 2.')
cmd= Button(menu_inicial, text ='executar')

# pack
cmd.pack()
label_1.pack()
label_2.pack()


menu_inicial.mainloop()