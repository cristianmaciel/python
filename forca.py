import os
import time
from random import randrange
#Entrado de dados para aceitar somento numero inteiros
def leiaInt(msg):
    while True:
        try:
            m=int(input(msg))
        except:
            print('\033[0;31mERRO Digite um numero Inteiro!\033[m')
        else:
            return m

#menu princial do jogo       
def menuForca(msg):
    print('\033[0;34m*********************************\033[m')
    print('\033[0;34m***{msg}***\033[m')
    print('\033[0;34m*********************************\033[m')
    
#MAIN PROGRAMA PRINCIPAL 
arquivo=open('palavras.txt', 'r')
palavras = []
for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)
arquivo.close()
numero=randrange(0,len(palavras))
palavra_secreta=palavras[numero].upper()
letras_acertada=['_'for letra in palavra_secreta]
acertou=False
enforcou=False
erros=0
os.system('clear')#no linux trocar o "clear" por "cls"
menuForca('Bem vindo ao jogo da Forca')
print(f'\033[0;33m{letras_acertada}\033[m')
while (not enforcou and not acertou):
    chute=str(input('\033[0;32mQual a letra? \033[m')).upper()
    chute = chute.strip().upper()
    os.system('clear')#no linux trocar o "clear" por "cls"
    menuForca('Bem vindo ao jogo da Forca')
    if chute in palavra_secreta:
        posicao=0
        for letra in palavra_secreta:
            if chute == letra:
                letras_acertada[posicao]=letra
            posicao=posicao+1
    else:
        erros=erros+1
    acertou='_'not in letras_acertada
    enforcou=erros==6
    print(f'\033[0;33m{letras_acertada}\033[m')
if acertou:
    print('\033[0;32mVocê Ganhou!\033[m')
else:
    print('\033[0;31mVocê Perdeu!\033[m')
time.sleep(2)
print('\033[0;31mFim do Jogo\033[m')
time.sleep(2)
os.system('clear')#no linux trocar o "clear" por "cls"
