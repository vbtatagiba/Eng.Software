class Cliente:
    def __init__(self,nome,sobrenome,cpf):
        self.nome=nome
        self.sobrenome=sobrenome
        self.cpf=cpf
    
    def exibir(self):
        print(f'O nome do Cliente é: {self.nome} {self.sobrenome} \n'
              f'O CPF do cliente é : {self.cpf}')

    