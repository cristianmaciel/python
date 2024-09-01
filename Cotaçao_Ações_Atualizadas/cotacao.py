import yfinance as yf
from tkinter import *
import json
from datetime import datetime

# Lista de tickers das ações
tickers = ['BBAS3.SA', 'CMIG4.SA', 'ITSA4.SA', 'KLBN4.SA', 'MXRF11.SA', 'PETR4.SA', 'SANB4.SA', 'TAEE4.SA', 'UNIP6.SA', 'VALE3.SA']

# Função para obter o preço atual de uma ação
def obter_preco_atual(ticker):
    acao = yf.Ticker(ticker)
    preco_atual = acao.history(period='1d')['Close'].iloc[-1]
    return preco_atual

# Função para salvar os preços em um arquivo JSON
def salvar_em_json(dados):
    try:
        with open('precos_acoes.json', 'w') as f:
            json.dump(dados, f, indent=4)
        print("Dados salvos em precos_acoes.json")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

# Itera sobre a lista de tickers e atualiza a interface gráfica com o preço atual
def mostrapreco():
    texto_precos = ""
    dados = {}
    
    for ticker in tickers:
        preco_atual = obter_preco_atual(ticker)
        texto_precos += f"° {ticker}: R$ {preco_atual:.2f}\n"
        dados[ticker] = {
            'preco_atual': preco_atual,
            'data_atualizacao': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    
    mostrar.config(text=texto_precos)
    salvar_em_json(dados)

janela = Tk()
janela.title('Cotações Ações')

texto = Label(janela, text='COTAÇÃO ATUAL')
texto.grid(column=1, row=0)
botao = Button(janela, text='Buscar', command=mostrapreco)
botao.grid(column=1, row=1)

mostrar = Label(janela, text='', justify=LEFT)
mostrar.grid(column=1, row=2)

janela.mainloop()
