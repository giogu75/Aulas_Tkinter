from tkinter import *                           # importa o tkinter

menu_inicial =  Tk()                            # CRIAR JANELA
menu_inicial.title('Primeiro App')              # TITULO DA JANELA
menu_inicial['bg'] = 'blue'                     # cor de fundo da janela
menu_inicial.geometry('500x250+600+200')        # tamanho inicial janela
menu_inicial.resizable(1, 1)                    # pode alterar tamanho janela
menu_inicial.minsize(500, 250)                  # tamanho mínimo
menu_inicial.maxsize(700, 400)                  # tamanho maximo
menu_inicial.iconbitmap ('icon2.ico')           # trocar icone da janela

def cmd_Click(mensagem):                             # define o comando do botão - ver entre parenteses
   print (mensagem)

def cmd_Click2():                                # define o comando do botão
   print ('mensagem2')

cmd = Button(menu_inicial, text = 'Executar', command =  lambda: cmd_Click('Outra mensagem'))        # criar botão - parametros
cmd.pack()                                      # faz aparecer na tela

cmd = Button(menu_inicial, text = 'Clicar', command = cmd_Click2)        # criar botão - parametros
cmd.pack()   

cmd = Button(menu_inicial, text = 'OK', command = lambda: print('OK'))
cmd.pack()                                      # faz aparecer na tela



menu_inicial.mainloop()                         # cria loop para não fechar janela

