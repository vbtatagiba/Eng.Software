#Aluno: Victor Bernardo Gomes de Tatagiba
#Matricula:202211960
#P2
from historico import Historico
class Conta:
    def __init__(self, numero_conta, saldo=0):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.historico = Historico()

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.registrar_transacao(f"Saque: {valor}")
            print(f'Deposito Realizado Com Sucesso seu novo saldo é de {self.saldo}')

        else:
            print("Saldo insuficiente.")

    def deposito(self, valor):
        self.saldo += valor
        self.historico.registrar_transacao(f"Depósito: {valor}")
        print(f'Deposito Realizado Com Sucesso seu novo saldo é de {self.saldo}')

    def transfere_para(self, outra_conta, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            outra_conta.saldo += valor
            self.historico.registrar_transacao(f"Transferência para conta {outra_conta.numero_conta}: {valor}")
            outra_conta.historico.registrar_transacao(f"Transferência recebida da conta {self.numero_conta}: {valor}")
        else:
            print("Saldo insuficiente.")

    def extrato(self):
        print(f"Número da conta: {self.numero_conta}")
        print(f"Saldo: {self.saldo}")
        print("Histórico de transações:")
        self.historico.imprimir_transacoes()

