from conta import Conta
from cliente import Cliente
from os import *
system('clear')
cliente01 = Cliente('Lucas','Marolo','123.654.789-12')
conta01 = Conta(7790569,cliente01,100)
cliente02 = Cliente('Gabriele','Marolo','951.357.852-89')
conta02 = Conta(2107562,cliente02,12000)
conta01.deposita(50)
conta01.extrato()
print('Sacando o valor')
conta01.saca(150)
conta01.extrato()
print('trasnferindo valor')
conta02.transfere_para(conta01,2000)
conta01.extrato()
print('****HISTORICO*****')
conta01.historico.imprime()
