from historico import Historico
class Conta:
    def __init__(self,numero,cliente,saldo,limite=50):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def deposita(self,valor):
        self.saldo = self.saldo+valor
        self.historico.transacoes.append(f'Deposito de {valor}')

    def saca(self, valor):
        if(self.saldo < valor):
            return False
        else:
            self.saldo = self.saldo - valor
            self.historico.transacoes.append(f'Saque de {valor}')
            return True

    def extrato(self):
        print(f'Numero: {self.numero}\nSaldo: {self.saldo}')
        self.historico.transacoes.append(f'Tirou Extrato - Saldo de {self.saldo}')

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if(retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append(f'Transferencia e {valor} para conta {destino.numero}')
            return True


    def mostrar(self):
        print(f'*******DADOS CONTA*******\nNumero: {self.numero} \nSaldo: {self.saldo} \nLimite: {self.limite} ')
