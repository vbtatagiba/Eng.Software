#Calculadora aula 3
n1=int(input('Digite o Primeiro Numero:'))
n2=int(input('Digite o Segundo Numero:'))
n3=int(input('Digite o Terceiro Numero:'))
op=str(input('Insira o Operador que deseja usar:'))
soma=n1+n2+n3
subs=n1-n2-n3
mult=n1*n2*n3
exp=n1**n2**n3
div=n1/n2/n3
rest=n1%n2%n3
if op==("+"):
    print ('O resultado da Soma é:',soma)
if op==("-"):
    print('O resuldado da Subtração é:',subs)
if op==('*'):
    print ('O resuldado da multiplicação é',mult)
if op==('**'):
    print ('O resuldado da exponenciação é:',exp)
if op==('/'):
    print ('O resultado da divisão é:',div)
if op==("%"):
    print ('O Resultado do Resto da divisão é:',rest)