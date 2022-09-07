'''11. Faça um Programa que leia três números e mostre o maior e o menor deles.'''

n1=int(input('Primeiro número: '))
n2=int(input('Segundo número: '))
n3=int(input('Terceiro número: '))
maior=n1
menor=n1
if (n2>maior):
    maior=n2
if (n3>maior):
    maior=n3
if (n2<n3) and (n2<n1):
    menor=n2
if n3<n2 and n3<n1:
    menor=n3
if n1==n2==n3:
    print('Os números são iguais')
else:
    print('O Maior Número digitado foi: ',maior)
    print('O Menor Número digitado foi: ',menor)
