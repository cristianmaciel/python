import requests
from tkinter import *
from os import *
#funçao pegar cotaçoa do dolar do euro e do bitcoin
def pegar_cotacoes():
    system('clear')
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dolar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    print(texto)

    texto_cotacoes["text"] = texto

#janela da interface grafica do programa
janela = Tk()
janela.title('Cotação Atual')

texto_orientacao = Label(janela, text='CLIQUE PARA CONSULTAR COTAÇAO' )
texto_orientacao.grid(column=0, row=0, padx=10, pady= 10)

botao = Button(janela, text="Buscar", command=pegar_cotacoes,)
botao.grid(column=0, row=1, padx=10, pady= 10)

texto_cotacoes = Label(janela, text='')
texto_cotacoes.grid(column=0, row=3, padx=10, pady= 10)

janela.mainloop()
