'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
contraram para desenvolver o programa que calculará os reajustes.
1. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:
2. salários até R$ 280,00 (incluindo) : aumento de 20%
3. salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
4. salários entre R$ 700,00 e R$ 700,00 : aumento de 10%
5. salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado,
informe na tela:
6. o salário antes do reajuste;
7. o percentual de aumento aplicado;
8. o valor do aumento;
9. o novo salário, após o aumento'''



salario=int(input('Insira seu salario: '))

if (salario<=280):
    percentual1=20
elif (salario>280 and salario<700):
    percentual1=15
elif (salario>700 and salario<1500):
    percentual1=10
elif (salario>1500):
    percentual1=5
else:
    print('Por favor insira um valor')
percentual=percentual1/100.0
aumento=percentual*salario
salario2=salario+aumento
print('Seu novo Salario é: ',salario2)
print(percentual1,'%')