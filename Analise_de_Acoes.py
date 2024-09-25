import yfinance as yf
from os import *

def analisar_acao(ticker):
    # Adiciona o sufixo .SA para ações brasileiras no Yahoo Finance
    ticker_completo = f"{ticker}.SA"
    
    # Obtém os dados da ação
    acao = yf.Ticker(ticker_completo)
    
    # Obtém informações básicas
    info = acao.info
    
    # Coleta os dados desejados
    preco_atual = info.get('currentPrice', 'N/A')
    dy = info.get('dividendYield', 'N/A')
    if dy != 'N/A':
        dy = dy * 100  # Converte para porcentagem
    
    p_vp = info.get('priceToBook', 'N/A')
    pl = info.get('trailingPE', 'N/A')
    roe = info.get('returnOnEquity', 'N/A')
    if roe != 'N/A':
        roe = roe * 100  # Converte para porcentagem
    
    
    # Exibe os resultados
    print(f"Análise para \033[0;33m{ticker_completo.upper()}:\033[m")
    print(f"Preço Atual: \033[0;33mR$ {preco_atual:.2f}\033[m" if preco_atual != 'N/A' else "Preço Atual: N/A")
    print(f"Dividend Yield (DY): \033[0;33m{dy:.2f}%\033[m" if dy != 'N/A' else "Dividend Yield (DY): N/A")
    print(f"Preço/Valor Patrimonial (P/VP): \033[0;33m{p_vp:.2f}\033[m" if p_vp != 'N/A' else "Preço/Valor Patrimonial (P/VP): N/A")
    print(f"Preço/Lucro (P/L): \033[0;33m{pl:.2f}\033[m" if pl != 'N/A' else "Preço/Lucro (P/L): N/A")
    print(f"Retorno sobre Patrimônio Líquido (ROE): \033[0;33m{roe:.2f}%\033[m" if roe != 'N/A' else "Retorno sobre Patrimônio Líquido (ROE): N/A")

# Exemplo de uso
system('clear')
ticker = input("Digite o ticker da ação brasileira (ex: PETR4, VALE3): ")
analisar_acao(ticker)
