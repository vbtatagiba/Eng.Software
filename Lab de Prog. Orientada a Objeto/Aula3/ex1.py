class Dog:
    kind='Canino'
    def __init__(self,name,raca):
        self.name=name
        self.raca=raca
    def latir(self):
        print('AU AU AU')



cao1=Dog('Zetsu','Vira lata')
cao2=Dog("San",'Caramelo')
cao3=Dog('Duque','Vira lata')
cao4=Dog('Princesa','Vira lata')

cao1.name
cao2.name
cao3.name
cao4.name

cao1.latir()

print(cao1.name,cao1.raca)
print(cao2.name,cao2.raca)
print(cao3.name,cao3.raca)
print(cao4.name,cao4.raca)




