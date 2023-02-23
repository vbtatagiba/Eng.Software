import  random

lista = []

for i in range(0,10):
    n=random.randrange(0,10)
    lista.append(n)

media = sum(lista)/ len(lista)
print('-='*30)
print(lista)
print("A média dos números na lista é:", media)
print('-='*30)