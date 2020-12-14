from tkinter import *


def bt_click():
  lb["text"] +=1


janela = Tk()
janela.geometry("300x300")


bt = Button(janela, width = 20, text = "Clique", command=bt_click)
bt.place(x=100,y=140)


lb = Label(janela, text=0 )
lb.place(x=180, y=100)


janela.mainloop()