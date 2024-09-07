from os import system
# Limpar a tela no início
system('clear')

# Função para ler o conteúdo do arquivo
def ler():
    try:
        with open('arquivo.txt', 'r') as arquivo:  # Modo leitura do arquivo
            conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo
            return conteudo
    except FileNotFoundError:
        return "Arquivo ainda não existe."

# Função para adicionar conteúdo em um arquivo
def adicionar(n):
    with open('arquivo.txt', 'a') as arquivo:  # Modo append para adicionar ao final
        arquivo.write(f'{n}\n')  # Adiciona o valor em uma nova linha

# Loop principal para adicionar entradas
while True:
    nome = input('Digite o que quer adicionar (ou 0 para sair): ')
    if nome == '0':  # Condição de parada
        break
    else:
        adicionar(nome)

# Exibe o conteúdo do arquivo ao final
print("\nConteúdo do arquivo:")
print(ler())
