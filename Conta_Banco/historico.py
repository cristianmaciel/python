import datetime
class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print(f'Data de Abertura: {self.data_abertura}')
        print('Transaçoes: ')
        for t in self.transacoes:
            print(f'- {t}')
