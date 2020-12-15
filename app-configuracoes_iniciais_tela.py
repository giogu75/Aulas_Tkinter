
from tkinter import *                       # importa o tkinter

menu_inicial =  Tk()                        # CRIAR JANELA
menu_inicial.title('Primeiro App')          # TITULO DA JANELA
menu_inicial.geometry('500x250+600+200')    # tamanho inicial janela
#menu_inicial.resizable(False, False)       # não pode alterar tamanho janela
menu_inicial.resizable(1, 1)                # pode alterar tamanho janela
menu_inicial.minsize(500, 250)              # tamanho mínimo
menu_inicial.maxsize(700, 400)              # tamanho maximo
#menu_inicial.state('zoomed')               # inicial maximizada
#menu_inicial.state('iconic')               # inicial minimizada
menu_inicial.iconbitmap ('icon2.ico')       # trocar icone da janela

menu_inicial.mainloop()                     # cria loop para não fechar janela

