from arquivo import *
from forca import *
import os
while True:
    os.system('clear')
    menuJogo()
    op=leiaInt('     \033[0;33mEscolha uma Opção! \033[m')
    if op == 1:
        jogoForca()
    elif op == 2:
        pass
    elif op == 3:
        break
    else:
        print('     \033[0;31mOpçao Invalida!!\033[m')
        time.sleep(2)
print('Desligando o Playstation !..........')
