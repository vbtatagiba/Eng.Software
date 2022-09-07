'''21. Faça um programa que leia 5 números e informe o maior número.'''
n1=int(input('Primeiro número: '))
n2=int(input('Segundo número: '))
n3=int(input('Terceiro número: '))
n4=int(input('Quarto número: '))
n5=int(input('Quinto número: '))
maior=n1
if (n2>maior):
    maior=n2
elif (n3>maior):
    maior=n3
elif (n4>maior):
    maior=n4
elif (n5>maior):
    maior=n5
print('Maior: ',maior)