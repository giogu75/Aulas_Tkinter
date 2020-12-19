from tkinter import *


root = Tk()
root.title("Titulo")


frame_nome = Frame (root)
frame_morada = Frame (root)

label_nome = Frame (frame_nome, text = 'Nome:')
label_apelido = Frame (frame_nome, text = 'Apelido:')
label_rua = Frame (frame_morada, text = 'Rua:')
label_cidade = Frame (frame_morada, text = 'Cidade:')

text_nome = Entry (frame_nome)
text_apelido = Entry (frame_nome)
text_rua = Entry (frame_morada)
text_cidade = Entry (frame_morada)

cmd_salvar = Button(root, text='Salvar')


label_nome.grid(row=0, column=0)
label_apelido.grid(row=1, column=0)
text_name.grid(row=0, column=1)
text_apelido.grid(row=1, column=1)


label_rua.grid(row=1, column=0)
label_cidade.grid(row=10, column=0)
text_rua.grid(row=0, column=1)
text_cidade.grid(row=1, column=1)

cmd_salvar.grid()

root.mainloop()