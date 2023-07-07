import random
palavra=['BANANA','LARANJA','MORANGO','JACA','UVA','PERA']
chave=random.choice(palavra)
while True:
    nome=str(input('Digite a Letra de uma Fruta: ')).upper()[0]
    if chave.upper()[0] == nome:
        print('\033[0;32mAcertou Misseraval hehe\033[m')
        print(f'\033[0;33mA Palavra Secreta é\033[m \033[0;32m{chave}\033[m')
        break
    else:
        print(f'\033[0;31mErrou a palavra nao começa com {nome}\033[m')
    while True:
        status=str(input('Quer continuar S/N? ')).upper()[0]
        if status in 'NS':
            break
        print('Digite S pra Sim ou N pra Não:')
    if status == 'N':
        break
print('\033[0;33mEncerrando o Sistema.......\033[m')

