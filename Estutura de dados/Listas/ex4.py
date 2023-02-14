lista=[]

tamanho=int(input("Insira Quantos numeros gostaria na lista: "))

for i in range(tamanho) :
    n=input('Insira os numeros que deseja na lista: ')
    lista.append(n)

rem=int(input('Qual a posição do valor desejado para ser retirado da lista? '))
print('-='*30)
print(lista)
print('-='*30)

lista.pop(rem)

print('-='*30)
print(lista)
print('-='*30)