'''2-Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se
que:
• Esse funcionário foi contratado em 1995, com salário inicial de R$
1.000,00;
• Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
• A partir de 1997 (inclusive), os aumentos salariais sempre correspondem
ao dobro do percentual do ano anterior. Faça um programa que
determine o salário atual desse funcionário. Após concluir isto, altere o
programa permitindo que o usuário digite o salário inicial do funcionário.'''

salario=float(input('Insira o salario desejado: '))
porcentage=float(input('Insira a porcentagem sendo: '))
percentual=porcentage/100.0
porcentage2=(porcentage*2**(25))
aumento=salario*percentual
novosalario=aumento+salario
percentual2=porcentage2/100.0
aumento2=novosalario*percentual2
novosalario2=aumento2+novosalario
print(porcentage2)
print("O Seu aumento foi de:",aumento)
print("O Seu novo Salario é: ", novosalario)
if str(input('Deseja ver seu Salario proximo ano?')) == 'Y' or 'y':
    print(novosalario2)
