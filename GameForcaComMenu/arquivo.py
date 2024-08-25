import os
import time
import random
#entrado de dados para aceitar somento numero inteiros
def leiaInt(msg):
    while True:
        try:
            m=int(input(msg))
        except:
            print('\033[0;31mERRO Digite um numero Inteiro!\033[m')
            time.sleep(2)
            os.system('clear')
            menuJogo()
        else:
            return m

#menu princial do jogo        
def menuPrincipal(msg):
    print('\033[0;34m*\033[m'*35)
    print(f'\033[0;34m{msg}\033[m')
    print('\033[0;34m*\033[m'*35)

#menu do jogo jogos radicais
def menuJogo():
    menuPrincipal('***********Jogos Radicais**********')
    print('\033[0;33m     ----------------------\033[m')
    print('\033[0;36m     |  [1] - Forca       |\033[m')
    print('\033[0;35m     |  [2] - Adivinhação |\033[m')
    print('\033[0;32m     |  [3] - SAIR        |\033[m')
    print('\033[0;33m     ----------------------\033[m')

#carrega a palavra secreta que esta no arquivo de testo pra a variavel palavra secreta
def carrega_palavra_secreta():
    arquivo=open('palavras.txt', 'r')
    palavra=[]
    for linha in arquivo:
        linha=linha.strip()
        palavra.append(linha)
    arquivo.close()
    numero=random.randrange(0, len(palavra))
    palavra_secreta=palavra[numero].upper()
    return palavra_secreta

#Inicializa a palavra secreta
def inicializa_letra_acertada(palavra):
    return (['_'for letra in palavra])

#pede uma letra para verificar se tem na palavra
def pedeChute():
    chute=str(input('\033[0;32mQual a letra? \033[m')).upper()
    chute = chute.strip().upper()
    return chute

def marcar_chute_correto(chute, letras_acertada, palavra_secreta):
    posicao=0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertada[posicao]=letra
        posicao=posicao+1

#mensagem exinbida de voce ganhou o jogo
def msg_Ganhou():
    print('\033[0;33m      Você Ganhou!\033[m')
    print("\033[0;32m      ___________      ")
    print("     '._==_==_=_.'     ")
    print("     .-\\:      /-.    ")
    print("    | (|:.     |) |    ")
    print("     '-|:.     |-'     ")
    print("       \\::.    /      ")
    print("        '::. .'        ")
    print("          ) (          ")
    print("        _.' '._        ")
    print("       '-------'       \033[m")

#mensagem exibida de voce perdeu o jogo
def msg_Perdeu(palavra_secreta):
    print('\033[0;31mVocê Perdeu!\033[m')
    print('\033[0;31mPuxa, você foi enforcado!\033[m')
    print(f'\033[0;33mA palavra era\033[m \033[0;32m{palavra_secreta}\033[m')
    print("\033[0;31m    _______________      \033[m")
    print("\033[0;31m   /               \     \033[m")
    print("\033[0;31m  /                 \    \033[m")
    print("\033[0;31m//                   \/\ \033[m")
    print("\033[0;31m\|\033[m   \033[0;33mXXXX      XXXX  \033[0;31m| / \033[m")
    print("\033[0;31m |\033[m   \033[0;33mXXXX      XXXX  \033[0;31m|/  \033[m")
    print("\033[0;31m |\033[m   \033[0;33mXXX        XXX  \033[0;31m|   \033[m")
    print("\033[0;31m |                   |   \033[m")
    print("\033[0;31m \__      XXX      __/   \033[m")
    print("\033[0;31m    |\    XXX     /|     \033[m")
    print("\033[0;31m    | |          | |     \033[m")
    print("\033[0;31m    | \033[mI I I I I I\033[0;31m  |     \033[m")
    print("\033[0;31m    |  \033[mI I I I I\033[0;31m   |     \033[m")
    print("\033[0;31m    \_           _/      \033[m")
    print("\033[0;31m      \_       _/        \033[m")
    print("\033[0;31m        \_____/          \033[m")


#mensagem de fim de jogo o jogo terminou!
def msg_FinDoJogo():
    print('\033[0;31mFim do Jogo\033[m')
