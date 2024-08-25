from arquivo import *
import os
import time
from random import randrange
def jogoForca():
    palavra_secreta=carrega_palavra_secreta()
    letras_acertada=inicializa_letra_acertada(palavra_secreta)
    acertou=False
    enforcou=False
    erros=0
    os.system('clear')
    menuPrincipal('*****Bem Vindo ao Jogo da Forca****')
    print(f'\033[0;33m{letras_acertada}\033[m')
    while (not enforcou and not acertou):
        chute = pedeChute()
        os.system('clear')
        menuPrincipal('*****Bem Vindo ao Jogo da Forca****')
        if chute in palavra_secreta:
            marcar_chute_correto(chute, letras_acertada,palavra_secreta)
        else:
            erros=erros+1
        acertou='_'not in letras_acertada
        enforcou=erros==6
        print(f'\033[0;33m{letras_acertada}\033[m')
    if acertou:
        msg_Ganhou()
    else:
        msg_Perdeu(palavra_secreta)
    time.sleep(5)
    msg_FinDoJogo()
    time.sleep(2)
    os.system('clear')
