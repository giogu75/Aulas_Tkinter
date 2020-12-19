from tkinter import *

def calcular():
    F=float(textbox1.get())
    C = (F-32)*5/6
    final.set(str(round(C,1)) + ' graus Celsius.')

root = Tk()

root.title('app - converter temperatura')
root.geometry('350x100')

final = StringVar()

label1=Label(root,text='Graus Fahreneit:')
textbox1=Entry(root)
button1=Button(root,text='Calcular', command=calcular)
label_resultado=Label (root,textvariable=final)

label1.grid()
textbox1.grid()
button1.grid(row=1,column=1)
label_resultado.grid()

root.mainloop()
