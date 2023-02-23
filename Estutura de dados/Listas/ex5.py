lista=[]

tamanho=int(input("Insira Quantos numeros gostaria na lista: "))

for i in range(tamanho) :
    n=int(input('Insira os numeros que deseja na lista: '))
    lista.append(n)

pares = 0
impar = 0

for num in lista:
    if num % 2 == 0:
        pares += 1
    else:
        impar += 1
print('-='*30)
print("Lista:", lista)
print("Número de pares:", pares)
print("Número de ímpares:", impar)
print('-='*30)