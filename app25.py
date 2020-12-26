from tkinter import *

root=Tk()

img = PhotoImage(file='imagem.jpg')

label_imagem = Label(root, image=img).pack()

root.mainloop()

