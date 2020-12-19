from tkinter import *

def mostrarNome():
    nome = textbox_1.get()
    label_final = Label (root, text='O teu nome é: ' + nome)
    label_final.grid()


root = Tk()
root.title("Titulo")
root.geometry('200x200')

label_1 = Label(root, text='Escreva o teu nome:')
textbox_1 = Entry(root)
butto_1 = Button (root, text='Executar', command=mostrarNome)

label_1.grid()
textbox_1.grid()
butto_1.grid()

root.mainloop()