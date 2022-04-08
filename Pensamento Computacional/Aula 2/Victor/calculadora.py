# CALCULADORA
n1 = int(input('\nDigite o PRIMEIRO NÚMERO: '))
n2 = int(input('Digite o SEGUNDO NÚMERO: '))
operador=str(input('qual o operador'))

soma = n1+n2
sub = n1-n2
mult = n1*n2
div = n1/n2
divi_int = n1//n2
expo = n1**n2
rest = n1%n2

if (operador=="+"):
    print(f'\nA Soma de {n1} e {n2} é igual a: {soma}')
if (operador=="-"):
    print(f'A Subtração de {n1} e {n2} é igual a: {sub}')
if (operador=="*"):
    print(f'A Multiplicação de {n1} e {n2} é igual a: {mult}')
if (operador=="/"):
    print(f'A Divisão de {n1} e {n2} é igual a: {div}')
if (operador=="//"):
    print(f'A Divisão Inteira de {n1} e {n2} é igual a: {div}')
if (operador=="**"):
    print(f'O Exponencial de {n1} para {n2} é igual a: {expo}')
if (operador=="%"):
    print(f'O Resto da divisão entre {n1} e {n2} é igual a: {rest}\n')