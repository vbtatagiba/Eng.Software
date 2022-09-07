'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F
- Feminino, M - Masculino, Sexo Inválido'''



sexo=str(input('Insira seu sexo sendo:"F":Feminino "M":Masculino:'))
if sexo=='M' or sexo=='m':
    print('Sexo Masculino')
elif sexo== 'f' or sexo=='F':
    print('Sexo Feminino')
else:
    print('Sexo Inválido')