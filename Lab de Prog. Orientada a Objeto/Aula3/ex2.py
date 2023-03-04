"""Crie um carro com os seguintes atributos:
Cor
Modelo
Placa

Um Metodo Chamado ligar
um metodo chamado Print_Carro(que tera que imprimir os valores das variaveis de todas as instancias)

instanciar 5 objeyos novos
"""

class Carro:
    kind='Toyota'
    def __init__(self,name,cor,placa):
        self.name=name
        self.cor=cor
        self.placa=placa
    def ligar(self):
        print('você ligou o carro')
    def Print_Carro(self):
        print(self.name,self.cor,self.placa)

carro1=Carro('Toyota','Prata','001')
carro2=Carro("Ferrari",'Vermelha','002')
carro3=Carro('Mercedes','Preta','003')
carro4=Carro('MCLAREN','Azul','004')

carro1.ligar()

carro1.Print_Carro()
carro2.Print_Carro()
carro3.Print_Carro()
carro4.Print_Carro()



