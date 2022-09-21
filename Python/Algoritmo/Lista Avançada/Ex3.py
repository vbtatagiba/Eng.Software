'''3. Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser
armazenado). Após esta entrada de dados, faça:
a. Mostre a quantidade de valores que foram lidos;
b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d. Calcule e mostre a soma dos valores;
e. Calcule e mostre a média dos valores;
f. Calcule e mostre a quantidade de valores acima da média calculada;
g. Calcule e mostre a quantidade de valores abaixo de sete;
h. Encerre o programa com uma mensagem;'''
from statistics import mean
notas=[]
nos=[]
soma=0
while True:
    if nos==-1:
        break
    nos=float(input('Insira a nota:'))
    if nos!=-1:
        notas.append(nos)
print(notas)
for n in notas[::-1]:
    print(n)
print('A soma da notas é ',sum(notas))
media=mean(notas)
print('A media das notas é',media)
for u in range(len(notas)):
    if notas[u]>media:
        print(f'A nota {notas[u]} Ficou a cima da media ')
for u in range(len(notas)):
    if notas[u]<7:
        print(f'A nota {notas[u]} Ficou abaixo de 7  ')

