from tkinter import *

root = Tk()

root.geometry('300x200')


#slide = Scale(root, from_=0, to=100)
slide = Scale(root, 
    from_=0, 
    to=100, 
    orient=HORIZONTAL,
    resolution=0.5)
slide.pack()

def vervalor():
    print(slide.get())
    

cmd = Button(root, text='Ver Valor', command=vervalor)
cmd.pack()

root.mainloop()