#calculadora com def 
x=float(input('Primeiro numero:  '))
y=float(input('Segundo numero:  '))

def soma ():
    print ('Soma: ', x+y)

def subtração ():
    print ("subtração: ",x-y)

def multiplicação ():
    print("Multiplicação: ",x*y)

def divisão () :
    print('Divisão:',x/y)

opção=1

while opção:
    print('0. Sair')
    print('1. Somar')
    print('2. Subtrair')
    print('3. Multiplicar')
    print('4. Divisão')
    opção= int(input('Opção: '))

    if (opção==1):
        soma()
    if (opção==2):
        subtração()
    if (opção==3):
        multiplicação()
    if (opção==4):
        divisão()