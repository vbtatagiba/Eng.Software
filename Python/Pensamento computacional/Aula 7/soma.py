#calculadora com def 
def soma ():
    x= float(input('Primeiro Numero: '))
    y= float(input('Segundo Numero: '))
    print ('Soma: ', x+y)

def subtração ():
    x= float(input('Primeiro Numero: '))
    y= float(input('Segundo Numero: '))
    print ("subtração: ",x-y)

def multiplicação ():
    x= float(input('Primeiro Numero: '))
    y= float(input('Segundo Numero: '))
    print("Multiplicação: ",x+y)

def divisao () :
    x= float(input('Primeiro Numero: '))
    y= float(input('Segundo Numero: '))
    print('Divisão:',x/y)
opcao=1
while opcao:
    print('0. Sair')
    print('1. Somar')
    print('2. Subtrair')
    print('3. Multiplicar')
    print('4. Sair')
    opcao= int(input('Opção: '))

    if (opcao==1):
        soma()
    if (opcao==2):
        subtração()
    if (opcao==3):
        multiplicação
    if (opcao==4):
        divisao()