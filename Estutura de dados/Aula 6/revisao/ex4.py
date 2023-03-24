# Escreva um programa que retorne o número de ocorrências de um elemento em uma lista.
count=0
lista=[1,2,3,4,5,1,3,2,1,3,5,6,]
ver=int(input('Insira qual numero deseja ver'))

for i in lista:
    if ver == i :
        count += 1
    
print(f'O Elemento',ver,'aparece na lista',count,'X')