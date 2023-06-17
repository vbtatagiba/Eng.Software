#Aluno: Victor Bernardo Gomes de Tatagiba
#Matricula:202211960
#P2
class Banco:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco
        self.clientes = []

    def imprimir_nome_banco(self):
        print(f"Nome do banco: {self.nome_banco}")

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def listar_clientes(self):
        for cliente in self.clientes:
            cliente.exibir_cliente()