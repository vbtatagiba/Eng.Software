# Um dado é lançado 10 vezes e o valor correspondente é armazenado em um vetor. 
# Faça um programa que determine o percentual de ocorrência de face 6 do dado dentre esses 10 lançamentos.

from random import randrange

l1 = []
cont =0

for i in range(1,11):
    numero = randrange(1,7)
    l1.append(numero)
    if numero==6:
        cont+=1
print(l1)

print('A Porcentagem é ',1000*(cont/100))

# while True:
#     if numero == 6:
#         calc = 10*(numero/100)
#         # print(calc)
#     break