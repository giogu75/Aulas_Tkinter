from tkinter import *

root = Tk()
root.title('LISTBOX')
root.geometry('300x200')

lista = Listbox(root)
#inserir um item de cada vez
lista.insert(END, 'Primeiro item da lista')
lista.insert(END, 'Segundo item da lista')
lista.pack()

root.mainloop()
