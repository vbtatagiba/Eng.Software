#Aluno: Victor Bernardo Gomes de Tatagiba
#Matricula:202211960
#P2
from random import randint
from conta import Conta
class Cliente:
    contador_id = 1

    def __init__(self,nome,banco,idade,sexo):
        self.id = Cliente.contador_id
        Cliente.contador_id += 1
        self.nome = nome
        self.banco = banco
        self.idade = idade
        self.sexo = sexo
        self.conta = Conta(Cliente.gerar_numero_conta(), 0)

    @classmethod
    def gerar_numero_conta(cls):
        return f"{cls.contador_id}-{randint(1000, 9999)}"

    def exibir_cliente(self):
        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f'Idade: {self.idade}')
        print(f'Sexo: {self.sexo}')
        print(f"Número da conta: {self.conta.numero_conta}")
        print(f"Saldo da conta: {self.conta.saldo}")
        self.banco.imprimir_nome_banco()

