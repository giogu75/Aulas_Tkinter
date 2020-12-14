import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.tela()
        self.create_widgets()

    def tela(self):
        self.master.title("EXEMPLO NO TKINTER")
        self.master.configure(background='#708090')
        self.master.geometry("850x550")
        self.master.resizable(True, True)
        self.master.maxsize(width=880, height=680)
        self.master.minsize(width=550, height=380)

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)\nseu merda"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")


    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()