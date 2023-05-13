from datetime import datetime

class Historico:
    def __init__(self):
        self.data_de_abertura=datetime.today()
        self.transacoes=[]
    
    def imprimir(self):
        print('Data de Abertura:{}'.format(self.data_de_abertura))
        print('Transações:')
        for t in self.transacoes:
            print('-',t)