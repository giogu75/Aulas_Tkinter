from tkinter import *

janela = Tk()

bt = Button(janela, width=20, text="ok")
bt.place(x=100, y=100)

lb = Label(janela, text="Fala Galera")
lb.place(x=150, y=150)

# Largura x altura + posição
janela.geometry("300x300+200+200")
janela.mainloop()
