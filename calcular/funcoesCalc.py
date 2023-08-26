
from os import *
from time import *
def soma():
    n1,n2= dados()
    total = n1 + n2
    return print(f"{n1}+{n2}={total}")

def divi():
    n1,n2= dados()
    total = n1 / n2
    return print(f"{n1}/{n2}={total}")

def mult():
    n1,n2= dados()
    total = n1 * n2
    return print(f"{n1}*{n2}={total}")

def subt():
    n1,n2= dados()
    total = n1 - n2
    return print(f"{n1}-{n2}={total}")

def erro():
    print("\033[0;31mOpcao Invalida:\033[m")
    sleep(2)
    system("clear")

def LeiaInt(msg):
    while True:
        try:
            m=int(input(msg))
        except:
            print(f'\033[0;31mERRO Digite um Numero Inteiro.\033[m')
            sleep(2)
            system("clear")
        else:
            return m
        
def menu():
    print('----------\033[0;33mCALCULADORA\033[m-----------')
    print("\033[0;33m[1]\033[m - \033[0;32mSoma: \033[m")
    print("\033[0;33m[2]\033[m - \033[0;32mDivisao: \033[m")
    print("\033[0;33m[3]\033[m - \033[0;32mMultiplicaçao: \033[m")
    print("\033[0;33m[4]\033[m - \033[0;32mSubtraçao: \033[m")
    print("\033[0;33m[0]\033[m - \033[0;32mSAIR: \033[m")

def saindo():
    print("\033[0;33mSaindo do sistema!\033[m") 
    sleep(3)

def dados():
    n1=LeiaInt("\033[0;34mDigite o Primeiro valor: \033[m")
    n2=LeiaInt("\033[0;34mDigite o Segundo valor: \033[m")
    return n1,n2
