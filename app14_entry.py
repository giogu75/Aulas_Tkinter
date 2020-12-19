from tkinter import *

root = Tk()

root.title('App')

t1 = Entry(root)
t2 = Entry(root)
t3 = Entry(root)

t1.grid()
t2.grid()
t3.grid()

l1=Label(root)
l2=Label(root)
l3=Label(root)

def executar():
    l1['text']=t1.get()
    l2['text']=t2.get()
    l3['text']=t3.get()

b=Button(root, text ='executar', command=executar)


l1.grid()
l2.grid()
l3.grid()

b.grid()

t1.focus()

root.mainloop()
