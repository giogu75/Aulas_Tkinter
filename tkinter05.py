from tkinter import *

janela = Tk()
janela.geometry("300x300")

bt = Button(janela, width=20, text="Clique")
bt.place(x=100, y=140)

lb = Label(janela, text="ola")
lb.place(x=100, y=100)

janela.mainloop()
