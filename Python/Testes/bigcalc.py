n1 = int(input('\nDigite o PRIMEIRO NÚMERO: '))
n2 = int(input('Digite o SEGUNDO NÚMERO: '))
n3 = int(input('Digite o TERCEIRO NÚMERO: '))
n4 = int(input('Digite o QUARTO NÚMERO: '))
n5 = int(input('Digite o QUINTO NÚMERO: '))
n6 = int(input('Digite o SEXTO NÚMERO: '))
n7 = int(input('Digite o SETIMO NÚMERO: '))
n8 = int(input('Digite o OITAVO NÚMERO: '))
n9 = int(input('Digite o NONO NÚMERO: '))
n10 = int(input('Digite o DECIMO NÚMERO: '))
operador=str(input('Qual Operador deseja usar? :'))

soma=n1+n2+n3+n4+n5+n6+n7+n8+n9+n10
subs=n1-n2-n3-n4-n5-n6-n7-n8-n9-n10
mult=n1*n2*n3*n4*n5*n6*n7*n8*n9*n10
exp=n1**n2**n3**n4**n5**n6**n7**n8**n9**n10
div=n1/n2/n3/n4/n5/n6/n7/n8/n9/n10
rest=n1%n2%n3%n4%n5%n6%n7%n8%n9%n10

if (operador=="+"):
    print(f'\nA Soma de {n1} e {n2} é igual a: {soma}')
elif (operador=="-"):
    print(f'A Subtração de {n1} e {n2} é igual a: {subs}')
elif (operador=="*"):
    print(f'A Multiplicação de {n1} e {n2} é igual a: {mult}')
elif (operador=="/"):
    print(f'A Divisão de {n1} e {n2} é igual a: {div}')
elif (operador=="**"):
    print(f'O Exponencial de {n1} para {n2} é igual a: {exp}')
else:
    print(f'O Resto da divisão entre {n1} e {n2} é igual a: {rest}\n')