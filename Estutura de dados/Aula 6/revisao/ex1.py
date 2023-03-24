# Dado uma lista de números, escreva um programa que remova todos os números pares e retorne uma nova lista.
lista=[]
pares=[]
impar=[]
for i in range (5):
    a=int(input('Insira um numero:'))
    lista.append(a)

for i in range(len(lista)):
    if lista[i]%2 ==0 :
        pares.append(lista[i])
        print('Par')   
    else:
        impar.append(lista[i])
        print("Impar")
        
print('-='*30)
print('Os Numeros pares São:',pares)
print('Os Numeros impares São:',impar)
print('-='*30)
