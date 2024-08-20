from tkinter import *
from os import system

# Cores
cor1 = "#3b3b3b"  # Preta
cor2 = "#feffff"  # Branca
cor3 = "#38576b"  # Azul
cor4 = "#ECEFF1"  # Cinza
cor5 = "#FFAB40"  # Laranja

# Limpar a tela do terminal (modifique para 'cls' no Windows)
system('clear')
print('Janela da calculadora está sendo exibida na tela gráfica')

# Criação da janela principal da calculadora
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)

# Criação da Tela
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

todos_valores = ''
valor_texto = StringVar()

# Funções
def entrar_valores(evento):
    global todos_valores
    todos_valores += str(evento)
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    try:
        resultado = eval(todos_valores)
        valor_texto.set(str(resultado))
    except Exception as e:
        valor_texto.set("Erro")
        todos_valores = ''

def limpa_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

# Criação do Label para exibir valores
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 16'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

# Criação dos botões
# Linha 1
Button(frame_corpo, command=limpa_tela, text="C", width=8, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=0, y=0)
Button(frame_corpo, command=lambda: entrar_valores('%'), text="%", width=4, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=118, y=0)
Button(frame_corpo, command=lambda: entrar_valores('/'), text="/", width=4, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=177, y=0)

# Linha 2
Button(frame_corpo, command=lambda: entrar_valores('7'), text="7", width=4, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=0, y=52)
Button(frame_corpo, command=lambda: entrar_valores('8'), text="8", width=4, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=59, y=52)
Button(frame_corpo, command=lambda: entrar_valores('9'), text="9", width=4, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=118, y=52)
Button(frame_corpo, command=lambda: entrar_valores('*'), text="*", width=4, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=177, y=52)

# Linha 3
Button(frame_corpo, command=lambda: entrar_valores('4'), text="4", width=4, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=0, y=104)
Button(frame_corpo, command=lambda: entrar_valores('5'), text="5", width=4, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=59, y=104)
Button(frame_corpo, command=lambda: entrar_valores('6'), text="6", width=4, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=118, y=104)
Button(frame_corpo, command=lambda: entrar_valores('-'), text="-", width=4, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=177, y=104)

# Linha 4
Button(frame_corpo, command=lambda: entrar_valores('1'), text="1", width=4, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=0, y=156)
Button(frame_corpo, command=lambda: entrar_valores('2'), text="2", width=4, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=59, y=156)
Button(frame_corpo, command=lambda: entrar_valores('3'), text="3", width=4, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=118, y=156)
Button(frame_corpo, command=lambda: entrar_valores('+'), text="+", width=4, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=177, y=156)

# Linha 5
Button(frame_corpo, command=lambda: entrar_valores('0'), text="0", width=8, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=0, y=208)
Button(frame_corpo, command=lambda: entrar_valores('.'), text=".", width=4, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=118, y=208)
Button(frame_corpo, command=calcular, text="=", width=4, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE).place(x=177, y=208)

janela.mainloop()
