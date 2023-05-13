from cliente import Cliente
from historico import Historico


class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico=Historico()

    def deposita(self,valor):
        self.saldo += valor
        self.historico.transacoes.append('Depósito de {}'.format(valor))
        self.historico.transacoes.append('Novo valor é {}'.format(self.saldo))
    
    def saca(self,valor):
        if (self.saldo >= valor):
            self.saldo -= valor
            print(f'O seu novo saldo é: {self.saldo}')
            self.historico.transacoes.append('Saque de {}'.format(valor))
            self.historico.transacoes.append('Novo valor é {}'.format(self.saldo))
        else:
            print('Procura um agiota')

    def transfere_para(self,destino,valor):
        self.saldo -= valor
        destino.saldo += valor
        self.historico.transacoes.append('Transferencia de {}'.format(valor))
        self.historico.transacoes.append('Novo valor é {}'.format(self.saldo))

    def extrato(self):
        print(f'O número da conta é: {self.numero} \nO saldo da conta é: {self.saldo}')