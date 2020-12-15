from tkinter import *

menu_inicial = Tk()

menu_inicial.title ('Titulo')

label_1 = Label(menu_inicial, text = 'Este é o label 1.')
label_1.pack()

label_2 = Label(menu_inicial, text = 'Este é o label 2.')
label_2.pack()
    
label_3 = Label(menu_inicial,
                text = 'este eh o label 3.',)
label_3.pack()

cmd= Button(menu_inicial, text ='executar')
cmd.pack()

menu_inicial.mainloop()

