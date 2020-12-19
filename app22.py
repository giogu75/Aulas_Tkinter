from tkinter import *

class MinhaFrame(Frame):
    def __init__(self,parent):
        super().__init__()

        self.text1_text=StringVar
        self.label1_text=StringVar

        # widgets
        self.Label1 = Label (self, textvariable = self.label1_text).grid()
        text1 = Entry(self, textvariable = self.text1_text).grid()
        cmd1 = Button(self, text='Clique', command=self.Executar).grid()

    def Executar(self):
        self.label1_text.set('Ola ' + self.text1_text.get()+'.')
        

root = Tk()
root.geometry('300x150')

frm1=MinhaFrame(root).grid()
frm2=MinhaFrame(root).grid()


root.mainloop()