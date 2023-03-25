class Conta:
    def __init__(self,numero,titular,saldo,limite):
        self.numero= numero
        self.titular= titular
        self.saldo= saldo
        self.limite= limite

    def deposito(self,valor):
        self.saldo += valor
    
    def saca(self,valor):
        if (self.saldo >= valor):
            self.saldo -= valor
        else:
            print('Saldo insuficiente')
            
    
    def extrato(self):
        Conta('123-4','Victor',10000.0,50000.0)
        print(f'Numero da conta:',self.numero ,'Nome do titular:', self.titular,'O saldo da conta é:',self.saldo,'O Limite da conta é',self.limite)

conta1= Conta('123-4','Victor',10000.0,50000.0)

conta1.saca(5000)
print(conta1.saldo)
conta1.deposito(5000)
print(conta1.saldo)

conta1.extrato()

#Encapsulamento -> Só acessar para trocar a informação aqui que necessario