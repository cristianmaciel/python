class Cliente:
    def __init__(self,nome,sobrenome,cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def mostrar(self):
        print(f'*******DADOS CLIENTE********\nNome: {self.nome} \nSobrenome: {self.sobrenome} \nCPF: {self.cpf}')
