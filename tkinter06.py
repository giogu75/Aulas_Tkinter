from tkinter import *


def bt_click():
  lb["text"]="Fala galera dos inferno!"


janela = Tk()
janela.geometry("300x300")


bt = Button(janela, width = 20, text = "Clique", command=bt_click)
bt.place(x=100,y=140)


lb = Label(janela, text="")
lb.place(x=200, y=200)


janela.mainloop()