import mysql.connector
from os import *

# Conectando ao MySQL (sem especificar o banco de dados)
meubd = mysql.connector.connect(
    host='localhost',
    user='user',
    password='123456'
)
#menu de opções para interagir com o banco e dados
def menu():
    print('INTERAGIR COM O BANCO DE DADOS')
    print('[1] - Listar Banco de dados:')
    print('[2] - Criar Banco de dados:')
    print('[3] - Deletar Bando de Dados')

#lista os bancos de dados ja criados
def listardb():
    cursor = meubd.cursor()
    try:
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()  # Retorna uma lista de tuplas

        print("Bancos de dados existentes:")
        for db in databases:
            print(f"\033[0;33m- {db[0]}\033[m")
    except mysql.connector.Error as err:
        print(f'\033[0;31mErro ao listar banco de dados: {err}\033[m')
    finally:
        cursor.close()

# Criando um novo banco de dados
def criarbd():
    cursor = meubd.cursor()
    nome = str(input('\033[0;32mQual o nome do Banco de dados que quer criar? \033[m'))
    try:
        cursor.execute(f"CREATE DATABASE {nome}")
        print(f"\033[0;32mBanco de dados \033[m'{nome}' \033[0;32mcriado.\033[m")
    except mysql.connector.Error as err:
        print(f'\033[0;31mErro ao criar bando de dados: {err}\033[m')
    finally:
        cursor.close()

# Deletando o banco de dados
def deletarbd():
    cursor = meubd.cursor()
    nome = str(input('\033[0;31mQual o nome do Banco de dados que quer DELETAR? \033[m'))
    try:
        cursor.execute(f"DROP DATABASE {nome}")
        print(f"\033[0;31mBanco de dados\033[m '{nome}'\033[0;31m deletado.\033[m")
    except mysql.connector.Error as err:
        print(f'\033[0;31mErro ao deletar bando de dados :{err}\033[m')
    finally:
        cursor.close()

#funçao para so aceitar numeros inteiros
def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except ValueError: 
            print('\033[0;31mErro Digite um Numero Inteiro: \033[m')
        else:
            return n
        
#Programa principal o main       
system('clear')
while True:
    menu()
    op = leiaint('Escolha uma Opçao:')
    if op == 1:
        listardb()
    elif op == 2:
        criarbd()
    elif op == 3:
        deletarbd()
    else:
        print('opçao invalida! finalizando consulta')
        break
print('Fechando o Sistema')
meubd.close()
