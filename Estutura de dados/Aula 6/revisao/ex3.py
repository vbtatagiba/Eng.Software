# Escreva um programa que some os elementos de duas listas de igual tamanho elemento a elemento.
soma=[]
lista1=[1,2,3,4]
lista2=[5,6,7,8]

for i in lista1:
    soma.append(i)
for i in lista2:
    soma.append(i)

print(sum(soma))