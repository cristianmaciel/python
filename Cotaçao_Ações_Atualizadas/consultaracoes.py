import json
from os import system

def listar():
    # Carrega os dados do arquivo JSON
    with open("precos_acoes.json", encoding="utf-8") as meus_dados:
        dados = json.load(meus_dados)
        print("\033[0;33m**** Cotações de Ações ****\033[m")
        
        # Itera sobre cada empresa e seus dados
        for nome_empresa, info in dados.items():
            print(f'Empresa: {nome_empresa}')
            # Formatação correta do preço para duas casas decimais
            print(f'Preço: {info["preco_atual"]:.2f}')
            print("\033[0;33m*************************\033[m")

# Loop principal do programa
system('clear')
while True:
    print("**** MENU DE OPÇÕES ****")
    print('[1] - VER COTAÇÃO ')
    print('[0] - SAIR ')
    try:
        op = int(input('Escolha uma Opção: '))
    except ValueError:
        print('\033[0;31mERRO: Digite um Número Inteiro.\033[m')
        continue 
    if op == 0:
        break
    elif op == 1:
        listar()
    else:
        print('\033[0;31mErro: Opção Inválida!\033[m')
print('\033[0;33mSaindo do Sistema.......\033[m')
