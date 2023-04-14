class Conta:
    def __init__(self, titular, numero, saldo, limite):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

    def saca(self, valor):
        if self.saldo < valor:
            print('Você não possui saldo suficiente para sacar!')
        else:
            print(f'Valor sacado: R$ {valor}')
            print('-=-'*30)
            self.saldo -= valor

    def deposita(self, valor):
        if valor <= 0:
            print('O valor mínimo para deposito tem que ser maior que R$ 0')
            print('-=-' * 30)
        else:
            print(f'Titular da conta: {self.titular}\n'
                  f'Valor depositado: R$ {valor}')
            print('-=-' * 30)
            self.saldo += valor

    def transfere(self, destino, valor):
        self.saldo -= valor
        destino.saldo += valor
        print(f'Valor transferido para o titular {destino.titular}: R$ {valor}')
        print('-=-' * 30)

    def extrato(self):
        print('EXTRATO DA CONTA')
        print(f'Nome do titular: {self.titular}\n'
              f'Número da conta: {self.numero}\n'
              f'Saldo: R$ {self.saldo}\n'
              f'Limite disponível: R$ {self.limite}')
        print('-=-'*30)