import  random

lista = []

for i in range(0,10):
    n=random.randrange(0,99)
    lista.append(n)

soma = sum(lista)
print('-='*30)
print(lista)
print("A soma dos números na lista é:", soma)
print('-='*30)