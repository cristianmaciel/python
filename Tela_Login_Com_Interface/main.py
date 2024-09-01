import json
from tkinter import *

# Função para validar login
def dadosentrada():
    nome = entradauser.get()
    typedPassword = entradasenha.get()
    # Verificar se o nome de usuário existe e se a senha corresponde
    if nome in usuarios and typedPassword == usuarios[nome]:
        resultado.config(text='Acesso concedido\nCarregando o Sistema!...')
        resultado.config(text='Acesso proibido\nDesconectando do Sistema...')

# Carregar os dados do arquivo JSON
with open('usuarios.json', 'r') as file:
    data = json.load(file)
    usuarios = data['usuarios']

# Criação da interface gráfica
janela = Tk()
janela.title('Login')
janela.geometry('290x210')

# Entrando com nome de usuário
textologin = Label(janela, text='Login')
textologin.grid(column=1, row=0)
textouser = Label(janela, text='Usuário:')
textouser.grid(column=0, row=1)
entradauser = Entry(janela)
entradauser.grid(column=1, row=2)

# Entrando com a senha de usuário
textosenha = Label(janela, text='Senha:')
textosenha.grid(column=0, row=4)
entradasenha = Entry(janela, show="*")
entradasenha.grid(column=1, row=5)

# Botão de entrada de login
botao = Button(janela, text='ENTRAR', command=dadosentrada)
botao.grid(column=1, row=6)

# Label para mostrar o resultado do login
resultado = Label(janela, text="")
resultado.grid(column=1, row=7)

janela.mainloop()
