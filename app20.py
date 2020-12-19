from tkinter import *

class MinhaFrame(Frame):
    def __init__(self, parent):
        super().__init__()
        self['height'] = 300
        self['width'] = 300
        self['bg'] = 'green'
      

root = Tk()
root.title("Titulo")
root.geometry('500x500')

frm1 = MinhaFrame(root)
frm1.grid()

root.mainloop() 