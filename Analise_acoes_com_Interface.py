import tkinter as tk
from tkinter import ttk, messagebox
import yfinance as yf

class AnalisadorAcoes:
    def __init__(self, master):
        self.master = master
        master.title("Analisador de Ações Brasileiras")
        master.geometry("400x350")

        self.frame = ttk.Frame(master, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(self.frame, text="Ticker da Ação:").grid(column=0, row=0, sticky=tk.W, pady=5)
        self.ticker_entry = ttk.Entry(self.frame, width=15)
        self.ticker_entry.grid(column=1, row=0, sticky=tk.W, pady=5)

        ttk.Button(self.frame, text="Analisar", command=self.analisar_acao).grid(column=2, row=0, sticky=tk.W, pady=5)

        self.resultado_text = tk.Text(self.frame, wrap=tk.WORD, width=45, height=15)
        self.resultado_text.grid(column=0, row=1, columnspan=3, pady=10)

    def analisar_acao(self):
        ticker = self.ticker_entry.get().upper()
        if not ticker:
            messagebox.showerror("Erro", "Por favor, insira um ticker válido.")
            return

        ticker_completo = f"{ticker}.SA"
        
        try:
            acao = yf.Ticker(ticker_completo)
            info = acao.info

            preco_atual = info.get('currentPrice', 'N/A')
            dy = info.get('dividendYield', 'N/A')
            if dy != 'N/A':
                dy = dy * 100
            
            p_vp = info.get('priceToBook', 'N/A')
            pl = info.get('trailingPE', 'N/A')
            roe = info.get('returnOnEquity', 'N/A')
            if roe != 'N/A':
                roe = roe * 100

            divida_total = info.get('totalDebt', 'N/A')
            caixa = info.get('totalCash', 'N/A')
            patrimonio_liquido = info.get('totalStockholderEquity', 'N/A')
            
            if divida_total != 'N/A' and caixa != 'N/A' and patrimonio_liquido != 'N/A' and patrimonio_liquido != 0:
                divida_liquida = divida_total - caixa
                dl_pl = divida_liquida / patrimonio_liquido
            else:
                dl_pl = 'N/A'

            resultado = f"Análise para {ticker_completo}:\n\n"
            resultado += f"Preço Atual: R$ {preco_atual:.2f}\n" if preco_atual != 'N/A' else "Preço Atual: N/A\n"
            resultado += f"Dividend Yield (DY): {dy:.2f}%\n" if dy != 'N/A' else "Dividend Yield (DY): N/A\n"
            resultado += f"Preço/Valor Patrimonial (P/VP): {p_vp:.2f}\n" if p_vp != 'N/A' else "Preço/Valor Patrimonial (P/VP): N/A\n"
            resultado += f"Preço/Lucro (P/L): {pl:.2f}\n" if pl != 'N/A' else "Preço/Lucro (P/L): N/A\n"
            resultado += f"Retorno sobre Patrimônio Líquido (ROE): {roe:.2f}%\n" if roe != 'N/A' else "Retorno sobre Patrimônio Líquido (ROE): N/A\n"
            resultado += f"Dívida Líquida / Patrimônio Líquido (DL/PL): {dl_pl:.2f}\n" if dl_pl != 'N/A' else "Dívida Líquida / Patrimônio Líquido (DL/PL): N/A\n"

            self.resultado_text.delete(1.0, tk.END)
            self.resultado_text.insert(tk.END, resultado)

        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível obter os dados para {ticker}. Erro: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AnalisadorAcoes(root)
    root.mainloop()
