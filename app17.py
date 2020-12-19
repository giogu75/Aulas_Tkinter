from tkinter import *


def mostrarNome():
    vartexto.set('O teu nome é '+textbox1.get())

root = Tk()
root.title('Aplicação')

vartexto = StringVar()

label1 = Label(root, text='O teu nome é:')
textbox1 = Entry(root)
button1 = Button(root, text='Executar', command=mostrarNome)
label2 = Label(root,textvariable=vartexto)

label1.grid()
textbox1.grid()
button1.grid()
label2.grid()


root.mainloop()
