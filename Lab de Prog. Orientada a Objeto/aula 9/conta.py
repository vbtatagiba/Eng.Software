from cliente import Cliente


class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite

    def deposita(self,valor):
        self.saldo += valor

    def saca(self,valor):
        if (self.saldo >= valor):
            self.saldo -= valor
            print(f'O seu novo saldo é: {self.saldo}')
        else:
            print('Procura um agiota')

    def transfere_para(self,destino,valor):
        self.saldo -= valor
        destino.saldo += valor

    def extrato(self):
        print(f'O número da conta é: {self.numero} \nO saldo da conta é: {self.saldo}')