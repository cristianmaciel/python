from os import *
system('clear')#limpar o tela  no linux usar "clear" no windows usar "cls"

spam = []# lista vazia criada

#funçao para buscar um nome em uma lista
def busca(spam):
    while True:
        nome = input('Digite o nome que quer procurar: ').strip()
        if not nome:
            print("Nome inválido. Tente novamente.")
            continue
        try:
            indice = spam.index(nome)
            print(f'Nome "{nome}" encontrado no índice {indice}.')
            break
        except ValueError:
            print(f'O nome "{nome}" não foi encontrado na lista.')
            retry = input('Deseja tentar novamente? (s/n): ').strip().lower()
            if retry != 's':
                break

#funçao para remover um nome de uma lista
def remover(spam):
    try:
        nome = input('Digite o nome que quer remover: ').strip()
        if not nome:
            print('O nome não pode ser vazio.')
            return
        # Verificar se o nome está na lista antes de tentar remover
        if nome in spam:
            spam.remove(nome)
            print(f'Nome "{nome}" removido com sucesso da lista!')
        else:
            print(f'O nome "{nome}" não foi encontrado na lista.')
    except AttributeError:
        print('Erro: a variável "spam" não é uma lista válida.')
    except ValueError:
        print(f'Erro: o nome "{nome}" não foi encontrado na lista.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')


#funçao para adicionar um nome em uma lista
def adicionar(spam):
    try:
        nome = input('Digite um novo nome para adicionar na lista: ').strip()
        if not nome:
            print("O nome não pode ser vazio.")
            return
        spam.append(nome)
        print(f'Nome "{nome}" adicionado com sucesso à lista!')
    except AttributeError:
        print('Erro: a variável "spam" não é uma lista válida.')
    except Exception as e:
        print(f'Erro ao adicionar um novo nome à lista: {e}')

#funçao para listar o conteudo de uma lista
def listar(spam):
    if not spam:
        print("A lista está vazia.")
        return
    print("Nomes na lista:")
    for idx, nome in enumerate(spam, start=1):
        print(f"{idx}. {nome}")

#funçao limpar tem 
def limpar():
    system('clear')

#menu de opçoẽs para o usuario escolher
def menu():
    print('********MENU*********')
    print('[1] - LISTAR')
    print('[2] - ADICIONAR')
    print('[3] - BUSCAR')
    print('[4] - REMOVER')
    print('[5] - LIMPAR TELA')
    print('[0] - SAIR')

#função que permite so adicionar numeros inteiros
def LeiaInt(msg):
    while True:
        try:
            m=int(input(msg))
        except:
            print(f'\033[0;31mERRO Digite um Numero Inteiro.\033[m')
        else:
            return m

#programa principal main
while True:
    menu()
    op = LeiaInt('Digite uma Opçao: ')
    if op == 0:
        break
    elif op == 1:
        listar(spam)
    elif op == 2:
        adicionar(spam)
    elif op == 3:
        busca(spam)
    elif op == 4:
        remover(spam)
    elif op == 5:
        limpar()
    else:
        print('Opção Invalida: ')
print('Encerrando o Sistema: Bye Bye.....')
