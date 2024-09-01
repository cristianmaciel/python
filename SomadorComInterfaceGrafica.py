from os import *
from tkinter import *
def somador():
    try:
        n1 = int(entrada1.get())
        n2 = int(entrada2.get())
        resultado.config(text=f'A Soma de {n1} mais {n2} é {n1+n2}')
    except ValueError:
        resultado.config(text='Erro: Digite apenas números inteiros.')
#configuraçao da janela de interface       
janela=Tk()
janela.title('Somador')
janela.geometry('180x180')

#pede o primeiro valor
texto1 = Label(janela, text='Digite o Primeiro Numero: ')
texto1.grid(column=0, row=0)
#entrada de dados do primeiro valor
entrada1 = Entry(janela)
entrada1.grid(column=0, row=1)

#pede o segundo valor
texto2 = Label(janela, text='Digite o Segundo Numero: ')
texto2.grid(column=0, row=2)
#entrada de dados do segundo valor
entrada2 = Entry(janela)
entrada2.grid(column=0, row=3)

#botao para somar os valores
botao = Button(janela, text='SOMAR', command=somador)
botao.grid(column=0,  row=4)

#texto na interface grafica mostrando o resultado da soma dos dois valores
resultado = Label(janela, text='')
resultado.grid(column=0, row=5)

janela.mainloop() 
