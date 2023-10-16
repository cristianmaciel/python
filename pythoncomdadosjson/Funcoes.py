import json
import os
dadosentra = []

#menu de opçaoes de escolha
def menu():
    print("**** MENU DE OPÇÕES ****")
    print('[1] - ADICIONAR DADOS')
    print('[2] - LER DADOS')
    print('[3] - EXCLUIR')
    print('[0] - SAIR')
    
#funçao que so permite adicionar numeros inteiros
def LeiaInt(msg):
    while True:
        try:
            m=int(input(msg))
        except:
            print(f'\033[0;31mERRO Digite um Numero Inteiro.\033[m')
        else:
            return m

#funcao que verifica se ja existe o arquivo json
def verificar_arquivo_json():
    return os.path.isfile("dados.json")

#funçao que salva as alteraçoes do arquivo json
def salvar_dados(dados):
    object_json = json.dumps(dados, indent=2)
    with open("dados.json", "w", encoding="utf-8") as meus_dados:
        meus_dados.write(object_json)

#funçao que carrega o conteudo do arquivo json
def carregar_dados():
    if verificar_arquivo_json():
        with open("dados.json", encoding="utf-8") as meus_dados:
            return json.load(meus_dados)
    else:
        return []

#funçao que cadastra dados em um dicionario e salva no arquivo json
def cadastrar():
    with open("dados.json",encoding= "utf-8" ) as meus_dados:
        dados = json.load(meus_dados)
    nome = str(input('Digite o Nome: ')).upper()
    idade = LeiaInt('Digite a idade: ')
    empresa = str(input('Nome da Empresa: ')).upper()
    id = 1 if not dados else max(dados, key=lambda x: x["id"])["id"] + 1
    dadosentra = carregar_dados()
    dadospessoais = {'id':id,'nome': nome,'idade': idade,'empresa':empresa}
    dadosentra.append(dadospessoais)
    salvar_dados(dadosentra)
    
#funcao que lista os dados do arquivo json de forma organizada 
def listar():
    with open("dados.json",encoding= "utf-8" ) as meus_dados:
        dados = json.load(meus_dados)
        for i in dados:
            print("\033[0;33m****Dados Pessoais****\033[m")
            print(f'Id: {i["id"]}\nNome:{i["nome"]}\nIdade: {i["idade"]}\nEmpresa: {i["empresa"]}')
            print("\033[0;33m**********************\033[m")

#funçao que exclui dados do arquivo json
def excluir():
    with open("dados.json",encoding= "utf-8" ) as meus_dados:
        dados = json.load(meus_dados)
        for i in dados:
            print(f'\033[0;31mId:{i["id"]} Nome:{i["nome"]}\033[m')
    try:
        id = LeiaInt('Digite o ID do registro a ser excluído: ')
        for i in dados:
            if i['id'] == id:
                dados.remove(i)
                object_json = json.dumps(dados, indent=2 )
                with open("dados.json", "w", encoding = "utf-8") as meus_dados:
                    meus_dados.write(object_json)
                print('Registro excluído com sucesso!')
                break
        else:
            print('Registro não encontrado!')
    except ValueError:
        print('Erro! Digite um número inteiro válido.')
