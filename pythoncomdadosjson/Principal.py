from funcoes import *
from os import *
from time import *
while True:
    system('clear')
    menu()
    op = LeiaInt('Escolha uma Opção: ')
    if op == 0:
        break
    else:
        if op == 1:
            cadastrar()
        elif op == 2:
            listar()
            sleep(4)
        elif op == 3:
            excluir()
            sleep(4)
        else:
            print('\033[0;32mErro Opçao Invalida!\033[m')
print('\033[0;33mSaindo do Sistema.......\033[m')
