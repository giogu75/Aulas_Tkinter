from tkinter import *                           # importa o tkinter

menu_inicial =  Tk()                            # CRIAR JANELA
menu_inicial.title('Primeiro App')              # TITULO DA JANELA
menu_inicial['bg'] = 'yellow'                     # cor de fundo da janela

# dimensões da janela
largura = 1000
altura = 800

# resolução do sitema
largura_screen = menu_inicial.winfo_screenwidth()
altura_screen = menu_inicial.winfo_screenheight()

print (largura_screen, altura_screen)

# posição da janela
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

# definir a geometry
menu_inicial.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))        # tamanho inicial janela
menu_inicial.iconbitmap ('icon2.ico')           # trocar icone da janela
menu_inicial.resizable(False, False)










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


