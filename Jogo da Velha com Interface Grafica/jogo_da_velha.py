import tkinter as tk
from tkinter import messagebox

# Função para verificar a vitória
def verificar_vitoria():
    combinacoes = [
        ('top-L', 'top-M', 'top-R'),
        ('mid-L', 'mid-M', 'mid-R'),
        ('low-L', 'low-M', 'low-R'),
        ('top-L', 'mid-L', 'low-L'),
        ('top-M', 'mid-M', 'low-M'),
        ('top-R', 'mid-R', 'low-R'),
        ('top-L', 'mid-M', 'low-R'),
        ('top-R', 'mid-M', 'low-L')
    ]

    for a, b, c in combinacoes:
        if dados[a] == dados[b] == dados[c] and dados[a] != ' ':
            mostrar_mensagem_vitoria(dados[a], [a, b, c])
            return

    if all(dados[c] != ' ' for c in dados):
        mostrar_mensagem_empate()

def mostrar_mensagem_vitoria(vencedor, linhas):
    mensagem = f'Jogador {vencedor} venceu!\nLinhas vencedoras: {linhas}'
    messagebox.showinfo("Vitória!", mensagem)
    resetar_tabuleiro()

def mostrar_mensagem_empate():
    messagebox.showinfo("Empate!", "O jogo empatou!")
    resetar_tabuleiro()

# Função para verificar empate
def verificar_empate():
    return all(dados[c] != ' ' for c in dados)

# Função para alternar jogador
def alternar_jogador():
    global jogador_atual
    jogador_atual = 'X' if jogador_atual == 'O' else 'O'

# Função para atualizar o tabuleiro na interface gráfica
def atualizar_tabuleiro(dados):
    for posicao, valor in dados.items():
        labels[posicao].config(text=valor)

# Função para reiniciar o tabuleiro
def resetar_tabuleiro():
    global jogador_atual
    for posicao in dados:
        dados[posicao] = ' '
    atualizar_tabuleiro(dados)
    jogador_atual = variavel_jogador.get()

# Função para lidar com cliques nas células do tabuleiro
def celula_clicada(posicao):
    if dados[posicao] == ' ':
        dados[posicao] = jogador_atual
        atualizar_tabuleiro(dados)
        verificar_vitoria()
        alternar_jogador()

# Inicializa a janela principal
root = tk.Tk()
root.title("Jogo da Velha")

# Dados do tabuleiro
dados = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' '
}

# Armazena o símbolo do jogador atual
jogador_atual = 'X'

# Define o layout do tabuleiro
labels = {}
for row in range(3):
    for col in range(3):
        posicao = ['top-L', 'top-M', 'top-R', 'mid-L', 'mid-M', 'mid-R', 'low-L', 'low-M', 'low-R'][row * 3 + col]
        labels[posicao] = tk.Label(root, text='', font=('Arial', 40), width=4, height=2, borderwidth=2, relief='solid', anchor='center')
        labels[posicao].grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
        labels[posicao].bind('<Button-1>', lambda e, pos=posicao: celula_clicada(pos))

# Botão para reiniciar o tabuleiro
botao_resetar = tk.Button(root, text="Resetar", command=resetar_tabuleiro)
botao_resetar.grid(row=3, column=0, columnspan=3, pady=10)

# Opções de seleção de jogador (X ou O)
variavel_jogador = tk.StringVar(value='X')

opcao_x = tk.Radiobutton(root, text='X', variable=variavel_jogador, value='X')
opcao_o = tk.Radiobutton(root, text='O', variable=variavel_jogador, value='O')

opcao_x.grid(row=4, column=0, padx=5, pady=5)
opcao_o.grid(row=4, column=1, padx=5, pady=5)

# Atualiza o tabuleiro com os dados iniciais
atualizar_tabuleiro(dados)

# Ajusta o tamanho das colunas e linhas
for i in range(3):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i, weight=1)

# Inicia o loop principal da interface gráfica
root.mainloop()
