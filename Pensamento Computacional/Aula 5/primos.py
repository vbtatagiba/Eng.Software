"""8.	Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1."""

n1=int(input('Digite um numero inteiro: '))

cont = 0

divisor = []

for i in range(n1):

    if n1%(i+1) == 0:

        cont += 1
        divisor.append(i+1)

    else:

        cont
        

if cont == 2:

    print ("O numero é primo divisivel por ",divisor)

else:

    print ("O numero não é primo pois é divisivel por ",divisor)