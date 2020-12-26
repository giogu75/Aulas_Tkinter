from tkinter import *

root = Tk()
root.geometry('300x300')
lista = Listbox(root)
lista.pack()

nomes = ['joao', 'ana', 'carlos']
for nome in nomes:
    lista.insert(END, nome)

def executar():
    print(lista.get(ACTIVE))
           
cmd = Button (root, text='Clique', command=executar).pack()

root.mainloop()

