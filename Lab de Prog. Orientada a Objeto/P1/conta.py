class Conta():
    def __init__(self,numero,nome,saldo,credito):
        self.nconta= numero
        self.titular= nome
        self.saldo=saldo
        self.limite=credito
    
    def saca(self,valor):
        if self.saldo<valor:
            print('Saldo insuficiente!')
        else:
            self.saldo-= valor
            print(f'O Valor de {valor} foi Sacado na conta {self.titular} o novo saldo é {self.saldo}')
    
    def depositar(self,valor):
        if self.saldo<valor:
            print('Saldo insuficiente!')
        else:
            self.saldo+= valor
            print(f'O Valor de {valor} foi depositado na conta de {self.titular} o novo saldo é {self.saldo}')

    def extrato(self,numero):
        if numero in self.nconta:
            print('Extrato da conta')
            print(f'o extrato da conta {self.nconta} com o titular  {self.titular} é R${self.saldo} e {self.limite} reais de limite')
            print('-='*30)
        else:
            print('Conta não encontrada tente novamente')

    def tranferencia(self,saldo,valor):
        if valor>self.saldo:
            print('Saldo insuficiente')
        else:
            opc=input('Insira qual a conta que deseja enviar')
            if opc=='1':
                saldo2=(100)
            elif opc=='2':
                saldo2=(500)
            else:
                print('Conta nao encontrada')
            saldo-= valor
            saldo2+=valor 
            print(f'O novo Saldo da sua conta é R${saldo}')
            print(f'O novo Saldo da outra conta é R${saldo2}')
