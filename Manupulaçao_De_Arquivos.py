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
        print('---------DADOS PREENCHIDOS--------')
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
    