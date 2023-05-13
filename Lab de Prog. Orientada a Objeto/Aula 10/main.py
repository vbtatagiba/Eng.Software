from conta import *
# from cliente import *
from historico import *
if __name__ == '__main__':
    cliente1=Cliente('Fabricio','Dias','000.000.000-00')
    cliente2=Cliente('Fabricio','Souza','000.000.000-00')
    cliente3=Cliente('Victor','Bernardo','000.000.000-00')
    cliente4=Cliente('Gabriel','Dias','000.000.000-00')
    cliente5=Cliente('Paulo','Victor','000.000.000-00')
    conta1 = Conta('1234',cliente1,1000,5000)
    # conta1.extrato()
    conta1.deposita(1000)
    conta1.historico.imprimir()
    print('-='*30)
    # cliente1.exibir()
    # cliente2.exibir()
    # cliente3.exibir()
    # cliente4.exibir()
    # cliente5.exibir()