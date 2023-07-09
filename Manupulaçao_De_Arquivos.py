#Conferir se o arquivo existe
def arquivoExiste(nome):
    try:
        a=open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


#Criar o arquivo
def criarArquivo(nome):
    try:
        a=open(nome, 'wt+')
        a.close()
    except:
        print('\033[0;31mHouve uma Erro na Criaçao do arquivo\033[m')
    else:
        print(f'\033[0;32mArquivo {nome} criado com sucesso\033[m')


#Ler um arquivo Existente
def lerArquivo(nome):
    try:
        a=open(nome, 'rt')
    except:
        print(f'\033[0;31mErro ao ler o Arquivo! \033[m')
    else:
        cabecalho('DADOS PREENCHIDOS')
        for linha in a:
            dados=linha.split(';')
            dados[1]=dados[1].replace('\n','')
            print(f'{dados[0]:<30}{dados[1]:>3}')
    finally:
        a.close()


#Cadastrar uma Novo dados no Arquivo
def cadastrar(arq, dados1='desconhecido', dados2=0):
    try:
        a=open(arq, 'at')
    except:
        print(f'\033[0;31mHouve uma ERRO na abertura do arquivo! \033[m')
    else:
        try:
            a.write(f'{dados1};{dados2}\n')
        except:
            print(f'\033[0;31mHouve um ERRO na hora de escrever o arquivo!\033[m')
        else:
            print(f'\033[0;32mNovo registo de {dados1} adicionado com Sucesso\033[m')
            a.close()

#Excluir dados cadastrado no arquivo
def excluirDado(arq, dado_pesquisado):
    try:
        with open(arq, 'r') as arquivo:
            linhas = arquivo.readlines()

        encontrado = False

        with open(arq, 'w') as arquivo:
            for linha in linhas:
                if dado_pesquisado not in linha:
                    arquivo.write(linha)
                else:
                    encontrado = True

        if encontrado:
            print(f'\033[0;32mO dado "{dado_pesquisado}" foi excluído com sucesso.\033[m')
        else:
            print(f'\033[0;33mO dado "{dado_pesquisado}" não foi encontrado para exclusão.\033[m')

    except FileNotFoundError:
        print(f'\033[0;31mO arquivo "{arq}" não foi encontrado.\033[m')


#linha do Menu
def linha(tam=42):
    return ('-'*tam)

#Cabeçalho do sistema
def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

#Menu do Sistema
def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f'\033[0;33m{c}\033[m - \033[0;34m{item}\033[m')
        c=c+1
    print(linha())
    opc=leiaInt('Escolha uma Opção: ')
    return opc

#Entrada só com valores inteiro
def leiaInt(msg):
    while True:
        try:
            m=int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO Digite uma valor Inteiro!\033[m')
            continue
        else:
            return m
    
    
