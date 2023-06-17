#Aluno: Victor Bernardo Gomes de Tatagiba
#Matricula:202211960
#P2
class Historico:
    def __init__(self):
        self.transacoes = []

    def registrar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def imprimir_transacoes(self):
        for transacao in self.transacoes:
            print(transacao)